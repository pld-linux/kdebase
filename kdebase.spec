Summary:     	K Desktop Environment - core files
Summary(pl): 	K Desktop Environment - pliki ¶rodowiska
Name:        	kdebase
Version:     	1.1.1
Release: 4
Copyright:   	GPL
Group:       	X11/KDE/Base
Group(pl):      X11/KDE
Vendor:      	The KDE Team
Source:      	ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/bz2/%{name}-%{version}.tar.bz2
Source2:     	kdeenv
Patch:		kdebase-DESTDIR.patch
BuildRequires:	qt-devel >= 1.44
BuildRequires:	kdelibs-devel = %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	pam-devel
BuildRequires:	Mesa-devel
Requires:    	qt >= 1.44
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

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
Requires:    	qt >= 1.4
Requires:	kdelibs = %{version}
Requires:	%{name} = %{version}

%description kcontrol
KDE Control Center - easy way to access KDE configuration modules
and several useful modules.

%description -l pl kcontrol
Centrum sterowania KDE - program obs³ugi modu³ów konfiguracyjnych KDE
oraz kilka przydatnych modu³ów.

%package kdehelp
Summary:     	KDE Help System	
Summary(pl): 	System Pomocy KDE
Group:       	X11/KDE/Base
Requires:    	qt >= 1.44
Requires:	kdelibs = %{version}

%description kdehelp
This program is used for viewing KDE applications' online manual.
It is also convinient for reading system's man pages and "info" documentation.

%description -l pl kdehelp
Program umo¿liwiaj±cy przegl±danie dokumentacji applikacji KDE.
Jest te¿ wygodnym narzêdziem do ogl±dania stron man i dokumentacji "info".

%package kdm
Summary:     	KDE Display Manager	
Summary(pl): 	KDE Display Manager
Group:       	X11/KDE/Base
Requires:    	qt >= 1.44
Requires:	kdelibs = %{version}

%description kdm
It is KDE replacement for XDM.
It manages local and remote X11 displays.

%description -l pl kdm
Zamiennik XDM rodem z KDE.

%package konsole
Summary:     	KDE Display Manager	
Summary(pl): 	KDE Display Manager
Group:       	X11/KDE/Base
Requires:    	qt >= 1.44
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
Requires:    	qt >= 1.44
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
Requires:	qt >= 1.44
Requires:	kdelibs = %{version} 

%description kfm
A file manager and a web browser for KDE.

%description -l pl kfm
Mened¿er plików i przegl±darka WWW dla KDE.

%package kfontmanager
Summary:     	KDE font manager	
Summary(pl): 	Mened¿er fontów KDE
Group:       	X11/KDE/Base
Requires:    	qt >= 1.44
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
Requires:    	qt >= 1.44
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
Requires:	qt >= 1.44
Requires:	kdelibs = %{version} 

%description kpanel
An easy way to start applications and switch desktops in KDE.

%description -l pl kpanel
U³atwia startowanie aplikacji oraz prze³±czanie ekranów w KDE.

%package kscreensaver
Summary:     	KDE Screen-savers
Summary(pl): 	Screen-savery dla KDE
Group:       	X11/KDE/Base
Requires:    	qt >= 1.44
Requires:	kdelibs = %{version}

%description kscreensaver
Several screen-savers for KDE.

%description -l pl kscreensaver
"Oszczêdzacze ekranu" dla KDE

%package kvt
Summary:     	KDE terminal emulator
Summary(pl): 	Emulator terminala dla KDE
Group:       	X11/KDE/Base
Requires:    	qt >= 1.44
Requires:	kdelibs = %{version}

%description kvt
Terminal emulator for KDE.

%description -l pl kvt
Emulator terminala znakowego dla KDE

%package kikbd
Summary:     	KDE international keyboard
Summary(pl): 	Klawiatura miedzynarodowa dla KDE
Group:       	X11/KDE/Base
Requires:    	qt >= 1.44
Requires:	kdelibs = %{version}

%description kikbd
International keyboard for KDE.

%description -l pl kikbd
Klawiatura miedzynarodowa dla KDE

%package kwm
Summary:     	KDE window manager
Summary(pl): 	Mened¿er okien KDE
Group:       	X11/KDE/Base
Requires:    	qt >= 1.44
Requires:	kdelibs = %{version}

%description kwm
Window manager for KDE

%description -l pl kwm
Mened¿er okien dla KDE

%package kbgndwm
Summary:     	KDE background manager and wallpapers
Summary(pl): 	Tapety oraz mened¿er t³a KDE 
Group:       	X11/KDE/Base
Requires:    	qt >= 1.44
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
%patch -p1

%build
export KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
 	--with-pam=yes

%{__make} KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/kde

%{__make} \
	RUN_KAPPFINDER=no \
	DESTDIR=$RPM_BUILD_ROOT \
	localedir="$RPM_BUILD_ROOT/usr/X11R6/share/locale" \
	install

install $RPM_SOURCE_DIR/kdeenv $RPM_BUILD_ROOT%{_bindir}/kdeenv

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :

#### kdebase - main package find_lang
%find_lang krootwm krootwm.lang
%find_lang kcmsample kcmsample.lang
%find_lang kcmdisplay kcmdisplay.lang
%find_lang kstart kstart.lang
%find_lang konsole konsole.lang
%find_lang kwm 
%find_lang kcmkwm 
%find_lang kpager 
%find_lang kcmsyssound 
cat kwm.lang kcmkwm.lang kpager.lang kcmsyssound.lang >  _kwm.lang
%find_lang kbgndwm kbgndwm.lang
%find_lang kdehelp kdehelp.lang
%find_lang kfm
%find_lang kcmkfm
cat kfm.lang kcmkfm.lang > _kfm.lang
%find_lang kfind kfind.lang
%find_lang kcontrol 
%find_lang kcmbell
%find_lang kcminfo
%find_lang kcmkeys
%find_lang kcminput
%find_lang kcmlocale
%find_lang kcmsamba
cat kcontrol.lang kcmbell.lang kcminfo.lang kcmkeys.lang kcminput.lang kcmlocale.lang kcmsamba.lang > _kcontrol.lang
%find_lang klock klock.lang
%find_lang kvt kvt.lang
%find_lang kmenuedit kmenuedit.lang
%find_lang kpanel kpanel.lang
%find_lang kcmkpanel kcmkpanel.lang
%find_lang kdm kdm.lang
%find_lang kdmconfig kdmconfig.lang
%find_lang kfontmanager kfontmanager.lang
%find_lang kikbd kikbd.lang

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KDEBASE - checking
#################################################

%files -f krootwm.lang -f kcmsample.lang -f kcmdisplay.lang -f kstart.lang
%defattr(644,root,root,755)

#directory hierarchy
%dir /etc/X11/kde/mimelnk
%dir /etc/X11/kde/applnk
%dir /etc/X11/kde/applnk/System
%dir /etc/X11/kde/applnk/Applications
%dir /etc/X11/kde/applnk/Games
%dir /etc/X11/kde/applnk/Graphics
%dir /etc/X11/kde/applnk/Internet
%dir /etc/X11/kde/applnk/Multimedia
%dir /etc/X11/kde/applnk/Utilities
%dir /etc/X11/kde/applnk/Settings
%dir /etc/X11/kde/applnk/Settings/Applications

%dir %{_datadir}/kde/doc
%dir %{_datadir}/kde/doc/HTML
%dir %{_datadir}/kde/doc/HTML/en

%config(missingok) /etc/X11/kde/applnk/Settings/Desktop/
%config(missingok) /etc/X11/kde/applnk/.directory

# Applications' files
%{_datadir}/kde/apps/kdisplay/
%{_datadir}/kde/apps/kappfinder
%{_datadir}/kde/apps/kdisknav

# some icons
%{_datadir}/kde/icons/*_package.xpm
%{_datadir}/kde/icons/mini/*_package.xpm

%{_datadir}/kde/icons/mini/mini*.xpm
%{_datadir}/kde/icons/mini/background.xpm
%{_datadir}/kde/icons/mini/colors.xpm
%{_datadir}/kde/icons/mini/screensaver.xpm
%{_datadir}/kde/icons/mini/style.xpm
%{_datadir}/kde/icons/mini/mouse.xpm
%{_datadir}/kde/icons/mini/keyboard.xpm
%{_datadir}/kde/icons/mini/windows.xpm
%{_datadir}/kde/icons/mini/titlebar.xpm
%{_datadir}/kde/icons/mini/buttons.xpm
%{_datadir}/kde/icons/mini/application_settings.xpm
%{_datadir}/kde/icons/mini/desktop_settings.xpm
%{_datadir}/kde/icons/mini/general_settings.xpm
%{_datadir}/kde/icons/mini/information_settings.xpm
%{_datadir}/kde/icons/mini/input_devices_settings.xpm
%{_datadir}/kde/icons/mini/network_settings.xpm
%{_datadir}/kde/icons/mini/panel_settings.xpm
%{_datadir}/kde/icons/mini/sound_settings.xpm
%{_datadir}/kde/icons/mini/exec.xpm
%{_datadir}/kde/icons/mini/folder.xpm
%{_datadir}/kde/icons/mini/terminal.xpm
%{_datadir}/kde/icons/mini/x.xpm
%{_datadir}/kde/icons/mini/audiovol.xpm
%{_datadir}/kde/icons/mini/bell.xpm
%{_datadir}/kde/icons/mini/desktop.xpm
%{_datadir}/kde/icons/mini/fonts.xpm
%{_datadir}/kde/icons/mini/kcmdevices.xpm
%{_datadir}/kde/icons/mini/kcmmemory.xpm
%{_datadir}/kde/icons/mini/kcmpartitions.xpm
%{_datadir}/kde/icons/mini/kcmpci.xpm
%{_datadir}/kde/icons/mini/kcmprocessor.xpm
%{_datadir}/kde/icons/mini/kcmscsi.xpm
%{_datadir}/kde/icons/mini/kcmsound.xpm
%{_datadir}/kde/icons/mini/kcmsyssound.xpm
%{_datadir}/kde/icons/mini/kcmx.xpm
%{_datadir}/kde/icons/mini/pci.xpm
%{_datadir}/kde/icons/mini/sample.xpm
%{_datadir}/kde/icons/mini/tablet.xpm
%{_datadir}/kde/icons/mini/winprops.xpm

%{_datadir}/kde/icons/background.xpm
%{_datadir}/kde/icons/application_settings.xpm
%{_datadir}/kde/icons/desktop_settings.xpm
%{_datadir}/kde/icons/general_settings.xpm
%{_datadir}/kde/icons/information_settings.xpm
%{_datadir}/kde/icons/input_devices_settings.xpm
%{_datadir}/kde/icons/network_settings.xpm
%{_datadir}/kde/icons/panel_settings.xpm
%{_datadir}/kde/icons/sound_settings.xpm
%{_datadir}/kde/icons/brightness.xpm
%{_datadir}/kde/icons/buttons.xpm
%{_datadir}/kde/icons/colors.xpm
%{_datadir}/kde/icons/colourness.xpm
%{_datadir}/kde/icons/contrast.xpm
%{_datadir}/kde/icons/desktop.xpm
%{_datadir}/kde/icons/fonts.xpm
%{_datadir}/kde/icons/kcmdevices.xpm
%{_datadir}/kde/icons/kcmmemory.xpm
%{_datadir}/kde/icons/kcmpartitions.xpm
%{_datadir}/kde/icons/kcmpci.xpm
%{_datadir}/kde/icons/kcmprocessor.xpm
%{_datadir}/kde/icons/kcmscsi.xpm
%{_datadir}/kde/icons/kcmsound.xpm
%{_datadir}/kde/icons/kcmsyssound.xpm
%{_datadir}/kde/icons/kcmx.xpm
%{_datadir}/kde/icons/kdisknav.xpm
%{_datadir}/kde/icons/locked.xpm
%{_datadir}/kde/icons/logo.xpm
%{_datadir}/kde/icons/monitor.xpm
%{_datadir}/kde/icons/properties.xpm
%{_datadir}/kde/icons/screensaver.xpm
%{_datadir}/kde/icons/style.xpm
%{_datadir}/kde/icons/tablet.xpm
%{_datadir}/kde/icons/titlebar.xpm

# KDE menu
%config(missingok) /etc/X11/kde/applnk/System/.directory
%config(missingok) /etc/X11/kde/applnk/System/kappfinder.kdelnk
%config(missingok) /etc/X11/kde/applnk/Applications/.directory
%config(missingok) /etc/X11/kde/applnk/Games/.directory
%config(missingok) /etc/X11/kde/applnk/Graphics/.directory
%config(missingok) /etc/X11/kde/applnk/Internet/.directory
%config(missingok) /etc/X11/kde/applnk/Multimedia/.directory
%config(missingok) /etc/X11/kde/applnk/Utilities/.directory
%config(missingok) /etc/X11/kde/applnk/Settings/Sound/.directory
%config(missingok) /etc/X11/kde/applnk/Settings/Applications/.directory
%config(missingok) /etc/X11/kde/applnk/Settings/.directory

#documentation
%{_datadir}/kde/doc/HTML/en/kmedia/*
%{_datadir}/kde/doc/HTML/en/kdisknav

#no go executables
%attr(755,root,root) %{_bindir}/startkde
%attr(755,root,root) %{_bindir}/kdeenv
%attr(755,root,root) %{_bindir}/kde
%attr(755,root,root) %{_bindir}/kstart
%attr(755,root,root) %{_bindir}/rman
%attr(755,root,root) %{_bindir}/krootwm
%attr(755,root,root) %{_bindir}/maudio
%attr(755,root,root) %{_bindir}/kaudioserver
%attr(755,root,root) %{_bindir}/kplayaudio
%attr(755,root,root) %{_bindir}/kappfinder
%attr(755,root,root) %{_bindir}/kappfinder_restart
%attr(755,root,root) %{_bindir}/krdb
%attr(755,root,root) %{_bindir}/kcmdisplay

# konsole_grantpty need SUID ?
%attr(755,root,root) %{_bindir}/konsole_grantpty

#################################################
#             KONSOLE - checking - on air
#################################################
%files konsole -f konsole.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/konsole.kdelnk

%{_datadir}/kde/icons/mini/konsole.xpm
%{_datadir}/kde/icons/konsole.xpm

%{_datadir}/kde/doc/HTML/en/konsole

%{_datadir}/kde/apps/konsole

%attr(755,root,root) %{_bindir}/konsole

#################################################
#             KWM - checking OK
#################################################

%files kwm -f _kwm.lang

%defattr(644,root,root,755)

%{_datadir}/kde/doc/HTML/en/kwm/
%{_datadir}/kde/doc/HTML/en/kcontrol/kcmkwm/
%{_datadir}/kde/doc/HTML/en/kcontrol/kcmsyssound/
%{_datadir}/kde/doc/HTML/en/kpager

%config(missingok) /etc/X11/kde/applnk/Settings/Windows/
%config(missingok) /etc/X11/kde/applnk/System/kpager.kdelnk
%config(missingok) /etc/X11/kde/applnk/Settings/Sound/syssound.kdelnk
%config(missingok) /etc/X11/kde/desktop?rc

%{_datadir}/kde/apps/kwm/

%{_datadir}/kde/icons/mini/maximize2.xpm
%{_datadir}/kde/icons/mini/kwm.xpm
%{_datadir}/kde/icons/kcmkwm.xpm
%{_datadir}/kde/icons/kwm.xpm

%attr(755,root,root) %{_bindir}/kcmkwm
%attr(755,root,root) %{_bindir}/kcmsyssound
%attr(755,root,root) %{_bindir}/kpager
%attr(755,root,root) %{_bindir}/kwm
%attr(755,root,root) %{_bindir}/kwmcom
%attr(755,root,root) %{_bindir}/kwmsound

#################################################
#             KBGNDWM - checking OK
#################################################

%files kbgndwm -f kbgndwm.lang

%defattr(644,root,root,755)

%{_datadir}/kde/wallpapers/*

%attr(755,root,root) %{_bindir}/kbgndwm

#################################################
#             KDEHELP - checking OK
#################################################

%files kdehelp -f kdehelp.lang
%defattr(644,root,root,755)

%{_datadir}/kde/doc/HTML/en/kdehelp/

%{_datadir}/kde/icons/mini/kdehelp.xpm
%{_datadir}/kde/icons/kdehelp.xpm

%attr(755,root,root) %{_prefix}/lib/kde/cgi-bin
%attr(755,root,root) %{_bindir}/kdehelp

%config(missingok) /etc/X11/kde/applnk/Help.kdelnk

#################################################
#             KFM - checking OK
#################################################

%files kfm -f _kfm.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Krefresh.kdelnk
%config(missingok) /etc/X11/kde/applnk/Trash.kdelnk
%config(missingok) /etc/X11/kde/applnk/Home.kdelnk
%config(missingok) /etc/X11/kde/applnk/System/kfmsu.kdelnk
%config(missingok) /etc/X11/kde/applnk/System/Arrange.kdelnk
%config(missingok) /etc/X11/kde/applnk/Settings/Applications/kfmbrowser.kdelnk
%config(missingok) /etc/X11/kde/applnk/Settings/Applications/kfm.kdelnk

%config /etc/X11/kde/mimelnk/*
%config /etc/X11/kde/kfmrc
%config /etc/X11/kde/desktop

%{_datadir}/kde/doc/HTML/en/kfm/
%{_datadir}/kde/doc/HTML/en/kcontrol/kcmkfm

%{_datadir}/kde/apps/kfm/
%{_datadir}/kde/icons/mini/3floppy_mount.xpm
%{_datadir}/kde/icons/mini/3floppy_unmount.xpm
%{_datadir}/kde/icons/mini/5floppy_mount.xpm
%{_datadir}/kde/icons/mini/5floppy_unmount.xpm
%{_datadir}/kde/icons/mini/binary.xpm
%{_datadir}/kde/icons/mini/blockdevice.xpm
%{_datadir}/kde/icons/mini/c_src.xpm
%{_datadir}/kde/icons/mini/cdrom_mount.xpm
%{_datadir}/kde/icons/mini/chardevice.xpm
%{_datadir}/kde/icons/mini/cdrom_unmount.xpm
%{_datadir}/kde/icons/mini/core.xpm
%{_datadir}/kde/icons/mini/document.xpm
%{_datadir}/kde/icons/mini/dvi.xpm
%{_datadir}/kde/icons/mini/folder_blue.xpm
%{_datadir}/kde/icons/mini/folder_cyan.xpm
%{_datadir}/kde/icons/mini/folder_green.xpm
%{_datadir}/kde/icons/mini/folder_open.xpm
%{_datadir}/kde/icons/mini/folder_red.xpm
%{_datadir}/kde/icons/mini/folder_yellow.xpm
%{_datadir}/kde/icons/mini/font.xpm
%{_datadir}/kde/icons/mini/ftp.xpm
%{_datadir}/kde/icons/mini/gf.xpm
%{_datadir}/kde/icons/mini/h_src.xpm
%{_datadir}/kde/icons/mini/html.xpm
%{_datadir}/kde/icons/mini/harddrive_mount.xpm
%{_datadir}/kde/icons/mini/harddrive_unmount.xpm
%{_datadir}/kde/icons/mini/image.xpm
%{_datadir}/kde/icons/mini/info.xpm
%{_datadir}/kde/icons/mini/java_src.xpm
%{_datadir}/kde/icons/mini/kfm*
%{_datadir}/kde/icons/mini/l_src.xpm
%{_datadir}/kde/icons/mini/library.xpm
%{_datadir}/kde/icons/mini/locked.xpm
%{_datadir}/kde/icons/mini/lockedfolder.xpm
%{_datadir}/kde/icons/mini/log.xpm
%{_datadir}/kde/icons/mini/make.xpm
%{_datadir}/kde/icons/mini/man.xpm
%{_datadir}/kde/icons/mini/metafont.xpm
%{_datadir}/kde/icons/mini/midi.xpm
%{_datadir}/kde/icons/mini/moc_src.xpm
%{_datadir}/kde/icons/mini/o_src.xpm
%{_datadir}/kde/icons/mini/p_src.xpm
%{_datadir}/kde/icons/mini/pdf.xpm
%{_datadir}/kde/icons/mini/pipe.xpm
%{_datadir}/kde/icons/mini/pk.xpm
%{_datadir}/kde/icons/mini/postscript.xpm
%{_datadir}/kde/icons/mini/printer.xpm
%{_datadir}/kde/icons/mini/readme.xpm
%{_datadir}/kde/icons/mini/resource.xpm
%{_datadir}/kde/icons/mini/s_src.xpm
%{_datadir}/kde/icons/mini/package.xpm
%{_datadir}/kde/icons/mini/script.xpm
%{_datadir}/kde/icons/mini/socket.xpm
%{_datadir}/kde/icons/mini/sound.xpm
%{_datadir}/kde/icons/mini/tex.xpm
%{_datadir}/kde/icons/mini/tgz.xpm
%{_datadir}/kde/icons/mini/trash.xpm
%{_datadir}/kde/icons/mini/txt.xpm
%{_datadir}/kde/icons/mini/unknown.xpm
%{_datadir}/kde/icons/mini/video.xpm
%{_datadir}/kde/icons/mini/www.xpm
%{_datadir}/kde/icons/mini/y_src.xpm
%{_datadir}/kde/icons/mini/zip_mount.xpm
%{_datadir}/kde/icons/mini/zip_unmount.xpm

%{_datadir}/kde/icons/kfm.xpm
%{_datadir}/kde/icons/link.xpm
%{_datadir}/kde/icons/3floppy_mount.xpm
%{_datadir}/kde/icons/3floppy_unmount.xpm
%{_datadir}/kde/icons/5floppy_mount.xpm
%{_datadir}/kde/icons/5floppy_unmount.xpm
%{_datadir}/kde/icons/binary.xpm
%{_datadir}/kde/icons/blockdevice.xpm
%{_datadir}/kde/icons/c_src.xpm
%{_datadir}/kde/icons/cdrom_mount.xpm
%{_datadir}/kde/icons/cdrom_unmount.xpm
%{_datadir}/kde/icons/chardevice.xpm
%{_datadir}/kde/icons/core.xpm
%{_datadir}/kde/icons/document.xpm
%{_datadir}/kde/icons/dvi.xpm
%{_datadir}/kde/icons/exec.xpm
%{_datadir}/kde/icons/f_src.xpm
%{_datadir}/kde/icons/folder.xpm
%{_datadir}/kde/icons/folder_blue.xpm
%{_datadir}/kde/icons/folder_cyan.xpm
%{_datadir}/kde/icons/folder_green.xpm
%{_datadir}/kde/icons/folder_open.xpm
%{_datadir}/kde/icons/folder_red.xpm
%{_datadir}/kde/icons/folder_yellow.xpm
%{_datadir}/kde/icons/font.xpm
%{_datadir}/kde/icons/ftp.xpm
%{_datadir}/kde/icons/gf.xpm
%{_datadir}/kde/icons/h_src.xpm
%{_datadir}/kde/icons/harddrive_mount.xpm
%{_datadir}/kde/icons/harddrive_unmount.xpm
%{_datadir}/kde/icons/html.xpm
%{_datadir}/kde/icons/image.xpm
%{_datadir}/kde/icons/info.xpm
%{_datadir}/kde/icons/java_src.xpm
%{_datadir}/kde/icons/kfm_fulltrash.xpm
%{_datadir}/kde/icons/kfm_home.xpm
%{_datadir}/kde/icons/kfm_refresh.xpm
%{_datadir}/kde/icons/kfm_trash.xpm
%{_datadir}/kde/icons/l_src.xpm
%{_datadir}/kde/icons/library.xpm
%{_datadir}/kde/icons/lockedfolder.xpm
%{_datadir}/kde/icons/log.xpm
%{_datadir}/kde/icons/magneto-optical_mount.xpm
%{_datadir}/kde/icons/magneto-optical_unmount.xpm
%{_datadir}/kde/icons/make.xpm
%{_datadir}/kde/icons/man.xpm
%{_datadir}/kde/icons/metafont.xpm
%{_datadir}/kde/icons/midi.xpm
%{_datadir}/kde/icons/moc_src.xpm
%{_datadir}/kde/icons/o_src.xpm
%{_datadir}/kde/icons/p_src.xpm
%{_datadir}/kde/icons/package.xpm
%{_datadir}/kde/icons/pdf.xpm
%{_datadir}/kde/icons/pipe.xpm
%{_datadir}/kde/icons/pk.xpm
%{_datadir}/kde/icons/postscript.xpm
%{_datadir}/kde/icons/printer.xpm
%{_datadir}/kde/icons/readme.xpm
%{_datadir}/kde/icons/readonly.xpm
%{_datadir}/kde/icons/resource.xpm
%{_datadir}/kde/icons/s_src.xpm
%{_datadir}/kde/icons/script.xpm
%{_datadir}/kde/icons/socket.xpm
%{_datadir}/kde/icons/sound.xpm
%{_datadir}/kde/icons/terminal.xpm
%{_datadir}/kde/icons/tex.xpm
%{_datadir}/kde/icons/tgz.xpm
%{_datadir}/kde/icons/trash.xpm
%{_datadir}/kde/icons/txt.xpm
%{_datadir}/kde/icons/unknown.xpm
%{_datadir}/kde/icons/video.xpm
%{_datadir}/kde/icons/www.xpm
%{_datadir}/kde/icons/x.xpm
%{_datadir}/kde/icons/y_src.xpm
%{_datadir}/kde/icons/zip_mount.xpm
%{_datadir}/kde/icons/zip_unmount.xpm

%attr(755,root,root) %{_bindir}/kcmkfm
%attr(755,root,root) %{_bindir}/kfm
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/kfmexec
%attr(755,root,root) %{_bindir}/kfmsu
%attr(755,root,root) %{_bindir}/kfmsu2
%attr(755,root,root) %{_bindir}/kfmwarn
%attr(755,root,root) %{_bindir}/kioslave
%attr(755,root,root) %{_bindir}/unpack

#################################################
#             KFIND - checking OK
#################################################

%files kfind -f kfind.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Kfind.kdelnk

%{_datadir}/kde/doc/HTML/en/kfind/

%{_datadir}/kde/apps/kfind/

%{_datadir}/kde/icons/mini/kfind.xpm
%{_datadir}/kde/icons/kfind.xpm

%attr(755,root,root) %{_bindir}/kfind

#################################################
#            KCONTROL - checking OK
#################################################

%files kcontrol -f _kcontrol.lang

%defattr(644,root,root,755)

%{_datadir}/kde/apps/kcontrol/
%{_datadir}/kde/apps/kcmlocale/

%config /etc/X11/kde/kcmlocalerc

%{_datadir}/kde/doc/HTML/en/kcontrol/kcmbell
%{_datadir}/kde/doc/HTML/en/kcontrol/kcmdisplay
%{_datadir}/kde/doc/HTML/en/kcontrol/kcminfo
%{_datadir}/kde/doc/HTML/en/kcontrol/kcminput
%{_datadir}/kde/doc/HTML/en/kcontrol/kcmlocale
%{_datadir}/kde/doc/HTML/en/kcontrol/kcmsamba
%{_datadir}/kde/doc/HTML/en/kcontrol/index.html
%{_datadir}/kde/doc/HTML/en/kcontrol/index-1.html
%{_datadir}/kde/doc/HTML/en/kcontrol/index-2.html
%{_datadir}/kde/doc/HTML/en/kcontrol/logotp3.gif

%dir /etc/X11/kde/applnk/Settings/Sound

%config(missingok) /etc/X11/kde/applnk/Settings/Input_Devices/
%config(missingok) /etc/X11/kde/applnk/Settings/Sound/bell.kdelnk
%config(missingok) /etc/X11/kde/applnk/Settings/Network/
%config(missingok) /etc/X11/kde/applnk/Settings/Information/
%config(missingok) /etc/X11/kde/applnk/Settings/Keys/
%config(missingok) /etc/X11/kde/applnk/KControl.kdelnk

%{_datadir}/kde/icons/mini/smbstatus.xpm
%{_datadir}/kde/icons/mini/kcontrol.xpm
%{_datadir}/kde/icons/mini/locale.xpm

%{_datadir}/kde/icons/bell.xpm
%{_datadir}/kde/icons/information.xpm
%{_datadir}/kde/icons/kcontrol.xpm
%{_datadir}/kde/icons/keyboard.xpm
%{_datadir}/kde/icons/locale.xpm
%{_datadir}/kde/icons/mouse.xpm
%{_datadir}/kde/icons/network.xpm
%{_datadir}/kde/icons/smbstatus.xpm

%attr(755,root,root) %{_bindir}/kcmbell
%attr(755,root,root) %{_bindir}/kcminfo
%attr(755,root,root) %{_bindir}/kcminput
%attr(755,root,root) %{_bindir}/kcmkeys
%attr(755,root,root) %{_bindir}/kcmkonsole
%attr(755,root,root) %{_bindir}/kcmlocale
%attr(755,root,root) %{_bindir}/kcmsamba
%attr(755,root,root) %{_bindir}/kcontrol

#################################################
#            KSCREENSAVER - checking OK
#################################################

%files kscreensaver -f klock.lang
%defattr(644,root,root,755)

%{_datadir}/kde/icons/mini/kscreensaver.xpm
%{_datadir}/kde/icons/kscreensaver.xpm

%{_datadir}/kde/apps/kscreensaver/

%attr(755,root,root) %{_bindir}/kcheckpass
%attr(755,root,root) %{_bindir}/klock
%attr(755,root,root) %{_bindir}/*.kss

#################################################
#            KVT - checking OK
#################################################

%files kvt -f kvt.lang
%defattr(644,root,root,755)

%{_datadir}/kde/doc/HTML/en/kvt

%config(missingok) /etc/X11/kde/applnk/Utilities/kvt.kdelnk

%{_datadir}/kde/icons/mini/kvt.xpm
%{_datadir}/kde/icons/kvt.xpm

%attr(755,root,root) %{_bindir}/kvt

#################################################
#            KMENUEDIT - checking OK
#################################################

%files kmenuedit -f kmenuedit.lang
%defattr(644,root,root,755)

%{_datadir}/kde/doc/HTML/en/kmenuedit/

%config(missingok) /etc/X11/kde/applnk/Utilities/KMenuEdit.kdelnk

%{_datadir}/kde/icons/mini/kmenuedit.xpm
%{_datadir}/kde/icons/kmenuedit.xpm

%attr(755,root,root) %{_bindir}/kmenuedit

#################################################
#            KPANEL - checking OK
#################################################

%files kpanel -f kpanel.lang -f kcmkpanel.lang
%defattr(644,root,root,755)

%config /etc/X11/kde/kpanelrc

%config(missingok) /etc/X11/kde/applnk/Settings/Applications/panel.kdelnk

%{_datadir}/kde/doc/HTML/en/kcontrol/kcmkpanel/
%{_datadir}/kde/doc/HTML/en/kpanel

%{_datadir}/kde/apps/kpanel/

%{_datadir}/kde/icons/mini/kcmkpanel.xpm
%{_datadir}/kde/icons/kcmkpanel.xpm

%attr(755,root,root) %{_bindir}/kpanel
%attr(755,root,root) %{_bindir}/kcmkpanel

#################################################
#            KDM - checking False
#################################################

%files kdm -f kdm.lang -f kdmconfig.lang
%defattr(644,root,root,755)

%{_datadir}/kde/doc/HTML/en/kdm/
%{_datadir}/kde/doc/HTML/en/kcontrol/kdmconfig/

%config(missingok) /etc/X11/kde/applnk/Settings/Applications/kdm.kdelnk
%config /etc/X11/kde/kdmrc

%{_datadir}/kde/apps/kdm/
%{_datadir}/kde/apps/kdmconfig/

%{_datadir}/kde/icons/mini/kdmconfig.xpm
%{_datadir}/kde/icons/kdmconfig.xpm

%attr(755, root, root) %{_bindir}/kdm
%attr(755, root, root) %{_bindir}/kdmdesktop
%attr(755, root, root) %{_bindir}/kdmconfig

#################################################
#            KFONTMANAGER - checking OK
#################################################

%files kfontmanager -f kfontmanager.lang
%defattr(644,root,root,755)

%{_datadir}/kde/doc/HTML/en/kfontmanager/

%config(missingok) /etc/X11/kde/applnk/System/Kfontmanager.kdelnk

%{_datadir}/kde/icons/mini/kfontmanager.xpm
%{_datadir}/kde/icons/kfontmanager.xpm

%attr(755,root,root) %{_bindir}/kfontmanager

#################################################
#            KIKBD - checking OK
#################################################

%files kikbd -f kikbd.lang
%defattr(644,root,root,755)

/etc/X11/kde/applnk/System/kikbd.kdelnk
/etc/X11/kde/kikbdrc

%{_datadir}/kde/apps/kikbd

%{_datadir}/kde/doc/HTML/en/kikbd

%{_datadir}/kde/icons/kikbd.xpm
%{_datadir}/kde/icons/mini/kikbd.xpm

%lang(ru) %{_datadir}/kde/doc/HTML/ru/kikbd

%attr(755,root,root) %{_bindir}/kcmikbd
%attr(755,root,root) %{_bindir}/kikbd
