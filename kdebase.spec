#
# TODO:
# * KDM: ColorSheme=Default works properly with GUIStyle=KDE only
# * KDM: Replacing findwm with a better solution (it's in the way)
#
# Conditional build:
# _without_alsa 	- disable alsa
# _without_ldap         - without LDAP support
#

%define		_state		stable
%define		_ver		3.1.4

%define		_kdelibsminrel	0.1

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
Release:	0.30
Epoch:		8
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	e6859ad85b176e11ce997490786c124d
Source1:	%{name}-extra_icons.tar.bz2
# Source1-md5:	e251f29dcabe367ebeb96824ee1823ab
Source2:	%{name}-kdm.pam
Source3:	%{name}-kdm.init
Source4:	%{name}-kdm.Xsession
Source5:	%{name}-kdm.Xservers
Source6:	%{name}-kdm_pldlogo.png
Source7:	%{name}-kdm_pldwallpaper.png
Source8:	%{name}-ircpld.desktop
Source9:	%{name}-specs.desktop
Source10:	%{name}-kdesktop.pam
Source11:	%{name}-kde-settings.menu
Source12:	%{name}-imdb.desktop
# generated from kde-i18n-%{version}.tar.bz2:
Source13:	ftp://blysk.ds.pg.gda.pl/linux/kde-i18n-package/%{version}/kde-i18n-%{name}-%{version}.tar.bz2
# Source13-md5:	6810997339287b491f5b57abbf472baf
Patch0:		%{name}-fix-mem-leak-in-kfind.patch
#Patch1:		%{name}-fix-mouse.cpp.patch
Patch2:		%{name}-fontdir.patch
Patch3:		%{name}-kcm_background.patch
Patch4:		%{name}-kdm.daemon_output.patch
Patch5:		%{name}-kdm_utmpx.patch
Patch6:		%{name}-kdmconfig.patch
Patch7:		%{name}-kicker.patch
Patch8:		%{name}-konsole_all.patch
Patch9:		%{name}-nsplugins_dirs.patch
Patch10:	%{name}-startkde.patch
Patch11:	%{name}-kcm_fonts.patch
Patch12:	%{name}-gtkrc.patch
Patch13:	%{name}-krdb.patch
#Patch14:	%{name}-pldcredits.patch
# rh stuff
Patch15:	%{name}-kicker_nodesktop.patch
Patch16:	%{name}-xfsreload.patch
#
Patch17:	%{name}-kdm_kgreeter.patch
Patch18:	%{name}-screensavers.patch
Patch19:	%{name}-prefmenu.patch
Patch20:	%{name}-kdesktop_lock.patch
Patch21:	%{name}-libtool-sanitize.patch
%{?_without_alsa:BuildConflicts:	alsa-driver-devel}
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
#BuildRequires:	XFree86-xrender-devel
BuildRequires:	arts-devel >= 1.1
BuildRequires:	arts-kde-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	awk
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cups-devel
BuildRequires:	db3-devel
BuildRequires:	ed
BuildRequires:	findutils
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 8:%{version}
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libsmbclient-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5-2
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	motif-devel
%{!?_without_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel >= 0.9.6k
BuildRequires:	pam-devel
BuildRequires:	qt-devel >= 3.1
BuildRequires:	zlib-devel
BuildRequires:	fam-devel
BuildRequires:	libart_lgpl-devel
# TODO: sensors
#BuildRequires:	sensors-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	applnk >= 1.5.16
Requires:	kde-splash
Requires:	kde-sdscreen
Requires:	konqueror = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-fonts
Obsoletes:	%{name}-kcheckpass
Obsoletes:	%{name}-kdesktop_lock
Obsoletes:	%{name}-khelpcenter
Obsoletes:	%{name}-screensaver
Obsoletes:	%{name}-kioslave
Obsoletes:	%{name}-konqueror
Obsoletes:	%{name}-kwin
Obsoletes:	%{name}-kxmlrpc
Obsoletes:	%{name}-kdesktop
Obsoletes:	%{name}-wallpapers
Obsoletes:	kde-theme-keramik
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_fontdir	/usr/share/fonts/misc
%define		_htmldir	/usr/share/doc/kde/HTML
%define		_sysconfdir	/etc/X11

%define		no_install_post_chrpath		1

%description
KDE specific files. Used by core KDE applications. Package includes:
- KDE menu hierarchy,
- kappfinder - script installing some non-KDE apps in KDE menu.

%description -l ja
KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ÍÑ¤Î´ðËÜ¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¡£
°Ê²¼¤Î¤è¤¦¤Ê¥Ñ¥Ã¥±¡¼¥¸¤¬Æþ¤Ã¤Æ¤¤¤Þ¤¹¡£

%description -l pl
Pliki specyficzne dla ¶rodowiska KDE i wykorzystywane przez g³ówne
aplikacje KDE. Pakiet zawiera:
- Hierarchiê menu KDE,
- kappfinder - skrypt u³awiaj±cy uruchamianie niektórych programów
  spoza KDE.

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
kwin (×¦ËÏÎÎÙÊ ÍÅÎÅÄÖÅÒ), konqueror (ÆÁÊÌÏ×ÉÊ ÍÅÎÅÄÖÅÒ, web-ÂÒÁÕÚÅÒ,
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
#Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-kicker = %{epoch}:%{version}-%{release}
Requires:	%{name}-ksysguard-libs = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= 8:%{version}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase-static

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
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kde-decoration-b2
KDE Window Decoration - B2.

%description -n kde-decoration-b2 -l pl
Dekoracja okna dla KDE - B2.

%package -n kde-decoration-laptop
Summary:	KDE Window Decoration - Laptop
Summary(pl):	Dekoracja okna dla KDE - Laptop
Group:		X11/Amusements
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kde-decoration-laptop
KDE Window Decoration - Laptop.

%description -n kde-decoration-laptop -l pl
Dekoracja okna dla KDE - Laptop.

%package -n kde-decoration-modernsys
Summary:	KDE Window Decoration - ModernSys
Summary(pl):	Dekoracja okna dla KDE - ModernSys
Group:		X11/Amusements
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kde-decoration-modernsys
KDE Window Decoration - ModernSys.

%description -n kde-decoration-modernsys -l pl
Dekoracja okna dla KDE - ModernSys.

%package -n kde-decoration-quartz
Summary:	KDE Window Decoration - Quartz
Summary(pl):	Dekoracja okna dla KDE - Quartz
Group:		X11/Amusements
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kde-decoration-quartz
KDE Window Decoration - Quartz.

%description -n kde-decoration-quartz -l pl
Dekoracja okna dla KDE - Quartz.

%package -n kde-decoration-redmond
Summary:	KDE Window Decoration - Redmond
Summary(pl):	Dekoracja okna dla KDE - Redmond
Group:		X11/Amusements
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kde-decoration-redmond
KDE Window Decoration - Redmond.

%description -n kde-decoration-redmond -l pl
Dekoracja okna dla KDE - Redmond.

%package -n kde-decoration-kde1
Summary:	KDE Window Decoration - KDE 1
Summary(pl):	Dekoracja okna dla KDE - KDE 1
Group:		X11/Amusements
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kde-decoration-kde1
KDE Window Decoration - KDE 1.

%description -n kde-decoration-kde1 -l pl
Dekoracja okna dla KDE - KDE 1.

%package -n kde-decoration-kstep
Summary:	KDE Window Decoration - Kstep
Summary(pl):	Dekoracja okna dla KDE - Kstep
Group:		X11/Amusements
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kde-decoration-kstep
KDE Window Decoration - Kstep.

%description -n kde-decoration-kstep -l pl
Dekoracja okna dla KDE - Kstep.

%package -n kde-decoration-icewm
Summary:	Extensions for KDE IceWM decoration
Summary(pl):	Rozszerzenie dekoracji okna "IceWM" dla KDE
Group:		X11/Amusements
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kde-decoration-icewm
Extensions for KDE "IceWM" decoration.

%description -n kde-decoration-icewm -l pl
Rozszerzenie dekoracji okna IceWM dla KDE.

%package -n kde-decoration-riscos
Summary:	KDE Window Decoration - Risc OS
Summary(pl):	Dekoracja okna dla KDE - Risc OS
Requires:	%{name} = %{epoch}:%{version}-%{release}
Group:		X11/Amusements

%description -n kde-decoration-riscos
KDE Window Decoration - Risc OS.

%description -n kde-decoration-riscos -l pl
Dekoracja okna dla KDE - Risc OS.

%package -n kde-decoration-system
Summary:	KDE Window Decoration - System
Summary(pl):	Dekoracja okna dla KDE - System
Group:		X11/Amusements
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kde-decoration-system
KDE Window Decoration - System.

%description -n kde-decoration-system -l pl
Dekoracja okna dla KDE - System.

%package -n kde-decoration-web
Summary:	KDE Window Decoration - Web
Summary(pl):	Dekoracja okna dla KDE - Web
Group:		X11/Amusements
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kde-decoration-web
KDE Window Decoration - Web.

%description -n kde-decoration-web -l pl
Dekoracja okna dla KDE - Web.

%package -n kde-sdscreen-default
Summary:	KDE "Logout" picture
Summary(pl):	Obrazek okna "Wyloguj" KDE
Group:		X11/Amusements
Provides:	kde-sdscreen
Requires:	%{name} >= 3.0.3
Obsoletes:	kde-sdscreen-KDEGirl
Obsoletes:	kde-sdscreen-keramik

%description -n kde-sdscreen-default
Default KDE "Logout" picture.

%description -n kde-sdscreen-default -l pl
Standardowy obrazek okna "Wyloguj" KDE.

%package -n kde-splash-default
Summary:	KDE splash screen
Summary(pl):	Obrazek startowy KDE
Group:		X11/Amusements
Provides:	kde-splash
Requires:	%{name} >= 3.0.3
Obsoletes:	kde-splash-KDEGirl
Obsoletes:	kde-splash-keramik

%description -n kde-splash-default
Default splash screen for KDE.

%description -n kde-splash-default -l pl
Standardowy obrazek startowy KDE.

%package common-filemanagement
Summary:	Common Files for kate and konqueror
Summary(pl):	Pliki wspólne dla kate i konquerora
Group:		X11/Libraries
Requires:	%{name}-common-konsole = %{epoch}:%{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4

%description common-filemanagement
Common files needed by kate and konqueror.

%description common-filemanagement -l pl
Pliki wspólne, u¿ywane przez kate i konquerora.

%package common-konsole
Summary:	Common files for konsole and konsolepart
Summary(pl):	Pliki wspólne dla konsole i konsolepart
Group:		X11/Applications
Requires(post,postun):	/usr/X11R6/bin/mkfontdir
Requires:	%{_fontdir}
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
Requires:	kdelibs >= 8:%{version}-%{_kdelibsminrel}
Obsoletes:	%{name} < 3.1.2
Obsoletes:	%{name}-kcontrol
Obsoletes:	%{name}-khelpcenter
Obsoletes:	%{name}-helpcenter

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
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description infocenter
KDE Info Center.

%description infocenter -l pl
Centrum informacji o systemie dla KDE.

%package kappfinder
Summary:	Menu Updating Tool
Summary(pl):	Narzêdzie do aktualizacji menu
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}
Obsoletes:	%{name} =< 3.1.1a-3

%description kappfinder
Menu Updating Tool.

%description kappfinder -l pl
Narzêdzie do aktualizacji menu.

%package kate
Summary:	KDE Advanced Text Editor
Summary(pl):	Zaawansowany edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-common-filemanagement = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	kate

%description kate
KDE advanced text editor.

%description kate -l pl
Zaawansowany edytor tekstu dla KDE.

%package kdeprintfax
Summary:	KDE Fax Tool
Summary(pl):	Narzêdzie do faksowania dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	efax
Requires:	enscript
Obsoletes:	%{name} <= 3.1-9

%description kdeprintfax
KDE Fax Tool.

%description kdeprintfax -l pl
Narzêdzie do faksowania dla KDE.

%package kdialog
Summary:	A KDE version of dialog
Summary(pl):	Wersja KDE dialogu
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}-%{_kdelibsminrel}
Obsoletes:	%{name} < 3.1.2

%description kdialog
Allows to display menu boxes from shell scripts.

%description kdialog -l pl
Umo¿liwia wy¶wietlanie komunikatów z poziomu skryptów
pow³oki.

%package kfind
Summary:	KDE Find Tool
Summary(pl):	Narzêdzie do wyszukiwania plików dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	kdelibs >= 8:%{version}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	kfind

%description kfind
KDE Find Tool.

%description kfind -l pl
Narzêdzie do wyszukiwania plików dla KDE.

%package kicker
Summary:	KDE Panel - kicker
Summary(pl):	Panel KDE - kicker
Group:		X11/Applications
Requires:	%{name}-kmenuedit = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkonq = %{epoch}:%{version}-%{release}

%description kicker
KDE Panel - kicker.

%description kicker -l pl
Panel KDE - kicker.

%package kjobviewer
Summary:	Print Job Viewer
Summary(pl):	Podgl±d zadañ drukowania
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description kjobviewer
KDE Print Job Viewer.

%description kjobviewer -l pl
Podgl±d zadañ drukowania dla KDE.

%package klipper
Summary:	Clipboard Tool
Summary(pl):	Narzêdzie schowka
Group:		X11/Applications
Requires:	%{name}-kicker = %{epoch}:%{version}-%{release}

%description klipper
KDE Clipboard Tool.

%description klipper -l pl
Narzêdzie schowka dla KDE.

%package kmenuedit
Summary:	Menu Editor
Summary(pl):	Edytor menu
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description kmenuedit
KDE Menu Editor.

%description kmenuedit -l pl
Edytor menu KDE.

%package konsole
Summary:	KDE Terminal Emulator
Summary(pl):	Emulator terminala dla KDE
Group:		X11/Applications
Requires:	%{name}-common-konsole = %{epoch}:%{version}-%{release}
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	konsole

%description konsole
KDE Terminal Emulator.

%description konsole -l pl
Emulator terminala dla KDE.

%package kpager
Summary:	Desktop Pager
Summary(pl):	Prze³±cznik biurek
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}
Obsoletes:	%{name} =< 3.1.1a-3

%description kpager
KDE Desktop Pager.

%description kpager -l pl
Prze³±cznik biurek dla KDE.

%package ksysguard-libs
Summary:	ksysguard shared libraries
Summary(pl):	Biblioteki wspó³dzielone ksysguard
Group:		X11/Applications
#Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description ksysguard-libs
Shared libraries for KDE System Guard.

%description ksysguard-libs -l pl
Biblioteki wspó³dzielone stra¿nika systemu dla KDE ksysguard.

%package ksysguard
Summary:	System Guard
Summary(pl):	Stra¿nik systemu
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-ksysguard-libs = %{epoch}:%{version}-%{release}

%description ksysguard
KDE System Guard.

%description ksysguard -l pl
Stra¿nik systemu dla KDE.

%package ksystraycmd
Summary:	A tool that allows running applications in taskbar
Summary(pl):	Narzêdzie do odpalania aplikacji w pasku zadañ
Group:		X11/Applications
Requires:	%{name}-kicker = %{epoch}:%{version}-%{release}

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
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description kwmtheme
KDE Desktop Theme Manager. This package contains also a few desktop
themes.

%description kwmtheme -l pl
Zarz±dca motywów biurka KDE. Ten pakiet zawiera równie¿ kilka motywów.

%package kwrite
Summary:	KDE Text Editor
Summary(pl):	Edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	kwrite

%description kwrite
KDE text editor with syntax highlighting.

%description kwrite -l pl
Edytor tekstu z pod¶wietlaniem sk³adni dla KDE.

%package kwrited
Summary:	KDE Write Daemon
Summary(pl):	Demon zapisu KDE
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}-%{_kdelibsminrel}
Obsoletes:	%{name} < 3.1.2

%description kwrited
KDE Write Daemon.

%description kwrited -l pl
Demon zapisu KDE.

%package libkate
Summary:	A libraries for KDE text editors
Summary(pl):	Biblioteki dla edytorów tekstu KDE
Group:		X11/Libraries
Requires:	%{name}-libkmultitabbar = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-kate < 3.1.2

%description libkate
A libraries for KDE text editors.

%description libkate -l pl
Biblioteki dla edytorów tekstu KDE.

%package libkmultitabbar
Summary:	Library containing multiple tab support
Summary(pl):	Biblioteka zawieraj±ca obs³ugê kilku kart
Group:		X11/Libraries
Requires:	kdelibs >= 8:%{version}-%{_kdelibsminrel}
Obsoletes:	%{name}-common-filemanagement < 3.1.2

%description libkmultitabbar
Library containing multiple tab support.

%description libkmultitabbar -l pl
Biblioteka zawieraj±ca obs³ugê kilku kart.

%package libkonq
Summary:	Konqueror library files
Summary(pl):	Biblioteki wykorzystywane przez konquerora
Group:		X11/Libraries
Requires:	kdelibs >= 8:%{version}-%{_kdelibsminrel}
Obsoletes:	konqueror < 3.1.2

%description libkonq
Libraries containing functions used by konqueror.

%description libkonq -l pl
Biblioteki zawieraj±ce funkcje wykorzystywane przez konquerora.

%package mailnews
Summary:	KDE Mail and News Services
Summary(pl):	Obs³uga protoko³ów pocztowych i news dla KDE
Group:		X11/Libraries
Requires:	kdelibs >= 8:%{version}
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
Requires:	%{name} = %{epoch}:%{version}-%{release}

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
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
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
Requires:	%{name}-common-filemanagement = %{epoch}:%{version}-%{release}
Requires:	%{name}-kicker = %{epoch}:%{version}-%{release}
Requires:	%{name}-konsole = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkonq = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkmultitabbar = %{epoch}:%{version}-%{release}
Requires:	%{name}-mailnews = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-konqueror

%description -n konqueror
Konqueror is a web browser and file manager similar to MS Internet
Explorer.

%description -n konqueror -l pl
Konqueror jest przegl±dark± WWW i zarz±dc± plików podobnym do MS
Internet Explorer.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
#%%patch14 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
#%patch20
# libtool cannot be refreshed, so patch it
%patch21 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CPPFLAGS="-I%{_includedir}"
export CPPFLAGS

for plik in `find . -name \*.desktop -o -name \*rc -o -name .directory -o \
	     -name directory.t\* | xargs grep -l '\[nb\]'` ; do
	echo -e ',s/\[nb\]=/[no]=/\n,w' | ed $plik 2>/dev/null
done

# bleh, this cannot be done (new libtool translates kicker.la to -lkicker, which fails)
#%{__libtoolize}
#%{__make} -f admin/Makefile.common cvs

%configure \
	--enable-final \
	--with-kdm-pam=kdm \
	--with-pam=kdesktop \
	--without-java

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{pam.d,rc.d/init.d,security,xdg/menus} \
	$RPM_BUILD_ROOT%{_libdir}/kde3/plugins/konqueror

%{__make} -i install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xservers{,.orig}
mv $RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xsession{,.orig}

install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/kdm
install %{SOURCE10}	$RPM_BUILD_ROOT/etc/pam.d/kdesktop
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/rc.d/init.d/kdm
install %{SOURCE4}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xsession
install %{SOURCE5}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xservers
install %{SOURCE6}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/pics/pldlogo.png
install %{SOURCE7}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/pics/pldwallpaper.png
install %{SOURCE8}	$RPM_BUILD_ROOT%{_datadir}/services/searchproviders/ircpld.desktop
install %{SOURCE9}	$RPM_BUILD_ROOT%{_datadir}/services/searchproviders/specs.desktop
install %{SOURCE11}	$RPM_BUILD_ROOT/etc/xdg/menus/kde-settings.menu
install %{SOURCE12}	$RPM_BUILD_ROOT%{_datadir}/services/searchproviders/imdb.desktop

touch $RPM_BUILD_ROOT/etc/security/blacklist.kdm

#cp $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/smb-network.desktop \
cp kioslave/smb/smb-network.desktop \
	$RPM_BUILD_ROOT%{_datadir}/apps/konqsidebartng/virtual_folders/remote

ALD=$RPM_BUILD_ROOT%{_applnkdir}

install -d $ALD/{Help,Network/WWW,Settings/KDE,System/Administration,Terminals}

mv -f $ALD/{Internet/konqbrowser.desktop,Network/WWW}
mv -f $ALD/{Internet/keditbookmarks.desktop,Utilities}
mv -f $ALD/{System/konsole.desktop,Terminals}
mv -f $ALD/{System/More/{konquerorsu,konsolesu}.desktop,System/Administration}
mv -f $ALD/{Utilities/More/*.desktop,Utilities}
mv -f $ALD/{Settings/[!K]*,Settings/KDE}
mv -f $ALD/{Settingsmenu/*.desktop,Settings}

echo -e	"Desktop\nThemes\nWindows"	> $ALD/Settings/KDE/LookNFeel/.order
echo	"WebBrowsing"			> $ALD/Settings/KDE/Network/.order

cat $ALD/Help.desktop | sed -e 's/Help/KDE Help/' -e 's/Pomoc/Pomoc KDE/' \
	> $ALD/Help/Help.desktop

echo -n ',s/\(^NoDisplay=\)/#\\1/\n,w' | \
	ed %{_applnkdir}/Settings/KDE/Information/.directory

for f in `find $ALD -name '.directory' -o -name '*.dekstop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}
for i in {access,agent,background,bell,cache,clock,cookie,date,email}.png \
	 {energy,energy_star,enhanced_browsing,filetypes,fonts,go}.png \
	 {hwinfo,icons,input_devices_settings,kappfinder,kate,kdmconfig}.png \
	 {kcmdevices,kcmkwm,kcmmemory,kcmpartitions,kcmpci,kcmprocessor}.png \
	 {kcmscsi,kcmsystem,key_bindings,keyboard,kfind,kfm,khelpcenter}.png \
	 {klipper,kmenuedit,knotify,konsole,konqueror,kpager}.png \
	 {kscreensaver,ksysguard,kthememgr,ktip,kwrite,locale,looknfeel}.png \
	 {multimedia,penguin,personal,proxy,samba,style,stylesheet,usb}.png; do
	ln -s crystalsvg/48x48/apps/$i $RPM_BUILD_ROOT%{_pixmapsdir}/$i
done

for i in `find $RPM_BUILD_ROOT%{_applnkdir} -type f`; do
	if grep '^Icon=.[^.]*$' $i >/dev/null; then
		echo -e ',s/\(^Icon=.*$\)/\\1.png/\n,w' | ed $i
	fi
done

bzip2 -dc %{SOURCE13} | tar xf - -C $RPM_BUILD_ROOT
for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
	[ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done

> core.lang
programs="drkonqi kcmcolors kcmfonts kcmkded kcmlocale kcmprintmgr \
	  kcontrol kdeprint kdeprint_part kdebugdialog kdesu kdesud \
	  khelpcenter kio_man kprinter 	krdb"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> core.lang
done
%find_lang kcmstyle; cat kcmstyle.lang >> core.lang

> %{name}.lang
programs="arts background bell desktop energy fontinst kaccess kcmaccess \
	  kcmarts kcmbackground kcmbell kcmcomponentchooser kcmemail \
	  kcmenergy kcmfontinst kcminput kcmkeys kcmkwindecoration kcmkwm \
	  kcmlaunch kcmlayout kcmnotify kcmsmserver kcmspellchecking \
	  kdcop kdesktop keyboard keys khotkeys kpersonalizer kreadconfig \
	  ksmserver ksplash kstart ktip kwin kwin_default_config \
	  kwin_keramik_config kwindecoration kxkb mouse passwords \
	  spellchecking windowmanagement"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> %{name}.lang
done
cd $RPM_BUILD_ROOT
for i in usr/X11R6/share/locale/{??,???,??_??}; do
	echo "%lang($i) %{_datadir}/locale/$i/entry.desktop" >> %{name}.lang
# these don't seem to be used
#	echo "%lang($i) %{_datadir}/locale/$i/flag.png" >> %{name}.lang
#	echo "%lang($i) %{_datadir}/locale/$i/charset" >> %{name}.lang
done
cd -

%find_lang kicker	--with-kde
programs="childpanelextension clock clockapplet dockbarextension \
	  kasbarextension kcmkclock kcmkicker kcmtaskbar kminipagerapplet \
	  krunapplet ksystemtrayapplet ktaskbarapplet libkicker \
	  libkickermenu_kdeprint libkickermenu_konsole \
	  libkickermenu_prefmenu libkickermenu_recentdocs libtaskbar \
	  libtaskmanager lockout naughtyapplet panel quicklauncher \
	  taskbarextension"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kicker.lang
done

%find_lang konqueror	--with-kde
programs="appletproxy cache cookies crypto ebrowsing email extensionproxy \
	  filemanager filetypes icons kcmcgi kcmcrypto kcmcss kcmicons \
	  kcmkio kcmkonq kcmkonqhtml kcmkurifilt kcmsocks kfile_font \
	  kfmclient kfmexec khtml kio_devices kio_finger kio_fish \
	  kio_floppy kio_mac kio_nfs kio_print kio_sftp kio_smbro netpref \
	  nsplugin proxy smb useragent"
# missing
#	kio_about
#	kio_ldap
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> konqueror.lang
done

%find_lang	kinfocenter	--with-kde
programs="kcminfo kcmioslaveinfo kcmnic kcmsamba kcmusb kioslave"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kinfocenter.lang
done

%find_lang	kdm	--with-kde
programs="kdmchooser kdmconfig kdmgreet"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kdm.lang
done

>mailnews.lang
programs="kio_imap4 kio_nntp kio_pop3 kio_smtp"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> mailnews.lang
done

%find_lang	kappfinder		--with-kde
%find_lang	kate			--with-kde
%find_lang	kcmfileshare		--with-kde
%find_lang	kcmkonsole		--with-kde
%find_lang	kcmscreensaver		--with-kde
%find_lang	kcmthemes		--with-kde
%find_lang	kdeprintfax		--with-kde
%find_lang	kdialog			--with-kde
%find_lang	kfind			--with-kde
# used by both: kfind and konqueror (libkfindpart)
%find_lang	kfindpart		--with-kde
%find_lang	kjobviewer		--with-kde
%find_lang	klipper			--with-kde
%find_lang	kmenuedit		--with-kde
%find_lang	konsole			--with-kde
%find_lang	kpager			--with-kde
%find_lang	kscreensaver		--with-kde
# ksysguard is also used by ksysguard-libs: should it be moved there?
%find_lang	ksysguard		--with-kde
%find_lang	ksystraycmd		--with-kde
%find_lang	kthememgr		--with-kde
%find_lang	kwin_b2_config		--with-kde
%find_lang	kwin_icewm_config	--with-kde
%find_lang	kwin_modernsys_config	--with-kde
%find_lang	kwin_quartz_config	--with-kde
%find_lang	kwrite			--with-kde
%find_lang	libkonq			--with-kde
%find_lang	screensaver		--with-kde

cat kcmkonsole.lang	>> konsole.lang
cat kcmscreensaver.lang	>> screensaver.lang
cat kcmthemes.lang	>> kthememgr.lang
cat kfindpart.lang	>> kfind.lang
cat kfindpart.lang	>> konqueror.lang
cat kscreensaver.lang	>> screensaver.lang

# do not build
#%find_lang	htmlsearch		--with-kde
#%find_lang	kcmhtmlsearch		--with-kde
#%find_lang	kcmsmartcard		--with-kde
#%find_lang	kfontviewpart		--with-kde
#%find_lang	kio_smb			--with-kde
#%find_lang	klegacyimport		--with-kde
#%find_lang	ppdtranslations		--with-kde

# probably from other packages
#%find_lang	kcmkwintheme		--with-kde
#%find_lang	kcmmidi			--with-kde
#%find_lang	klprfax			--with-kde
#%find_lang	kpm			--with-kde
#%find_lang	kxsconfig		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post common-konsole
cd %{_fontdir}
umask 022
/usr/X11R6/bin/mkfontdir
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%postun common-konsole
cd %{_fontdir}
umask 022
/usr/X11R6/bin/mkfontdir
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%pre -n kdm
/usr/sbin/groupadd -g 55 -r -f xdm
if [ -z "`id -u xdm 2>/dev/null`" ]; then
	/usr/sbin/useradd -u 55 -r -d /dev/null -s /bin/false -c 'X Display Manager' -g xdm xdm 1>&2
fi

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

%postun -n kdm
if [ "$1" = "0" ]; then
	if [ -n "`id -u xdm 2>/dev/null`" ]; then
		/usr/sbin/userdel xdm
	fi
	/usr/sbin/groupdel xdm
fi

%post	-n konqueror -p /sbin/ldconfig
%postun	-n konqueror -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README README.pam
%config(noreplace) %verify(not size mtime md5) /etc/pam.d/kdesktop
%attr(755,root,root) %{_bindir}/kaccess
%attr(755,root,root) %{_bindir}/kcheckpass
%attr(755,root,root) %{_bindir}/kdcop
%attr(755,root,root) %{_bindir}/kdeeject
%attr(755,root,root) %{_bindir}/kdesktop
%attr(755,root,root) %{_bindir}/kdesktop_lock
%attr(755,root,root) %{_bindir}/khotkeys
%attr(755,root,root) %{_bindir}/kpersonalizer
%attr(755,root,root) %{_bindir}/krdb
%attr(755,root,root) %{_bindir}/kreadconfig
%attr(755,root,root) %{_bindir}/ksmserver
%attr(755,root,root) %{_bindir}/ksplash
%attr(755,root,root) %{_bindir}/kstart
%attr(755,root,root) %{_bindir}/ktip
%attr(755,root,root) %{_bindir}/kwebdesktop
%attr(755,root,root) %{_bindir}/kwin
%attr(755,root,root) %{_bindir}/kxkb
%attr(755,root,root) %{_bindir}/startkde
# KDE-style (lt_)dlopenable binaries
%attr(755,root,root) %{_libdir}/kaccess.so
%{_libdir}/kaccess.la
%attr(755,root,root) %{_libdir}/kdesktop.so
%{_libdir}/kdesktop.la
%attr(755,root,root) %{_libdir}/khotkeys.so
%{_libdir}/khotkeys.la
%attr(755,root,root) %{_libdir}/ksmserver.so
%{_libdir}/ksmserver.la
%attr(755,root,root) %{_libdir}/kwin.so
%{_libdir}/kwin.la
%attr(755,root,root) %{_libdir}/kxkb.so
%{_libdir}/kxkb.la
# plugins
%attr(755,root,root) %{_libdir}/kde3/kcm_access.so
%{_libdir}/kde3/kcm_access.la
%attr(755,root,root) %{_libdir}/kde3/kcm_arts.so
%{_libdir}/kde3/kcm_arts.la
%attr(755,root,root) %{_libdir}/kde3/kcm_background.so
%{_libdir}/kde3/kcm_background.la
%attr(755,root,root) %{_libdir}/kde3/kcm_bell.so
%{_libdir}/kde3/kcm_bell.la
%attr(755,root,root) %{_libdir}/kde3/kcm_componentchooser.so
%{_libdir}/kde3/kcm_componentchooser.la
%attr(755,root,root) %{_libdir}/kde3/kcm_email.so
%{_libdir}/kde3/kcm_email.la
%attr(755,root,root) %{_libdir}/kde3/kcm_energy.so
%{_libdir}/kde3/kcm_energy.la
%attr(755,root,root) %{_libdir}/kde3/kcm_fontinst.so
%{_libdir}/kde3/kcm_fontinst.la
%attr(755,root,root) %{_libdir}/kde3/kcm_input.so
%{_libdir}/kde3/kcm_input.la
%attr(755,root,root) %{_libdir}/kde3/kcm_keyboard.so
%{_libdir}/kde3/kcm_keyboard.la
%attr(755,root,root) %{_libdir}/kde3/kcm_keys.so
%{_libdir}/kde3/kcm_keys.la
%attr(755,root,root) %{_libdir}/kde3/kcm_khotkeys.so
%{_libdir}/kde3/kcm_khotkeys.la
%attr(755,root,root) %{_libdir}/kde3/kcm_knotify.so
%{_libdir}/kde3/kcm_knotify.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kwindecoration.so
%{_libdir}/kde3/kcm_kwindecoration.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kwinoptions.so
%{_libdir}/kde3/kcm_kwinoptions.la
%attr(755,root,root) %{_libdir}/kde3/kcm_launch.so
%{_libdir}/kde3/kcm_launch.la
%attr(755,root,root) %{_libdir}/kde3/kcm_passwords.so
%{_libdir}/kde3/kcm_passwords.la
%attr(755,root,root) %{_libdir}/kde3/kcm_smserver.so
%{_libdir}/kde3/kcm_smserver.la
%attr(755,root,root) %{_libdir}/kde3/kcm_spellchecking.so
%{_libdir}/kde3/kcm_spellchecking.la
%attr(755,root,root) %{_libdir}/kde3/kwin_default.so
%{_libdir}/kde3/kwin_default.la
%attr(755,root,root) %{_libdir}/kde3/kwin_default_config.so
%{_libdir}/kde3/kwin_default_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_keramik.so
%{_libdir}/kde3/kwin_keramik.la
%attr(755,root,root) %{_libdir}/kde3/kwin_keramik_config.so
%{_libdir}/kde3/kwin_keramik_config.la
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
%{_datadir}/services/kaccess.desktop
%{_datadir}/services/kdeprint_part.desktop
%{_datadir}/services/kxkb.desktop
%{_datadir}/sounds
%{_datadir}/templates
%{_datadir}/wallpapers
%{_applnkdir}/Settings/KDE/System/.directory
%{_applnkdir}/Home.desktop
%{_applnkdir}/.hidden/[bcmspv]*.desktop
%{_applnkdir}/.hidden/k[!cio]*.desktop
%{_applnkdir}/.hidden/kcmkxmlrpcd.desktop
%{_applnkdir}/System/k[!ios]*.desktop
%{_applnkdir}/Utilities/k[!dejlp]*.desktop
%{_applnkdir}/Settings/kpersonalizer.desktop
%{_applnkdir}/Settings/KDE/email.desktop
%{_applnkdir}/Settings/KDE/Accessibility
%{_applnkdir}/Settings/KDE/Components/[!f]*
%{_applnkdir}/Settings/KDE/Components/filebrowser.desktop
%{_applnkdir}/Settings/KDE/Desktop
%dir %{_applnkdir}/Settings/KDE/LookNFeel
%{_applnkdir}/Settings/KDE/LookNFeel/.directory
%{_applnkdir}/Settings/KDE/LookNFeel/.order
%{_applnkdir}/Settings/KDE/LookNFeel/[!ks]*
%{_applnkdir}/Settings/KDE/LookNFeel/k[!t]*
%{_applnkdir}/Settings/KDE/LookNFeel/s[!c]*
%{_applnkdir}/Settings/KDE/Network/email.desktop
%{_applnkdir}/Settings/KDE/Peripherals
%{_applnkdir}/Settings/KDE/Personalization
%{_applnkdir}/Settings/KDE/PowerControl
%{_applnkdir}/Settings/KDE/Security/passwords.desktop
%{_applnkdir}/Settings/KDE/Sound
%{_applnkdir}/Settings/KDE/System/[!ck]*
%{_applnkdir}/Settings/KDE/System/kcmfontinst.desktop
%{_applnkdir}/Settings/KDE/System/kcmhelpcenter.desktop
%{_applnkdir}/Settings/KDE/WebBrowsing
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
%{_pixmapsdir}/access.png
%{_pixmapsdir}/background.png
%{_pixmapsdir}/bell.png
%{_pixmapsdir}/email.png
%{_pixmapsdir}/energy_star.png
%{_pixmapsdir}/ktip.png
%{_pixmapsdir}/kcmfontinst.png
%{_pixmapsdir}/kcmkwm.png
%{_pixmapsdir}/key_bindings.png
%{_pixmapsdir}/keyboard.png
%{_pixmapsdir}/kfm.png
%{_pixmapsdir}/knotify.png
%{_pixmapsdir}/launch.png
%{_pixmapsdir}/locale.png
%{_pixmapsdir}/spellcheck.png
%{_pixmapsdir}/style.png
%{_pixmapsdir}/usb.png

%files devel
%defattr(644,root,root,755)
# shared libraries
%attr(755,root,root) %{_libdir}/libkmultitabbar.so
%{_libdir}/libkmultitabbar.la
%attr(755,root,root) %{_libdir}/libkonq.so
%{_libdir}/libkonq.la
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so
%{_libdir}/libkonqsidebarplugin.la
%attr(755,root,root) %{_libdir}/libksgrd.so
%{_libdir}/libksgrd.la
%attr(755,root,root) %{_libdir}/libsensordisplays.so
%{_libdir}/libsensordisplays.la
%attr(755,root,root) %{_libdir}/libtaskbar.so
%{_libdir}/libtaskbar.la
# shared, possibly (lt_)dlopened libraries (.la in main package)
%attr(755,root,root) %{_libdir}/libkickermain.so
%attr(755,root,root) %{_libdir}/libtaskmanager.so
%attr(755,root,root) %{_libdir}/libnsplugin.so
# static-only library
%{_libdir}/libccont.a
%dir %{_includedir}/kwin
%{_includedir}/*.h
%{_includedir}/kwin/*.h
%{_includedir}/kate
%{_includedir}/ksgrd

%files -n kde-decoration-b2 -f kwin_b2_config.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_b2.so
%{_libdir}/kde3/kwin_b2.la
%attr(755,root,root) %{_libdir}/kde3/kwin_b2_config.so
%{_libdir}/kde3/kwin_b2_config.la
%{_datadir}/apps/kwin/b2.desktop

%files -n kde-decoration-laptop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_laptop.so
%{_libdir}/kde3/kwin_laptop.la
%{_datadir}/apps/kwin/laptop.desktop

%files -n kde-decoration-modernsys -f kwin_modernsys_config.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_modernsys.so
%{_libdir}/kde3/kwin_modernsys.la
%attr(755,root,root) %{_libdir}/kde3/kwin_modernsys_config.so
%{_libdir}/kde3/kwin_modernsys_config.la
%{_datadir}/apps/kwin/modernsystem.desktop

%files -n kde-decoration-quartz -f kwin_quartz_config.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_quartz.so
%{_libdir}/kde3/kwin_quartz.la
%attr(755,root,root) %{_libdir}/kde3/kwin_quartz_config.so
%{_libdir}/kde3/kwin_quartz_config.la
%{_datadir}/apps/kwin/quartz.desktop

%files -n kde-decoration-redmond
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_redmond.so
%{_libdir}/kde3/kwin_redmond.la
%{_datadir}/apps/kwin/redmond.desktop

%files -n kde-decoration-web
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_web.so
%{_libdir}/kde3/kwin_web.la
%{_datadir}/apps/kwin/web.desktop

%files -n kde-sdscreen-default
%defattr(644,root,root,755)
%{_datadir}/apps/ksmserver/*

%files -n kde-splash-default
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/*

%files common-filemanagement -f kcmfileshare.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/filesharelist
%attr(755,root,root) %{_bindir}/fileshareset
%attr(755,root,root) %{_libdir}/kde3/kcm_fileshare.so
%{_libdir}/kde3/kcm_fileshare.la
%attr(755,root,root) %{_libdir}/kde3/kio_thumbnail.so
%{_libdir}/kde3/kio_thumbnail.la
%attr(755,root,root) %{_libdir}/kde3/fontthumbnail.so
%{_libdir}/kde3/fontthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/gsthumbnail.so
%{_libdir}/kde3/gsthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/htmlthumbnail.so
%{_libdir}/kde3/htmlthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/imagethumbnail.so
%{_libdir}/kde3/imagethumbnail.la
%attr(755,root,root) %{_libdir}/kde3/libkonsolepart.so
%{_libdir}/kde3/libkonsolepart.la
%attr(755,root,root) %{_libdir}/kde3/picturethumbnail.so
%{_libdir}/kde3/picturethumbnail.la
%attr(755,root,root) %{_libdir}/kde3/textthumbnail.so
%{_libdir}/kde3/textthumbnail.la
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
%dir %{_applnkdir}/Settings/KDE/Network
%{_applnkdir}/Settings/KDE/Network/.directory
%{_applnkdir}/Settings/KDE/Network/.order
%{_pixmapsdir}/encrypted.png
%{_pixmapsdir}/history.png
%{_pixmapsdir}/kcmkicker.png
%{_pixmapsdir}/kcmsound.png
%{_pixmapsdir}/kcmx.png
%{_pixmapsdir}/kpersonalizer.png
%{_pixmapsdir}/printmgr.png

%files common-konsole
%defattr(644,root,root,755)
%{_fontdir}/console*.gz
%{_datadir}/apps/konsole
%{_datadir}/mimelnk/application/x-konsole.desktop
%{_pixmapsdir}/[!l]*/*/apps/bell.png
%{_pixmapsdir}/*/*/apps/key_bindings.png

%files core -f core.lang
%defattr(644,root,root,755)
/etc/xdg/menus/kde-settings.menu
%attr(755,root,root) %{_bindir}/drkonqi
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcmshell
%attr(755,root,root) %{_bindir}/kcontrol
%attr(755,root,root) %{_bindir}/kdebugdialog
%attr(755,root,root) %{_bindir}/kdesu
%attr(755,root,root) %{_bindir}/kdesud
%attr(755,root,root) %{_bindir}/khelpcenter
%attr(755,root,root) %{_bindir}/kprinter
# KDE-style (lt_)dlopenable binaries
%attr(755,root,root) %{_libdir}/kcminit.so
%{_libdir}/kcminit.la
%attr(755,root,root) %{_libdir}/kcmshell.so
%{_libdir}/kcmshell.la
%attr(755,root,root) %{_libdir}/kcontrol.so
%{_libdir}/kcontrol.la
%attr(755,root,root) %{_libdir}/kprinter.so
%{_libdir}/kprinter.la
# plugins
%attr(755,root,root) %{_libdir}/kde3/kcm_colors.so
%{_libdir}/kde3/kcm_colors.la
%attr(755,root,root) %{_libdir}/kde3/kcm_fonts.so
%{_libdir}/kde3/kcm_fonts.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kded.so
%{_libdir}/kde3/kcm_kded.la
%attr(755,root,root) %{_libdir}/kde3/kcm_style.so
%{_libdir}/kde3/kcm_style.la
%attr(755,root,root) %{_libdir}/kde3/kcm_locale.so
%{_libdir}/kde3/kcm_locale.la
%attr(755,root,root) %{_libdir}/kde3/kcm_printmgr.so
%{_libdir}/kde3/kcm_printmgr.la
%attr(755,root,root) %{_libdir}/kde3/khelpcenter.so
%{_libdir}/kde3/khelpcenter.la
%attr(755,root,root) %{_libdir}/kde3/kcm_helpcenter.so
%{_libdir}/kde3/kcm_helpcenter.la
%attr(755,root,root) %{_libdir}/kde3/kio_info.so
%{_libdir}/kde3/kio_info.la
%attr(755,root,root) %{_libdir}/kde3/kio_man.so
%{_libdir}/kde3/kio_man.la
%attr(755,root,root) %{_libdir}/kde3/libkdeprint_part.so
%{_libdir}/kde3/libkdeprint_part.la
%attr(755,root,root) %{_libdir}/kde3/libkmanpart.so
%{_libdir}/kde3/libkmanpart.la
%{_datadir}/apps/drkonqi
%{_datadir}/apps/kcontrol
%{_datadir}/apps/kdeprint/*
%{_datadir}/apps/kdeprint_part
%{_datadir}/apps/khelpcenter
%dir %{_datadir}/apps/kdisplay
%{_datadir}/apps/kdisplay/color-schemes
%dir %{_datadir}/apps/kio_info
%attr(755,root,root) %{_datadir}/apps/kio_info/kde-info2html
%{_datadir}/apps/kio_info/kde-info2html.conf
%{_datadir}/locale/en_US/*
%{_datadir}/locale/l10n
%{_datadir}/mimelnk/print
%{_datadir}/services/info.protocol
%{_datadir}/services/khelpcenter.desktop
%{_datadir}/services/man.protocol
%{_applnkdir}/Help/Help.desktop
%dir %{_applnkdir}/Settings/KDE/Components
%{_applnkdir}/Settings/KDE/Components/.directory
%{_pixmapsdir}/*/*/apps/clock.png
%{_pixmapsdir}/*/*/apps/colors.png
%{_pixmapsdir}/*/*/apps/energy.png
%{_pixmapsdir}/*/*/apps/fonts.png
%{_pixmapsdir}/*/*/apps/go.png
%{_pixmapsdir}/*/*/apps/help_index.png
%{_pixmapsdir}/*/*/apps/input_devices_settings.png
%{_pixmapsdir}/*/*/apps/kcmdrkonqi.png
%{_pixmapsdir}/*/*/apps/khelpcenter.png
%{_pixmapsdir}/*/*/apps/kcmsystem.png
%{_pixmapsdir}/*/*/apps/kcontrol.png
%{_pixmapsdir}/*/*/apps/locale.png
%{_pixmapsdir}/*/*/apps/looknfeel.png
%{_pixmapsdir}/*/*/apps/multimedia.png
%{_pixmapsdir}/*/*/apps/penguin.png
%{_pixmapsdir}/*/*/apps/personal.png
%{_pixmapsdir}/*/*/apps/printmgr.png
%{_pixmapsdir}/*/*/apps/style.png
%{_pixmapsdir}/*/*/devices/print_printer.png
%{_pixmapsdir}/*/*/filesystems/folder_print2.png
# infocenter & konqueror need it:
%{_pixmapsdir}/*/*/apps/samba.png
%{_pixmapsdir}/*/*/apps/usb.png
%{_pixmapsdir}/clock.png
%{_pixmapsdir}/energy.png
%{_pixmapsdir}/go.png
%{_pixmapsdir}/input_devices_settings.png
%{_pixmapsdir}/kcmsystem.png
%{_pixmapsdir}/khelpcenter.png
%{_pixmapsdir}/looknfeel.png
%{_pixmapsdir}/multimedia.png
%{_pixmapsdir}/penguin.png
%{_pixmapsdir}/personal.png

%files infocenter -f kinfocenter.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kinfocenter
%attr(755,root,root) %{_libdir}/kde3/kcm_info.so
%{_libdir}/kde3/kcm_info.la
%attr(755,root,root) %{_libdir}/kde3/kcm_ioslaveinfo.so
%{_libdir}/kde3/kcm_ioslaveinfo.la
%attr(755,root,root) %{_libdir}/kde3/kcm_nic.so
%{_libdir}/kde3/kcm_nic.la
%attr(755,root,root) %{_libdir}/kde3/kcm_samba.so
%{_libdir}/kde3/kcm_samba.la
%attr(755,root,root) %{_libdir}/kde3/kcm_usb.so
%{_libdir}/kde3/kcm_usb.la
%{_datadir}/apps/kcmusb
%{_datadir}/apps/kinfocenter
%{_applnkdir}/Settings/KDE/Information
%{_applnkdir}/System/kinfocenter.desktop
%{_pixmapsdir}/*/*/apps/hwinfo.png
%{_pixmapsdir}/*/*/apps/kcmdevices.png
%{_pixmapsdir}/*/*/apps/kcmmemory.png
%{_pixmapsdir}/*/*/apps/kcmpartitions.png
%{_pixmapsdir}/*/*/apps/kcmpci.png
%{_pixmapsdir}/*/*/apps/kcmprocessor.png
%{_pixmapsdir}/*/*/apps/kcmscsi.png
%{_pixmapsdir}/*/*/apps/kcmsound.png
%{_pixmapsdir}/*/*/apps/kcmx.png
%{_pixmapsdir}/hwinfo.png
%{_pixmapsdir}/kcmdevices.png
%{_pixmapsdir}/kcmmemory.png
%{_pixmapsdir}/kcmpartitions.png
%{_pixmapsdir}/kcmpci.png
%{_pixmapsdir}/kcmprocessor.png
%{_pixmapsdir}/kcmscsi.png
#%{_pixmapsdir}/kcmsound.png
#%{_pixmapsdir}/kcmx.png

%files kappfinder -f kappfinder.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kappfinder
%{_datadir}/apps/kappfinder
%{_applnkdir}/Settings/kappfinder.desktop
%{_pixmapsdir}/*/*/apps/kappfinder.png
%{_pixmapsdir}/kappfinder.png

%files kate -f kate.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kate
%attr(755,root,root) %{_libdir}/kate.so
%{_libdir}/kate.la
%{_datadir}/apps/kate
%{_datadir}/servicetypes/kateplugin.desktop
%{_applnkdir}/Editors/kate.desktop
%{_pixmapsdir}/*/*/apps/kate.png
%{_pixmapsdir}/kate.png

%files kdeprintfax -f kdeprintfax.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdeprintfax
%dir %{_datadir}/apps/kdeprintfax
%attr(755,root,root) %{_datadir}/apps/kdeprintfax/anytops
%{_datadir}/apps/kdeprintfax/[!a]*
%{_applnkdir}/Utilities/kdeprintfax.desktop
%{_pixmapsdir}/*/*/apps/kdeprintfax.png
%{_pixmapsdir}/kdeprintfax.png

%files kdialog -f kdialog.lang
%defattr(644,root,root,755)
%doc kdialog/{README,test}
%attr(755,root,root) %{_bindir}/kdialog

%files kfind -f kfind.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfind
%{_applnkdir}/Kfind.desktop
%{_pixmapsdir}/*/*/apps/kfind.png
%{_pixmapsdir}/kfind.png

%files kicker -f kicker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kicker
# shared library (.la in -devel)
%attr(755,root,root) %{_libdir}/libtaskbar.so.*.*.*
# shared, possibly (lt_)dlopened libraries
%attr(755,root,root) %{_libdir}/libkickermain.so.*.*.*
%{_libdir}/libkickermain.la
%attr(755,root,root) %{_libdir}/libtaskmanager.so.*.*.*
%{_libdir}/libtaskmanager.la
# KDE-style, (lt_)dlopenable binaries
%attr(755,root,root) %{_libdir}/kicker.so
%{_libdir}/kicker.la
# plugins
%attr(755,root,root) %{_libdir}/kde3/childpanel_panelextension.so
%{_libdir}/kde3/childpanel_panelextension.la
%attr(755,root,root) %{_libdir}/kde3/clock_panelapplet.so
%{_libdir}/kde3/clock_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/dockbar_panelextension.so
%{_libdir}/kde3/dockbar_panelextension.la
%attr(755,root,root) %{_libdir}/kde3/kasbar_panelextension.so
%{_libdir}/kde3/kasbar_panelextension.la
%attr(755,root,root) %{_libdir}/kde3/kcm_clock.so
%{_libdir}/kde3/kcm_clock.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kicker.so
%{_libdir}/kde3/kcm_kicker.la
%attr(755,root,root) %{_libdir}/kde3/kcm_taskbar.so
%{_libdir}/kde3/kcm_taskbar.la
%attr(755,root,root) %{_libdir}/kde3/kickermenu_kdeprint.so
%{_libdir}/kde3/kickermenu_kdeprint.la
%attr(755,root,root) %{_libdir}/kde3/kickermenu_konsole.so
%{_libdir}/kde3/kickermenu_konsole.la
%attr(755,root,root) %{_libdir}/kde3/kickermenu_prefmenu.so
%{_libdir}/kde3/kickermenu_prefmenu.la
%attr(755,root,root) %{_libdir}/kde3/kickermenu_recentdocs.so
%{_libdir}/kde3/kickermenu_recentdocs.la
%attr(755,root,root) %{_libdir}/kde3/launcher_panelapplet.so
%{_libdir}/kde3/launcher_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/lockout_panelapplet.so
%{_libdir}/kde3/lockout_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/minipager_panelapplet.so
%{_libdir}/kde3/minipager_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/naughty_panelapplet.so
%{_libdir}/kde3/naughty_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/run_panelapplet.so
%{_libdir}/kde3/run_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/systemtray_panelapplet.so
%{_libdir}/kde3/systemtray_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/taskbar_panelapplet.so
%{_libdir}/kde3/taskbar_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/taskbar_panelextension.so
%{_libdir}/kde3/taskbar_panelextension.la
%{_datadir}/apps/kicker
%{_datadir}/apps/naughtyapplet
%{_datadir}/autostart/panel.desktop
%{_applnkdir}/.hidden/kicker*.desktop
%{_applnkdir}/Settings/KDE/System/clock.desktop
%{_pixmapsdir}/*/*/apps/date.png
%{_pixmapsdir}/*/*/apps/kcmkicker.png
%{_pixmapsdir}/*/*/apps/kicker.png
%{_pixmapsdir}/*/*/apps/package*.png
%{_pixmapsdir}/*/*/apps/panel.png
%{_pixmapsdir}/*/*/apps/panel_settings.png
%{_pixmapsdir}/date.png

%files kjobviewer -f kjobviewer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjobviewer
# KDE-style, (lt_)dlopenable binary
%attr(755,root,root) %{_libdir}/kjobviewer.so
%{_libdir}/kjobviewer.la
%{_datadir}/apps/kjobviewer
%{_applnkdir}/Utilities/kjobviewer.desktop
%{_pixmapsdir}/*/*/apps/kjobviewer.png
%{_pixmapsdir}/kjobviewer.png

%files klipper -f klipper.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klipper
# KDE-style, (lt_)dlopenable binary
%attr(755,root,root) %{_libdir}/klipper.so
%{_libdir}/klipper.la
# plugin
%attr(755,root,root) %{_libdir}/kde3/klipper_panelapplet.so
%{_libdir}/kde3/klipper_panelapplet.la
%{_datadir}/autostart/klipper.desktop
%{_datadir}/config/klipperrc
%{_applnkdir}/Utilities/klipper.desktop
%{_pixmapsdir}/*/*/apps/klipper.png

%files kmenuedit -f kmenuedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmenuedit
# KDE-style, (lt_)dlopenable binary
%attr(755,root,root) %{_libdir}/kmenuedit.so
%{_libdir}/kmenuedit.la
%{_datadir}/apps/kmenuedit
%{_applnkdir}/Settings/kmenuedit.desktop
%{_applnkdir}/System/kmenuedit.desktop
%{_pixmapsdir}/*/*/apps/kmenu.png
%{_pixmapsdir}/*/*/apps/kmenuedit.png
%{_pixmapsdir}/kmenuedit.png

%files konsole -f konsole.lang
%defattr(644,root,root,755)
%doc konsole/README*
%attr(755,root,root) %{_bindir}/konsole*
# KDE-style, (lt_)dlopenable binary
%attr(755,root,root) %{_libdir}/konsole.so
%{_libdir}/konsole.la
# plugin
%attr(755,root,root) %{_libdir}/kde3/kcm_konsole.so
%{_libdir}/kde3/kcm_konsole.la
%{_datadir}/config/konsolerc
%{_datadir}/services/konsole-script.desktop
%{_applnkdir}/.hidden/kcmkonsole.desktop
%{_applnkdir}/System/konsolesu.desktop
%{_applnkdir}/System/Administration/konsolesu.desktop
%{_applnkdir}/Terminals/*.desktop
%{_pixmapsdir}/*/*/apps/konsole.png
%{_pixmapsdir}/konsole.png

%files kpager -f kpager.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpager
%{_applnkdir}/Utilities/kpager.desktop
%{_pixmapsdir}/*/*/apps/kpager.png
%{_pixmapsdir}/kpager.png

%files ksysguard-libs
%defattr(644,root,root,755)
# shared libraries (.la in -devel)
%attr(755,root,root) %{_libdir}/libksgrd.so.*.*.*
%attr(755,root,root) %{_libdir}/libsensordisplays.so.*.*.*

%files ksysguard -f ksysguard.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) /etc/X11/ksysguarddrc
%attr(755,root,root) %{_bindir}/kpm
%attr(755,root,root) %{_bindir}/ksysguard
%attr(755,root,root) %{_bindir}/ksysguardd
# plugin
%attr(755,root,root) %{_libdir}/kde3/sysguard_panelapplet.so
%{_libdir}/kde3/sysguard_panelapplet.la
%{_datadir}/apps/ksysguard
%{_datadir}/mimelnk/application/x-ksysguard.desktop
%{_applnkdir}/System/ksysguard.desktop
%{_pixmapsdir}/*/*/apps/ksysguard.png
%{_pixmapsdir}/ksysguard.png

%files ksystraycmd -f ksystraycmd.lang
%defattr(644,root,root,755)
%doc ksystraycmd/README
%attr(755,root,root) %{_bindir}/ksystraycmd

%files kwmtheme -f kthememgr.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwmtheme
%attr(755,root,root) %{_libdir}/kde3/kcm_themes.so
%{_libdir}/kde3/kcm_themes.la
%attr(755,root,root) %{_libdir}/kde3/kwin_kwmtheme.so
%{_libdir}/kde3/kwin_kwmtheme.la
%{_datadir}/apps/kthememgr
%{_datadir}/mimelnk/application/x-ktheme.desktop
%{_applnkdir}/Settings/KDE/LookNFeel/kthememgr.desktop
%{_pixmapsdir}/*/*/apps/kthememgr.png
%{_pixmapsdir}/kthememgr.png

%files kwrite -f kwrite.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwrite
# KDE-style, (lt_)dlopenable binary
%attr(755,root,root) %{_libdir}/kwrite.so
%{_libdir}/kwrite.la
%{_datadir}/apps/kwrite
%{_applnkdir}/Editors/kwrite.desktop
%{_pixmapsdir}/*/*/apps/kwrite.png
%{_pixmapsdir}/kwrite.png

%files kwrited
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwrited
# KDE-style, (lt_)dlopenable binary
%attr(755,root,root) %{_libdir}/kwrited.so
%{_libdir}/kwrited.la
%{_datadir}/autostart/kwrited.desktop
%{_datadir}/config/kwritedrc
%{_datadir}/services/kwrited.desktop

%files libkate
%defattr(644,root,root,755)
# plugin
%attr(755,root,root) %{_libdir}/libkateinterfaces.so
%{_libdir}/libkateinterfaces.la

%files -n kde-decoration-kde1
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_kde1.so
%{_libdir}/kde3/kwin_kde1.la
%{_datadir}/apps/kwin/kde1*

%files -n kde-decoration-kstep
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_kstep.so
%{_libdir}/kde3/kwin_kstep.la
%{_datadir}/apps/kwin/kstep*

%files -n kde-decoration-riscos
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_riscos.so
%{_libdir}/kde3/kwin_riscos.la
%{_datadir}/apps/kwin/riscos*

%files -n kde-decoration-system
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_system.so
%{_libdir}/kde3/kwin_system.la
%{_datadir}/apps/kwin/system*

%files -n kde-decoration-icewm -f kwin_icewm_config.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_icewm*.so
%{_libdir}/kde3/kwin_icewm*.la
%{_datadir}/apps/kwin/icewm-themes/*
%{_datadir}/apps/kwin/icewm*.desktop

%files libkmultitabbar
%defattr(644,root,root,755)
# shared library (.la in -devel)
%attr(755,root,root) %{_libdir}/libkmultitabbar.so.*.*.*

%files libkonq -f libkonq.lang
%defattr(644,root,root,755)
# shared library (.la in -devel)
%attr(755,root,root) %{_libdir}/libkonq.so.*.*.*
# plugin
%attr(755,root,root) %{_libdir}/kde3/konq_sound.so
%{_libdir}/kde3/konq_sound.la

%files mailnews -f mailnews.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kio_imap4.so
%{_libdir}/kde3/kio_imap4.la
%attr(755,root,root) %{_libdir}/kde3/kio_nntp.so
%{_libdir}/kde3/kio_nntp.la
%attr(755,root,root) %{_libdir}/kde3/kio_pop3.so
%{_libdir}/kde3/kio_pop3.la
%attr(755,root,root) %{_libdir}/kde3/kio_smtp.so
%{_libdir}/kde3/kio_smtp.la
%{_datadir}/services/imap4.protocol
%{_datadir}/services/imaps.protocol
%{_datadir}/services/nntp.protocol
%{_datadir}/services/pop3.protocol
%{_datadir}/services/pop3s.protocol
%{_datadir}/services/smtp.protocol
%{_datadir}/services/smtps.protocol

%files screensavers -f screensaver.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.kss
%attr(755,root,root) %{_libdir}/kde3/kcm_screensaver.so
%{_libdir}/kde3/kcm_screensaver.la
%{_datadir}/apps/kscreensaver
%{_applnkdir}/Settings/KDE/LookNFeel/screensaver.desktop
%{_pixmapsdir}/*/*/apps/kscreensaver.png
%{_pixmapsdir}/kscreensaver.png

%files -n kdm -f kdm.lang
%defattr(644,root,root,755)
%doc README.pam kdm/{ChangeLog,README,TODO}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/kdm
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.kdm
%attr(754,root,root) /etc/rc.d/init.d/kdm
%dir %{_sysconfdir}/kdm
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/kdmrc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/backgroundrc
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xreset
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xsession
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xsetup
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xstartup
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xwilling
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xaccess
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kdm/Xservers
%{_sysconfdir}/kdm/pics
%attr(755,root,root) %{_bindir}/chooser
%attr(755,root,root) %{_bindir}/kdm*
%attr(755,root,root) %{_bindir}/krootimage
%attr(755,root,root) %{_libdir}/kde3/kcm_kdm.so
%{_libdir}/kde3/kcm_kdm.la
%{_applnkdir}/Settings/KDE/System/kdm.desktop
%{_pixmapsdir}/*/*/apps/kdmconfig.png
%{_pixmapsdir}/kdmconfig.png

%files -n konqueror -f konqueror.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/appletproxy
%attr(755,root,root) %{_bindir}/extensionproxy
%attr(755,root,root) %{_bindir}/keditbookmarks
%attr(755,root,root) %{_bindir}/keditfiletype
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/kfmexec
%attr(755,root,root) %{_bindir}/kio_devices_mounthelper
%attr(755,root,root) %{_bindir}/klocaldomainurifilterhelper
%attr(755,root,root) %{_bindir}/konqueror
%attr(755,root,root) %{_bindir}/nspluginscan
%attr(755,root,root) %{_bindir}/nspluginviewer
# shared library (.la in -devel)
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so.*.*.*
# shared, possibly (lt_)dlopened library
%attr(755,root,root) %{_libdir}/libnsplugin.so.*.*.*
%{_libdir}/libnsplugin.la
# KDE-style, (lt_)dlopenable binaries
%attr(755,root,root) %{_libdir}/appletproxy.so
%{_libdir}/appletproxy.la
%attr(755,root,root) %{_libdir}/extensionproxy.so
%{_libdir}/extensionproxy.la
%attr(755,root,root) %{_libdir}/keditbookmarks.so
%{_libdir}/keditbookmarks.la
%attr(755,root,root) %{_libdir}/kfmclient.so
%{_libdir}/kfmclient.la
%attr(755,root,root) %{_libdir}/konqueror.so
%{_libdir}/konqueror.la
# plugins
%attr(755,root,root) %{_libdir}/libkonq_sidebar_tree.so
%{_libdir}/libkonq_sidebar_tree.la
%attr(755,root,root) %{_libdir}/kde3/kcm_cgi.so
%{_libdir}/kde3/kcm_cgi.la
%attr(755,root,root) %{_libdir}/kde3/kcm_crypto.so
%{_libdir}/kde3/kcm_crypto.la
%attr(755,root,root) %{_libdir}/kde3/kcm_css.so
%{_libdir}/kde3/kcm_css.la
%attr(755,root,root) %{_libdir}/kde3/kcm_filetypes.so
%{_libdir}/kde3/kcm_filetypes.la
%attr(755,root,root) %{_libdir}/kde3/kcm_history.so
%{_libdir}/kde3/kcm_history.la
%attr(755,root,root) %{_libdir}/kde3/kcm_icons.so
%{_libdir}/kde3/kcm_icons.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kio.so
%{_libdir}/kde3/kcm_kio.la
%attr(755,root,root) %{_libdir}/kde3/kcm_konq.so
%{_libdir}/kde3/kcm_konq.la
%attr(755,root,root) %{_libdir}/kde3/kcm_konqhtml.so
%{_libdir}/kde3/kcm_konqhtml.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kurifilt.so
%{_libdir}/kde3/kcm_kurifilt.la
%attr(755,root,root) %{_libdir}/kde3/kded_favicons.so
%{_libdir}/kde3/kded_favicons.la
%attr(755,root,root) %{_libdir}/kde3/kded_mountwatcher.so
%{_libdir}/kde3/kded_mountwatcher.la
%attr(755,root,root) %{_libdir}/kde3/kfile_font.so
%{_libdir}/kde3/kfile_font.la
%attr(755,root,root) %{_libdir}/kde3/kio_about.so
%{_libdir}/kde3/kio_about.la
%attr(755,root,root) %{_libdir}/kde3/kio_cgi.so
%{_libdir}/kde3/kio_cgi.la
%attr(755,root,root) %{_libdir}/kde3/kio_devices.so
%{_libdir}/kde3/kio_devices.la
%attr(755,root,root) %{_libdir}/kde3/kio_filter.so
%{_libdir}/kde3/kio_filter.la
%attr(755,root,root) %{_libdir}/kde3/kio_finger.so
%{_libdir}/kde3/kio_finger.la
%attr(755,root,root) %{_libdir}/kde3/kio_fish.so
%{_libdir}/kde3/kio_fish.la
%attr(755,root,root) %{_libdir}/kde3/kio_floppy.so
%{_libdir}/kde3/kio_floppy.la
%if %{?_without_ldap:0}%{!?_without_ldap:1}
%attr(755,root,root) %{_libdir}/kde3/kio_ldap.so
%{_libdir}/kde3/kio_ldap.la
%endif
%attr(755,root,root) %{_libdir}/kde3/kio_mac.so
%{_libdir}/kde3/kio_mac.la
%attr(755,root,root) %{_libdir}/kde3/kio_nfs.so
%{_libdir}/kde3/kio_nfs.la
%attr(755,root,root) %{_libdir}/kde3/kio_print.so
%{_libdir}/kde3/kio_print.la
%attr(755,root,root) %{_libdir}/kde3/kio_sftp.so
%{_libdir}/kde3/kio_sftp.la
%attr(755,root,root) %{_libdir}/kde3/kio_smb.so
%{_libdir}/kde3/kio_smb.la
%attr(755,root,root) %{_libdir}/kde3/kio_tar.so
%{_libdir}/kde3/kio_tar.la
%attr(755,root,root) %{_libdir}/kde3/kio_zip.so
%{_libdir}/kde3/kio_zip.la
%attr(755,root,root) %{_libdir}/kde3/konq_aboutpage.so
%{_libdir}/kde3/konq_aboutpage.la
%attr(755,root,root) %{_libdir}/kde3/konq_iconview.so
%{_libdir}/kde3/konq_iconview.la
%attr(755,root,root) %{_libdir}/kde3/konq_listview.so
%{_libdir}/kde3/konq_listview.la
%attr(755,root,root) %{_libdir}/kde3/konq_shellcmdplugin.so
%{_libdir}/kde3/konq_shellcmdplugin.la
%attr(755,root,root) %{_libdir}/kde3/konq_sidebar.so
%{_libdir}/kde3/konq_sidebar.la
%attr(755,root,root) %{_libdir}/kde3/konq_sidebartree_bookmarks.so
%{_libdir}/kde3/konq_sidebartree_bookmarks.la
%attr(755,root,root) %{_libdir}/kde3/konq_sidebartree_dirtree.so
%{_libdir}/kde3/konq_sidebartree_dirtree.la
%attr(755,root,root) %{_libdir}/kde3/konq_sidebartree_history.so
%{_libdir}/kde3/konq_sidebartree_history.la
%attr(755,root,root) %{_libdir}/kde3/konqsidebar_tree.so
%{_libdir}/kde3/konqsidebar_tree.la
%attr(755,root,root) %{_libdir}/libkfindpart.so
%{_libdir}/libkfindpart.la
%attr(755,root,root) %{_libdir}/kde3/libkshorturifilter.so
%{_libdir}/kde3/libkshorturifilter.la
%attr(755,root,root) %{_libdir}/kde3/libkuriikwsfilter.so
%{_libdir}/kde3/libkuriikwsfilter.la
%attr(755,root,root) %{_libdir}/kde3/libkurisearchfilter.so
%{_libdir}/kde3/libkurisearchfilter.la
%attr(755,root,root) %{_libdir}/kde3/liblocaldomainurifilter.so
%{_libdir}/kde3/liblocaldomainurifilter.la
%attr(755,root,root) %{_libdir}/kde3/plugins/konqueror
%{_datadir}/apps/kbookmark
%{_datadir}/apps/kcmcss
%{_datadir}/apps/keditbookmarks
%{_datadir}/apps/kfindpart
%{_datadir}/apps/kio_finger
%{_datadir}/apps/konqiconview
%{_datadir}/apps/konqlistview
%{_datadir}/apps/konqsidebartng
%{_datadir}/apps/konqueror
%{_datadir}/config/konqsidebartng.rc
%{_datadir}/config/kshorturifilterrc
%{_datadir}/config/kuriikwsfilterrc
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
%{!?_without_ldap:%{_datadir}/services/ldap.protocol}
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
%{_applnkdir}/konqueror.desktop
%{_applnkdir}/.hidden/file*.desktop
%{_applnkdir}/.hidden/kcmkonq.desktop
%{_applnkdir}/.hidden/konq*.desktop
%{_applnkdir}/Network/WWW/konq*.desktop
%{_applnkdir}/Utilities/keditbookmarks.desktop
%{_applnkdir}/Settings/KDE/Components/filetypes.desktop
%{_applnkdir}/Settings/KDE/Network/WebBrowsing
%{_applnkdir}/Settings/KDE/Network/fileshare.desktop
%{_applnkdir}/Settings/KDE/Network/lanbrowser.desktop
%{_applnkdir}/Settings/KDE/Network/netpref.desktop
%{_applnkdir}/Settings/KDE/Network/proxy.desktop
%dir %{_applnkdir}/Settings/KDE/Security
%{_applnkdir}/Settings/KDE/Security/.directory
%{_applnkdir}/Settings/KDE/Security/crypto.desktop
%{_applnkdir}/System/konq*.desktop
%{_applnkdir}/System/Administration/konq*.desktop
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
%{_pixmapsdir}/*/*/apps/konqueror.png
%{_pixmapsdir}/*/*/apps/mac.png
%{_pixmapsdir}/*/*/apps/proxy.png
%{_pixmapsdir}/*/*/apps/stylesheet.png
%{_pixmapsdir}/agent.png
%{_pixmapsdir}/cache.png
%{_pixmapsdir}/cookie.png
%{_pixmapsdir}/enhanced_browsing.png
%{_pixmapsdir}/filetypes.png
%{_pixmapsdir}/fonts.png
%{_pixmapsdir}/icons.png
%{_pixmapsdir}/konqueror.png
%{_pixmapsdir}/proxy.png
%{_pixmapsdir}/samba.png
%{_pixmapsdir}/stylesheet.png
