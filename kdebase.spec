Summary:	K Desktop Environment - core files
Summary(pl):	K Desktop Environment - pliki ¶rodowiska
Name:		kdebase
Version:	2.0
Release:	5
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.kde.org/pub/kde/stable/2.0/distribution/generic/tar/src/%{name}-%{version}.tar.bz2
Source1:	%{name}-startkde.sh
Source2:	kdm.pamd
Source3:	kdm.init
Patch0:		%{name}-key.patch
Patch1:		%{name}-waitkdm.patch
BuildRequires:	qt >= 2.2.1-6
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	pam-devel
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
Requires:	kdelibs = %{version}
Requires:	qt >= 2.2.1-6
Obsoletes:	kdebase-kcontrol
Obsoletes:	kdebase-khelpcenter
Obsoletes:	kdebase-konsole
Obsoletes:	kdebase-screensaver
Obsoletes:	kdebase-kicker
Obsoletes:	kdebase-kioslave
Obsoletes:	kdebase-kwin
Obsoletes:	kdebase-kxmlrpc
Obsoletes:	kdebase-kdesktop
Obsoletes:	kdebase-kwrite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix 		/usr/X11R6

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
Requires:	qt-devel >= 2.2.1-6
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
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}
Obsoletes:	gdm
Obsoletes:	xdm
Obsoletes:	kdebase-kdm

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
Requires:	qt >= 2.2.1-6
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

%build
kde_icondir="%{_pixmapsdir}"; export kde_icondir
kde_htmldir="%{_docdir}/HTML"; export kde_htmldir
%configure \
 	--with-pam=yes \
	--without-shadow \
	--disable-shadow

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	RUN_KAPPFINDER="no" \
	DESTDIR="$RPM_BUILD_ROOT" \
	localedir="$RPM_BUILD_ROOT%{_datadir}/locale" \
	ac_xdmdir="%{_sysconfdir}/X11/kdm" \
	install

install -d $RPM_BUILD_ROOT%{_applnkdir}/{Network/WWW,Office/Editors,Amusements}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{pam.d,security,rc.d/init.d}

install kwrite/kwrite.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Editors
install konqueror/konqbrowser.desktop	$RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install ktip/ktip.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE1}			$RPM_BUILD_ROOT%{_bindir}/startkde
install %{SOURCE2}			$RPM_BUILD_ROOT%{_sysconfdir}/pam.d/kdm
install %{SOURCE3}			$RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/kdm
touch $RPM_BUILD_ROOT%{_sysconfdir}/security/blacklist.kdm

# this is included in control-center
rm -f $RPM_BUILD_ROOT%%{_applnk}/Settings/Peripherals/.directory

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/[as]*
%attr(0755,root,root) %{_bindir}/k[abcefhilmprstvwx]*
%attr(0755,root,root) %{_bindir}/conttest
%attr(0755,root,root) %{_bindir}/kdebugdialog
%attr(0755,root,root) %{_bindir}/kdeeject
%attr(0755,root,root) %{_bindir}/kdesktop
%attr(0755,root,root) %{_bindir}/kdesu
%attr(2750,root,root) %{_bindir}/kdesud
%attr(0755,root,root) %{_bindir}/kdmdesktop
%attr(0755,root,root) %{_bindir}/konsole
%attr(0755,root,root) %{_bindir}/konsole_grantpty

%attr(0755,root,root) %{_libdir}/a*
%attr(0755,root,root) %{_libdir}/k[acdfhilwx]*
%attr(0755,root,root) %{_libdir}/kmenuedit.*.*.*
%attr(0755,root,root) %{_libdir}/libclockapplet.*.*.*
%attr(0755,root,root) %{_libdir}/libkhelpcenter.*.*.*
%attr(0755,root,root) %{_libdir}/libkminipagerapplet.*.*.*
%attr(0755,root,root) %{_libdir}/libkrunapplet.*.*.*
%attr(0755,root,root) %{_libdir}/libk[stu]*.*.*.*
%attr(0755,root,root) %{_libdir}/lib[qs]*.*.*.*
%attr(0755,root,root) %{_libdir}/libkwindefault.*.*.*
%attr(0755,root,root) %{_libdir}/konsole.??
%attr(0755,root,root) %{_libdir}/libkonsolepart.??
%attr(0755,root,root) %{_libdir}/libkwinb2.??
%attr(0755,root,root) %{_libdir}/libkwinkde1.??
%attr(0755,root,root) %{_libdir}/libkwinkstep.??
%attr(0755,root,root) %{_libdir}/libkwinlaptop.??
%attr(0755,root,root) %{_libdir}/libkwinmodernsys.??
%attr(0755,root,root) %{_libdir}/libkwinriscos.??
%attr(0755,root,root) %{_libdir}/libkwinsystem.??
%attr(0755,root,root) %{_libdir}/libkwritepart.??
%attr(0755,root,root) %{_libdir}/libh*
%attr(0755,root,root) %{_libdir}/libkcm_[abcefhilmpsvx]*
%attr(0755,root,root) %{_libdir}/libkcm_k[ehinuw]*

%{_applnkdir}/*.desktop
%{_applnkdir}/Office/Editors/*.desktop
%{_applnkdir}/Amusements/*.desktop
%{_applnkdir}/Settings/FileBrowsing
%{_applnkdir}/Settings/Help
%{_applnkdir}/Settings/Information
%{_applnkdir}/Settings/LookNFeel
%{_applnkdir}/Settings/Network
%{_applnkdir}/Settings/Peripherals
%{_applnkdir}/Settings/Personalization
%{_applnkdir}/Settings/PowerControl
%{_applnkdir}/Settings/Sound
%{_applnkdir}/Settings/System
%{_applnkdir}/Settings/WebBrowsing
%{_applnkdir}/System/*.desktop
%{_applnkdir}/System/ScreenSavers
%{_applnkdir}/Utilities/*.desktop
%{_applnkdir}/.hidden

%{_datadir}/apps/clockapplet
%{_datadir}/apps/drkonqi
%{_datadir}/apps/kappfinder
%{_datadir}/apps/kbookmark
%{_datadir}/apps/kcmlocale
%{_datadir}/apps/kcontrol
%{_datadir}/apps/kdcop
%{_datadir}/apps/kdesktop
%{_datadir}/apps/kdewizard
%{_datadir}/apps/kdisplay
%{_datadir}/apps/khelpcenter
%{_datadir}/apps/kicker
%{_datadir}/apps/kio_info
%{_datadir}/apps/kmenuedit
%{_datadir}/apps/konsole
%{_datadir}/apps/kscreensaver
%{_datadir}/apps/ksplash
%{_datadir}/apps/ksysguard
%{_datadir}/apps/kwin
%{_datadir}/apps/kwrite
%{_datadir}/apps/quickbrowser

%{_docdir}/HTML/en/kcontrol
%{_docdir}/HTML/en/kdebugdialog
%{_docdir}/HTML/en/kdesu
%{_docdir}/HTML/en/khelpcenter
%{_docdir}/HTML/en/kicker
%{_docdir}/HTML/en/klipper
%{_docdir}/HTML/en/kmenuedit
%{_docdir}/HTML/en/konsole
%{_docdir}/HTML/en/kpager
%{_docdir}/HTML/en/ksysguard
%{_docdir}/HTML/en/kwrite

%{_pixmapsdir}/hicolor/*x*/actions/*
%{_pixmapsdir}/hicolor/*x*/apps/*
%{_pixmapsdir}/hicolor/*x*/devices/*
%{_pixmapsdir}/locolor/*x*/actions/*
%{_pixmapsdir}/locolor/*x*/apps/*
%{_pixmapsdir}/locolor/*x*/devices/*

%{_datadir}/config/*
%{_datadir}/mimelnk/application/*
%{_datadir}/services/*
%{_datadir}/sounds
%{_datadir}/templates
%{_datadir}/wallpapers
%{_datadir}/locale/C/*
%{_datadir}/locale/l10n/*/*
%{_datadir}/locale/l10n/*.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/kmenuedit.??
%{_libdir}/libclockapplet.??
%{_libdir}/libkhelpcenter.??
%{_libdir}/libkonq.??
%{_libdir}/libkminipagerapplet.??
%{_libdir}/libkrunapplet.??
%{_libdir}/libk[stu]*.??
%{_libdir}/libkwindefault.??
%{_libdir}/lib[qs]*.??

%files -n kdm
%defattr(644,root,root,755)
%doc %{_docdir}/HTML/en/kdm
%attr(0755,xdm,xdm) %{_bindir}/chooser
%attr(0755,xdm,xdm) %{_bindir}/kdm
%attr(0755,root,root) %{_libdir}/libkcm_kdm.??
%attr(0755,xdm,xdm) %{_sysconfdir}/X11/kdm
%attr(0640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/pam.d/kdm
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/security/blacklist.kdm
%attr(0754,root,root) %{_sysconfdir}/rc.d/init.d/kdm
%{_datadir}/apps/kdm

%files -n konqueror
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/konqueror
%attr(0755,root,root) %{_libdir}/libkonq.*.*.*
%attr(0755,root,root) %{_libdir}/konqueror.??
%attr(0755,root,root) %{_libdir}/libkcm_konq*
%attr(0755,root,root) %{_libdir}/libkonqdirtree.??
%attr(0755,root,root) %{_libdir}/libkonqiconview.??
%attr(0755,root,root) %{_libdir}/libkonqlistview.??
%{_applnkdir}/Network/WWW/*.desktop
%{_datadir}/apps/konqiconview
%{_datadir}/apps/konqlistview
%{_datadir}/apps/konqueror
%{_docdir}/HTML/en/konqueror
