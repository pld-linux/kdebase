Summary:	K Desktop Environment - core files
Summary(pl):	K Desktop Environment - pliki ¶rodowiska
Name:		kdebase
Version:	2.1.1
Release:	1
Epoch:		6
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/src/%{name}-%{version}.tar.bz2
Source1:	%{name}-startkde.sh
Source2:	kdm.pamd
Source3:	kdm.init
Source4:	kdm.Xsession
Source5:	kdmrc
Patch0:		%{name}-waitkdm.patch
Patch1:		%{name}-konsole-TERM.patch
Patch2:		%{name}-time.patch
Patch3:		%{name}-glibc-2.2.2.patch
Patch4:		%{name}-kxmlrpcd-tcpsocket.patch
Patch5:		%{name}-arrange.patch
Patch6:		%{name}-utmp.patch
BuildRequires:	grep
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	qt-devel >= 2.3.0
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	pam-devel
BuildRequires:	OpenGL-devel
BuildRequires:	openssl-devel
BuildRequires:	motif-devel
Prereq:		/sbin/ldconfig
Requires:	applnk
Requires:	konqueror
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

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix 	/usr/X11R6
%define		_fontdir 	/usr/share/fonts
%define		_htmldir	%{_datadir}/doc/kde/HTML

%description
KDE specific files. Used by core KDE applications. Package includes:
KDE menu hierarchy kappfinder - script installing some non-KDE apps in
KDE menu krootwm - module used by KWM and KFM kaudio - audio server
for KDE.

%description -l pl
Pliki specyficzne dla ¶rodowiska KDE i wykorzystywane przez g³ówne
aplikacje KDE. Pakiet zawiera: Hierarchiê menu KDE kappfinder - skrypt
u³awiaj±cy uruchamianie niektórych programów spoza KDE krootwm - modu³
wykorzystywany przez kwm i kfm kaudio - serwer d¼wiêku dla KDE.

%package devel
Summary:	Include files to develop KDE applications.
Summary(pl):	Pliki nag³ówkowe potrzebne do programowania.
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	qt-devel >= 2.3.0
Requires:	kdelibs-devel = %{version}

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe niezbêdne do programowania aplikacji
KDE.

%package static
Summary:	Include static libraries to develop KDE applications
Summary(pl):	Statyczne biblioteki KDE
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	qt-devel >= 2.3.0
Requires:	kdelibs-devel = %{version}

%description static
This package contains KDE static libraries.

%description static -l pl
Pakiet zawiera statyczne biblioteki KDE.

%package -n kdm
Summary:	KDE Display Manager	
Summary(pl):	KDE Display Manager
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	qt >= 2.3.0
Requires:	kdelibs >= %{version}
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
Requires:	qt >= 2.3.0
Requires:	kdelibs >= %{version}
Obsoletes:	kdebase-konqueror

%description -n konqueror
Konqueror is a web browser and file manager similar to MS Internet
Explorer.

%description -n konqueror -l pl
Konqueror jest przegl±dark± WWW i mene¿derem plików podobnym do MS
Internet Explorer.

%package screensavers
Summary:	KDE screensavers
Summary(pl):	Wygaszacze ekranu desktopu KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	qt >= 2.3.0
Requires:	kdelibs >= %{version}
Requires:	OpenGL

%description screensavers
KDE screensavers.

%description screensavers -l pl
Wygaszacze ekranu desktopu KDE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
libtoolize --copy --force
aclocal
autoconf
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CPPFLAGS="-I/usr/X11R6/include"
export CPPFLAGS
%configure \
	--with-pam=kdm \
	--without-shadow \
	--disable-shadow \
	--with-xdmdir="%{_sysconfdir}/X11/kdm" \
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
install konqueror/keditbookmarks/keditbookmarks.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install ktip/ktip.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE1}			$RPM_BUILD_ROOT%{_bindir}/startkde
install %{SOURCE2}			$RPM_BUILD_ROOT%{_sysconfdir}/pam.d/kdm
install %{SOURCE3}			$RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/kdm
install %{SOURCE4}			$RPM_BUILD_ROOT%{_sysconfdir}/X11/kdm/Xsession
install %{SOURCE5}			$RPM_BUILD_ROOT%{_datadir}/config/kdmrc

# Make Control Center a subdirectory of Settings. Control Center applets can
# not be mixed with normal programs or CC will die on startup.
mv -f $RPM_BUILD_ROOT%{_applnkdir}/Settings/{[!K]*,KDE}
cat > $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/.directory << EOF
[Desktop Entry]
Name=KDE
Icon=package_settings
X-KDE-BaseGroup=settings
EOF

# removing unneeded directories
rm -rf $RPM_BUILD_ROOT%{_applnkdir}/{Editors,Toys}

# make compatibile with GNOME
for a in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory'`; do
        cat $a |sed -n '/^Icon=/!p' > $a.
        echo "Type=Directory" >> $a.
        cat $a |awk '/^Icon/ {print $1".png" }' >> $a.
        mv -f $a. $a
done
for a in `find $RPM_BUILD_ROOT%{_applnkdir} -name '*.desktop'`; do
        cat $a |sed -n '/^Icon=/!p' > $a.
        echo >> $a.
        cat $a |awk '/^Icon/ {print $1".png" }' >> $a.
        mv -f $a. $a
done

touch $RPM_BUILD_ROOT%{_sysconfdir}/security/blacklist.kdm

%find_lang tmp.%{name} --with-kde --all-name
grep -vE konqueror\|kdm tmp.%{name}.lang > %{name}.lang
%find_lang konqueror --with-kde
%find_lang kdm --with-kde

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
%attr(0755,root,root) %{_bindir}/[ades]*
%attr(0755,root,root) %{_bindir}/conttest
%attr(0755,root,root) %{_bindir}/k[acitwx]*
%attr(0755,root,root) %{_bindir}/keditfiletype
%attr(0755,root,root) %{_bindir}/kd[ce]*
%attr(0755,root,root) %{_bindir}/konsole*
%attr(0755,root,root) %{_bindir}/khelpcenter
%attr(0755,root,root) %{_bindir}/khotkeys
%attr(0755,root,root) %{_bindir}/khtmlindex
%attr(0755,root,root) %{_bindir}/klegacyimport
%attr(0755,root,root) %{_bindir}/klipper
%attr(0755,root,root) %{_bindir}/ks[mty]*
%attr(0755,root,root) %{_bindir}/ksplash
%attr(0755,root,root) %{_bindir}/krdb
%attr(0755,root,root) %{_bindir}/kreadconfig
%attr(0755,root,root) %{_bindir}/kpager
%attr(0755,root,root) %{_bindir}/kmenuedit

%attr(0755,root,root) %{_libdir}/[ae]*.la
%attr(0755,root,root) %{_libdir}/[ae]*.so*
%attr(0755,root,root) %{_libdir}/k[dhilmwx]*.la
%attr(0755,root,root) %{_libdir}/k[dhilmwx]*.so*
%attr(0755,root,root) %{_libdir}/kcminit.??
%attr(0755,root,root) %{_libdir}/kcontrol.??
%attr(0755,root,root) %{_libdir}/konsole.la
%attr(0755,root,root) %{_libdir}/konsole.so*
%attr(0755,root,root) %{_libdir}/lib[cdqt]*.la
%attr(0755,root,root) %{_libdir}/lib[cdqt]*.so*
%attr(0755,root,root) %{_libdir}/libk[ahmrstw]*.la
%attr(0755,root,root) %{_libdir}/libk[ahmrstw]*.so*
%attr(0755,root,root) %{_libdir}/libkcm_[ilx]*.la*
%attr(0755,root,root) %{_libdir}/libkcm_[ilx]*.so*
%attr(0755,root,root) %{_libdir}/libkonsolepart.la
%attr(0755,root,root) %{_libdir}/libkonsolepart.so*
%attr(0755,root,root) %{_libdir}/libnaughtyapplet.la
%attr(0755,root,root) %{_libdir}/libnaughtyapplet.so*

%attr(0755,root,root) %{_libdir}/kde2/[ikt]*.la
%attr(0755,root,root) %{_libdir}/kde2/[ikt]*.so*
%attr(0755,root,root) %{_libdir}/kde2/libkcm_[abcefilmpt]*.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_[abcefilmpt]*.so*
%attr(0755,root,root) %{_libdir}/kde2/libkcm_k[ehinuw]*.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_k[ehinuw]*.so*
%attr(0755,root,root) %{_libdir}/kde2/libkcm_s[amt]*.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_s[amt]*.so*
%attr(0755,root,root) %{_libdir}/kde2/libk[fsuw]*.la*
%attr(0755,root,root) %{_libdir}/kde2/libk[fsuw]*.so*

# NOTE:	There are many directories created by kappfinder. They should be
#	ignored as such functionality is provided by applnk package and
#	*.dekstop files from apropriate packages.
%{_applnkdir}/Help.desktop
%{_applnkdir}/Home.desktop
%{_applnkdir}/KControl.desktop
%{_applnkdir}/.hidden/konqfilemgr.desktop
%{_applnkdir}/Amusements/*.desktop
%{_applnkdir}/Office/Editors/*.desktop
%{_applnkdir}/Settings/KDE/Help
%{_applnkdir}/Settings/KDE/Information
%{_applnkdir}/Settings/KDE/LookNFeel/background.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/colors.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/fonts.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/icons.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/kcmnotify.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/kcmtaskbar.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/keys.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/kthememgr.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/kwinoptions.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/panel.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/style.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/virtualdesktops.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/Desktop
%{_applnkdir}/Settings/KDE/LookNFeel/Themes
%{_applnkdir}/Settings/KDE/LookNFeel/Windows
%{_applnkdir}/Settings/KDE/Network
%{_applnkdir}/Settings/KDE/Peripherals
%{_applnkdir}/Settings/KDE/Personalization
%{_applnkdir}/Settings/KDE/PowerControl
%{_applnkdir}/Settings/KDE/Sound
%{_applnkdir}/Settings/KDE/System
%{_applnkdir}/System/k[!o]*.desktop
%{_applnkdir}/System/kon[!q]*.desktop
%{_applnkdir}/Utilities/klipper.desktop
%{_applnkdir}/Utilities/kpager.desktop

%{_datadir}/apps/[cdn]*
%{_datadir}/apps/k[abcfhimtw]*
%{_datadir}/apps/kd[cei]*
%{_datadir}/apps/konsole
%{_datadir}/apps/ks[py]*

%{_datadir}/autostart
%dir %{_datadir}/config
%{_datadir}/config/[!k]*
%{_datadir}/config/k[!d]*
%{_datadir}/config/kdesktop*
%{_datadir}/locale
%{_datadir}/mimelnk
%{_datadir}/services/[abfghimnpst]*
%{_datadir}/services/k[afhsuwx]*
%{_datadir}/sounds
%{_datadir}/templates
%{_datadir}/wallpapers
#pascalek %{_datadir}/fonts
%{_datadir}/servicetypes/[stf]*.desktop

%{_pixmapsdir}/*/*/apps/[abcdefghilmnprstwx]*
%{_pixmapsdir}/*/*/apps/k[acefhilmnptwm]*
%{_pixmapsdir}/*/*/apps/konsole.png
%{_pixmapsdir}/*/*/apps/ksysguard.png
%{_pixmapsdir}/*/*/apps/kdisknav.png

%{_pixmapsdir}/*/*/actions/*
%{_pixmapsdir}/*/*/devices/*
%{_pixmapsdir}/*/*/filesystems/*

# TODO:	file /usr/share/fonts/misc/9x15.pcf.gz from install of kdebase-2.0.1-3
# 	conflicts with file from package XFree86-fonts-4.0.1-2.
# TODO:	there is a name conflict between cursor_large and cursor from XFree86.
%{_fontdir}/misc/console8*.gz

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/kwin
%{_includedir}/*.h
%{_includedir}/kwin/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libccont.a

%files -f kdm.lang -n kdm
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/chooser
%attr(0755,root,root) %{_bindir}/kdm
%attr(0755,root,root) %{_bindir}/kdmdesktop

%attr(0755,root,root) %{_libdir}/libKdmGreet.la
%attr(0755,root,root) %{_libdir}/libKdmGreet.so*

%attr(0755,root,root) %{_libdir}/kde2/libkcm_kdm.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_kdm.so*

%dir %{_sysconfdir}/X11/kdm
%attr(0755,root,root) %{_sysconfdir}/X11/kdm/*
%attr(0754,root,root) %{_sysconfdir}/rc.d/init.d/kdm
%attr(0640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/pam.d/kdm
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/security/blacklist.kdm

%{_applnkdir}/Settings/KDE/System/kdm.desktop

%{_datadir}/apps/kdm
%{_datadir}/config/kdmrc

%{_pixmapsdir}/*/*/apps/kdmconfig.png

%files -n konqueror -f konqueror.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/keditbookmarks
%attr(0755,root,root) %{_bindir}/konqueror
%attr(0755,root,root) %{_bindir}/kfm*
%attr(0755,root,root) %{_bindir}/nspluginscan
%attr(0755,root,root) %{_bindir}/nspluginviewer

%attr(0755,root,root) %{_libdir}/keditbookmarks.la
%attr(0755,root,root) %{_libdir}/keditbookmarks.so
%attr(0755,root,root) %{_libdir}/kcmshell.??
%attr(0755,root,root) %{_libdir}/kfm*.??
%attr(0755,root,root) %{_libdir}/konqueror.la
%attr(0755,root,root) %{_libdir}/konqueror.so*
%attr(0755,root,root) %{_libdir}/libhtmlsearch.la
%attr(0755,root,root) %{_libdir}/libhtmlsearch.so*
%attr(0755,root,root) %{_libdir}/libkcm_htmlsearch.la
%attr(0755,root,root) %{_libdir}/libkcm_htmlsearch.so*
%attr(0755,root,root) %{_libdir}/libkcm_nsplugin.la
%attr(0755,root,root) %{_libdir}/libkcm_nsplugin.so*
%attr(0755,root,root) %{_libdir}/libkonq*.la
%attr(0755,root,root) %{_libdir}/libkonq*.so*
%attr(0755,root,root) %{_libdir}/libnsplugin.la
%attr(0755,root,root) %{_libdir}/libnsplugin.so*

%attr(0755,root,root) %{_libdir}/kde2/htmlthumbnail.la
%attr(0755,root,root) %{_libdir}/kde2/htmlthumbnail.so*
%attr(0755,root,root) %{_libdir}/kde2/libkcm_konq*.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_konq*.so*
%attr(0755,root,root) %{_libdir}/kde2/libkonq*la
%attr(0755,root,root) %{_libdir}/kde2/libkonq*so*

%{_applnkdir}/Network/WWW/konq*.desktop
%{_applnkdir}/Network/WWW/keditbookmarks.desktop
%{_applnkdir}/System/konq*.desktop
%dir %{_applnkdir}/Settings/KDE
%{_applnkdir}/Settings/KDE/.directory
%{_applnkdir}/Settings/KDE/FileBrowsing
%{_applnkdir}/Settings/KDE/WebBrowsing

%{_datadir}/apps/konq*
%{_datadir}/apps/keditbookmarks
%{_datadir}/services/htmlthumbnail.desktop
%{_datadir}/services/konq*.desktop
%{_datadir}/servicetypes/konqaboutpage.desktop

%{_pixmapsdir}/*/*/apps/konqueror.png


%files screensavers
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/*.kss

%attr(0755,root,root) %{_libdir}/kde2/libkcm_screensaver.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_screensaver.so*

%{_applnkdir}/Settings/KDE/LookNFeel/screensaver.desktop
%{_applnkdir}/System/ScreenSavers/*

%{_datadir}/apps/kscreensaver

%{_pixmapsdir}/*/*/apps/kscreensaver.png
