Summary:	K Desktop Environment - core files
Summary(pl):	K Desktop Environment - pliki ¶rodowiska
Name:		kdebase
Version:	2.0
Release:	4
License:	GPL
Group:		X11/KDE
Group(de):	X11/KDE
Group(pl):	X11/KDE
Vendor:		The KDE Team
Source0:	ftp://ftp.kde.org/pub/kde/stable/2.0/distribution/generic/tar/src/%{name}-%{version}.tar.bz2
Source1:	kdeenv
Source2:	kde.pamd
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
Requires:	kdelibs = %{version}
Requires:	qt >= 2.2.1-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix 		/usr/X11R6
%define		_includedir		%{_includedir}/kde
%define		_bindir			%{_prefix}/bin
%define		_datadir		%{_prefix}/share
%define		_libdir			%{_prefix}/lib
%define		_includedir		%{_prefix}/include
%define		_docdir			%{_datadir}/doc
%define		_applnkdir		%{_datadir}/applnk

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

%package kcontrol
Summary:	KDE Control Center
Summary(pl):	Centrum Sterowania KDE
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}
Requires:	%{name} = %{version}

%description kcontrol
KDE Control Center - easy way to access KDE configuration modules and
several useful modules.

%description -l pl kcontrol
Centrum sterowania KDE - program obs³ugi modu³ów konfiguracyjnych KDE
oraz kilka przydatnych modu³ów.

%package khelpcenter
Summary:	KDE Help System	
Summary(pl):	System Pomocy KDE
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}

%description khelpcenter
This program is used for viewing KDE applications' online manual. It
is also convinient for reading system's man pages and "info"
documentation.

%description -l pl khelpcenter
Program umo¿liwiaj±cy przegl±danie dokumentacji applikacji KDE. Jest
te¿ wygodnym narzêdziem do ogl±dania stron man i dokumentacji "info".

%package kdm
Summary:	KDE Display Manager	
Summary(pl):	KDE Display Manager
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}

%description kdm
It is KDE replacement for XDM. It manages local and remote X11
displays.

%description -l pl kdm
Zamiennik XDM rodem z KDE.

%package konsole
Summary:	KDE Display Manager	
Summary(pl):	KDE Display Manager
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}

%description konsole
It is KDE replacement for XDM. It manages local and remote X11
displays.

%description -l pl konsole
Zamiennik XDM rodem z KDE.

%package kscreensaver
Summary:	KDE Screen-savers
Summary(pl):	Screen-savery dla KDE
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}

%description kscreensaver
Several screen-savers for KDE.

%description -l pl kscreensaver
"Oszczêdzacze ekranu" dla KDE

%package kicker
Summary:	KDE international keyboard
Summary(pl):	Klawiatura miedzynarodowa dla KDE
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}

%description kicker
International keyboard for KDE.

%description -l pl kicker
Klawiatura miedzynarodowa dla KDE

%package kioslave
Summary:	KDE international keyboard
Summary(pl):	Klawiatura miedzynarodowa dla KDE
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}

%description kioslave
International keyboard for KDE.

%description -l pl kioslave
Klawiatura miedzynarodowa dla KDE

%package konqueror
Summary:	KDE international keyboard
Summary(pl):	Klawiatura miedzynarodowa dla KDE
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}

%description konqueror
File manager for KDE.

%description -l pl konqueror
Menad¿er plików dla KDE

%package kwin
Summary:	KDE window manager
Summary(pl):	Mened¿er okien KDE
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}

%description kwin
Window manager for KDE

%description -l pl kwin
Mened¿er okien dla KDE

%package kxmlrpc
Summary:	KDE window manager
Summary(pl):	Mened¿er okien KDE
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}

%description kxmlrpc
Window manager for KDE

%description -l pl kxmlrpc
Mened¿er okien dla KDE

%package kdesktop
Summary:	KDE desktop
Summary(pl):	Mened¿er okien KDE
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}

%description kdesktop
Window manager for KDE

%description -l pl kdesktop
Mened¿er okien dla KDE

%package kwrite
Summary:	KDE office
Group:		X11/KDE
Requires:	qt >= 2.2.1-6
Requires:	kdelibs = %{version}

%description kwrite
Office


%prep
%setup -q
%build
make -f Makefile.cvs

%configure \
 	--with-pam=yes \
	--without-shadow \
	--disable-shadow \
	--with-extra-includes=%{_includedir} \
	--x-includes=%{_includedir}/kde \
	--with-qt-includes=%{_includedir}/qt 


export KDEDIR=/usr/X11R6/share/kde



%{__make} KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -d $RPM_BUILD_ROOT/usr/share/fonts/misc

%{__make} \
	RUN_KAPPFINDER=no \
	DESTDIR=$RPM_BUILD_ROOT \
	localedir="$RPM_BUILD_ROOT%{_prefix}/share/locale" \
	install

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/kdeenv
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/kde

#install applnk

rm -rf $RPM_BUILD_ROOT%{_applnkdir}


install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/Editors/
install -d $RPM_BUILD_ROOT%{_applnkdir}/.hidden/
install -d $RPM_BUILD_ROOT%{_applnkdir}/Internet

%define _applnk_FileBrows %{_applnkdir}/System/FileBrowsing
install -d $RPM_BUILD_ROOT%{_applnk_FileBrows}
install ./kcontrol/filetypes/filetypes.desktop $RPM_BUILD_ROOT%{_applnk_FileBrows}
install ./kcontrol/konq/kcmkonq.desktop $RPM_BUILD_ROOT%{_applnk_FileBrows}

%define _applnk_Help %{_applnkdir}/System/Help
install -d $RPM_BUILD_ROOT/%{_applnkdir}/System/Help
install ./khelpcenter/htmlsearch/htmlsearch.desktop $RPM_BUILD_ROOT/%{_applnk_Help}

%define _applnk_Infor %{_applnkdir}/System/Information
install -d $RPM_BUILD_ROOT%{_applnk_Infor}
install ./kcontrol/info/*.desktop $RPM_BUILD_ROOT%{_applnk_Infor}


%define _applnk_LNF %{_applnkdir}/Settings/LookNFeel/
install -d $RPM_BUILD_ROOT%{_applnk_LNF} 					
install ./kcontrol/colors/colors.desktop $RPM_BUILD_ROOT%{_applnk_LNF}         
install ./kcontrol/fonts/fonts.desktop $RPM_BUILD_ROOT%{_applnk_LNF}           
install ./kcontrol/icons/icons.desktop $RPM_BUILD_ROOT%{_applnk_LNF} 		
install ./kcontrol/knotify/kcmnotify.desktop $RPM_BUILD_ROOT%{_applnk_LNF} 	
install ./kcontrol/taskbar/kcmtaskbar.desktop $RPM_BUILD_ROOT%{_applnk_LNF} 	
install ./kcontrol/keys/keys.desktop $RPM_BUILD_ROOT%{_applnk_LNF} 		
install ./kcontrol/screensaver/screensaver.desktop $RPM_BUILD_ROOT%{_applnk_LNF} 
install ./kcontrol/kicker/panel.desktop $RPM_BUILD_ROOT%{_applnk_LNF} 		


%define _applnk_Desktop %{_applnk_LNF}/Desktop
install -d $RPM_BUILD_ROOT%{_applnk_Desktop}
install ./kcontrol/background/background.desktop $RPM_BUILD_ROOT%{_applnk_Desktop} 
install ./kcontrol/kwm/borders.desktop $RPM_BUILD_ROOT%{_applnk_Desktop} 
install ./kcontrol/konq/desktop.desktop  $RPM_BUILD_ROOT%{_applnk_Desktop} 
install ./kcontrol/desktop/virtualdesktops.desktop $RPM_BUILD_ROOT%{_applnk_Desktop} 

%define _applnk_Panel %{_applnk_LNF}/Panel 			
install -d $RPM_BUILD_ROOT%{_applnk_Panel} 			
%define _applnk_Themes %{_applnk_LNF}/Themes 			
install -d $RPM_BUILD_ROOT%{_applnk_Themes}  			
install ./kcontrol/icons/icons.desktop $RPM_BUILD_ROOT%{_applnk_Themes} 
install ./kcontrol/display/style.desktop $RPM_BUILD_ROOT%{_applnk_Themes} 
%define _applnk_Windows %{_applnk_LNF}/Windows 			
install -d $RPM_BUILD_ROOT%{_applnk_Windows} 			
install ./kcontrol/kwm/actions.desktop $RPM_BUILD_ROOT%{_applnk_Windows} 
install ./kcontrol/kwm/mouse.desktop $RPM_BUILD_ROOT%{_applnk_Windows} 


install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/SMB 			 
install ./kcontrol/samba/smb.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/SMB 

install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/Peripherals 		
install ./kcontrol/input/keyboard.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Peripherals 
install ./kcontrol/input/mouse.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Peripherals 

install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/Personalization
install ./kcontrol/crypto/crypto.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Personalization 
install ./kcontrol/email/email.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Personalization 
install ./kcontrol/access/kcmaccess.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Personalization 
install ./kxkb/kcmlayout.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Personalization 
install ./kcontrol/locale/language.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Personalization 
install ./kcontrol/passwords/passwords.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Personalization 

install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/Energy 
install ./kcontrol/energy/energy.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Energy 

install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/Multimedia  

install ./kcontrol/arts/arts.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Multimedia 
install ./kcontrol/bell/bell.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Multimedia 
install ./kcontrol/midi/midi.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/Multimedia 

install -d $RPM_BUILD_ROOT%{_applnkdir}/System
install ./kcontrol/clock/clock.desktop $RPM_BUILD_ROOT%{_applnkdir}/System
install ./kcontrol/kdm/kdm.desktop  $RPM_BUILD_ROOT%{_applnkdir}/System

install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/WebBrowsing
install ./kcontrol/kio/cookies.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/WebBrowsing
install ./kcontrol/ebrowsing/ebrowsing.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/WebBrowsing
install ./kcontrol/konqhtml/konqhtml.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/WebBrowsing
install ./nsplugins/control/nsplugin.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/WebBrowsing
install ./kcontrol/kio/proxy.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/WebBrowsing
install ./kcontrol/kio/useragent.desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/WebBrowsing

install -d $RPM_BUILD_ROOT%{_applnkdir}/System
install ./konqueror/Arrange.desktop $RPM_BUILD_ROOT%{_applnkdir}/System
install ./kappfinder/kappfinder.desktop $RPM_BUILD_ROOT%{_applnkdir}/System
install ./konqueror/kfmclient.desktop $RPM_BUILD_ROOT%{_applnkdir}/System
install ./legacyimport/klegacyimport.desktop $RPM_BUILD_ROOT%{_applnkdir}/System
install ./kmenuedit/kmenuedit.desktop $RPM_BUILD_ROOT%{_applnkdir}/System
install ./konqueror/konquerorsu.desktop $RPM_BUILD_ROOT%{_applnkdir}/System
install ./konsole/konsole.desktop $RPM_BUILD_ROOT%{_applnkdir}/System
install ./konsole/konsolesu.desktop $RPM_BUILD_ROOT%{_applnkdir}/System
install ./ksysguard/gui/ksysguard.desktop $RPM_BUILD_ROOT%{_applnkdir}/System

install -d $RPM_BUILD_ROOT%{_applnkdir}/System/ScreenSavers
install ./kscreensaver/*.desktop $RPM_BUILD_ROOT%{_applnkdir}/System/ScreenSavers

install -d $RPM_BUILD_ROOT%{_applnkdir}/Amusements/
install ./ktip/ktip.desktop  $RPM_BUILD_ROOT%{_applnkdir}/Amusements

install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install ./klipper/klipper.desktop  $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install ./kpager/kpager.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities

install ./khelpcenter/Help.desktop $RPM_BUILD_ROOT%{_applnkdir}
install ./kcontrol/kcontrol/KControl.desktop $RPM_BUILD_ROOT%{_applnkdir}
install ./konqueror/Home.desktop $RPM_BUILD_ROOT%{_applnkdir}

install ./kwrite/kwrite.desktop $RPM_BUILD_ROOT%{_applnkdir}/Office/Editors/
install ./konqueror/konqfilemgr.desktop $RPM_BUILD_ROOT%{_applnkdir}/.hidden/
install ./konqueror/konqbrowser.desktop $RPM_BUILD_ROOT%{_applnkdir}/Internet








# install fonts
install konsole/fonts/*.pcf.gz $RPM_BUILD_ROOT/usr/share/fonts/misc
#rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk/
%post 

ln -sf %{_docdir}/ %{_datadir}/doc
%postun
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

#### KXMLRPD
%post kwrite -p /sbin/ldconfig
%postun kwrite -p /sbin/ldconfig


%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             BASE
#################################################
%files 
%defattr(644,root,root,755)


%attr(0600,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/pam.d/kde
%attr(755,root,root) %{_bindir}/drkonqi
%attr(755,root,root) %{_bindir}/kdebugdialog
%attr(755,root,root) %{_bindir}/kdesu
%attr(755,root,root) %{_bindir}/kcheckpass
%attr(2750,root,root) %{_bindir}/kdesud
%attr(755,root,root) %{_bindir}/kappfinder
%attr(755,root,root) %{_bindir}/conttest
%attr(755,root,root) %{_bindir}/kdcop
%attr(755,root,root) %{_bindir}/kdeenv
%attr(755,root,root) %{_bindir}/klegacyimport
%attr(755,root,root) %{_bindir}/klipper
%attr(755,root,root) %{_bindir}/kpager
%attr(755,root,root) %{_bindir}/ksplash
%attr(755,root,root) %{_bindir}/ksysguard
%attr(755,root,root) %{_bindir}/ksysguardd
%attr(755,root,root) %{_bindir}/ktip
%attr(755,root,root) %{_bindir}/nsplugin*
%attr(755,root,root) %{_bindir}/startkde
%attr(755,root,root) %{_bindir}/khotkeys
%attr(755,root,root) %{_bindir}/ksmserver
%attr(755,root,root) %{_bindir}/kstart

%{_libdir}/klegacyimport.??
%{_libdir}/klipper.??
%{_libdir}/kmenuedit.??
%{_libdir}/kmenuedit.so.*.*.*
%{_libdir}/kxkb.??
%{_libdir}/libccont.a
%{_libdir}/libnsplugin.??
%{_libdir}/libnsplugin.so.*.*.*
%attr(755,root,root) %{_libdir}/khotkeys.??

%{_datadir}/apps/drkonqi/*
%{_datadir}/apps/kdewizard/*
%{_datadir}/apps/kappfinder/*
%{_datadir}/apps/kbookmark/
%{_datadir}/apps/kcminput/
%{_datadir}/apps/kcmlocale/
%{_datadir}/apps/kdcop/
%{_datadir}/apps/ksplash/
%{_datadir}/apps/ksysguard/

%{_datadir}/locale/

%{_datadir}/mimelnk/application/x-konsole.desktop
%{_datadir}/services/kxkb.desktop

%{_datadir}/sounds/

%{_datadir}/templates/

%{_includedir}/ccont.h
%{_includedir}/kfileivi.h


%doc %{_docdir}/HTML/en/kdesu/*
%doc %{_docdir}/HTML/en/kdebugdialog/*
%doc %{_docdir}/HTML/en/klipper/*
%doc %{_docdir}/HTML/en/kmenuedit/*
%doc %{_docdir}/HTML/en/kpager/*
%doc %{_docdir}/HTML/en/ksysguard/*

%config(missingok) %{_applnkdir}/Amusements/*.desktop

%config(missingok) %{_applnkdir}/System/kappfinder.desktop
%config(missingok) %{_applnkdir}/System/klegacyimport.desktop
%config(missingok) %{_applnkdir}/System/kmenuedit.desktop
%config(missingok) %{_applnkdir}/System/ksysguard.desktop
%config(missingok) %{_applnkdir}/Utilities/klipper.desktop
%config(missingok) %{_applnkdir}/Utilities/kpager.desktop
%config(missingok) %{_applnkdir}/Help.desktop
%config(missingok) %{_applnkdir}/Home.desktop
%config(missingok) %{_applnkdir}/.hidden/konqfilemgr.desktop


#################################################
#            KCONTROL - checking OK
#################################################
%files kcontrol
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcmshell
%attr(755,root,root) %{_bindir}/kcontrol
%attr(755,root,root) %{_bindir}/krdb
%attr(755,root,root) %{_bindir}/kaccess
%attr(755,root,root) %{_bindir}/keditfiletype
%attr(755,root,root) %{_bindir}/kxkb


%attr(755,root,root) %{_libdir}/libkcm_access.??
%attr(755,root,root) %{_libdir}/libkcm_arts.??
%attr(755,root,root) %{_libdir}/libkcm_background.??
%attr(755,root,root) %{_libdir}/libkcm_bell.??
%attr(755,root,root) %{_libdir}/libkcm_clock.??
%attr(755,root,root) %{_libdir}/libkcm_colors.??
%attr(755,root,root) %{_libdir}/libkcm_crypto.??
%attr(755,root,root) %{_libdir}/libkcm_energy.??
%attr(755,root,root) %{_libdir}/libkcm_email.??
%attr(755,root,root) %{_libdir}/libkcm_filetypes.??
%attr(755,root,root) %{_libdir}/libkcm_fonts.??
%attr(755,root,root) %{_libdir}/libkcm_htmlsearch.??
%attr(755,root,root) %{_libdir}/libkcm_icons.??
%attr(755,root,root) %{_libdir}/libkcm_iconthemes.??
%attr(755,root,root) %{_libdir}/libkcm_info.??
%attr(755,root,root) %{_libdir}/libkcm_input.??
%attr(755,root,root) %{_libdir}/libkcm_kdm.??
%attr(755,root,root) %{_libdir}/libkcm_keys.??
%attr(755,root,root) %{_libdir}/libkcm_khotkeys.??
%attr(755,root,root) %{_libdir}/libkcm_kicker.??
%attr(755,root,root) %{_libdir}/libkcm_kio.??
%attr(755,root,root) %{_libdir}/libkcm_knotify.??
%attr(755,root,root) %{_libdir}/libkcm_konq.??
%attr(755,root,root) %{_libdir}/libkcm_konqhtml.??
%attr(755,root,root) %{_libdir}/libkcm_kurifilt.??
%attr(755,root,root) %{_libdir}/libkcm_kwindesktop.??
%attr(755,root,root) %{_libdir}/libkcm_kwinmouse.??
%attr(755,root,root) %{_libdir}/libkcm_kwinoptions.??
%attr(755,root,root) %{_libdir}/libkcm_layout.??
%attr(755,root,root) %{_libdir}/libkcm_locale.??
%attr(755,root,root) %{_libdir}/libkcm_midi.??
%attr(755,root,root) %{_libdir}/libkcm_nsplugin.??
%attr(755,root,root) %{_libdir}/libkcm_passwords.??
%attr(755,root,root) %{_libdir}/libkcm_samba.??
%attr(755,root,root) %{_libdir}/libkcm_screensaver.??
%attr(755,root,root) %{_libdir}/libkcm_style.??
%attr(755,root,root) %{_libdir}/libkcm_taskbar.??
%attr(755,root,root) %{_libdir}/libkcm_virtualdesktops.??
%attr(755,root,root) %{_libdir}/libkcm_xmlrpcd.??
%attr(755,root,root) %{_libdir}/kaccess.??
%attr(755,root,root) %{_libdir}/kcminit.??
%attr(755,root,root) %{_libdir}/kcmshell.??
%attr(755,root,root) %{_libdir}/kcontrol.??

%attr(755,root,root) %{_libdir}/libkshorturifilter.??
%attr(755,root,root) %{_libdir}/libkshorturifilter.so.*.*.*
%attr(755,root,root) %{_libdir}/libkuriikwsfilter.??
%attr(755,root,root) %{_libdir}/libkuriikwsfilter.so.*.*.*
%attr(755,root,root) %{_libdir}/libkurisearchfilter.??
%attr(755,root,root) %{_libdir}/libkurisearchfilter.so.*.*.*



%{_datadir}/apps/kcontrol/*
%{_datadir}/apps/kdisplay/*


%{_datadir}/services/kshorturifilter.desktop
%{_datadir}/services/kuriikwsfilter.desktop
%{_datadir}/services/kurisearchfilter.desktop
%{_datadir}/services/kaccess.desktop

%config(missingok) %{_applnk_LNF}/*.desktop
%config(missingok) %{_applnk_Panel}/
%config(missingok) %{_applnk_Desktop}/*.desktop
%config(missingok) %{_applnk_Themes}/*.desktop
%config(missingok) %{_applnk_Windows}/*.desktop
%config(missingok) %{_applnkdir}/Settings/Peripherals/*.desktop
%config(missingok) %{_applnkdir}/Network/SMB/*.desktop
%config(missingok) %{_applnkdir}/Settings/Personalization/*.desktop
%config(missingok) %{_applnkdir}/Settings/Energy/*.desktop
%config(missingok) %{_applnkdir}/Settings/Multimedia/*.desktop
%config(missingok) %{_applnkdir}/System/clock.desktop
%config(missingok) %{_applnkdir}/System/kdm.desktop
%config(missingok) %{_applnkdir}/System/FileBrowsing/*.desktop
%config(missingok) %{_applnk_Help}/htmlsearch.desktop
%config(missingok) %{_applnk_Infor}/*.desktop

%config(missingok) %{_applnkdir}/KControl.desktop


%config(missingok) %{_datadir}/config/kuriikwsfilterrc
%config(missingok) %{_datadir}/config/kshorturifilterrc


%attr(644,root,root) %{_datadir}/locale/C/*

%doc %{_docdir}/HTML/en/kcontrol/*

#################################################
#             kdesktop
#################################################
%files kdesktop
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kdesktop
%attr(755,root,root) %{_bindir}/kdmdesktop
%attr(755,root,root) %{_bindir}/kdeeject



%attr(755,root,root) %{_libdir}/kdesktop.??

%attr(644,root,root) %{_includedir}/KBackgroundIface.h
%attr(644,root,root) %{_includedir}/KDesktopIface.h
%attr(644,root,root) %{_includedir}/KScreensaverIface.h

%{_datadir}/icons/*

%{_datadir}/apps/kdesktop/*
%{_datadir}/wallpapers/*


#################################################
#            kdm
#################################################
%files kdm
%defattr(644,root,root,755)

%attr(755, root, root) %{_bindir}/chooser
%attr(755, root, root) %{_bindir}/kdm

%{_datadir}/apps/kdm/*

%{_datadir}/config/kdmrc

%doc %{_docdir}/HTML/en/kdm/*

#################################################
#            khelpcenter
#################################################
%files khelpcenter
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/khelpcenter
%attr(755,root,root) %{_bindir}/khtmlindex



%attr(755,root,root) %{_libdir}/libkhelpcenter.??
%attr(755,root,root) %{_libdir}/libkhelpcenter.so.*.*.*
%attr(755,root,root) %{_libdir}/libhtmlsearch.??

#%config(missingok) %{_applnkdir}/Help.desktop

%{_datadir}/apps/khelpcenter/

%{_datadir}/services/khelpcenter.desktop

%doc %{_docdir}/HTML/en/khelpcenter/*
#################################################
#             kicker
#################################################
%files kicker
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kicker
%attr(755,root,root) %{_bindir}/appletproxy


%attr(755,root,root) %{_libdir}/libkminipagerapplet.la
%attr(755,root,root) %{_libdir}/libkminipagerapplet.so.*.*.*
%attr(755,root,root) %{_libdir}/libktaskbarapplet.la
%attr(755,root,root) %{_libdir}/libktaskbarapplet.so.*.*.*
%attr(755,root,root) %{_libdir}/libksystemtrayapplet.la
%attr(755,root,root) %{_libdir}/libksystemtrayapplet.so.*.*.*
%attr(755,root,root) %{_libdir}/libclockapplet.??
%attr(755,root,root) %{_libdir}/libclockapplet.so.*.*.*
%attr(755,root,root) %{_libdir}/libkrunapplet.??
%attr(755,root,root) %{_libdir}/libkrunapplet.so.*.*.*
%attr(755,root,root) %{_libdir}/appletproxy.??
%attr(755,root,root) %{_libdir}/kicker.??
%attr(755,root,root) %{_libdir}/libquicklauncher.??
%attr(755,root,root) %{_libdir}/libquicklauncher.so.*.*.*
#%config(missingok) %{_applnkdir}/Toys/*

%{_datadir}/apps/kicker/
%{_datadir}/apps/quickbrowser/
%{_datadir}/apps/clockapplet/

%doc %{_docdir}/HTML/en/kicker/*


#################################################
#             kioslave
#################################################
%files kioslave
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kman2html


%attr(755,root,root) %{_libdir}/kio_gopher.??
%attr(755,root,root) %{_libdir}/kio_gzip.??
%attr(755,root,root) %{_libdir}/kio_help.??
%attr(755,root,root) %{_libdir}/kio_info.??
%attr(755,root,root) %{_libdir}/kio_man.??
%attr(755,root,root) %{_libdir}/kio_nntp.??
%attr(755,root,root) %{_libdir}/kio_nfs.??
%attr(755,root,root) %{_libdir}/kio_pop3.??
%attr(755,root,root) %{_libdir}/kio_smtp.??
%attr(755,root,root) %{_libdir}/kio_smb.??
%attr(755,root,root) %{_libdir}/kio_tar.??


%attr(755,root,root) %{_libdir}/libsmb++.??
%attr(755,root,root) %{_libdir}/libsmb++.so.*.*.*

%{_datadir}/apps/kio_info/*

%{_datadir}/services/gopher.protocol
%{_datadir}/services/gzip.protocol
%{_datadir}/services/help.protocol
%{_datadir}/services/info.protocol
%{_datadir}/services/man.protocol
%{_datadir}/services/nntp.protocol
%{_datadir}/services/nfs.protocol
%{_datadir}/services/pop3*.protocol
%{_datadir}/services/smtp.protocol
%{_datadir}/services/smb.protocol
%{_datadir}/services/tar.protocol


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
%attr(644,root,root) %{_includedir}/knewmenu.h

%attr(755,root,root) %{_libdir}/libkonq.??
%attr(755,root,root) %{_libdir}/libkonq.so.*
%attr(755,root,root) %{_libdir}/libkonqdirtree.??
%attr(755,root,root) %{_libdir}/libkonqiconview.??
%attr(755,root,root) %{_libdir}/libkonqlistview.??
%attr(755,root,root) %{_libdir}/konqueror.??
%attr(755,root,root) %{_libdir}/kfmclient.??


%config(missingok) %{_applnkdir}/System/Arrange.desktop
%config(missingok) %{_applnkdir}/System/kfmclient.desktop
%config(missingok) %{_applnkdir}/System/konquerorsu.desktop

#%config(missingok) %{_applnkdir}/Home.desktop
#%config(missingok) %{_applnkdir}/.hidden/konqfilemgr.desktop
#%config(missingok) %{_applnkdir}/Internet/konqbrowser.desktop



%{_datadir}/apps/konqiconview/
%{_datadir}/apps/konqlistview/
%{_datadir}/apps/konqueror/

%{_datadir}/services/konq*
%config(missingok) %{_applnkdir}/Settings/WebBrowsing/*.desktop
%config(missingok) %{_applnkdir}/Internet/konqbrowser.desktop

%doc %{_docdir}/HTML/en/konqueror/*
#################################################
#             KONSOLE
#################################################
%files konsole
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/konsole*
%attr(755,root,root) %{_bindir}/kwrited

%attr(755,root,root) %{_libdir}/libkonsolepart.??
%attr(755,root,root) %{_libdir}/kwrited.??
%attr(755,root,root) %{_libdir}/konsole.??

#%config(missingok) %{_applnkdir}/System/konsolesu.desktop

%{_datadir}/mimelnk/application/x-konsole.desktop

%{_datadir}/config/konsolerc

%{_datadir}/services/konsolepart.desktop

%{_datadir}/apps/konsole/

%attr(644,root,root) /usr/share/fonts/misc/9x15.pcf.gz
%attr(644,root,root) /usr/share/fonts/misc/console8x16.pcf.gz
%attr(644,root,root) /usr/share/fonts/misc/console8x8.pcf.gz

%doc %{_docdir}/HTML/en/konsole/*

%config(missingok) %{_applnkdir}/System/konsole*.desktop


#################################################
#            KSCREENSAVER - checking OK
#################################################
%files kscreensaver 
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kxsconfig
%attr(755,root,root) %{_bindir}/kxsrun
%attr(755,root,root) %{_bindir}/*.kss

#%config(missingok) %{_applnkdir}/System/ScreenSavers/*.desktop

%{_datadir}/apps//kscreensaver/

%attr(644,root,root) %{_datadir}/config/antrc
%attr(644,root,root) %{_datadir}/config/attractionrc
%attr(644,root,root) %{_datadir}/config/bouboulerc
%attr(644,root,root) %{_datadir}/config/bubblesrc
%attr(644,root,root) %{_datadir}/config/coralrc
%attr(644,root,root) %{_datadir}/config/crystalrc
%attr(644,root,root) %{_datadir}/config/decayscreenrc
%attr(644,root,root) %{_datadir}/config/deluxerc
%attr(644,root,root) %{_datadir}/config/demonrc
%attr(644,root,root) %{_datadir}/config/driftrc
%attr(644,root,root) %{_datadir}/config/epicyclerc
%attr(644,root,root) %{_datadir}/config/fadeplotrc
%attr(644,root,root) %{_datadir}/config/flamerc
%attr(644,root,root) %{_datadir}/config/flowrc
%attr(644,root,root) %{_datadir}/config/forestrc
%attr(644,root,root) %{_datadir}/config/gearsrc
%attr(644,root,root) %{_datadir}/config/gooprc
%attr(644,root,root) %{_datadir}/config/gravrc
%attr(644,root,root) %{_datadir}/config/halorc
%attr(644,root,root) %{_datadir}/config/interferencerc
%attr(644,root,root) %{_datadir}/config/kumpparc
%attr(644,root,root) %{_datadir}/config/laserrc
%attr(644,root,root) %{_datadir}/config/lissierc
%attr(644,root,root) %{_datadir}/config/penroserc
%attr(644,root,root) %{_datadir}/config/rocksrc
%attr(644,root,root) %{_datadir}/config/sliprc
%attr(644,root,root) %{_datadir}/config/imsmaprc

%config(missingok) %{_applnkdir}/System/ScreenSavers/*.desktop

#################################################
#             kwin
#################################################
%files kwin
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kwin

%attr(755,root,root) %{_libdir}/kwin.??
%attr(755,root,root) %{_libdir}/libkwinb2.??
%attr(755,root,root) %{_libdir}/libkwindefault.??
%attr(755,root,root) %{_libdir}/libkwindefault.so.*
%attr(755,root,root) %{_libdir}/libkwinkde1.??
%attr(755,root,root) %{_libdir}/libkwinmodernsys.??
%attr(755,root,root) %{_libdir}/libkwinkstep.??
%attr(755,root,root) %{_libdir}/libkwinlaptop.??
%attr(755,root,root) %{_libdir}/libkwinriscos.??
%attr(755,root,root) %{_libdir}/libkwinsystem.??


%{_includedir}/KWinInterface.h

%{_datadir}/apps/kwin/



#################################################
#             kxmlrpc
#################################################

%files kxmlrpc
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kxmlrpcd

%attr(755,root,root) %{_libdir}/kxmlrpcd.??


%{_datadir}/services/kxmlrpcd.desktop
#################################################
#             kwrite
#################################################

%files kwrite
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kwrite

%{_libdir}/kwrite.??
%{_libdir}/libkwritepart.??


%{_datadir}/apps/kwrite/*

%doc %{_docdir}/HTML/en/kwrite/*

%{_datadir}/services/kwrite_component.desktop


%config(missingok) %{_applnkdir}/Office/Editors/kwrite.desktop
