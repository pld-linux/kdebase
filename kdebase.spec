Summary:	K Desktop Environment - core files
Summary(pl):	K Desktop Environment - pliki ¶rodowiska
Name:		kdebase
Version:	2.0.1
Release:	3
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/src/%{name}-%{version}.tar.bz2
Source1:	%{name}-startkde.sh
Source2:	kdm.pamd
Source3:	kdm.init
Patch0:		%{name}-key.patch
Patch1:		%{name}-waitkdm.patch
Patch2:		%{name}-konsole-TERM.patch
BuildRequires:	qt-devel >= 2.2.2
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	pam-devel
BuildRequires:	OpenGL-devel
BuildRequires:	glut-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	openssl-devel
Requires:	kdelibs = %{version}
Requires:	qt >= 2.2.2
Requires:	applnk
Obsoletes:	%{name}-kcontrol
Obsoletes:	%{name}-khelpcenter
Obsoletes:	%{name}-konsole
Obsoletes:	%{name}-screensaver
Obsoletes:	%{name}-kicker
Obsoletes:	%{name}-kioslave
Obsoletes:	%{name}-konqueror
Obsoletes:	%{name}-kwin
Obsoletes:	%{name}-kxmlrpc
Obsoletes:	%{name}-kdesktop
Obsoletes:	%{name}-kwrite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix 	/usr/X11R6
%define		_fontdir 	/usr/share/fonts
%define		_htmldir	%{_datadir}/doc/kde/HTML

%description
KDE specific files. Used by core KDE applications. Package includes:
KDE menu hierarchy kappfinder - script installing some non-KDE apps in
KDE menu krootwm - module used by KWM and KFM kaudio - audio server
for KDE

%description -l pl
Pliki specyficzne dla ¶rodowiska KDE i wykorzystywane przez g³ówne
aplikacje KDE. Pakiet zawiera: Hierarchiê menu KDE kappfinder - skrypt
u³awiaj±cy uruchamianie niektórych programów spoza KDE krootwm - modu³
wykorzystywany przez kwm i kfm kaudio - serwer d¼wiêku dla KDE

%package devel
Summary:	Include files to develop KDE applications.
Summary(pl):	Pliki nag³ówkowe potrzebne do programowania.
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	qt-devel >= 2.2.2
Requires:	kdelibs-devel = %{version}

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe niezbêdne do programowania aplikacji KDE.

%package -n kdm
Summary:	KDE Display Manager	
Summary(pl):	KDE Display Manager
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	qt >= 2.2.2
Requires:	kdelibs = %{version}
Obsoletes:	gdm
Obsoletes:	xdm
Obsoletes:	%{name}-kdm

%description -n kdm
It is KDE replacement for XDM. It manages local and remote X11
displays.

%description -n kdm -l pl
Zamiennik XDM rodem z KDE.

%package -n konqueror
Summary:	Konqueror - web browser and file manager
Summary(pl):	Konqueror - przegl±darka WWW i mened¿er plików
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	qt >= 2.2.2
Requires:	kdelibs = %{version}
Obsoletes:	kdebase-konqueror

%description -n konqueror
Konqueror is a web browser and file manager similar to MS Internet Explorer.

%description -n konqueror -l pl
Konqueror jest przegl±dark± WWW i mene¿derem plików podobnym do MS Internet
Explorer.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

#CFLAGS="%{!?debug:$RPM_OPT_FLAGS}"
#CXXFLAGS="%{!?debug:$RPM_OPT_FLAGS}"
export CPPFLAGS="-I/usr/X11R6/include"
%configure \
 	--with-pam=kdm \
	--without-shadow \
	--disable-shadow \
	--with-xdmdir="/etc/X11/kdm" \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Network/WWW,Office/Editors,Amusements,Settings/KDE} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{pam.d,security,rc.d/init.d}

%{__make} install \
 	DESTDIR="$RPM_BUILD_ROOT" \
 	fontdir="%{_fontdir}/misc"

install kwrite/kwrite.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Editors
install konqueror/konqbrowser.desktop	$RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install ktip/ktip.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE1}			$RPM_BUILD_ROOT%{_bindir}/startkde
install %{SOURCE2}			$RPM_BUILD_ROOT%{_sysconfdir}/pam.d/kdm
install %{SOURCE3}			$RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/kdm

# Make Control Center a subdirectory of Settings. Control Center applets can
# not be mixed with normal programs or CC will die on startup.
mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/{[!K]*,KDE}
cat > $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/.directory << EOF
[Desktop Entry]
Name=KDE
Icon=package_settings
X-KDE-BaseGroup=KDE
EOF

# removing unneeded directories
rm -fr $RPM_BUILD_ROOT%{_applnkdir}/{Editors,Toys}

touch $RPM_BUILD_ROOT%{_sysconfdir}/security/blacklist.kdm

%find_lang kcontrol --with-kde
%find_lang kdebugdialog --with-kde
%find_lang kdesu --with-kde
%find_lang kdm --with-kde
%find_lang khelpcenter --with-kde
%find_lang kicker --with-kde
%find_lang klipper --with-kde
%find_lang kmenuedit --with-kde
%find_lang konqueror --with-kde
%find_lang konsole --with-kde
%find_lang kpager --with-kde
%find_lang ksysguard --with-kde
%find_lang kwrite --with-kde

cat kcontrol.lang \
	kdebugdialog.lang \
	kdesu.lang \
	khelpcenter.lang \
	kicker.lang \
	klipper.lang \
	kmenuedit.lang \
	konsole.lang \
	kpager.lang \
	ksysguard.lang \
	kwrite.lang > %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun
/sbin/ldconfig

cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir

%post	-n konqueror -p /sbin/ldconfig 
%postun	-n konqueror -p /sbin/ldconfig 

%pre -n kdm
/usr/sbin/groupadd -g 55 -r -f xdm

if [ -z "`id -u xdm 2>/dev/null`" ]; then
	/usr/sbin/useradd -u 55 -r -d /dev/null -s /bin/false -c 'X Display Manager' -g xdm xdm 1>&2
fi

%post -n kdm
/sbin/chkconfig --add kdm
if [ -f /var/lock/subsys/kdm ]; then
        /etc/rc.d/init.d/kdm restart >&2
else
        echo "Run \"/etc/rc.d/init.d/kdm start\" to start kdm." >&2
fi

%preun -n kdm
if [ -f /var/lock/subsys/kdm ]; then
		 /etc/rc.d/init.d/kdm stop >&2
fi
/sbin/chkconfig --del kdm

%postun -n kdm
if [ "$1" = "0" ]; then
	if [ -n "`id -u xdm 2>/dev/null`" ]; then
		/usr/sbin/userdel xdm
	fi
	/usr/sbin/groupdel xdm
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/[adns]*
%attr(0755,root,root) %{_bindir}/conttest
%attr(0755,root,root) %{_bindir}/k[abcefhilmprstvwx]*
%attr(0755,root,root) %{_bindir}/kdcop
%attr(0755,root,root) %{_bindir}/kdebugdialog
%attr(0755,root,root) %{_bindir}/kdeeject
%attr(0755,root,root) %{_bindir}/kdesktop
%attr(0755,root,root) %{_bindir}/kdesu
%attr(2750,root,root) %{_bindir}/kdesud
%attr(0755,root,root) %{_bindir}/kdmdesktop
%attr(0755,root,root) %{_bindir}/konsole
%attr(0755,root,root) %{_bindir}/konsole_grantpty

%attr(0755,root,root) %{_libdir}/appletproxy.*
%attr(0755,root,root) %{_libdir}/k[acdfhilmwx]*.la*
%attr(0755,root,root) %{_libdir}/k[acdfhilmwx]*.so*
%attr(0755,root,root) %{_libdir}/konsole.*
%attr(0755,root,root) %{_libdir}/lib[chnqs]*.la*
%attr(0755,root,root) %{_libdir}/lib[chnqs]*.so*
%attr(0755,root,root) %{_libdir}/libkcm_[abcefhilmnpstvx]*.la*
%attr(0755,root,root) %{_libdir}/libkcm_[abcefhilmnpstvx]*.so*
%attr(0755,root,root) %{_libdir}/libkcm_k[ehinuw]*.la*
%attr(0755,root,root) %{_libdir}/libkcm_k[ehinuw]*.so*
%attr(0755,root,root) %{_libdir}/libk[hmrstuw]*.la*
%attr(0755,root,root) %{_libdir}/libk[hmrstuw]*.so*
%attr(0755,root,root) %{_libdir}/libkonsolepart.*

# NOTE:	There are many directories created by kappfinder. They should be
#	ignored as such functionality is provided by applnk package and
#	*.dekstop files from apropriate packages.
%{_applnkdir}/Amusements/*.desktop
%{_applnkdir}/Development/*.desktop
# This will go to "konqueror".
#%{_applnkdir}/Network/WWW/*.desktop
%{_applnkdir}/Office/Editors/*.desktop
%{_applnkdir}/Settings/KDE
%{_applnkdir}/System/[!k]*.desktop
%{_applnkdir}/System/k[!o]*.desktop
#%{_applnkdir}/System/ko[!n]*.desktop
%{_applnkdir}/System/kon[!q]*.desktop
%{_applnkdir}/System/ScreenSavers/*.desktop
%{_applnkdir}/Utilities/*.desktop
%{_applnkdir}/Help.desktop
%{_applnkdir}/Home.desktop
%{_applnkdir}/KControl.desktop

%{_datadir}/apps/[cdq]*
%{_datadir}/apps/k[abchimsw]*
%{_datadir}/apps/kdcop
%{_datadir}/apps/kdesktop
%{_datadir}/apps/kdewizard
%{_datadir}/apps/kdisplay
%{_datadir}/apps/konsole

%{_pixmapsdir}/*/*/actions/*
%{_pixmapsdir}/*/*/devices/*
%{_pixmapsdir}/*/*/apps/[abcdefghilmnprstwx]*
%{_pixmapsdir}/*/*/apps/k[acdefhlmnpstw]*
%{_pixmapsdir}/*/*/apps/konsole.png

%dir %{_datadir}/config
%{_datadir}/config/[!k]*
%{_datadir}/config/k[!d]*
%{_datadir}/locale
%{_datadir}/mimelnk
%{_datadir}/services
%{_datadir}/sounds
%{_datadir}/templates
%{_datadir}/wallpapers

# TODO:	file /usr/share/fonts/misc/9x15.pcf.gz from install of kdebase-2.0.1-3
# 	conflicts with file from package XFree86-fonts-4.0.1-2.
# TODO:	there is a name conflict between cursor_large and cursor from XFree86.
%{_fontdir}/misc/console8*.gz

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/*.a

%files -f kdm.lang -n kdm
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/chooser
%attr(0755,root,root) %{_bindir}/kdm
%attr(0755,root,root) %{_sysconfdir}/X11/kdm
%attr(0755,root,root) %{_libdir}/libkcm_kdm.??
%attr(0640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/pam.d/kdm
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/security/blacklist.kdm
%attr(0754,root,root) %{_sysconfdir}/rc.d/init.d/kdm
%{_applnkdir}/Settings/KDE/System/kdm.desktop
%{_datadir}/apps/kdm
%{_datadir}/config/kdmrc

%files -n konqueror -f konqueror.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/konqueror
%attr(0755,root,root) %{_libdir}/libkonq*
%attr(0755,root,root) %{_libdir}/konqueror.??
%attr(0755,root,root) %{_libdir}/libkcm_konq*
%{_pixmapsdir}/*/*/apps/konqueror.png
%{_applnkdir}/Network/WWW/konq*.desktop
%{_applnkdir}/System/konq*.desktop
%{_applnkdir}/Settings/KDE/FileBrowsing/kcmkonq.desktop
%{_applnkdir}/Settings/KDE/WebBrowsing/konq*.desktop
%{_datadir}/apps/konq*
