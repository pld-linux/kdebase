Summary:     	K Desktop Environment - core files
Summary(pl): 	K Desktop Environment - pliki ¶rodowiska
Name:        	kdebase
Version:     	1.93
Release: 3
Copyright:   	GPL
Group:       	X11/KDE/Base
Group(pl):      X11/KDE
Vendor:      	The KDE Team
Source0:      	ftp://ftp.kde.org/pub/kde/unstable/distribution/2.0Beta4/tar/src/%{name}-%{version}.tar.bz2
Source1:     	kdeenv
Patch0:		kdebase-DESTDIR.patch
BuildRequires:	qt >= 2.2.0
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	pam-devel
BuildRequires:	OpenGL-devel
Requires:	kdelibs = %{version}
Requires:	qt >= 2.2.0
BuildRoot:   	/tmp/%{name}-%{version}-root

%define		_prefix 		/usr/X11R6
%define		_sysconfdir		/etc/X11/kde
%define		_kde_htmldir		%{_datadir}/doc/HTML
%define		_kde_icondir		%{_datadir}/pixmaps
%define		_kde_minidir		%{_kde_icondir}/mini
%define		_kde_appsdir		%{_datadir}/applnk
%define		_kde_sounddir		%{_datadir}/sounds
%define		_kde_datadir		%{_datadir}/apps
%define		_kde_locale		%{_datadir}/locale
%define		_kde_cgidir		%{_libdir}/kde/cgi-bin
%define		_kde_confdir		%{_sysconfdir}
%define		_kde_mimedir		%{_datadir}/mimelnk
%define		_kde_toolbardir		%{_datadir}/kde/toolbar
%define		_kde_wallpaperdir	%{_datadir}/wallpapers
%define		_kde_bindir		%{_bindir}
%define		_kde_partsdir		%{_libdir}/parts

%description
KDE specific files. Used by core KDE applications.
Package includes:
  KDE menu hierarchy
  kappfinder - script installing some non-KDE apps in KDE menu
  krootwm - module used by KWM and KFM
  kaudio - audio server for KDE

%description -l pl
Pliki specyficzne dla ¶rodowiska KDE i wykorzystywane przez g³ówne
aplikacje KDE.
Pakiet zawiera:
  Hierarchiê menu KDE
  kappfinder - skrypt u³awiaj±cy uruchamianie niektórych programów spoza KDE
  krootwm - modu³ wykorzystywany przez kwm i kfm
  kaudio - serwer d¼wiêku dla KDE

%package kcontrol
Summary:     	KDE Control Center
Summary(pl): 	Centrum Sterowania KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}
Requires:	%{name} = %{version}

%description kcontrol
KDE Control Center - easy way to access KDE configuration modules
and several useful modules.

%description -l pl kcontrol
Centrum sterowania KDE - program obs³ugi modu³ów konfiguracyjnych KDE
oraz kilka przydatnych modu³ów.

%package khelpcenter
Summary:     	KDE Help System	
Summary(pl): 	System Pomocy KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description khelpcenter
This program is used for viewing KDE applications' online manual.
It is also convinient for reading system's man pages and "info" documentation.

%description -l pl khelpcenter
Program umo¿liwiaj±cy przegl±danie dokumentacji applikacji KDE.
Jest te¿ wygodnym narzêdziem do ogl±dania stron man i dokumentacji "info".

%package kdm
Summary:     	KDE Display Manager	
Summary(pl): 	KDE Display Manager
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kdm
It is KDE replacement for XDM.
It manages local and remote X11 displays.

%description -l pl kdm
Zamiennik XDM rodem z KDE.

%package kdesu
Summary:     	KDE Display Manager	
Summary(pl): 	KDE Display Manager
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kdesu
It is KDE replacement for XDM.
It manages local and remote X11 displays.

%description -l pl kdesu
Zamiennik XDM rodem z KDE.

%package kstart
Summary:     	KDE Display Manager	
Summary(pl): 	KDE Display Manager
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kstart
It is KDE replacement for XDM.
It manages local and remote X11 displays.

%description -l pl kstart
Zamiennik XDM rodem z KDE.

%package ksmserver
Summary:     	KDE Display Manager	
Summary(pl): 	KDE Display Manager
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description ksmserver
It is KDE replacement for XDM.
It manages local and remote X11 displays.

%description -l pl ksmserver
Zamiennik XDM rodem z KDE.

%package konsole
Summary:     	KDE Display Manager	
Summary(pl): 	KDE Display Manager
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description konsole
It is KDE replacement for XDM.
It manages local and remote X11 displays.

%description -l pl konsole
Zamiennik XDM rodem z KDE.

%package kfind
Summary:     	KDE file finder	
Summary(pl): 	Wyszukiwarka plików dla KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kfind
A simple frontend to find and grep.

%description -l pl kfind
Prosty interfejs dla poleceñ find i grep.

%package kfm
Summary:     	KDE file manager	
Summary(pl): 	Mened¿er plików KDE
Group:       	X11/KDE/Base
Requires:    	%{name} = %{version}
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version} 

%description kfm
A file manager and a web browser for KDE.

%description -l pl kfm
Mened¿er plików i przegl±darka WWW dla KDE.

%package kappfinder
Summary:     	KDE file manager	
Summary(pl): 	Mened¿er plików KDE
Group:       	X11/KDE/Base
Requires:    	%{name} = %{version}
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version} 

%description kappfinder
A file manager and a web browser for KDE.

%description -l pl kappfinder
Mened¿er plików i przegl±darka WWW dla KDE.

%package kfontmanager
Summary:     	KDE font manager	
Summary(pl): 	Mened¿er fontów KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kfontmanager
A font manager for KDE.
It may be used to choose fonts which can be used by KDE.

%description -l pl kfm
Mened¿er fontów dla KDE.
Mo¿e byæ wykorzystany do okre¶lenia listy czcionek dostêpnych dla aplikacji KDE.

%package kmenuedit
Summary:     	KDE Menu Editor	
Summary(pl): 	Edytor menu KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kmenuedit
A system menu editor for KDE.

%description -l pl kmenuedit
Edytor menu systemowego KDE.

%package kpanel
Summary:     	KDE Panel	
Summary(pl): 	Panel KDE
Group:       	X11/KDE/Base
Requires:    	kdebase-kfm = %{version}
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version} 

%description kpanel
An easy way to start applications and switch desktops in KDE.

%description -l pl kpanel
U³atwia startowanie aplikacji oraz prze³±czanie ekranów w KDE.

%package kscreensaver
Summary:     	KDE Screen-savers
Summary(pl): 	Screen-savery dla KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kscreensaver
Several screen-savers for KDE.

%description -l pl kscreensaver
"Oszczêdzacze ekranu" dla KDE

%package kvt
Summary:     	KDE terminal emulator
Summary(pl): 	Emulator terminala dla KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kvt
Terminal emulator for KDE.

%description -l pl kvt
Emulator terminala znakowego dla KDE

%package kikbd
Summary:     	KDE international keyboard
Summary(pl): 	Klawiatura miedzynarodowa dla KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kikbd
International keyboard for KDE.

%description -l pl kikbd
Klawiatura miedzynarodowa dla KDE

%package kicker
Summary:     	KDE international keyboard
Summary(pl): 	Klawiatura miedzynarodowa dla KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kicker
International keyboard for KDE.

%description -l pl kicker
Klawiatura miedzynarodowa dla KDE

%package kioslave
Summary:     	KDE international keyboard
Summary(pl): 	Klawiatura miedzynarodowa dla KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kioslave
International keyboard for KDE.

%description -l pl kioslave
Klawiatura miedzynarodowa dla KDE

%package konqueror
Summary:     	KDE international keyboard
Summary(pl): 	Klawiatura miedzynarodowa dla KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description konqueror
International keyboard for KDE.

%description -l pl konqueror
Klawiatura miedzynarodowa dla KDE

%package kwm
Summary:     	KDE window manager
Summary(pl): 	Mened¿er okien KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kwm
Window manager for KDE

%description -l pl kwm
Mened¿er okien dla KDE

%package kwin
Summary:     	KDE window manager
Summary(pl): 	Mened¿er okien KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kwin
Window manager for KDE

%description -l pl kwin
Mened¿er okien dla KDE

%package kxmlrpc
Summary:     	KDE window manager
Summary(pl): 	Mened¿er okien KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kxmlrpc
Window manager for KDE

%description -l pl kxmlrpc
Mened¿er okien dla KDE

%package kdesktop
Summary:     	KDE desktop
Summary(pl): 	Mened¿er okien KDE
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kdesktop
Window manager for KDE

%description -l pl kdesktop
Mened¿er okien dla KDE

%package kbgndwm
Summary:     	KDE background manager and wallpapers
Summary(pl): 	Tapety oraz mened¿er t³a KDE 
Group:       	X11/KDE/Base
Requires:	qt >= 2.2.0_beta2
Requires:	kdelibs = %{version}

%description kbgndwm
Background manager for KDE.
It is responsible for displaying KDE wallpapers.
Sample wallpapers are also included.

%description -l pl kbgndwm
Mened¿er t³a dla KDE.
Odpowiedzialny za wy¶wietlanie tapet.
Przyk³adowe tapety s± tak¿e do³±czone

%prep
%setup -q
%patch0 -p1
%build

export KDEDIR=%{_prefix}

kde_htmldir=%{_kde_htmldir}
kde_icondir=%{_kde_icondir}
kde_minidir=%{_kde_minidir}
kde_appsdir=%{_kde_appsdir}
kde_sounddir=%{_kde_sounddir}
kde_datadir=%{_kde_datadir}
kde_locale=%{_kde_locale}
kde_cgidir=%{_kde_cgidir}
kde_confdir=%{_kde_confdir}
kde_mimedir=%{_kde_mimedir}
kde_toolbardir=%{_kde_toolbardir}
kde_wallpaperdir=%{_kde_wallpaperdir}
kde_bindir=%{_kde_bindir}
kde_partsdir=%{_kde_partsdir}
export  kde_htmldir kde_icondir kde_minidir kde_appsdir kde_sounddir \
	kde_datadir kde_locale kde_cgidir kde_confdir kde_mimedir \
	kde_toolbardir kde_wallpaperdir kde_bindir kde_partsdir

make -f Makefile.cvs

CXXFLAGS="$RPM_OPT_FLAGS -Wall";	export CXXFLAGS
CFLAGS="$RPM_OPT_FLAGS -Wall";		export CFLAGS
LDFLAGS="-s" ; 				export LDFLAGS
%configure \
 	--with-pam=yes

%{__make} KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/kde
install -d $RPM_BUILD_ROOT/usr/share/fonts/misc

%{__make} \
	RUN_KAPPFINDER=no \
	DESTDIR=$RPM_BUILD_ROOT \
	localedir="$RPM_BUILD_ROOT/usr/X11R6/share/locale" \
	install

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/kdeenv

# install fonts
install konsole/fonts/*.pcf.gz $RPM_BUILD_ROOT/usr/share/fonts/misc
strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :

#### KCONTROL
%post kcontrol -p /sbin/ldconfig
%postun kcontrol -p /sbin/ldconfig

#### KDESKTOP
%post kdesktop -p /sbin/ldconfig
%postun kdesktop -p /sbin/ldconfig

#### KHELPCENTER
%post khelpcenter -p /sbin/ldconfig
%postun khelpcenter -p /sbin/ldconfig

#### KICKER
%post kicker -p /sbin/ldconfig
%postun kicker -p /sbin/ldconfig

#### KIOSLAVE
%post kioslave -p /sbin/ldconfig
%postun kioslave -p /sbin/ldconfig

#### KONQUEROR
%post konqueror -p /sbin/ldconfig
%postun konqueror -p /sbin/ldconfig

#### KONSOLE
%post konsole
/sbin/ldconfig
(cd /usr/share/fonts/misc;mkfontdir)

%postun konsole
/sbin/ldconfig
(cd /usr/share/fonts/misc;mkfontdir)

#### KWIN
%post kwin -p /sbin/ldconfig
%postun kwin -p /sbin/ldconfig

#### KXMLRPD
%post kxmlrpc -p /sbin/ldconfig
%postun kxmlrpc -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
#################################################
#             drkonqi
#################################################
#%files drkonqi
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/drkonqi

#################################################
#             kdebugdialog
#################################################
#%files kdebugdialog
#%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kdebugdialog

#################################################
#             kdewizard
#################################################
#%files kdewizard
#%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kdewizard
%attr(755,root,root) %{_bindir}/kprintwrapper
%attr(755,root,root) %{_bindir}/krunonce

%config(missingok) %{_applnkdir}/Utilities/kdewizard.desktop

%{_datadir}/apps/kdewizard/

#################################################
#             kdesu
#################################################
%files kdesu
%defattr(644,root,root,755)

##################################################
##             kcheckpass
##################################################
#%files kcheckpass
#%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kcheckpass

%attr(755,root,root) %{_bindir}/kdesu
%attr(2750,root,admin) %{_bindir}/kdesud


#################################################
#             kappfinder
#################################################
%files kappfinder
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kappfinder

%config(missingok) %{_applnkdir}/System/kappfinder.desktop

%{_datadir}/apps/kappfinder


#################################################
#            KCONTROL - checking OK
#################################################
%files kcontrol
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcmshell
%attr(755,root,root) %{_bindir}/kcontrol
%attr(755,root,root) %{_bindir}/krdb

%attr(755,root,root) %{_libdir}/libkcm_arts.??
%attr(755,root,root) %{_libdir}/libkcm_clock.??
%attr(755,root,root) %{_libdir}/libkcm_display.??
%attr(755,root,root) %{_libdir}/libkcm_email.??
%attr(755,root,root) %{_libdir}/libkcm_filetypes.??
%attr(755,root,root) %{_libdir}/libkcm_info.??
%attr(755,root,root) %{_libdir}/libkcm_input.??
%attr(755,root,root) %{_libdir}/libkcm_kdm.??
%attr(755,root,root) %{_libdir}/libkcm_keys.??
%attr(755,root,root) %{_libdir}/libkcm_kicker.??
%attr(755,root,root) %{_libdir}/libkcm_kio.??
%attr(755,root,root) %{_libdir}/libkcm_knotify.??
%attr(755,root,root) %{_libdir}/libkcm_konq.??
%attr(755,root,root) %{_libdir}/libkcm_konqhtml.??
%attr(755,root,root) %{_libdir}/libkcm_kurifilt.??
%attr(755,root,root) %{_libdir}/libkcm_kwindesktop.??
%attr(755,root,root) %{_libdir}/libkcm_kwinmouse.??
%attr(755,root,root) %{_libdir}/libkcm_kwinoptions.??
%attr(755,root,root) %{_libdir}/libkcm_locale.??
%attr(755,root,root) %{_libdir}/libkcm_passwords.??
%attr(755,root,root) %{_libdir}/libkcm_samba.??
%attr(755,root,root) %{_libdir}/libkcm_sample.??
%attr(755,root,root) %{_libdir}/libkcm_syssound.??

%attr(755,root,root) %{_libdir}/libkshorturifilter.la
%attr(755,root,root) %{_libdir}/libkshorturifilter.so.*.*.*
%attr(755,root,root) %{_libdir}/libkuriikwsfilter.la
%attr(755,root,root) %{_libdir}/libkuriikwsfilter.so.*.*.*

%{_datadir}/apps/kcontrol/
%{_datadir}/apps/kdisplay/

%config(missingok) %{_applnkdir}/Control/SysInfo.desktop
%config(missingok) %{_applnkdir}/Control/System.desktop
%config(missingok) %{_applnkdir}/Control/User.desktop

%{_datadir}/services/kshorturifilter.desktop
%{_datadir}/services/kuriikwsfilter.desktop

%config(missingok) %{_applnkdir}/Settings/

%config(missingok) %{_datadir}/config/kuriikwsfilterrc

%attr(644,root,root) %{_datadir}/locale/C/entry.desktop
%attr(644,root,root) %{_datadir}/locale/C/flag.png

%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/bell.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/buttons.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/colors.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/fonts.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/kcmdevices.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/kcmkwm.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/kcmmemory.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/kcmpartitions.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/kcmpci.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/kcmprocessor.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/kcmscsi.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/kcmsound.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/kcmx.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/kcontrol.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/knotify.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/locale.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/mouse.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/screensaver.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/style.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/titlebar.png
%attr(644,root,root) %{_datadir}/icons/hicolor/32x32/apps/winprops.png

%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/background.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/bell.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/buttons.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/colors.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/fonts.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/kcmdevices.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/kcmkwm.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/kcmmemory.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/kcmpartitions.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/kcmpci.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/kcmprocessor.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/kcmscsi.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/kcontrol.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/keyboard.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/knotify.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/locale.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/mouse.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/screensaver.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/style.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/titlebar.png
%attr(644,root,root) %{_datadir}/icons/hicolor/48x48/apps/winprops.png

%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/application_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/background.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/bell.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/buttons.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/colors.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/desktop_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/energy.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/fonts.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/general_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/information_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/input_devices_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcmdevices.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcmkwm.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcmmemory.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcmpartitions.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcmpci.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcmprocessor.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcmscsi.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcmsound.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcmx.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcontrol.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcontrol_system.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kcontrol_user.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/keyboard.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/knotify.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/locale.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/mouse.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/network_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/panel_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/samba.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/screensaver.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/smbstatus.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/sound_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/style.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/titlebar.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/winprops.png

%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/application_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/background.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/bell.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/buttons.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/colors.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/desktop_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/energy.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/fonts.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/general_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/information_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/input_devices_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/kcmdevices.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/kcmkwm.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/kcmmemory.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/kcmpartitions.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/kcmpci.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/kcmprocessor.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/kcmscsi.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/kcmsound.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/kcmx.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/kcontrol.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/keyboard.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/knotify.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/locale.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/mouse.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/network_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/panel_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/samba.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/screensaver.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/sound_settings.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/style.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/titlebar.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/winprops.png

#################################################
#             kdesktop
#################################################
%files kdesktop
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kdesktop
%attr(755,root,root) %{_bindir}/kdmdesktop

%attr(755,root,root) %{_libdir}/kdesktop.??

%attr(644,root,root) %{_includedir}/KBackgroundIface.h
%attr(644,root,root) %{_includedir}/KDesktopIface.h
%attr(644,root,root) %{_includedir}/KScreensaverIface.h

%attr(644,root,root) %{_datadir}/icons/locolor/*x*/apps/error.png

%{_datadir}/apps/kdesktop/


#################################################
#            kdm
#################################################
%files kdm
%defattr(644,root,root,755)

%attr(755, root, root) %{_bindir}/chooser
%attr(755, root, root) %{_bindir}/kdm

%{_datadir}/apps/kdm/

%{_datadir}/config/kdmrc

%{_datadir}/wallpapers/kdm_bg.jpg

#################################################
#            kfontmanager
#################################################
%files kfontmanager
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kfontmanager

%config(missingok) %{_applnkdir}/System/Kfontmanager.desktop

%{_datadir}/icons/hicolor/*x*/apps/kfontmanager.png
%{_datadir}/icons/locolor/*x*/apps/kfontmanager.png

#################################################
#            khelpcenter
#################################################
%files khelpcenter
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/khelpcenter
%attr(755,root,root) %{_bindir}/kwelcome

%attr(644,root,root) %{_includedir}/khc_*.h

%attr(755,root,root) %{_libdir}/libkhc.la
%attr(755,root,root) %{_libdir}/libkhc.so.*.*.*
%attr(755,root,root) %{_libdir}/libkhelpcenter.la
%attr(755,root,root) %{_libdir}/libkhelpcenter.so.*.*.*

%config(missingok) %{_applnkdir}/Help.desktop
%config(missingok) %{_applnkdir}/Utilities/kinfobrowser.desktop

%{_datadir}/apps/khelpcenter/
%{_datadir}/apps/kwelcome/

%{_datadir}/icons/hicolor/*x*/apps/khelpcenter.png
%{_datadir}/icons/locolor/32x32/apps/khelpcenter.png

%{_datadir}/icons/locolor/16x16/apps/khelpcenter.png
%{_datadir}/icons/locolor/16x16/apps/helpbook.png
%{_datadir}/icons/locolor/16x16/apps/helpbook_open.png
%{_datadir}/icons/locolor/16x16/apps/helpdoc.png

%{_datadir}/services/khelpcenter.desktop

%{_datadir}/toolbar/hidenavigator.png
%{_datadir}/toolbar/shownavigator.png

#################################################
#             kicker
#################################################
%files kicker
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kicker
%attr(755,root,root) %{_bindir}/exampleapplet
%attr(755,root,root) %{_bindir}/eyesapplet

%attr(755,root,root) %{_libdir}/libkasbarapplet.la
%attr(755,root,root) %{_libdir}/libkasbarapplet.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdockapplet.la
%attr(755,root,root) %{_libdir}/libkdockapplet.so.*.*.*
%attr(755,root,root) %{_libdir}/libkminipagerapplet.la
%attr(755,root,root) %{_libdir}/libkminipagerapplet.so.*.*.*
%attr(755,root,root) %{_libdir}/libkoolclockapplet.la
%attr(755,root,root) %{_libdir}/libkoolclockapplet.so.*.*.*
%attr(755,root,root) %{_libdir}/libktaskbarapplet.la
%attr(755,root,root) %{_libdir}/libktaskbarapplet.so.*.*.*

%config(missingok) %{_applnkdir}/Toys/

%{_datadir}/apps/kicker/
%{_datadir}/apps/quickbrowser/

%attr(644,root,root) %{_datadir}/icons/hicolor/*x*/apps/go.png
%attr(644,root,root) %{_datadir}/icons/hicolor/*x*/apps/kdisknav.png
%attr(644,root,root) %{_datadir}/icons/hicolor/*x*/apps/package_favourite.png
%attr(644,root,root) %{_datadir}/icons/hicolor/*x*/apps/window_list.png

%attr(644,root,root) %{_datadir}/icons/locolor/*x*/apps/go.png
%attr(644,root,root) %{_datadir}/icons/locolor/*x*/apps/kdisknav.png
%attr(644,root,root) %{_datadir}/icons/locolor/*x*/apps/package_favourite.png
%attr(644,root,root) %{_datadir}/icons/locolor/*x*/apps/window_list.png

%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/default.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/mini_run.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/panel.png

#################################################
#            KIKBD - can't compile !!!
#	missing file kcontrol.h
#################################################

%files kikbd 
%defattr(644,root,root,755)

#################################################
#             kioslave
#################################################
%files kioslave
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/man2html

%attr(755,root,root) %{_libdir}/kio_info.??
%attr(755,root,root) %{_libdir}/kio_man.??
%attr(755,root,root) %{_libdir}/kio_nntp.??
%attr(755,root,root) %{_libdir}/kio_pop3.??
%attr(755,root,root) %{_libdir}/kio_smb.??

%attr(755,root,root) %{_libdir}/libsmb++.la
%attr(755,root,root) %{_libdir}/libsmb++.so.*.*.*

%{_datadir}/apps/kio_info/

%{_datadir}/config/protocols/info.desktop
%{_datadir}/config/protocols/man.desktop
%{_datadir}/config/protocols/nntp.desktop
%{_datadir}/config/protocols/pop3.desktop
%{_datadir}/config/protocols/smb.desktop

#################################################
#             konqueror
#################################################
%files konqueror
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/kfmexec
%attr(755,root,root) %{_bindir}/konqueror

%attr(644,root,root) %{_includedir}/KonquerorIface.h

%attr(644,root,root) %{_includedir}/konq*.h
%attr(644,root,root) %{_includedir}/kbookmark*.h
%attr(644,root,root) %{_includedir}/kdirlister.h
%attr(644,root,root) %{_includedir}/kfileivi.h
%attr(644,root,root) %{_includedir}/knewmenu.h

%attr(755,root,root) %{_libdir}/libkonq.la
%attr(755,root,root) %{_libdir}/libkonq.so.*.*.*
%attr(755,root,root) %{_libdir}/konqueror.??
%attr(755,root,root) %{_libdir}/libkonqdirtree.la
%attr(755,root,root) %{_libdir}/libkonqdirtree.so.*.*.*
%attr(755,root,root) %{_libdir}/libkonqiconview.la
%attr(755,root,root) %{_libdir}/libkonqiconview.so.*.*.*
%attr(755,root,root) %{_libdir}/libkonqlistview.la
%attr(755,root,root) %{_libdir}/libkonqlistview.so.*.*.*

%config(missingok) %{_applnkdir}/Home.desktop
%config(missingok) %{_applnkdir}/Trash.desktop
%config(missingok) %{_applnkdir}/System/Arrange.desktop
%config(missingok) %{_applnkdir}/System/kfmclient.desktop
%config(missingok) %{_applnkdir}/System/konquerorsu.desktop

%{_datadir}/apps/konqiconview/
%{_datadir}/apps/konqlistview/
%{_datadir}/apps/konqueror/

%attr(644,root,root) %{_datadir}/icons/hicolor/*x*/apps/konqueror.png

%attr(644,root,root) %{_datadir}/icons/locolor/*x*/apps/konqueror.png

%attr(644,root,root) %{_datadir}/services/konq*.desktop

%attr(644,root,root) %{_datadir}/servicetypes/konq*.desktop

#################################################
#             KONSOLE
#################################################
%files konsole
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/konsole*
%attr(755,root,root) %{_bindir}/kwrited

%attr(755,root,root) %{_libdir}/libkonsole.so.*.*.*
%attr(755,root,root) %{_libdir}/libkonsole.la
%attr(755,root,root) %{_libdir}/kwrited.so
%attr(755,root,root) %{_libdir}/kwrited.la

%config(missingok) %{_applnkdir}/System/konsole.desktop
%config(missingok) %{_applnkdir}/System/konsolesu.desktop

%{_datadir}/mimelnk/application/x-konsole.desktop

%{_datadir}/doc/HTML/en/konsole

%{_datadir}/apps/konsole
%{_datadir}/icons/hicolor/*x*/apps/konsole.*
%{_datadir}/icons/locolor/*x*/apps/konsole.*

%attr(644,root,root) %{_datadir}/toolbar/brightness.png
%attr(644,root,root) %{_datadir}/toolbar/colourness.png
%attr(644,root,root) %{_datadir}/toolbar/contrast.png

%attr(644,root,root) /usr/share/fonts/misc/9x15.pcf.gz
%attr(644,root,root) /usr/share/fonts/misc/console8x16.pcf.gz
%attr(644,root,root) /usr/share/fonts/misc/console8x8.pcf.gz

#################################################
#            KSCREENSAVER - checking OK
#################################################
%files kscreensaver 
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kxsconfig
%attr(755,root,root) %{_bindir}/kxsrun
%attr(755,root,root) %{_bindir}/*.kss

%config(missingok) %{_applnkdir}/System/ScreenSavers/*.desktop

%{_datadir}/apps/kscreensaver/

%attr(644,root,root) %{_datadir}/config/attractionrc
%attr(644,root,root) %{_datadir}/config/bouboulerc
%attr(644,root,root) %{_datadir}/config/coralrc
%attr(644,root,root) %{_datadir}/config/crystalrc
%attr(644,root,root) %{_datadir}/config/decayscreenrc
%attr(644,root,root) %{_datadir}/config/deluxerc
%attr(644,root,root) %{_datadir}/config/demonrc
%attr(644,root,root) %{_datadir}/config/epicyclerc
%attr(644,root,root) %{_datadir}/config/fadeplotrc
%attr(644,root,root) %{_datadir}/config/flamerc
%attr(644,root,root) %{_datadir}/config/flowrc
%attr(644,root,root) %{_datadir}/config/forestrc
%attr(644,root,root) %{_datadir}/config/gearsrc
%attr(644,root,root) %{_datadir}/config/gravrc
%attr(644,root,root) %{_datadir}/config/halorc
%attr(644,root,root) %{_datadir}/config/interferencerc
%attr(644,root,root) %{_datadir}/config/kumpparc
%attr(644,root,root) %{_datadir}/config/laserrc
%attr(644,root,root) %{_datadir}/config/lissierc
%attr(644,root,root) %{_datadir}/config/penroserc
%attr(644,root,root) %{_datadir}/config/rocksrc
%attr(644,root,root) %{_datadir}/config/sliprc

%{_datadir}/icons/locolor/*x*/apps/kscreensaver.png

#################################################
#             ksmserver
#################################################
%files ksmserver
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/ksmserver

#################################################
#             kstart
#################################################
%files kstart
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kstart

#################################################
#             kwin
#################################################
%files kwin
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kwin

%attr(755,root,root) %{_libdir}/kwin.??
%attr(755,root,root) %{_libdir}/libkwinb2.la
%attr(755,root,root) %{_libdir}/libkwinb2.so.*.*.*
%attr(755,root,root) %{_libdir}/libkwinkstep.la
%attr(755,root,root) %{_libdir}/libkwinkstep.so.*.*.*
%attr(755,root,root) %{_libdir}/libkwinlaptop.la
%attr(755,root,root) %{_libdir}/libkwinlaptop.so.*.*.*
%attr(755,root,root) %{_libdir}/libkwinriscos.la
%attr(755,root,root) %{_libdir}/libkwinriscos.so.*.*.*
%attr(755,root,root) %{_libdir}/libkwinsystem.la
%attr(755,root,root) %{_libdir}/libkwinsystem.so.*.*.*

%{_datadir}/apps/kwin
%{_datadir}/apps/kwm

%{_datadir}/icons/hicolor/*x*/apps/kwin.png
%{_datadir}/icons/locolor/*x*/apps/kwin.png

#################################################
#             kxmlrpc
#################################################
%files kxmlrpc
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kxmlrpcd

%attr(755,root,root) %{_libdir}/kxmlrpcd.??
