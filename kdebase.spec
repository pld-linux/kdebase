#
# TODO:
# * KDM: ColorSheme=Default works properly with GUIStyle=KDE only
# * KDM: Replacing findwm with a better solution (it's in the way)
# * Fixing 48x48 pld applnk-pixmaps scaling (konqsidebar, kicker)
# * Adding %%doc to subpkgs
# * Kicker dosn't work properly without kwin (taskbar, systray,
#   other applets)
#
# Conditional build:
# _without_alsa		- without alsa support
#

%define         _state          snapshots
%define         _ver		3.2
%define         _snap		030516
%define		_kdelibsminrel	0.%{_snap}.1

%ifarch	sparc sparcv9 sparc64
%define		_without_alsa	1
%endif

Summary:	K Desktop Environment - core files
Summary(es):	K Desktop Environment - archivos básicos
Summary(ja):	KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ - ´ðËÜ¥Õ¥¡¥¤¥ë
Summary(ko):	KDE - ±âº» ÆÄÀÏ
Summary(pl):	K Desktop Environment - pliki ¶rodowiska
Summary(pt_BR):	K Desktop Environment - arquivos básicos
Summary(ru):	K Desktop Environment - ÂÁÚÏ×ÙÅ ÆÁÊÌÙ
Summary(uk):	K Desktop Environment - ÂÁÚÏ×¦ ÆÁÊÌÉ
Summary(zh_CN):	KDEºËÐÄ
Name:		kdebase
Version:	%{_ver}
Release:	0.%{_snap}.1
Epoch:		8
License:	GPL
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_snap}.tar.bz2
Source0:        http://team.pld.org.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
Source1:	%{name}-kdesktop.pam
Source2:	%{name}-kdm.pam
Source3:	%{name}-kdm.init
Source4:	%{name}-kdm.Xsession
Source5:	%{name}-kdm.Xservers
Source6:	%{name}-kdm_pldlogo.png
Source7:	%{name}-kdm_pldwallpaper.png
Source8:	%{name}-ircpld.desktop
Source9:	%{name}-specs.desktop
Source10:	%{name}-kde-settings.menu
Patch0:		%{name}-fix-mem-leak-in-kfind.patch
Patch2:		%{name}-fontdir.patch
Patch3:		%{name}-kcm_background.patch
#Patch4:	%{name}-kdm.daemon_output.patch
Patch5:		%{name}-kdm_utmpx.patch
Patch6:		%{name}-kdmconfig.patch
Patch7:		%{name}-kicker.patch
Patch8:		%{name}-konsole_all.patch
Patch9:		%{name}-nsplugins_dirs.patch
Patch10:	%{name}-startkde.patch
Patch11:        %{name}-kcm_fonts.patch
Patch12:	%{name}-gtkrc.patch
Patch14:	%{name}-pldcredits.patch
Patch16:	%{name}-kicker_nodesktop.patch
Patch17:        %{name}-xfsreload.patch
Patch18:	%{name}-kdesukonsole.patch
Patch19:	%{name}-vroot.patch
Patch21:	%{name}-vcategories.patch
Patch22:	%{name}-screensavers.patch
Patch23:	%{name}-prefmenu.patch
%{?_without_alsa:BuildConflicts:	alsa-driver-devel}
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	arts-devel >= 1.1
BuildRequires:	arts-kde-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	awk
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cups-devel
BuildRequires:	db-devel
BuildRequires:	findutils
BuildRequires:	gettext-devel
BuildRequires:	grep
BuildRequires:	kdelibs-devel >= %{version}-%{_kdelibsminrel}
BuildRequires:	kdelibs-static >= %{version}-%{_kdelibsminrel}
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libsmbclient-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	motif-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	sed >= 4.0
# TODO: sensors
#BuildRequires:	sensors-devel
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
Requires:       kde-sdscreen
Requires:	konqueror = %{version}-%{release}
Obsoletes:	%{name}-fonts
Obsoletes:	%{name}-kcheckpass
Obsoletes:	%{name}-kdesktop
Obsoletes:	%{name}-kdesktop_lock
Obsoletes:	%{name}-khelpcenter
Obsoletes:	%{name}-kioslave
Obsoletes:	%{name}-konqueror
Obsoletes:	%{name}-kwin
Obsoletes:	%{name}-kxmlrpc
Obsoletes:	%{name}-screensaver
Obsoletes:	%{name}-static
Obsoletes:	%{name}-wallpapers
Obsoletes:	kde-splash
Obsoletes:	kde-theme-keramik
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_fontdir	/usr/share/fonts/misc
%define		_htmldir	%{_docdir}/kde/HTML
%define		_sysconfdir	/etc/X11
%define		_vfinfodir	%{_datadir}/desktop-directories

%define 	_noautoreqdep			libGL.so.1 libGLU.so.1
%define		no_install_post_chrpath		1

%description
KDE specific files. Used by core KDE applications. Package includes:
- KDE menu hierarchy,
- kappfinder - script installing some non-KDE apps in KDE menu,

%description -l ja
KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ÍÑ¤Î´ðËÜ¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¡£
°Ê²¼¤Î¤è¤¦¤Ê¥Ñ¥Ã¥±¡¼¥¸¤¬Æþ¤Ã¤Æ¤¤¤Þ¤¹¡£

%description -l pl
Pliki specyficzne dla ¶rodowiska KDE i wykorzystywane przez g³ówne
aplikacje KDE. Pakiet zawiera:
- Hierarchiê menu KDE,
- kappfinder - skrypt u³awiaj±cy uruchamianie niektórych programów
  spoza KDE

%description -l ru
âÁÚÏ×ÙÅ ÐÒÏÇÒÁÍÍÙ ÄÌÑ K Desktop Environment. ÷ËÌÀÞÅÎÙ: kdm (ÚÁÍÅÎÁ
xdm), kwin (ÏËÏÎÎÙÊ ÍÅÎÅÄÖÅÒ), konqueror (ÆÁÊÌÏ×ÙÊ ÍÅÎÅÄÖÅÒ,
web-ÂÒÁÕÚÅÒ, ftp-ËÌÉÅÎÔ, ...), konsole (ÚÁÍÅÎÁ xterm), kicker
(ÚÁÐÕÓËÁÌËÁ ÐÒÏÇÒÁÍÍ É ÐÅÊÄÖÅÒ ÒÁÂÏÞÅÇÏ ÓÔÏÌÁ), kaudio (ÁÕÄÉÏÓÅÒ×ÅÒ),
kdehelp (ÐÒÏÇÒÁÍÍÁ ÄÌÑ ÐÒÏÓÍÏÔÒÁ ÓÐÒÁ×ÏÞÎÙÈ ÆÁÊÌÏ× kde, ÆÁÊÌÏ× info É
man), kthememgr (ÓÉÓÔÅÍÁ ÄÌÑ ÕÐÒÁ×ÌÅÎÉÑ ÁÌØÔÅÒÎÁÔÉ×ÎÙÍÉ ÐÁËÅÔÁÍÉ ÔÅÍ)
É ÄÒÕÇÉÅ ËÏÍÐÏÎÅÎÔÙ KDE (kcheckpass, kikbd, kscreensaver, kcontrol,
kfind, kfontmanager, kmenuedit, kappfinder).

%description -l uk
âÁÚÏ×¦ ÐÒÏÇÒÁÍÉ ÄÌÑ K Desktop Environment. ÷ËÌÀÞÅÎ¦: kdm (ÚÁÍ¦ÎÁ xdm),
ftp-ËÌ¦ÅÎÔ, ...), konsole (ÚÁÍ¦ÎÁ xterm), kicker (ÚÁÐÕÓËÁÌËÁ ÐÒÏÇÒÁÍ
ÔÁ ÐÅÊÄÖÅÒ ÒÏÂÏÞÏÇÏ ÓÔÏÌÕ), kaudio (ÁÕÄ¦ÏÓÅÒ×ÅÒ), kdehelp (ÐÒÏÇÒÁÍÁ
ÄÌÑ ÐÅÒÅÇÌÑÄÕ ÆÁÊÌ¦× ÄÏ×¦ÄËÉ kde, ÆÁÊÌ¦× info ÔÁ man), kthememgr
(ÓÉÓÔÅÍÁ ÄÌÑ ËÅÒÕ×ÁÎÎÑ ÁÌØÔÅÒÎÁÔÉ×ÎÉÍÉ ÐÁËÅÔÁÍÉ ÔÅÍ) ÔÁ ¦ÎÛ¦
ËÏÍÐÏÎÅÎÔÉ KDE (kcheckpass, kikbd, kscreensaver, kcontrol, kfind,
kfontmanager, kmenuedit, kappfinder).

%package devel
Summary:	Include files to develop KDE applications
Summary(pl):	Pliki nag³ówkowe potrzebne do programowania
Summary(pt_BR):	Arquivos de inclusão para compilar aplicativos que usem bibliotecas do kdebase
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-kicker = %{version}-%{release}
Requires:	%{name}-ksysguard = %{version}-%{release}
Requires:	kdelibs-devel >= %{version}-%{_kdelibsminrel}

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe niezbêdne do programowania aplikacji
KDE.

%description devel -l pt_BR
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos que usem bibliotecas do kdebase.

%package -n kde-decoration-b2
Summary:	KDE Window Decoration - B2
Summary(pl):	Dekoracja okna dla KDE - B2
Group:		X11/Amusements
Requires:	%{name} = %{version}-%{release}

%description -n kde-decoration-b2
KDE Window Decoration - B2.

%description -n kde-decoration-b2 -l pl
Dekoracja okna dla KDE - B2.

%package -n kde-decoration-laptop
Summary:	KDE Window Decoration - Laptop
Summary(pl):	Dekoracja okna dla KDE - Laptop
Group:		X11/Amusements
Requires:	%{name} = %{version}-%{release}

%description -n kde-decoration-laptop
KDE Window Decoration - Laptop.

%description -n kde-decoration-laptop -l pl
Dekoracja okna dla KDE - Laptop.

%package -n kde-decoration-modernsys
Summary:	KDE Window Decoration - ModernSys
Summary(pl):	Dekoracja okna dla KDE - ModernSys
Group:		X11/Amusements
Requires:	%{name} = %{version}-%{release}

%description -n kde-decoration-modernsys
KDE Window Decoration - ModernSys.

%description -n kde-decoration-modernsys -l pl
Dekoracja okna dla KDE - ModernSys.

%package -n kde-decoration-quartz
Summary:	KDE Window Decoration - Quartz
Summary(pl):	Dekoracja okna dla KDE - Quartz
Group:		X11/Amusements
Requires:	%{name} = %{version}-%{release}

%description -n kde-decoration-quartz
KDE Window Decoration - Quartz.

%description -n kde-decoration-quartz -l pl
Dekoracja okna dla KDE - Quartz.

%package -n kde-decoration-redmond
Summary:	KDE Window Decoration - Redmond
Summary(pl):	Dekoracja okna dla KDE - Redmond
Group:		X11/Amusements
Requires:	%{name} = %{version}-%{release}

%description -n kde-decoration-redmond
KDE Window Decoration - Redmond.

%description -n kde-decoration-redmond -l pl
Dekoracja okna dla KDE - Redmond.

%package -n kde-decoration-web
Summary:	KDE Window Decoration - Web
Summary(pl):	Dekoracja okna dla KDE - Web
Group:		X11/Amusements
Requires:	%{name} = %{version}-%{release}

%description -n kde-decoration-web
KDE Window Decoration - Web.

%description -n kde-decoration-web -l pl
Dekoracja okna dla KDE - Web.

%package -n kde-sdscreen-default
Summary:        KDE "Logout" picture
Summary(pl):    Obrazek okna "Wyloguj" KDE
Group:          X11/Amusements
Provides:       kde-sdscreen
Requires:	%{name} >= 3.0.3
Obsoletes:	kde-sdscreen-KDEGirl
Obsoletes:      kde-sdscreen-keramik

%description -n kde-sdscreen-default
Default KDE "Logout" picture.

%description -n kde-sdscreen-default -l pl
Standardowy obrazek okna "Wyloguj" KDE.

%package common-filemanagement
Summary:	Common Files for kate and konqueror
Summary(pl):	Pliki wspólne dla kate i konquerora
Group:		X11/Libraries
Requires:	%{name}-common-konsole = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}

%description common-filemanagement
Common files needed by kate and konqueror.

%description common-filemanagement -l pl
Pliki wspólne, u¿ywane przez kate i konquerora.

%package common-konsole
Summary:	Common files for konsole and konsolepart
Summary(pl):	Pliki wspólne dla konsole i konsolepart
Group:		X11/Applications
Requires(post,postun):	/usr/X11R6/bin/mkfontdir
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	%{name}-fonts

%description common-konsole
Common files for konsole and konsolepart.

%description common-konsole -l pl
Pliki wspólne dla konsole i konsolepart.

%package core
Summary:	KDE Core Apps
Summary(pl):	Podstawowe aplikacje KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name} < 3.2-0.030428.1
Obsoletes:	%{name}-kcontrol
Obsoletes:	%{name}-khelpcenter
Obsoletes:      %{name}-helpcenter

%description core
KDE Core apps. This package contains:
- Control Center;
- Help Center;
- Print System;
- Crash Handlers;
- A Frontend for "su" program.

%description core -l pl
Podstawowe aplikacje ¶rodowiska KDE. Pakiet ten zawiera:
- Centrum sterowania;
- System drukowania;
- System pomocy;
- Programy obs³ugi b³êdów;
- Frontend dla programu "su".

%package infocenter
Summary:	KDE Info Center
Summary(pl):	Centrum informacji o systemie dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}

%description infocenter
KDE Info Center.

%description infocenter -l pl
Centrum informacji o systemie dla KDE.

%package kappfinder
Summary:	Menu Updating Tool
Summary(pl):	Narzêdzie do aktualizacji menu
Group:		X11/Applications
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name} =< 3.2-0.030418.2

%description kappfinder
Menu Updating Tool.

%description kappfinder -l pl
Narzêdzie do aktualizacji menu.

%package kate
Summary:	KDE Advanced Text Editor
Summary(pl):	Zaawansowany edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-common-filemanagement = %{version}-%{release}
Requires:	%{name}-libkate = %{version}-%{release}

Obsoletes:	kate

%description kate
KDE advanced text editor.

%description kate -l pl
Zaawansowany edytor tekstu dla KDE.

%package kdeprintfax
Summary:	KDE Fax Tool
Summary(pl):	Narzêdzie do faksowania dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	efax
Requires:	enscript

%description kdeprintfax
KDE Fax Tool.

%description kdeprintfax -l pl
Narzêdzie do faksowania dla KDE.

%package kdialog
Summary:	A KDE version of dialog
Summary(pl):	Wersja KDE dialogu
Group:		X11/Applications
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name} < 3.2-0.030423.2

%description kdialog
Allows to display menu boxes from shell scripts.

%description kdialog -l pl
Umo¿liwia wy¶wietlanie komunikatów z poziomu skryptów
pow³oki.

%package kfind
Summary:	KDE Find Tool
Summary(pl):	Narzêdzie do wyszukiwania plików dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	kfind

%description kfind
KDE Find Tool.

%description kfind -l pl
Narzêdzie do wyszukiwania plików dla KDE.

%package kicker
Summary:        KDE Panel - kicker
Summary(pl):    Panel KDE - kicker
Group:          X11/Applications
Requires:	applnk >= 1.6.2
Requires:	%{name}-kmenuedit = %{version}-%{release}
Requires:	%{name}-libkonq = %{version}-%{release}

%description kicker
KDE Panel - kicker.

%description kicker -l pl
Panel KDE - kicker.

%package kjobviewer
Summary:        Print Job Viewer
Summary(pl):    Podgl±d zadañ drukowania
Group:          X11/Applications
Requires:	%{name} = %{version}-%{release}

%description kjobviewer
KDE Print Job Viewer.

%description kjobviewer -l pl
Podgl±d zadañ drukowania dla KDE.

%package klipper
Summary:        Clipboard Tool
Summary(pl):    Narzêdzie schowka
Group:          X11/Applications
Requires:       %{name}-kicker = %{version}-%{release}

%description klipper
KDE Clipboard Tool.

%description klipper -l pl
Narzêdzie schowka dla KDE.

%package kmenuedit
Summary:        Menu Editor
Summary(pl):    Edytor menu
Group:          X11/Applications
Requires:       %{name}-core = %{version}-%{release}

%description kmenuedit
KDE Menu Editor.

%description kmenuedit -l pl
Edytor menu KDE.

%package konsole
Summary:	KDE Terminal Emulator
Summary(pl):	Emulator terminala dla KDE
Group:		X11/Applications
Requires:	%{name}-common-konsole = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	konsole

%description konsole
KDE Terminal Emulator.

%description konsole -l pl
Emulator terminala dla KDE.

%package kpager
Summary:	Desktop Pager
Summary(pl):	Prze³±cznik biurek
Group:		X11/Applications
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name} =< 3.2-0.030418.2

%description kpager
KDE Desktop Pager.

%description kpager -l pl
Prze³±cznik biurek dla KDE.

%package ksysguard
Summary:	System Guard
Summary(pl):	Stra¿nik systemu
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}

%description ksysguard
KDE System Guard.

%description ksysguard -l pl
Stra¿nik systemu dla KDE.

%package ksystraycmd
Summary:	A tool that allows running applications in taskbar
Summary(pl):	Narzêdzie do uruchamiania aplikacji w pasku zadañ
Group:		X11/Applications
Requires:	%{name}-kicker = %{version}-%{release}

%description ksystraycmd
KSysTrayCmd is a utility that allows you to run any application you
like in the system tray, not just those designed to use it.

%description ksystraycmd -l pl
KSysTrayCmd to narzêdzie pozwalaj±ce na uruchomienie dowolnej
aplikacji w tacce systemowej - nie tylko tych, które zosta³y
wyposa¿one w tak± w³a¶ciwo¶æ.

%package kwmtheme
Summary:	Desktop Theme Manager
Summary(pl):	Zarz±dca motywów biurka
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description kwmtheme
KDE Desktop Theme Manager. This package contains also a few desktop
themes.

%description kwmtheme -l pl
Zarz±dca motywów biurka KDE. Ten pakiet zawiera równie¿ kilka motywów.

%package kwrite
Summary:	KDE Text Editor
Summary(pl):	Edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-libkate = %{version}-%{release}
Obsoletes:	kwrite

%description kwrite
KDE text editor with syntax highlighting.

%description kwrite -l pl
Edytor tekstu z pod¶wietlaniem sk³adni dla KDE.

%package kwrited
Summary:	KDE Write Daemon
Summary(pl):	Demon zapisu KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name} < 3.2-0.030423.1

%description kwrited
KDE Write Daemon.

%description kwrited -l pl
Demon zapisu KDE.

%package libkate
Summary:	A libraries for KDE text editors
Summary(pl):	Biblioteki dla edytorów tekstu KDE
Group:		X11/Libraries
Requires:	%{name}-libkmultitabbar = %{version}-%{release}
Obsoletes:	%{name}-kate < 3.2-0.030423.1

%description libkate
A libraries for KDE text editors.

%description libkate -l pl
Biblioteki dla edytorów tekstu KDE.

%package libkmultitabbar
Summary:	Library containing multiple tab support
Summary(pl):	Biblioteka zawieraj±ca obs³ugê kilku kart
Group:		X11/Libraries
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name}-common-filemanagement < 3.2-0.030428.1

%description libkmultitabbar
Library containing multiple tab support.

%description libkmultitabbar -l pl
Biblioteka zawieraj±ca obs³ugê kilku kart.

%package libkonq
Summary:	Konqueror library files
Summary(pl):	Biblioteki wykorzystywane przez konquerora
Group:		X11/Libraries
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	konqueror < 3.2-0.030423.2

%description libkonq
Libraries containing functions used by konqueror.

%description libkonq -l pl
Biblioteki zawieraj±ce funkcje wykorzystywane przez konquerora.

%package mailnews
Summary:	KDE Mail and News Services
Summary(pl):	Obs³uga protoko³ów pocztowych i news dla KDE
Group:		X11/Libraries
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	%{name}-kioslave

%description mailnews
KDE Mail and News Services.

%description mailnews -l pl
Obs³uga protoko³ów pocztowych i news dla KDE.

%package screensavers
Summary:	KDE screensavers
Summary(pl):	Wygaszacze ekranu desktopu KDE
Summary(ru):	ÈÒÁÎÉÔÅÌÉ ÜËÒÁÎÁ ÄÌÑ KDE
Summary(uk):	ÚÂÅÒ¦ÇÁÞ¦ ÅËÒÁÎÕ ÄÌÑ KDE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description screensavers
KDE screensavers.

%description screensavers -l pl
Wygaszacze ekranu desktopu KDE.

%description screensavers -l ru
îÅËÏÔÏÒÙÅ 3D ÈÒÁÎÉÔÅÌÉ ÜËÒÁÎÁ ÄÌÑ K Desktop Environment.

%package -n kdm
Summary:	KDE Display Manager
Summary(pl):	Zarz±dca ekranów KDE
Group:		X11/Applications
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires(pre):	user-xdm
Requires:	%{name}-core = %{version}-%{release}
Requires:	pam
Requires:	sessreg
Requires:	xinitrc
Obsoletes:	gdm
Obsoletes:	xdm
Obsoletes:	%{name}-kdm
Obsoletes:	%{name}-pam

%description -n kdm
It is KDE replacement for XDM. It manages local and remote X11
displays.

%description -n kdm -l pl
Zamiennik XDM rodem z KDE. Zarz±dza lokalnymi i zdalnymi ekranami X11.

%package -n konqueror
Summary:	Konqueror - web browser and file manager
Summary(pl):	Konqueror - przegl±darka WWW i zarz±dca plików
Group:		X11/Applications
Requires:	%{name}-common-filemanagement = %{version}-%{release}
Requires:	%{name}-konsole = %{version}-%{release}
Requires:	%{name}-libkonq = %{version}-%{release}
Requires:	%{name}-libkmultitabbar = %{version}-%{release}
Requires:	%{name}-mailnews = %{version}-%{release}
Obsoletes:	%{name}-konqueror

%description -n konqueror
Konqueror is a web browser and file manager similar to MS Internet
Explorer.

%description -n konqueror -l pl
Konqueror jest przegl±dark± WWW i zarz±dc± plików podobnym do MS
Internet Explorer.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch14 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

for plik in `find ./ -name *.desktop` ; do
	echo $plik
	sed -i -e "s/\[nb\]/\[no\]/g" $plik
done

%configure \
	--with-kdm-pam=kdm \
	--with-pam=kdesktop

%{__make}

cd ksplashml
%{__make}
cd -

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cd ksplashml
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd -

install -d \
	$RPM_BUILD_ROOT/etc/{xdg/menus,pam.d,rc.d/init.d,security} \
	$RPM_BUILD_ROOT%{_libdir}/kde3/plugins/konqueror

mv $RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xservers{,.orig}
mv $RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xsession{,.orig}

touch $RPM_BUILD_ROOT/etc/security/blacklist.kdm

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/pam.d/kdesktop
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/kdm
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/rc.d/init.d/kdm
install %{SOURCE4}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xsession
install %{SOURCE5}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xservers
install %{SOURCE6}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/pics/pldlogo.png
install %{SOURCE7}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/pics/pldwallpaper.png
install %{SOURCE8}	$RPM_BUILD_ROOT%{_datadir}/services/searchproviders/ircpld.desktop
install %{SOURCE9}	$RPM_BUILD_ROOT%{_datadir}/services/searchproviders/specs.desktop
install %{SOURCE10}	$RPM_BUILD_ROOT/etc/xdg/menus/kde-settings.menu

cp $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/dirtree/remote/smb-network.desktop \
    $RPM_BUILD_ROOT%{_datadir}/apps/konqsidebartng/virtual_folders/remote

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv $ALD/{Settings,KDE-Settings}
mv $ALD/Help.desktop			$RPM_BUILD_ROOT%{_desktopdir}
mv $ALD/Settingsmenu/*.desktop		$RPM_BUILD_ROOT%{_desktopdir}
mv $ALD/System/kinfocenter.desktop	$RPM_BUILD_ROOT%{_desktopdir}


> core.lang
programs=" \
	colors \
	fonts \
	kcmstyle \
	kdeprint \
	kdebugdialog \
	kdesu \
	khelpcenter \
	language"

for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> core.lang
done

> %{name}.lang
programs=" \
	arts \
	background \
	bell \
	desktop \
	energy \
	kcmaccess \
	kcmfontinst \
	kcmlaunch \
	kcmnotify \
	kcmsmserver \
	keyboard \
	keys \
	kwindecoration \
	mouse \
	passwords \
	spellchecking \
	windowmanagement"

for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> %{name}.lang
done

%find_lang kicker	--with-kde
programs=" \
	clock \
	kcmtaskbar \
	panel"

for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kicker.lang
done

%find_lang konqueror	--with-kde
programs="\
	cache \
	cookies \
	crypto \
	ebrowsing \
	email \
	filemanager \
	filetypes \
	icons \
	kcmcss \
	khtml \
	netpref \
	proxy \
	smb \
	useragent"

for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> konqueror.lang
done

%find_lang	kate		--with-kde
%find_lang	kcmkonsole	--with-kde
%find_lang	kdm		--with-kde
%find_lang	kfind		--with-kde
%find_lang	kinfocenter	--with-kde
%find_lang	kioslave	--with-kde
%find_lang	klipper		--with-kde
%find_lang	kmenuedit	--with-kde
%find_lang	konsole		--with-kde
%find_lang	ksysguard	--with-kde
%find_lang	kpager		--with-kde
%find_lang	kthememgr	--with-kde
%find_lang	kwrite		--with-kde
%find_lang	screensaver	--with-kde

cat kcmkonsole.lang	>> konsole.lang
cat kioslave.lang	>> kinfocenter.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%post common-konsole
cd %{_fontdir}
umask 022
/usr/X11R6/bin/mkfontdir

%postun common-konsole
cd %{_fontdir}
umask 022
/usr/X11R6/bin/mkfontdir

%post	kicker		-p /sbin/ldconfig
%postun	kicker		-p /sbin/ldconfig

%post	ksysguard	-p /sbin/ldconfig
%postun	ksysguard	-p /sbin/ldconfig

%post	libkate		-p /sbin/ldconfig
%postun	libkate		-p /sbin/ldconfig

%post	libkmultitabbar	-p /sbin/ldconfig
%postun	libkmultitabbar	-p /sbin/ldconfig

%post	libkonq		-p /sbin/ldconfig
%postun	libkonq		-p /sbin/ldconfig

%post -n kdm
/sbin/chkconfig --add kdm
if [ -f /var/lock/subsys/kdm ]; then
	echo "To make sure that new version of KDM is running you should restart"
	echo "KDM with:"
	echo "/etc/rc.d/init.d/kdm restart"
	echo
	echo "WARNING: restarting KDM will terminate any X session started by it!"
	else
	echo "Run \"/etc/rc.d/init.d/kdm start\" to start kdm." >&2
fi

%preun -n kdm
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/kdm ]; then
		/etc/rc.d/init.d/kdm stop >&2
	fi
	/sbin/chkconfig --del kdm
fi

%post	-n konqueror	-p /sbin/ldconfig
%postun	-n konqueror	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README README.pam
%config(noreplace) %verify(not size mtime md5) /etc/pam.d/kdesktop
%attr(0755,root,root) %{_bindir}/kaccess
%attr(0755,root,root) %{_bindir}/kcheckpass
%attr(0755,root,root) %{_bindir}/kdcop
%attr(0755,root,root) %{_bindir}/kdeeject
%attr(0755,root,root) %{_bindir}/kdesktop
%attr(0755,root,root) %{_bindir}/kdesktop_lock
%attr(0755,root,root) %{_bindir}/khotkeys
%attr(0755,root,root) %{_bindir}/kpersonalizer
%attr(0755,root,root) %{_bindir}/krdb
%attr(0755,root,root) %{_bindir}/kreadconfig
%attr(0755,root,root) %{_bindir}/ksmserver
%attr(0755,root,root) %{_bindir}/ksplash
%attr(0755,root,root) %{_bindir}/kstart
%attr(0755,root,root) %{_bindir}/ktip
%attr(0755,root,root) %{_bindir}/kwebdesktop
%attr(0755,root,root) %{_bindir}/kwin
%attr(0755,root,root) %{_bindir}/kxkb
%attr(0755,root,root) %{_bindir}/startkde
%{_libdir}/kaccess.la
%attr(0755,root,root) %{_libdir}/kaccess.so
%{_libdir}/kdesktop.la
%attr(0755,root,root) %{_libdir}/kdesktop.so
%{_libdir}/khotkeys.la
%attr(0755,root,root) %{_libdir}/khotkeys.so
%{_libdir}/ksmserver.la
%attr(0755,root,root) %{_libdir}/ksmserver.so
%{_libdir}/kwin.la
%attr(0755,root,root) %{_libdir}/kwin.so
%{_libdir}/kxkb.la
%attr(0755,root,root) %{_libdir}/kxkb.so
%{_libdir}/libksplashthemes.la
%attr(0755,root,root) %{_libdir}/libksplashthemes.so.*.*.*
%{_libdir}/kde3/kcm_access.la
#%{_libdir}/libsensordisplays.la
#%attr(0755,root,root) %{_libdir}/libsensordisplays.so.*.*.*
%attr(0755,root,root) %{_libdir}/kde3/kcm_access.so
%{_libdir}/kde3/kcm_arts.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_arts.so
%{_libdir}/kde3/kcm_background.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_background.so
%{_libdir}/kde3/kcm_bell.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_bell.so
%{_libdir}/kde3/kcm_componentchooser.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_componentchooser.so
%{_libdir}/kde3/kcm_email.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_email.so
%{_libdir}/kde3/kcm_energy.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_energy.so
%{_libdir}/kde3/kcm_fontinst.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_fontinst.so
%{_libdir}/kde3/kcm_input.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_input.so
%{_libdir}/kde3/kcm_keyboard.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_keyboard.so
%{_libdir}/kde3/kcm_keys.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_keys.so
 %{_libdir}/kde3/kcm_khotkeys.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_khotkeys.so
%{_libdir}/kde3/kcm_knotify.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_knotify.so
%{_libdir}/kde3/kcm_ksplashthemes.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_ksplashthemes.so
%{_libdir}/kde3/kcm_kwindecoration.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kwindecoration.so
%{_libdir}/kde3/kcm_kwinoptions.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kwinoptions.so
%{_libdir}/kde3/kcm_launch.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_launch.so
%{_libdir}/kde3/kcm_passwords.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_passwords.so
%{_libdir}/kde3/kcm_smserver.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_smserver.so
%{_libdir}/kde3/kcm_spellchecking.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_spellchecking.so
%{_libdir}/kde3/kcm_xinerama.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_xinerama.so
%{_libdir}/kde3/kwin_default.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_default.so
%{_libdir}/kde3/kwin_default_config.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_default_config.so
%{_libdir}/kde3/kwin_keramik.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_keramik.so
%{_libdir}/kde3/kwin_keramik_config.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_keramik_config.so
%{_libdir}/kde3/libksplashdefault.la
%attr(0755,root,root) %{_libdir}/kde3/libksplashdefault.so*
%{_datadir}/apps/clockapplet
%{_datadir}/apps/kcm_componentchooser/*
%{_datadir}/apps/kcmfontinst
%{_datadir}/apps/kcminput
%{_datadir}/apps/kcmkeys
%{_datadir}/apps/kcmlocale
%{_datadir}/apps/kconf_update/*
%{_datadir}/apps/kdcop
%{_datadir}/apps/kdesktop
%{_datadir}/apps/kdewizard
%{_datadir}/apps/kdisplay/app-defaults
%{_datadir}/apps/kpersonalizer
%dir %{_datadir}/apps/ksmserver
%dir %{_datadir}/apps/ksplash
%dir %{_datadir}/apps/ksplash/Themes
%{_datadir}/apps/ksplash/Themes/Default
%dir %{_datadir}/apps/kwin
%{_datadir}/apps/kwin/eventsrc
%{_datadir}/apps/kwin/keramik.desktop
%dir %{_datadir}/apps/kwin/pics
%{_datadir}/apps/kwin/pics/*
%{_datadir}/autostart/kdesktop.desktop
%{_datadir}/autostart/khotkeys.desktop
%{_datadir}/autostart/ktip.desktop
%{_datadir}/config/kdesktop_custom_menu1
%{_datadir}/config/kdesktop_custom_menu2
%{_datadir}/config/kxkb_groups
%{_datadir}/services/kaccess.desktop
%{_datadir}/services/kdeprint_part.desktop
%{_datadir}/services/ksplash.desktop
%{_datadir}/services/ksplashdefault.desktop
%{_datadir}/services/kxkb.desktop
%{_datadir}/servicetypes/ksplashplugins.desktop
%{_datadir}/sounds
%{_datadir}/templates
%{_datadir}/wallpapers
%{_applnkdir}/.hidden/battery.desktop
%{_applnkdir}/.hidden/bwarning.desktop
%{_applnkdir}/.hidden/cwarning.desktop
%{_applnkdir}/.hidden/kcmkxmlrpcd.desktop
%{_applnkdir}/.hidden/kwinactions.desktop
%{_applnkdir}/.hidden/kwinadvanced.desktop
%{_applnkdir}/.hidden/kwinfocus.desktop
%{_applnkdir}/.hidden/kwinmoving.desktop
%{_applnkdir}/.hidden/midi.desktop
%{_applnkdir}/.hidden/power.desktop
%{_applnkdir}/.hidden/socks.desktop
%{_applnkdir}/.hidden/virtualdesktops.desktop
%{_applnkdir}/Home.desktop
%{_applnkdir}/KDE-Settings/Accessibility/kcmaccess.desktop
%{_applnkdir}/KDE-Settings/Accessibility/keyboard_layout.desktop
%{_applnkdir}/KDE-Settings/Accessibility/keys.desktop
%{_applnkdir}/KDE-Settings/Components/componentchooser.desktop
%{_applnkdir}/KDE-Settings/Components/kcmsmserver.desktop
%{_applnkdir}/KDE-Settings/Components/spellchecking.desktop
%{_applnkdir}/KDE-Settings/Desktop/desktop.desktop
%{_applnkdir}/KDE-Settings/Desktop/desktopbehavior.desktop
%{_applnkdir}/KDE-Settings/Desktop/kwinoptions.desktop
%{_applnkdir}/KDE-Settings/Desktop/xinerama.desktop
# hidden
%{_applnkdir}/KDE-Settings/LookNFeel/Themes
%{_applnkdir}/KDE-Settings/email.desktop
#
%{_applnkdir}/KDE-Settings/LookNFeel/background.desktop
%{_applnkdir}/KDE-Settings/LookNFeel/kcmlaunch.desktop
%{_applnkdir}/KDE-Settings/LookNFeel/ksplashthememgr.desktop
%{_applnkdir}/KDE-Settings/LookNFeel/kwindecoration.desktop
%{_applnkdir}/KDE-Settings/Network/email.desktop
%{_applnkdir}/KDE-Settings/Peripherals/keyboard.desktop
%{_applnkdir}/KDE-Settings/Peripherals/mouse.desktop
%{_applnkdir}/KDE-Settings/PowerControl/energy.desktop
%{_applnkdir}/KDE-Settings/Security/passwords.desktop
%{_applnkdir}/KDE-Settings/Sound/arts.desktop
%{_applnkdir}/KDE-Settings/Sound/bell.desktop
%{_applnkdir}/KDE-Settings/Sound/kcmnotify.desktop
%{_applnkdir}/KDE-Settings/System/desktoppath.desktop
%{_applnkdir}/KDE-Settings/System/kcmfontinst.desktop
# hidden
%{_applnkdir}/System/kpersonalizer.desktop
#
%{_desktopdir}/kpersonalizer.desktop
%{_desktopdir}/ktip.desktop
#%{_desktopdir}/printmgr.desktop
%{_pixmapsdir}/*/*/apps/access.png
%{_pixmapsdir}/*/*/apps/acroread.png
%{_pixmapsdir}/*/*/apps/alevt.png
%{_pixmapsdir}/*/*/apps/applixware.png
%{_pixmapsdir}/*/*/apps/arts.png
%{_pixmapsdir}/*/*/apps/background.png
%{_pixmapsdir}/*/*/apps/blender.png
%{_pixmapsdir}/*/*/apps/clanbomber.png
%{_pixmapsdir}/*/*/apps/designer.png
%{_pixmapsdir}/*/*/apps/dlgedit.png
%{_pixmapsdir}/*/*/apps/emacs.png
%{_pixmapsdir}/*/*/apps/email.png
%{_pixmapsdir}/*/*/apps/energy_star.png
%{_pixmapsdir}/*/*/apps/error.png
%{_pixmapsdir}/*/*/apps/galeon.png
%{_pixmapsdir}/*/*/apps/gimp.png
%{_pixmapsdir}/*/*/apps/gnome
%{_pixmapsdir}/*/*/apps/gvim.png
%{_pixmapsdir}/*/*/apps/gv.png
%{_pixmapsdir}/[!l]*/*/apps/kcmfontinst.png
%{_pixmapsdir}/*/*/apps/kcmkwm.png
%{_pixmapsdir}/*/*/apps/kcmmidi.png
%{_pixmapsdir}/*/*/apps/kdisknav.png
%{_pixmapsdir}/*/*/apps/keyboard_layout.png
%{_pixmapsdir}/*/*/apps/keyboard.png
%{_pixmapsdir}/*/*/apps/knotify.png
%{_pixmapsdir}/*/*/apps/kpersonalizer.png
%{_pixmapsdir}/*/*/apps/ktip.png
%{_pixmapsdir}/*/*/apps/kvirc.png
%{_pixmapsdir}/*/*/apps/kwin.png
%{_pixmapsdir}/*/*/apps/kxkb.png
%{_pixmapsdir}/*/*/apps/licq.png
%{_pixmapsdir}/*/*/apps/linuxconf.png
%{_pixmapsdir}/*/*/apps/lyx.png
%{_pixmapsdir}/*/*/apps/mathematica.png
%{_pixmapsdir}/*/*/apps/mozilla
%{_pixmapsdir}/*/*/apps/mozilla.png
%{_pixmapsdir}/*/*/apps/nedit.png
%{_pixmapsdir}/*/*/apps/netscape.png
%{_pixmapsdir}/*/*/apps/opera.png
%{_pixmapsdir}/*/*/apps/password.png
%{_pixmapsdir}/*/*/apps/penguin.png
%{_pixmapsdir}/*/*/apps/phppg.png
%{_pixmapsdir}/*/*/apps/plan.png
%{_pixmapsdir}/*/*/apps/pybliographic.png
%{_pixmapsdir}/*/*/apps/pysol.png
%{_pixmapsdir}/*/*/apps/qtella.png
%{_pixmapsdir}/*/*/apps/realplayer.png
%{_pixmapsdir}/*/*/apps/remote.png
%{_pixmapsdir}/*/*/apps/soffice.png
%{_pixmapsdir}/*/*/apps/staroffice.png
%{_pixmapsdir}/*/*/apps/terminal.png
%{_pixmapsdir}/*/*/apps/tux.png
%{_pixmapsdir}/*/*/apps/vnc.png
%{_pixmapsdir}/*/*/apps/wabi.png
%{_pixmapsdir}/*/*/apps/window_list.png
%{_pixmapsdir}/*/*/apps/winprops.png
%{_pixmapsdir}/*/*/apps/wmaker_apps.png
%{_pixmapsdir}/*/*/apps/wp.png
%{_pixmapsdir}/*/*/apps/xapp.png
%{_pixmapsdir}/*/*/apps/xawtv.png
%{_pixmapsdir}/*/*/apps/xcalc.png
%{_pixmapsdir}/*/*/apps/xchat.png
%{_pixmapsdir}/*/*/apps/xclipboard.png
%{_pixmapsdir}/*/*/apps/xclock.png
%{_pixmapsdir}/*/*/apps/xconsole.png
%{_pixmapsdir}/*/*/apps/xedit.png
%{_pixmapsdir}/*/*/apps/xemacs.png
%{_pixmapsdir}/*/*/apps/xeyes.png
%{_pixmapsdir}/*/*/apps/xfig.png
%{_pixmapsdir}/*/*/apps/xfmail.png
%{_pixmapsdir}/*/*/apps/xload.png
%{_pixmapsdir}/*/*/apps/xmag.png
%{_pixmapsdir}/*/*/apps/xmms.png
%{_pixmapsdir}/*/*/apps/xosview.png
%{_pixmapsdir}/*/*/apps/xpaint.png
%{_pixmapsdir}/*/*/apps/x.png
%{_pixmapsdir}/*/*/apps/xv.png

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/kwin
%{_includedir}/*.h
%{_includedir}/kwin/*.h
%{_includedir}/kate
%{_includedir}/ksgrd
%{_includedir}/ksplash
%{_libdir}/libkateinterfaces.so
%{_libdir}/libkateutils.so
%{_libdir}/libkickermain.so
%{_libdir}/libkmultitabbar.so
%{_libdir}/libkonq.so
%{_libdir}/libkonqsidebarplugin.so
%{_libdir}/libksgrd.so
%{_libdir}/libksplashthemes.so
%{_libdir}/libnsplugin.so
##%{_libdir}/libsensordisplays.so
%{_libdir}/libtaskbar.so
%{_libdir}/libtaskmanager.so

%files -n kde-decoration-b2
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin_b2.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_b2.so
%{_libdir}/kde3/kwin_b2_config.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_b2_config.so
%{_datadir}/apps/kwin/b2.desktop

%files -n kde-decoration-laptop
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin_laptop.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_laptop.so
%{_datadir}/apps/kwin/laptop.desktop

%files -n kde-decoration-modernsys
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin_modernsys.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_modernsys.so
%{_libdir}/kde3/kwin_modernsys_config.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_modernsys_config.so
%{_datadir}/apps/kwin/modernsystem.desktop

%files -n kde-decoration-quartz
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin_quartz.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_quartz.so
%{_libdir}/kde3/kwin_quartz_config.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_quartz_config.so
%{_datadir}/apps/kwin/quartz.desktop

%files -n kde-decoration-redmond
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin_redmond.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_redmond.so
%{_datadir}/apps/kwin/redmond.desktop

%files -n kde-decoration-web
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin_web.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_web.so
%{_datadir}/apps/kwin/web.desktop

%files -n kde-sdscreen-default
%defattr(644,root,root,755)
%{_datadir}/apps/ksmserver/*

%files common-filemanagement
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/filesharelist
%attr(0755,root,root) %{_bindir}/fileshareset
%{_libdir}/kde3/kcm_fileshare.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_fileshare.so
%{_libdir}/kde3/kio_thumbnail.la
%attr(0755,root,root) %{_libdir}/kde3/kio_thumbnail.so
%{_libdir}/kde3/fontthumbnail.la
%attr(0755,root,root) %{_libdir}/kde3/fontthumbnail.so
%{_libdir}/kde3/gsthumbnail.la
%attr(0755,root,root) %{_libdir}/kde3/gsthumbnail.so
%{_libdir}/kde3/htmlthumbnail.la
%attr(0755,root,root) %{_libdir}/kde3/htmlthumbnail.so
%{_libdir}/kde3/imagethumbnail.la
%attr(0755,root,root) %{_libdir}/kde3/imagethumbnail.so
%{_libdir}/kde3/libkonsolepart.la
%attr(0755,root,root) %{_libdir}/kde3/libkonsolepart.so
%{_libdir}/kde3/picturethumbnail.la
%attr(0755,root,root) %{_libdir}/kde3/picturethumbnail.so
%{_libdir}/kde3/textthumbnail.la
%attr(0755,root,root) %{_libdir}/kde3/textthumbnail.so
%{_datadir}/services/konsolepart.desktop
%{_datadir}/services/fontthumbnail.desktop
%{_datadir}/services/gsthumbnail.desktop
%{_datadir}/services/htmlthumbnail.desktop
%{_datadir}/services/imagethumbnail.desktop
%{_datadir}/services/textthumbnail.desktop
%{_datadir}/services/picturethumbnail.desktop
%{_datadir}/services/thumbnail.protocol
%{_datadir}/servicetypes/terminalemulator.desktop
%{_datadir}/servicetypes/thumbcreator.desktop
%{_applnkdir}/KDE-Settings/Network/fileshare.desktop
# konqueror needs it
%{_pixmapsdir}/*/*/apps/kate.png
#

%files common-konsole
%defattr(644,root,root,755)
%{_fontdir}/console*.gz
%{_datadir}/apps/konsole
%{_datadir}/mimelnk/application/x-konsole.desktop
%{_pixmapsdir}/[!l]*/*/apps/bell.png
%{_pixmapsdir}/*/*/apps/key_bindings.png

%files core -f core.lang
%defattr(644,root,root,755)
%lang(en) %dir %{_htmldir}/en/kcontrol
%lang(en) %{_htmldir}/en/kcontrol/common
%lang(en) %{_htmldir}/en/kcontrol/helpindex.html
%lang(en) %{_htmldir}/en/kcontrol/index.*
%lang(en) %{_htmldir}/en/kcontrol/screenshot.png
/etc/xdg/menus/kde-settings.menu
%attr(0755,root,root) %{_bindir}/drkonqi
%attr(0755,root,root) %{_bindir}/kcminit
%attr(0755,root,root) %{_bindir}/kcmshell
%attr(0755,root,root) %{_bindir}/kcontrol
%attr(0755,root,root) %{_bindir}/kdebugdialog
%attr(0755,root,root) %{_bindir}/kdesu
%attr(0755,root,root) %{_bindir}/kdesud
%attr(0755,root,root) %{_bindir}/khc_indexbuilder
%attr(0755,root,root) %{_bindir}/khelpcenter
%attr(0755,root,root) %{_bindir}/kprinter
%{_libdir}/kcminit.la
%attr(0755,root,root) %{_libdir}/kcminit.so
%{_libdir}/kcmshell.la
%attr(0755,root,root) %{_libdir}/kcmshell.so
%{_libdir}/kcontrol.la
%attr(0755,root,root) %{_libdir}/kcontrol.so
%{_libdir}/kprinter.la
%attr(0755,root,root) %{_libdir}/kprinter.so
%{_libdir}/kde3/kcm_colors.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_colors.so
%{_libdir}/kde3/kcm_fonts.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_fonts.so
%{_libdir}/kde3/kcm_kded.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kded.so
%{_libdir}/kde3/kcm_style.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_style.so
%{_libdir}/kde3/kcm_locale.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_locale.so
%{_libdir}/kde3/kcm_printmgr.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_printmgr.so
%{_libdir}/kde3/khelpcenter.la
%attr(0755,root,root) %{_libdir}/kde3/khelpcenter.so
%{_libdir}/kde3/kio_info.la
%attr(0755,root,root) %{_libdir}/kde3/kio_info.so
%{_libdir}/kde3/kio_man.la
%attr(0755,root,root) %{_libdir}/kde3/kio_man.so
%{_libdir}/kde3/libkdeprint_part.la
%attr(0755,root,root) %{_libdir}/kde3/libkdeprint_part.so
%{_libdir}/kde3/libkmanpart.la
%attr(0755,root,root) %{_libdir}/kde3/libkmanpart.so
%{_datadir}/apps/drkonqi
%{_datadir}/apps/kcontrol
%{_datadir}/apps/kdeprint/*
%{_datadir}/apps/kdeprint_part
%{_datadir}/apps/khelpcenter
%dir %{_datadir}/apps/kdisplay
%{_datadir}/apps/kdisplay/color-schemes
%dir %{_datadir}/apps/kio_info
%attr(0755,root,root) %{_datadir}/apps/kio_info/kde-info2html
%{_datadir}/apps/kio_info/kde-info2html.conf
%{_datadir}/locale/en_US/*
%{_datadir}/locale/l10n
%{_datadir}/mimelnk/print
%{_datadir}/services/info.protocol
%{_datadir}/services/khelpcenter.desktop
%{_datadir}/services/man.protocol
%{_vfinfodir}/kde-settings*.directory
%dir %{_applnkdir}/.hidden
%dir %{_applnkdir}/KDE-Settings
%dir %{_applnkdir}/KDE-Settings/Accessibility
%dir %{_applnkdir}/KDE-Settings/Components
%dir %{_applnkdir}/KDE-Settings/Desktop
%dir %{_applnkdir}/KDE-Settings/LookNFeel
%dir %{_applnkdir}/KDE-Settings/Network
%dir %{_applnkdir}/KDE-Settings/Network/WebBrowsing
%dir %{_applnkdir}/KDE-Settings/Peripherals
%dir %{_applnkdir}/KDE-Settings/PowerControl
%dir %{_applnkdir}/KDE-Settings/Security
%dir %{_applnkdir}/KDE-Settings/Sound
%dir %{_applnkdir}/KDE-Settings/System
# hidden
%{_applnkdir}/KControl.desktop
#
%{_applnkdir}/KDE-Settings/Accessibility/language.desktop
%{_applnkdir}/KDE-Settings/Components/kcmkded.desktop
%{_applnkdir}/KDE-Settings/LookNFeel/colors.desktop
%{_applnkdir}/KDE-Settings/LookNFeel/fonts.desktop
%{_applnkdir}/KDE-Settings/LookNFeel/style.desktop
%{_applnkdir}/KDE-Settings/Peripherals/printers.desktop
%{_desktopdir}/Help.desktop
%{_desktopdir}/KControl.desktop
%{_pixmapsdir}/*/*/apps/colors.png
%{_pixmapsdir}/*/*/apps/energy.png
%{_pixmapsdir}/*/*/apps/fonts.png
%{_pixmapsdir}/*/*/apps/help_index.png
%{_pixmapsdir}/*/*/apps/input_devices_settings.png
%{_pixmapsdir}/*/*/apps/kcmdrkonqi.png
%{_pixmapsdir}/*/*/apps/khelpcenter.png
%{_pixmapsdir}/*/*/apps/kcmsystem.png
%{_pixmapsdir}/*/*/apps/kcontrol.png
%{_pixmapsdir}/*/*/apps/konqueror.png
%{_pixmapsdir}/*/*/apps/locale.png
%{_pixmapsdir}/*/*/apps/looknfeel.png
%{_pixmapsdir}/*/*/apps/multimedia.png
%{_pixmapsdir}/*/*/apps/personal.png
%{_pixmapsdir}/*/*/apps/printmgr.png
%{_pixmapsdir}/*/*/apps/style.png
%{_pixmapsdir}/*/*/devices/print_printer.png
%{_pixmapsdir}/*/*/filesystems/folder_print2.png
# infocenter & konqueror need it:
%{_pixmapsdir}/*/*/apps/samba.png
%{_pixmapsdir}/*/*/apps/usb.png
#

%files infocenter -f kinfocenter.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kinfocenter
%{_libdir}/kde3/kcm_info.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_info.so
%{_libdir}/kde3/kcm_ioslaveinfo.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_ioslaveinfo.so
%{_libdir}/kde3/kcm_nic.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_nic.so
%{_libdir}/kde3/kcm_samba.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_samba.so
%{_libdir}/kde3/kcm_usb.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_usb.so
%{_datadir}/apps/kcmusb
%{_datadir}/apps/kinfocenter
%{_vfinfodir}/kde-information.directory
%dir %{_applnkdir}/KDE-Settings/Information
%{_applnkdir}/KDE-Settings/Information/devices.desktop
%{_applnkdir}/KDE-Settings/Information/dma.desktop
%{_applnkdir}/KDE-Settings/Information/interrupts.desktop
%{_applnkdir}/KDE-Settings/Information/ioports.desktop
%{_applnkdir}/KDE-Settings/Information/kcmusb.desktop
%{_applnkdir}/KDE-Settings/Information/ioslaveinfo.desktop
%{_applnkdir}/KDE-Settings/Information/memory.desktop
%{_applnkdir}/KDE-Settings/Information/nic.desktop
%{_applnkdir}/KDE-Settings/Information/partitions.desktop
%{_applnkdir}/KDE-Settings/Information/pci.desktop
%{_applnkdir}/KDE-Settings/Information/processor.desktop
%{_applnkdir}/KDE-Settings/Information/scsi.desktop
%{_applnkdir}/KDE-Settings/Information/smbstatus.desktop
%{_applnkdir}/KDE-Settings/Information/sound.desktop
%{_applnkdir}/KDE-Settings/Information/xserver.desktop
%{_desktopdir}/kinfocenter.desktop
%{_pixmapsdir}/*/*/apps/hwinfo.png
%{_pixmapsdir}/*/*/apps/kcmdevices.png
%{_pixmapsdir}/*/*/apps/kcmmemory.png
%{_pixmapsdir}/*/*/apps/kcmpartitions.png
%{_pixmapsdir}/*/*/apps/kcmpci.png
%{_pixmapsdir}/*/*/apps/kcmprocessor.png
%{_pixmapsdir}/*/*/apps/kcmscsi.png
%{_pixmapsdir}/*/*/apps/kcmsound.png
%{_pixmapsdir}/*/*/apps/kcmx.png

%files kappfinder
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kappfinder
%{_datadir}/apps/kappfinder
# hidden
%{_applnkdir}/System/kappfinder.desktop
#
%{_desktopdir}/kappfinder.desktop
%{_pixmapsdir}/*/*/apps/kappfinder.png

%files kate -f kate.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kate
%{_libdir}/kate.la
%attr(0755,root,root) %{_libdir}/kate.so
%{_libdir}/kde3/katedefaultprojectplugin.la
%attr(0755,root,root) %{_libdir}/kde3/katedefaultprojectplugin.so
%{_datadir}/apps/kate
%{_datadir}/services/katedefaultproject.desktop
%{_datadir}/servicetypes/kateinitplugin.desktop
%{_datadir}/servicetypes/kateplugin.desktop
%{_datadir}/servicetypes/kateprojectplugin.desktop
%{_desktopdir}/kate.desktop

%files kdeprintfax
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kdeprintfax
%dir %{_datadir}/apps/kdeprintfax
%attr(0755,root,root) %{_datadir}/apps/kdeprintfax/anytops
%{_datadir}/apps/kdeprintfax/[!a]*
%{_desktopdir}/kdeprintfax.desktop
%{_pixmapsdir}/*/*/apps/kdeprintfax.png

%files kdialog
%defattr(644,root,root,755)
%doc kdialog/{README,test}
%attr(0755,root,root) %{_bindir}/kdialog

%files kfind -f kfind.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kfind
%{_applnkdir}/Kfind.desktop
%{_pixmapsdir}/*/*/apps/kfind.png

%files kicker -f kicker.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kicker
%{_libdir}/kicker.la
%attr(0755,root,root) %{_libdir}/kicker.so
%{_libdir}/libkickermain.la
%attr(0755,root,root) %{_libdir}/libkickermain.so.*.*.*
%{_libdir}/libtaskbar.la
%attr(0755,root,root) %{_libdir}/libtaskbar.so.*.*.*
%{_libdir}/libtaskmanager.la
%attr(0755,root,root) %{_libdir}/libtaskmanager.so.*.*.*
%{_libdir}/kde3/childpanel_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/childpanel_panelextension.so
%{_libdir}/kde3/clock_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/clock_panelapplet.so
%{_libdir}/kde3/dockbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/dockbar_panelextension.so
%{_libdir}/kde3/kasbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/kasbar_panelextension.so
%{_libdir}/kde3/kcm_clock.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_clock.so
%{_libdir}/kde3/kcm_kicker.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kicker.so
%{_libdir}/kde3/kcm_taskbar.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_taskbar.so
%{_libdir}/kde3/kickermenu_kdeprint.la
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_kdeprint.so
%{_libdir}/kde3/kickermenu_konsole.la
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_konsole.so
%{_libdir}/kde3/kickermenu_prefmenu.la
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_prefmenu.so
%{_libdir}/kde3/kickermenu_recentdocs.la
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_recentdocs.so
%{_libdir}/kde3/launcher_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/launcher_panelapplet.so
%{_libdir}/kde3/lockout_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/lockout_panelapplet.so
%{_libdir}/kde3/menu_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/menu_panelapplet.so
%{_libdir}/kde3/minipager_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/minipager_panelapplet.so
%{_libdir}/kde3/naughty_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/naughty_panelapplet.so
%{_libdir}/kde3/run_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/run_panelapplet.so
%{_libdir}/kde3/systemtray_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/systemtray_panelapplet.so
%{_libdir}/kde3/taskbar_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelapplet.so
%{_libdir}/kde3/taskbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelextension.so
%{_datadir}/apps/kicker
%{_datadir}/apps/naughtyapplet
%{_datadir}/autostart/panel.desktop
%{_applnkdir}/.hidden/kicker_config.desktop
%{_applnkdir}/.hidden/kicker_config_appearance.desktop
%{_applnkdir}/KDE-Settings/Desktop/kcmtaskbar.desktop
%{_applnkdir}/KDE-Settings/Desktop/panel.desktop
# hidden
%{_applnkdir}/KDE-Settings/LookNFeel/kcmtaskbar.desktop
%{_applnkdir}/KDE-Settings/LookNFeel/panel.desktop
#
%{_applnkdir}/KDE-Settings/LookNFeel/panel_appearance.desktop
%{_applnkdir}/KDE-Settings/System/clock.desktop
#%{_desktopdir}/kcmkicker.desktop
%{_pixmapsdir}/*/*/apps/clock.png
%{_pixmapsdir}/*/*/apps/date.png
%{_pixmapsdir}/*/*/apps/go.png
%{_pixmapsdir}/*/*/apps/kcmkicker.png
%{_pixmapsdir}/*/*/apps/kicker.png
%{_pixmapsdir}/*/*/apps/package*.png
%{_pixmapsdir}/*/*/apps/panel.png
%{_pixmapsdir}/*/*/apps/panel_settings.png

%files kjobviewer
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kjobviewer
%{_libdir}/kjobviewer.la
%attr(0755,root,root) %{_libdir}/kjobviewer.so
%{_datadir}/apps/kjobviewer
%{_desktopdir}/kjobviewer.desktop
%{_pixmapsdir}/*/*/apps/kjobviewer.png

%files klipper -f klipper.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/klipper
%{_libdir}/klipper.la
%attr(0755,root,root) %{_libdir}/klipper.so
%{_libdir}/kde3/klipper_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/klipper_panelapplet.so
%{_datadir}/autostart/klipper.desktop
%{_datadir}/config/klipperrc
%{_desktopdir}/klipper.desktop
%{_pixmapsdir}/*/*/apps/klipper.png

%files kmenuedit -f kmenuedit.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kmenuedit
%{_libdir}/kmenuedit.la
%attr(0755,root,root) %{_libdir}/kmenuedit.so
%{_datadir}/apps/kmenuedit
%{_applnkdir}/System/kmenuedit.desktop
%{_desktopdir}/kmenuedit.desktop
%{_pixmapsdir}/*/*/apps/kmenu.png
%{_pixmapsdir}/*/*/apps/kmenuedit.png

%files konsole -f konsole.lang
%defattr(644,root,root,755)
%doc konsole/README*
%attr(0755,root,root) %{_bindir}/konsole
%{_libdir}/konsole.la
%attr(0755,root,root) %{_libdir}/konsole.so
%{_libdir}/kde3/kcm_konsole.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_konsole.so
%{_datadir}/config/konsolerc
%{_datadir}/services/konsole-script.desktop
%{_applnkdir}/.hidden/kcmkonsole.desktop
%{_desktopdir}/konsole*.desktop
%{_pixmapsdir}/*/*/apps/konsole.png

%files kpager -f kpager.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kpager
# hidden
%{_applnkdir}/Utilities/kpager.desktop
#
%{_desktopdir}/kpager.desktop
%{_pixmapsdir}/*/*/apps/kpager.png

%files ksysguard -f ksysguard.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) /etc/X11/ksysguarddrc
%attr(0755,root,root) %{_bindir}/kpm
%attr(0755,root,root) %{_bindir}/ksysguard
%attr(0755,root,root) %{_bindir}/ksysguardd
%{_libdir}/libksgrd.la
%attr(0755,root,root) %{_libdir}/libksgrd.so.*.*.*
%{_libdir}/kde3/sysguard_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/sysguard_panelapplet.so
%{_datadir}/apps/ksysguard
%{_datadir}/mimelnk/application/x-ksysguard.desktop
%{_desktopdir}/ksysguard.desktop
%{_pixmapsdir}/*/*/apps/ksysguard.png

%files ksystraycmd
%defattr(644,root,root,755)
%doc ksystraycmd/README
%attr(0755,root,root) %{_bindir}/ksystraycmd

%files kwmtheme -f kthememgr.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kwmtheme
%{_libdir}/kde3/kcm_themes.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_themes.so
%{_libdir}/kde3/kwin_kwmtheme.la
%attr(0755,root,root) %{_libdir}/kde3/kwin_kwmtheme.so
%{_datadir}/apps/kthememgr
%{_datadir}/mimelnk/application/x-ktheme.desktop
%{_applnkdir}/KDE-Settings/LookNFeel/kthememgr.desktop
%{_pixmapsdir}/*/*/apps/kthememgr.png

%files kwrite -f kwrite.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kwrite
%attr(0755,root,root) %{_bindir}/kwriteconfig
%{_libdir}/kwrite.la
%attr(0755,root,root) %{_libdir}/kwrite.so
%{_datadir}/apps/kwrite
%{_desktopdir}/kwrite.desktop
%{_pixmapsdir}/*/*/apps/kwrite.png

%files kwrited
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kwrited
%{_libdir}/kwrited.la
%attr(0755,root,root) %{_libdir}/kwrited.so
%{_datadir}/autostart/kwrited.desktop
%{_datadir}/config/kwritedrc
%{_datadir}/services/kwrited.desktop

%files libkate
%defattr(644,root,root,755)
%{_libdir}/libkateinterfaces.la
%attr(0755,root,root) %{_libdir}/libkateinterfaces.so.*.*.*
%{_libdir}/libkateutils.la
%attr(0755,root,root) %{_libdir}/libkateutils.so.*.*.*

%files libkmultitabbar
%defattr(644,root,root,755)
%{_libdir}/libkmultitabbar.la
%attr(0755,root,root) %{_libdir}/libkmultitabbar.so.*.*.*

%files libkonq
%defattr(644,root,root,755)
%{_libdir}/libkonq.la
%attr(0755,root,root) %{_libdir}/libkonq.so.*.*.*
%{_libdir}/kde3/konq_sound.la
%attr(0755,root,root) %{_libdir}/kde3/konq_sound.so

%files mailnews
%defattr(644,root,root,755)
%{_libdir}/kde3/kio_imap4.la
%attr(0755,root,root) %{_libdir}/kde3/kio_imap4.so
%{_libdir}/kde3/kio_nntp.la
%attr(0755,root,root) %{_libdir}/kde3/kio_nntp.so
%{_libdir}/kde3/kio_pop3.la
%attr(0755,root,root) %{_libdir}/kde3/kio_pop3.so
%{_libdir}/kde3/kio_smtp.la
%attr(0755,root,root) %{_libdir}/kde3/kio_smtp.so
%{_datadir}/services/imap4.protocol
%{_datadir}/services/imaps.protocol
%{_datadir}/services/nntp.protocol
%{_datadir}/services/pop3.protocol
%{_datadir}/services/pop3s.protocol
%{_datadir}/services/smtp.protocol
%{_datadir}/services/smtps.protocol

%files screensavers -f screensaver.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/*.kss
%{_libdir}/kde3/kcm_screensaver.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_screensaver.so
%{_datadir}/apps/kscreensaver
%{_applnkdir}/KDE-Settings/LookNFeel/screensaver.desktop
%{_pixmapsdir}/*/*/apps/kscreensaver.png

%files -n kdm -f kdm.lang
%defattr(644,root,root,755)
%doc README.pam kdm/{ChangeLog,README,TODO}
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/kdm
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.kdm
%attr(0754,root,root) /etc/rc.d/init.d/kdm
%dir %{_sysconfdir}/kdm
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/kdmrc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/backgroundrc
%attr(0755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xreset
%attr(0755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xsession
%attr(0755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xsetup
%attr(0755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xstartup
%attr(0755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xwilling
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xaccess
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xservers
%{_sysconfdir}/kdm/pics
%attr(0755,root,root) %{_bindir}/kdm*
%attr(0755,root,root) %{_bindir}/krootimage
%{_libdir}/kde3/kcm_kdm.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kdm.so
%{_applnkdir}/KDE-Settings/System/kdm.desktop
%{_pixmapsdir}/*/*/apps/kdmconfig.png

%files -n konqueror -f konqueror.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/appletproxy
%attr(0755,root,root) %{_bindir}/extensionproxy
%attr(0755,root,root) %{_bindir}/keditbookmarks
%attr(0755,root,root) %{_bindir}/keditfiletype
%attr(0755,root,root) %{_bindir}/kfmclient
%attr(0755,root,root) %{_bindir}/kfmexec
%attr(0755,root,root) %{_bindir}/kio_devices_mounthelper
%attr(0755,root,root) %{_bindir}/klocaldomainurifilterhelper
%attr(0755,root,root) %{_bindir}/konqueror
%attr(0755,root,root) %{_bindir}/nspluginscan
%attr(0755,root,root) %{_bindir}/nspluginviewer
%{_libdir}/appletproxy.la
%attr(0755,root,root) %{_libdir}/appletproxy.so
%{_libdir}/extensionproxy.la
%attr(0755,root,root) %{_libdir}/extensionproxy.so
%{_libdir}/keditbookmarks.la
%attr(0755,root,root) %{_libdir}/keditbookmarks.so
%{_libdir}/kfmclient.la
%attr(0755,root,root) %{_libdir}/kfmclient.so
%{_libdir}/konqueror.la
%attr(0755,root,root) %{_libdir}/konqueror.so
%{_libdir}/libkonq_sidebar_tree.la
%attr(0755,root,root) %{_libdir}/libkonq_sidebar_tree.so
%{_libdir}/libkonqsidebarplugin.la
%attr(0755,root,root) %{_libdir}/libkonqsidebarplugin.so.*.*.*
%{_libdir}/libnsplugin.la
%attr(0755,root,root) %{_libdir}/libnsplugin.so.*.*.*
%{_libdir}/kde3/kcm_cgi.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_cgi.so
%{_libdir}/kde3/kcm_crypto.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_crypto.so
%{_libdir}/kde3/kcm_css.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_css.so
%{_libdir}/kde3/kcm_filetypes.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_filetypes.so
%{_libdir}/kde3/kcm_history.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_history.so
%{_libdir}/kde3/kcm_icons.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_icons.so
%{_libdir}/kde3/kcm_kio.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kio.so
%{_libdir}/kde3/kcm_konq.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_konq.so
%{_libdir}/kde3/kcm_konqhtml.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_konqhtml.so
%{_libdir}/kde3/kcm_kurifilt.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kurifilt.so
%{_libdir}/kde3/kcm_performance.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_performance.so
%{_libdir}/kde3/kded_favicons.la
%attr(0755,root,root) %{_libdir}/kde3/kded_favicons.so
%{_libdir}/kde3/kded_konqy_preloader.la
%attr(0755,root,root) %{_libdir}/kde3/kded_konqy_preloader.so
%{_libdir}/kde3/kded_mountwatcher.la
%attr(0755,root,root) %{_libdir}/kde3/kded_mountwatcher.so
%{_libdir}/kde3/kfile_font.la
%attr(0755,root,root) %{_libdir}/kde3/kfile_font.so
%{_libdir}/kde3/kio_about.la
%attr(0755,root,root) %{_libdir}/kde3/kio_about.so
%{_libdir}/kde3/kio_cgi.la
%attr(0755,root,root) %{_libdir}/kde3/kio_cgi.so
%{_libdir}/kde3/kio_devices.la
%attr(0755,root,root) %{_libdir}/kde3/kio_devices.so
%{_libdir}/kde3/kio_filter.la
%attr(0755,root,root) %{_libdir}/kde3/kio_filter.so
%{_libdir}/kde3/kio_finger.la
%attr(0755,root,root) %{_libdir}/kde3/kio_finger.so
%{_libdir}/kde3/kio_fish.la
%attr(0755,root,root) %{_libdir}/kde3/kio_fish.so
%{_libdir}/kde3/kio_floppy.la
%attr(0755,root,root) %{_libdir}/kde3/kio_floppy.so
%{_libdir}/kde3/kio_ldap.la
%attr(0755,root,root) %{_libdir}/kde3/kio_ldap.so
%{_libdir}/kde3/kio_mac.la
%attr(0755,root,root) %{_libdir}/kde3/kio_mac.so
%{_libdir}/kde3/kio_nfs.la
%attr(0755,root,root) %{_libdir}/kde3/kio_nfs.so
%{_libdir}/kde3/kio_print.la
%attr(0755,root,root) %{_libdir}/kde3/kio_print.so
%{_libdir}/kde3/kio_sftp.la
%attr(0755,root,root) %{_libdir}/kde3/kio_sftp.so
%{_libdir}/kde3/kio_smb.la
%attr(0755,root,root) %{_libdir}/kde3/kio_smb.so
%{_libdir}/kde3/kio_tar.la
%attr(0755,root,root) %{_libdir}/kde3/kio_tar.so
%{_libdir}/kde3/kio_zip.la
%attr(0755,root,root) %{_libdir}/kde3/kio_zip.so
%{_libdir}/kde3/konq_aboutpage.la
%attr(0755,root,root) %{_libdir}/kde3/konq_aboutpage.so
%{_libdir}/kde3/konq_iconview.la
%attr(0755,root,root) %{_libdir}/kde3/konq_iconview.so
%{_libdir}/kde3/konq_listview.la
%attr(0755,root,root) %{_libdir}/kde3/konq_listview.so
%{_libdir}/kde3/konq_shellcmdplugin.la
%attr(0755,root,root) %{_libdir}/kde3/konq_shellcmdplugin.so
%{_libdir}/kde3/konq_sidebar.la
%attr(0755,root,root) %{_libdir}/kde3/konq_sidebar.so
%{_libdir}/kde3/konq_sidebartree_bookmarks.la
%attr(0755,root,root) %{_libdir}/kde3/konq_sidebartree_bookmarks.so
%{_libdir}/kde3/konq_sidebartree_dirtree.la
%attr(0755,root,root) %{_libdir}/kde3/konq_sidebartree_dirtree.so
%{_libdir}/kde3/konq_sidebartree_history.la
%attr(0755,root,root) %{_libdir}/kde3/konq_sidebartree_history.so
%{_libdir}/kde3/konqsidebar_tree.la
%attr(0755,root,root) %{_libdir}/kde3/konqsidebar_tree.so
%{_libdir}/kde3/konqsidebar_web.la
%attr(0755,root,root) %{_libdir}/kde3/konqsidebar_web.so
%{_libdir}/kde3/libkfindpart.la
%attr(0755,root,root) %{_libdir}/kde3/libkfindpart.so
%{_libdir}/kde3/libkshorturifilter.la
%attr(0755,root,root) %{_libdir}/kde3/libkshorturifilter.so
%{_libdir}/kde3/libkuriikwsfilter.la
%attr(0755,root,root) %{_libdir}/kde3/libkuriikwsfilter.so
%{_libdir}/kde3/libkurisearchfilter.la
%attr(0755,root,root) %{_libdir}/kde3/libkurisearchfilter.so
%{_libdir}/kde3/liblocaldomainurifilter.la
%attr(0755,root,root) %{_libdir}/kde3/liblocaldomainurifilter.so
%attr(0755,root,root) %{_libdir}/kde3/plugins/konqueror
%{_datadir}/apps/kbookmark
%{_datadir}/apps/kcmcss
%{_datadir}/apps/keditbookmarks
%{_datadir}/apps/kfindpart
%{_datadir}/apps/kio_finger
%{_datadir}/apps/konqiconview
%{_datadir}/apps/konqlistview
%{_datadir}/apps/konqsidebartng
%{_datadir}/apps/konqueror
%{_datadir}/autostart/konqy_preload.desktop
%{_datadir}/config/konqsidebartng.rc
%{_datadir}/config/kshorturifilterrc
%{_datadir}/mimelnk/application/x-smb-workgroup.desktop
%{_datadir}/mimelnk/kdedevice
%{_datadir}/services/searchproviders
%{_datadir}/services/useragentstrings
%{_datadir}/services/about.protocol
%{_datadir}/services/bzip.protocol
%{_datadir}/services/bzip2.protocol
%{_datadir}/services/cgi.protocol
%{_datadir}/services/devices.protocol
%{_datadir}/services/finger.protocol
%{_datadir}/services/fish.protocol
%{_datadir}/services/floppy.protocol
%{_datadir}/services/gzip.protocol
%{_datadir}/services/kded/favicons.desktop
%{_datadir}/services/kded/konqy_preloader.desktop
%{_datadir}/services/kded/mountwatcher.desktop
%{_datadir}/services/kfile_font.desktop
%{_datadir}/services/kfindpart.desktop
%{_datadir}/services/kmanpart.desktop
%{_datadir}/services/konq_aboutpage.desktop
%{_datadir}/services/konq_detailedlistview.desktop
%{_datadir}/services/konq_iconview.desktop
%{_datadir}/services/konq_infolistview.desktop
%{_datadir}/services/konq_multicolumnview.desktop
%{_datadir}/services/konq_sidebartng.desktop
%{_datadir}/services/konq_textview.desktop
%{_datadir}/services/konq_treeview.desktop
%{_datadir}/services/konqueror_config.desktop
%{_datadir}/services/kshorturifilter.desktop
%{_datadir}/services/kuriikwsfilter.desktop
%{_datadir}/services/kurisearchfilter.desktop
%{_datadir}/services/ldap.protocol
%{_datadir}/services/localdomainurifilter.desktop
%{_datadir}/services/mac.protocol
%{_datadir}/services/nfs.protocol
%{_datadir}/services/print.protocol
%{_datadir}/services/sftp.protocol
%{_datadir}/services/smb.protocol
%{_datadir}/services/tar.protocol
%{_datadir}/services/zip.protocol
%{_datadir}/servicetypes/findpart.desktop
%{_datadir}/servicetypes/konqaboutpage.desktop
%{_datadir}/servicetypes/konqpopupmenuplugin.desktop
%{_datadir}/servicetypes/searchprovider.desktop
%{_datadir}/servicetypes/uasprovider.desktop
%{_applnkdir}/.hidden/fileappearance.desktop
%{_applnkdir}/.hidden/filebehavior.desktop
%{_applnkdir}/.hidden/filepreviews.desktop
%{_applnkdir}/.hidden/kcmkonq.desktop
%{_applnkdir}/.hidden/konqfilemgr.desktop
%{_applnkdir}/.hidden/konqhtml.desktop
%{_applnkdir}/.hidden/smb.desktop
%{_applnkdir}/KDE-Settings/Components/filebrowser.desktop
%{_applnkdir}/KDE-Settings/Components/filetypes.desktop
%{_applnkdir}/KDE-Settings/Components/kcmkonqyperformance.desktop
%{_applnkdir}/KDE-Settings/Components/kcmperformance.desktop
%{_applnkdir}/KDE-Settings/LookNFeel/icons.desktop
%{_applnkdir}/KDE-Settings/Network/WebBrowsing/cache.desktop
%{_applnkdir}/KDE-Settings/Network/WebBrowsing/cookies.desktop
%{_applnkdir}/KDE-Settings/Network/WebBrowsing/ebrowsing.desktop
%{_applnkdir}/KDE-Settings/Network/WebBrowsing/kcmcgi.desktop
%{_applnkdir}/KDE-Settings/Network/WebBrowsing/kcmcss.desktop
%{_applnkdir}/KDE-Settings/Network/WebBrowsing/kcmhistory.desktop
%{_applnkdir}/KDE-Settings/Network/WebBrowsing/khtml_behavior.desktop
%{_applnkdir}/KDE-Settings/Network/WebBrowsing/khtml_fonts.desktop
%{_applnkdir}/KDE-Settings/Network/WebBrowsing/khtml_java_js.desktop
%{_applnkdir}/KDE-Settings/Network/WebBrowsing/khtml_plugins.desktop
%{_applnkdir}/KDE-Settings/Network/WebBrowsing/useragent.desktop
%{_applnkdir}/KDE-Settings/Network/lanbrowser.desktop
%{_applnkdir}/KDE-Settings/Network/netpref.desktop
%{_applnkdir}/KDE-Settings/Network/proxy.desktop
%{_applnkdir}/KDE-Settings/Security/crypto.desktop
# hidden
%{_applnkdir}/KDE-Settings/WebBrowsing
%{_applnkdir}/System/konquerorsu.desktop
#
%{_applnkdir}/konqueror.desktop
%{_desktopdir}/kfmclient.desktop
%{_desktopdir}/kfmclient_dir.desktop
%{_desktopdir}/kfmclient_html.desktop
%{_desktopdir}/kfmclient_war.desktop
%{_desktopdir}/konqbrowser.desktop
%{_desktopdir}/konquerorsu.desktop
%{_pixmapsdir}/*/*/apps/agent.png
%{_pixmapsdir}/*/*/apps/cache.png
%{_pixmapsdir}/*/*/apps/cookie.png
%{_pixmapsdir}/*/*/apps/enhanced_browsing.png
%{_pixmapsdir}/*/*/apps/filetypes.png
%{_pixmapsdir}/*/*/apps/icons.png
%{_pixmapsdir}/*/*/apps/iconthemes.png
%{_pixmapsdir}/*/*/apps/keditbookmarks.png
%{_pixmapsdir}/*/*/apps/kfm_home.png
%{_pixmapsdir}/*/*/apps/kfm.png
%{_pixmapsdir}/*/*/apps/mac.png
%{_pixmapsdir}/*/*/apps/proxy.png
%{_pixmapsdir}/*/*/apps/stylesheet.png
