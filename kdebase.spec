#
# TODO:
# * KDM: ColorSheme=Default works properly with GUIStyle=KDE only
# * Adding %%doc to subpkgs
#
# Conditional build:
%bcond_without	i18n	# don't build i18n packages per module
%bcond_without	ldap	# build without LDAP support
#
%define		_state		stable
%define		_ver		3.2.0
#%%define		_snap		040110

Summary:	K Desktop Environment - core files
Summary(es):	K Desktop Environment - archivos b�sicos
Summary(ja):	KDE�ǥ����ȥå״Ķ� - ���ܥե�����
Summary(ko):	KDE - �⺻ ����
Summary(pl):	K Desktop Environment - pliki �rodowiska
Summary(pt_BR):	K Desktop Environment - arquivos b�sicos
Summary(ru):	K Desktop Environment - ������� �����
Summary(uk):	K Desktop Environment - ����צ �����
Summary(zh_CN):	KDE����
Name:		kdebase
Version:	%{_ver}
Release:	5
Epoch:		9
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{version}.tar.bz2
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
# Source0-md5:	9d05be3ccd6cc0294d6153e5d4dfa63a
Source1:	%{name}-kdesktop.pam
Source2:	%{name}-kdm.pam
Source3:	%{name}-kdm.init
Source4:	%{name}-kdm.Xsession
Source6:	%{name}-kdm_pldlogo.png
Source7:	%{name}-kdm_pldwallpaper.png
Source8:	%{name}-ircpld.desktop
Source9:	%{name}-specs.desktop
Source11:	%{name}-QtCurve.kcsrc
Source12:	http://ep09.pld-linux.org/~adgor/kde/%{name}-splash-Default-PLD-0.2.tar.bz2
# Source12-md5:	24f9c6a4b711be36437639c410b400b2
Source13:	http://ep09.pld-linux.org/~adgor/kde/%{name}-konqsidebartng-PLD-entries-0.1.tar.bz2
# Source13-md5:	c8b947bc3e8a2ac050d9e9548cf585fc
%if %{with i18n}
Source14:	http://ep09.pld-linux.org/~djurban/kde/i18n/kde-i18n-%{name}-%{version}.tar.bz2
# Source14-md5:	30848effd6e53fb459a620a50f761b85
%endif
Patch0:		%{name}-3.2branch.diff
Patch1:		%{name}-fontdir.patch
Patch2:		%{name}-kcm_background.patch
Patch3:		%{name}-kdm_utmpx.patch
Patch4:		%{name}-kdmconfig.patch
Patch5:		%{name}-kicker.patch
Patch6:		%{name}-konsole_all.patch
Patch7:		%{name}-nsplugins_dirs.patch
Patch8:		%{name}-startkde.patch
Patch9:		%{name}-kcm_fonts.patch
Patch10:	%{name}-kdesukonsole.patch
Patch11:	%{name}-vcategories.patch
Patch12:	%{name}-screensavers.patch
Patch13:	%{name}-prefmenu.patch
Patch14:	%{name}-session.patch
Patch15:	%{name}-bgdefaults.patch
Patch16:	%{name}-vmenus.patch
Patch17:	kde-common-utmpx.patch
Patch18:	%{name}-fileshareset.patch
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cups-devel
BuildRequires:	db-devel
BuildRequires:	ed
BuildRequires:	gettext-devel
BuildRequires:	jasper-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libraw1394-devel
BuildRequires:	libsmbclient-devel >= 3.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	motif-devel
BuildRequires:	openssl-devel >= 0.9.7c
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	pam-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xcursor-devel
BuildConflicts:	kdebase-konqueror-libs
Conflicts:	kdelibs < 9:3.1.94.040110-1
# TODO: sensors
#BuildRequires:	sensors-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xdgdatadir	%{_datadir}/desktop-directories

%define 	_noautoreqdep			libGL.so.1 libGLU.so.1

%description
KDE specific files. Used by core KDE applications. Package includes:
- KDE menu hierarchy,
- kappfinder - script installing some non-KDE apps in KDE menu.

%description -l ja
KDE�ǥ����ȥå״Ķ��Ѥδ��ܥ��ץꥱ�������
�ʲ��Τ褦�ʥѥå����������äƤ��ޤ���

%description -l pl
Pliki specyficzne dla �rodowiska KDE i wykorzystywane przez g��wne
aplikacje KDE. Pakiet zawiera:
- Hierarchi� menu KDE,
- kappfinder - skrypt u�awiaj�cy uruchamianie niekt�rych program�w
  spoza KDE.

%description -l ru
������� ��������� ��� K Desktop Environment. ��������: kdm (������
xdm), kwin (������� ��������), konqueror (�������� ��������,
web-�������, ftp-������, ...), konsole (������ xterm), kicker
(���������� �������� � ������� �������� �����), kaudio (�����������),
kdehelp (��������� ��� ��������� ���������� ������ kde, ������ info �
man), kthememgr (������� ��� ���������� ��������������� �������� ���)
� ������ ���������� KDE (kcheckpass, kikbd, kscreensaver, kcontrol,
kfind, kfontmanager, kmenuedit, kappfinder).

%description -l uk
����צ �������� ��� K Desktop Environment. ������Φ: kdm (��ͦ�� xdm),
kwin (צ������ ��������), konqueror (�������� ��������, web-�������,
ftp-�̦���, ...), konsole (��ͦ�� xterm), kicker (���������� �������
�� ������� �������� �����), kaudio (��Ħ�������), kdehelp (��������
��� ��������� ���̦� ��צ��� kde, ���̦� info �� man), kthememgr
(������� ��� ��������� ��������������� �������� ���) �� ��ۦ
���������� KDE (kcheckpass, kikbd, kscreensaver, kcontrol, kfind,
kfontmanager, kmenuedit, kappfinder).

%package devel
Summary:	Include files to develop KDE applications
Summary(pl):	Pliki nag��wkowe potrzebne do programowania
Summary(pt_BR):	Arquivos de inclus�o para compilar aplicativos que usem bibliotecas do kdebase
Group:		X11/Development/Libraries
Requires:	%{name}-desktop-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-kicker-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkonq = %{epoch}:%{version}-%{release}
Requires:	%{name}-libksgrd = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= 9:%{version}

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l pl
Pakiet zawiera pliki nag��wkowe niezb�dne do programowania aplikacji
KDE.

%description devel -l pt_BR
Este pacote cont�m os arquivos de inclus�o que s�o necess�rios para
compilar aplicativos que usem bibliotecas do kdebase.

%package -n kde-decoration-b2
Summary:	KDE Window Decoration - B2
Summary(pl):	Dekoracja okna dla KDE - B2
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-b2
KDE Window Decoration - B2.

%description -n kde-decoration-b2 -l pl
Dekoracja okna dla KDE - B2.

%package -n kde-decoration-laptop
Summary:	KDE Window Decoration - Laptop
Summary(pl):	Dekoracja okna dla KDE - Laptop
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-laptop
KDE Window Decoration - Laptop.

%description -n kde-decoration-laptop -l pl
Dekoracja okna dla KDE - Laptop.

%package -n kde-decoration-modernsys
Summary:	KDE Window Decoration - ModernSys
Summary(pl):	Dekoracja okna dla KDE - ModernSys
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-modernsys
KDE Window Decoration - ModernSys.

%description -n kde-decoration-modernsys -l pl
Dekoracja okna dla KDE - ModernSys.

%package -n kde-decoration-quartz
Summary:	KDE Window Decoration - Quartz
Summary(pl):	Dekoracja okna dla KDE - Quartz
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-quartz
KDE Window Decoration - Quartz.

%description -n kde-decoration-quartz -l pl
Dekoracja okna dla KDE - Quartz.

%package -n kde-decoration-redmond
Summary:	KDE Window Decoration - Redmond
Summary(pl):	Dekoracja okna dla KDE - Redmond
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-redmond
KDE Window Decoration - Redmond.

%description -n kde-decoration-redmond -l pl
Dekoracja okna dla KDE - Redmond.

%package -n kde-decoration-web
Summary:	KDE Window Decoration - Web
Summary(pl):	Dekoracja okna dla KDE - Web
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-web
KDE Window Decoration - Web.

%description -n kde-decoration-web -l pl
Dekoracja okna dla KDE - Web.

%package -n kde-kside-default
Summary:	Default kicker sidebar
Summary(pl):	Domy�lny boczny pasek do menu KDE
Group:		Themes
Requires:	kdebase-kicker >= 9:3.1.91
Provides:	kde-kside

%description -n kde-kside-default
Default kicker sidebar.

%description -n kde-kside-default -l pl
Domy�lny boczny pasek do menu KDE.

%package -n kde-logoutpic-default
Summary:	KDE "Logout" picture
Summary(pl):	Obrazek okna "Wyloguj" KDE
Group:		X11/Amusements
Requires:	%{name}-desktop
Provides:	kde-logoutpic
Obsoletes:	kde-logoutpic-PLD

%description -n kde-logoutpic-default
Default KDE "Logout" picture.

%description -n kde-logoutpic-default -l pl
Standardowy obrazek okna "Wyloguj" KDE.

%package -n kde-splash-Default-KDE
Summary:	Default clasic KDE splashscreen
Summary(pl):	Domy�lny klasyczny ekran startowy KDE
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-splash-Default-KDE
Default classic KDE splashscreen.

%description -n kde-splash-Default-KDE -l pl
Domy�lny klasyczny ekran startowy KDE.

%package -n kde-splash-blue-bend
Summary:	KDE blue-bend splashscreen
Summary(pl):	Ekran startowy KDE blue-bend
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-splash-blue-bend
KDE blue-bend splashscreen.

%description -n kde-splash-blue-bend -l pl
Ekran startowy KDE blue-bend.

%package -n kde-splashplugin-Redmond
Summary:	ksplash plugin Redmond
Summary(pl):	Wtyczka ksplash Redmond
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Obsoletes:	kde-splashplugin-XpLike

%description -n kde-splashplugin-Redmond
ksplash plugin Redmond.

%description -n kde-splashplugin-Redmond -l pl
Wtyczka ksplash Redmond.

%package -n kde-splashplugin-Standard
Summary:	ksplash plugin Standard
Summary(pl):	Wtyczka ksplash Standard
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-splashplugin-Standard
ksplash plugin Standard.

%description -n kde-splashplugin-Standard -l pl
Wtyczka ksplash Standard.

%package common-filemanagement
Summary:	Common Files for kate and konqueror
Summary(pl):	Pliki wsp�lne dla kate i konquerora
Group:		X11/Libraries
Requires:	%{name}-common-konsole = %{epoch}:%{version}-%{release}
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description common-filemanagement
Common files needed by kate and konqueror.

%description common-filemanagement -l pl
Pliki wsp�lne, u�ywane przez kate i konquerora.

%package common-konsole
Summary:	Common files for konsole and konsolepart
Summary(pl):	Pliki wsp�lne dla konsole i konsolepart
Group:		X11/Applications
Requires(post,postun):	fontpostinst
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	%{name}-fonts

%description common-konsole
Common files for konsole and konsolepart.

%description common-konsole -l pl
Pliki wsp�lne dla konsole i konsolepart.

%package core
Summary:	KDE Core Apps
Summary(pl):	Podstawowe aplikacje KDE
Group:		X11/Applications
Requires:	applnk >= 1.9.0
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name} < 8:3.2-0.030428.1
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
Podstawowe aplikacje �rodowiska KDE. Pakiet ten zawiera:
- Centrum sterowania;
- System drukowania;
- System pomocy;
- Programy obs�ugi b��d�w;
- Frontend dla programu "su".

%package desktop
Summary:	KDesktop - handling of desktop icons, popup menus etc.
Summary(pl):	KDesktop - obs�uga ikon na pulpicie, menu itp.
Group:		X11/Applications
Requires:	kde-logoutpic
Requires:	%{name}-desktop-libs = %{epoch}:%{version}-%{release}
Requires:	kicker
Requires:	konqueror = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}
Obsoletes:	%{name}-fonts
Obsoletes:	%{name}-kcheckpass
Obsoletes:	%{name}-kdesktop
Obsoletes:	%{name}-kdesktop_lock
Obsoletes:	%{name}-khelpcenter
Obsoletes:	%{name}-kioslave
Obsoletes:	%{name}-konqueror
Obsoletes:	%{name}-kwin
Obsoletes:	%{name}-kwmtheme
Obsoletes:	%{name}-kxmlrpc
Obsoletes:	%{name}-screensaver
Obsoletes:	%{name}-static
Obsoletes:	%{name}-wallpapers
Obsoletes:	kde-theme-keramik

%description desktop
KDesktop is the program that handles the desktop icons, the popup
menus for the desktop, the mac menubar, and the screensaver system.

%description desktop -l pl
KDesktop to program obs�uguj�cy ikony na pulpicie, menu dla pulpitu,
pasek menu oraz system wygaszacza ekranu.

%package desktop-libs
Summary:	KDesktop libraries
Summary(pl):	Biblioteki KDesktop
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name}-desktop < 9:3.1.92.031006

%description desktop-libs
KDesktop libraries.

%description desktop-libs -l pl
Biblioteki KDesktop.

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
Summary(pl):	Narz�dzie do aktualizacji menu
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name} =< 8:3.2-0.030418.2

%description kappfinder
Menu Updating Tool.

%description kappfinder -l pl
Narz�dzie do aktualizacji menu.

%package kate
Summary:	KDE Advanced Text Editor
Summary(pl):	Zaawansowany edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-common-filemanagement = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Obsoletes:	kate

%description kate
KDE advanced text editor.

%description kate -l pl
Zaawansowany edytor tekstu dla KDE.

%package kdeprintfax
Summary:	KDE Fax Tool
Summary(pl):	Narz�dzie do faksowania dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	efax
Requires:	enscript

%description kdeprintfax
KDE Fax Tool.

%description kdeprintfax -l pl
Narz�dzie do faksowania dla KDE.

%package kdcop
Summary:	Graphic DCOP browser/client
Summary(pl):	Graficzna przegladarka/klient DCOP
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-desktop < 9:3.1.91.030911

%description kdcop
Graphic DCOP browser/client.

%description kdcop -l pl
Graficzna przegl�darka/klient DCOP.

%package kdialog
Summary:	A KDE version of dialog
Summary(pl):	Wersja KDE dialogu
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name} < 8:3.2-0.030423.2

%description kdialog
Kdialog allows to display menu boxes from shell scripts.

%description kdialog -l pl
Kdialog umo�liwia wy�wietlanie komunikat�w z poziomu skrypt�w pow�oki.

%package kfind
Summary:	KDE Find Tool
Summary(pl):	Narz�dzie do wyszukiwania plik�w dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	kfind

%description kfind
KDE Find Tool.

%description kfind -l pl
Narz�dzie do wyszukiwania plik�w dla KDE.

%package kfontinst
Summary:	K Font Installer
Summary(pl):	Instalator font�w dla KDE
Group:		X11/Applications
#Requires:	konqueror = %{epoch}:%{version}-%{release}
Requires:	kdebase-core = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-desktop < 3.1.90.030720

%description kfontinst
K Font Installer.

%description kfontinst -l pl
Instalator font�w dla KDE.

%package kicker
Summary:	KDE Panel - kicker
Summary(pl):	Panel KDE - kicker
Group:		X11/Applications
Requires:	%{name}-kfind = %{epoch}:%{version}-%{release}
Requires:	%{name}-kicker-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-kjobviewer = %{epoch}:%{version}-%{release}
Requires:	%{name}-kmenuedit = %{epoch}:%{version}-%{release}
Requires:	%{name}-kpager = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkickermain = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkonq = %{epoch}:%{version}-%{release}
Requires:	kde-kside
Provides:	kicker

%description kicker
KDE Panel - kicker.

%description kicker -l pl
Panel KDE - kicker.

%package kicker-libs
Summary:	kicker shared libraries
Summary(pl):	Biblioteki wsp�dzielone kickera
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name}-libkickermain = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-kicker < 9:3.1.92.031006

%description kicker-libs
Shared libraries used by kicker.

%description kicker-libs -l pl
Biblioteki wsp�dzielone u�ywane przez kickera.

%package kjobviewer
Summary:	Print Job Viewer
Summary(pl):	Podgl�d zada� drukowania
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description kjobviewer
KDE Print Job Viewer.

%description kjobviewer -l pl
Podgl�d zada� drukowania dla KDE.

%package klipper
Summary:	Clipboard Tool
Summary(pl):	Narz�dzie schowka
Group:		X11/Applications
Requires:	%{name}-kicker = %{epoch}:%{version}-%{release}

%description klipper
KDE Clipboard Tool.

%description klipper -l pl
Narz�dzie schowka dla KDE.

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
Obsoletes:	konsole

%description konsole
KDE Terminal Emulator.

%description konsole -l pl
Emulator terminala dla KDE.

%package kpager
Summary:	Desktop Pager
Summary(pl):	Prze��cznik biurek
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name} =< 8:3.2-0.030418.2

%description kpager
KDE Desktop Pager.

%description kpager -l pl
Prze��cznik biurek dla KDE.

%package kpersonalizer
Summary:	KDE desktop settings wizard
Summary(pl):	Kreator ustawie� �rodowiska KDE
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Requires:	%{name}-klipper = %{epoch}:%{version}-%{release}
Obsoletes:	%{name} < 9:3.1.92.031021

%description kpersonalizer
KDE desktop settings wizard.

%description kpersonalizer -l pl
Kreator ustawie� �rodowiska KDE.

%package ksysguard
Summary:	System Guard
Summary(pl):	Stra�nik systemu
Group:		X11/Applications
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-libksgrd = %{epoch}:%{version}-%{release}

%description ksysguard
KDE System Guard.

%description ksysguard -l pl
Stra�nik systemu dla KDE.

%package ksystraycmd
Summary:	A tool that allows running applications in taskbar
Summary(pl):	Narz�dzie do uruchamiania aplikacji w pasku zada�
Group:		X11/Applications
Requires:	%{name}-kicker = %{epoch}:%{version}-%{release}

%description ksystraycmd
KSysTrayCmd is a utility that allows you to run any application you
like in the system tray, not just those designed to use it.

%description ksystraycmd -l pl
KSysTrayCmd to narz�dzie pozwalaj�ce na uruchomienie dowolnej
aplikacji w tacce systemowej - nie tylko tych, kt�re zosta�y
wyposa�one w tak� w�a�ciwo��.

%package kwmtheme
Summary:	Desktop Theme Manager
Summary(pl):	Zarz�dca motyw�w biurka
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description kwmtheme
KDE Desktop Theme Manager. This package contains also a few desktop
themes.

%description kwmtheme -l pl
Zarz�dca motyw�w biurka KDE. Ten pakiet zawiera r�wnie� kilka motyw�w.

%package kwrite
Summary:	KDE Text Editor
Summary(pl):	Edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Obsoletes:	kwrite

%description kwrite
KDE text editor with syntax highlighting.

%description kwrite -l pl
Edytor tekstu z pod�wietlaniem sk�adni dla KDE.

%package kwrited
Summary:	KDE Write Daemon
Summary(pl):	Demon zapisu KDE
Group:		X11/Applications
# With functional reasons
Requires:	kdebase-core = %{epoch}:%{version}-%{release}
Obsoletes:	%{name} < 8:3.2-0.030423.1

%description kwrited
KDE Write Daemon.

%description kwrited -l pl
Demon zapisu KDE.

%package libkate
Summary:	A libraries for KDE text editors
Summary(pl):	Biblioteki dla edytor�w tekstu KDE
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name}-kate < 8:3.2-0.030423.1
Obsoletes:	%{name}-libkmultitabbar

%description libkate
A libraries for KDE text editors.

%description libkate -l pl
Biblioteki dla edytor�w tekstu KDE.

%package libkickermain
Summary:	libkickermain library
Summary(pl):	Biblioteka libkickermain
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name}-kicker < 9:3.1.90.030629-0.1

%description libkickermain
libkickermain shared library.

%description libkickermain -l pl
Biblioteka wsp�dzielona libkickermain.

%package libkonq
Summary:	Konqueror library files
Summary(pl):	Biblioteki wykorzystywane przez konquerora
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdebase-konqueror-libs
Obsoletes:	konqueror < 8:3.2-0.030423.2

%description libkonq
Libraries containing functions used by konqueror and kicker.

%description libkonq -l pl
Biblioteki zawieraj�ce funkcje wykorzystywane przez konquerora i
kickera.

%package libksgrd
Summary:	ksgrd library
Summary(pl):	Biblioteka ksgrd
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= 9:%{version}
Obsoletes:	ksysguard < 9:3.1.92.031012

%description libksgrd
ksgrd library.

%description libksgrd -l pl
Biblioteka ksgrd.

%package mailnews
Summary:	KDE Mail and News Services
Summary(pl):	Obs�uga protoko��w pocztowych i news dla KDE
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name} < 8:3.0.9-2.4
Obsoletes:	%{name}-kioslave

%description mailnews
KDE Mail and News Services.

%description mailnews -l pl
Obs�uga protoko��w pocztowych i news dla KDE.

%package screensavers
Summary:	KDE screensavers
Summary(pl):	Wygaszacze ekranu desktopu KDE
Summary(ru):	��������� ������ ��� KDE
Summary(uk):	���Ҧ��ަ ������ ��� KDE
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description screensavers
KDE screensavers.

%description screensavers -l pl
Wygaszacze ekranu desktopu KDE.

%description screensavers -l ru
��������� 3D ��������� ������ ��� K Desktop Environment.

%package -n kdm
Summary:	KDE Display Manager
Summary(pl):	Zarz�dca ekran�w KDE
Group:		X11/Applications
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
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
Zamiennik XDM rodem z KDE. Zarz�dza lokalnymi i zdalnymi ekranami X11.

%package -n konqueror
Summary:	Konqueror - web browser and file manager
Summary(pl):	Konqueror - przegl�darka WWW i zarz�dca plik�w
Group:		X11/Applications
Requires:	%{name}-common-filemanagement = %{epoch}:%{version}-%{release}
Requires:	%{name}-konsole = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkickermain = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkonq = %{epoch}:%{version}-%{release}
Requires:	%{name}-mailnews = %{epoch}:%{version}-%{release}
%{?with_ldap:Requires:	openldap}
Obsoletes:	%{name}-konqueror
Obsoletes:	%{name}-libkmultitabbar

%description -n konqueror
Konqueror is a web browser and file manager similar to MS Internet
Explorer.

%description -n konqueror -l pl
Konqueror jest przegl�dark� WWW i zarz�dc� plik�w podobnym do MS
Internet Explorer.

%package i18n
Summary:	Common internationalization and localization files for kdebase
Summary(pl):	Wsp�dzielone pliki umi�dzynarodawiaj�ce dla kdebase
Group:		X11/Applications
#Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdelibs-i18n >= 9:%{version}

%description i18n
Internationalization and localization files for kdebase.

%description i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kdebase.

%package core-i18n
Summary:	Internationalization and localization files for core
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla core
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description core-i18n
Internationalization and localization files for core.

%description core-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla core.

%package desktop-i18n
Summary:	Internationalization and localization files for desktop
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla desktop
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Requires:	%{name}-desktop-libs-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-kicker-i18n = %{epoch}:%{version}-%{release}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description desktop-i18n
Internationalization and localization files for desktop.

%description desktop-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla desktop.

%package infocenter-i18n
Summary:	Internationalization and localization files for infocenter
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla infocenter
Group:		X11/Applications
Requires:	%{name}-infocenter = %{epoch}:%{version}-%{release}
Requires:	%{name}-core-i18n = %{epoch}:%{version}-%{release}

%description infocenter-i18n
Internationalization and localization files for infocenter.

%description infocenter-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla infocenter.

%package kate-i18n
Summary:	Internationalization and localization files for kate
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kate
Group:		X11/Applications
Requires:	%{name}-kate = %{epoch}:%{version}-%{release}
Requires:	%{name}-common-filemanagement-i18n = %{epoch}:%{version}-%{release}

%description kate-i18n
Internationalization and localization files for kate.

%description kate-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kate.

%package kfind-i18n
Summary:	Internationalization and localization files for kfind
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kfind
Group:		X11/Applications
Requires:	%{name}-kfind = %{epoch}:%{version}-%{release}
Requires:	%{name}-core-i18n = %{epoch}:%{version}-%{release}

%description kfind-i18n
Internationalization and localization files for kfind.

%description kfind-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kfind.

%package kfontinst-i18n
Summary:	Internationalization and localization files for kfontinst
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kfontinst
Group:		X11/Applications
Requires:	%{name}-kfontinst = %{epoch}:%{version}-%{release}
Requires:	%{name}-core-i18n = %{epoch}:%{version}-%{release}

%description kfontinst-i18n
Internationalization and localization files for kfontinst.

%description kfontinst-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kfontinst.

%package kicker-i18n
Summary:	Internationalization and localization files for kicker
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kickera
Group:		X11/Applications
Requires:	%{name}-kicker = %{epoch}:%{version}-%{release}
Requires:	%{name}-kfind-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-kicker-libs-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-kjobviewer-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-kmenuedit-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-kpager-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkonq-i18n = %{epoch}:%{version}-%{release}

%description kicker-i18n
Internationalization and localization files for kicker.

%description kicker-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kickera.

%package klipper-i18n
Summary:	Internationalization and localization files for klipper
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla klippera
Group:		X11/Applications
Requires:	%{name}-klipper = %{epoch}:%{version}-%{release}
Requires:	%{name}-kicker-i18n = %{epoch}:%{version}-%{release}

%description klipper-i18n
Internationalization and localization files for klipper.

%description klipper-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla klippera.

%package kmenuedit-i18n
Summary:	Internationalization and localization files for kmenuedit
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kmenuedit
Group:		X11/Applications
Requires:	%{name}-kmenuedit = %{epoch}:%{version}-%{release}
Requires:	%{name}-core-i18n = %{epoch}:%{version}-%{release}

%description kmenuedit-i18n
Internationalization and localization files for kmenuedit.

%description kmenuedit-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kmenuedit.

%package konsole-i18n
Summary:	Internationalization and localization files for konsole
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla konsole
Group:		X11/Applications
Requires:	%{name}-konsole = %{epoch}:%{version}-%{release}
Requires:	%{name}-core-i18n = %{epoch}:%{version}-%{release}

%description konsole-i18n
Internationalization and localization files for konsole.

%description konsole-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla konsole.

%package kpager-i18n
Summary:	Internationalization and localization files for kpager
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kpagera
Group:		X11/Applications
Requires:	%{name}-kpager = %{epoch}:%{version}-%{release}
Requires:	kdelibs-i18n >= 9:%{version}

%description kpager-i18n
Internationalization and localization files for kpager.

%description kpager-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kpagera.

%package ksysguard-i18n
Summary:	Internationalization and localization files for ksysguard
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla ksysguarda
Group:		X11/Applications
Requires:	%{name}-ksysguard = %{epoch}:%{version}-%{release}
Requires:	%{name}-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-klipper-i18n = %{epoch}:%{version}-%{release}

%description ksysguard-i18n
Internationalization and localization files for ksysguard.

%description ksysguard-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla ksysguarda.

%package kwrite-i18n
Summary:	Internationalization and localization files for kwrite
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kwrite
Group:		X11/Applications
Requires:	%{name}-kwrite = %{epoch}:%{version}-%{release}
Requires:	%{name}-core-i18n = %{epoch}:%{version}-%{release}

%description kwrite-i18n
Internationalization and localization files for kwrite.

%description kwrite-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kwrite.

%package screensavers-i18n
Summary:	Internationalization and localization files for screensavers
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla screensavers
Group:		X11/Applications
Requires:	%{name}-screensavers = %{epoch}:%{version}-%{release}
Requires:	%{name}-desktop-i18n = %{epoch}:%{version}-%{release}

%description screensavers-i18n
Internationalization and localization files for screensavers.

%description screensavers-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla screensavers.

%package -n kdm-i18n
Summary:	Internationalization and localization files for kdm
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kdm-a
Group:		X11/Applications
Requires:	kdm = %{epoch}:%{version}-%{release}
Requires:	%{name}-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdm-i18n
Internationalization and localization files for kdm.

%description -n kdm-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kdm-a.

%package -n konqueror-i18n
Summary:	Internationalization and localization files for konqueror
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla konquerora
Group:		X11/Applications
Requires:	konqueror = %{epoch}:%{version}-%{release}
Requires:	%{name}-common-filemanagement-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-konsole-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkonq-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-mailnews-i18n = %{epoch}:%{version}-%{release}

%description -n konqueror-i18n
Internationalization and localization files for konqueror.

%description -n konqueror-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla konquerora.

%package -n kde-decoration-b2-i18n
Summary:	Internationalization and localization files for kde-decoration-b2
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kde-decoration-b2
Group:		X11/Applications
Requires:	kde-decoration-b2 = %{epoch}:%{version}-%{release}
Requires:	%{name}-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-b2-i18n
Internationalization and localization files for kde-decoration-b2.

%description -n kde-decoration-b2-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kde-decoration-b2.

%package -n kde-decoration-modernsys-i18n
Summary:	Internationalization and localization files for kde-decoration-modernsys
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kde-decoration-modernsys
Group:		X11/Applications
Requires:	%{name}-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-decoration-modernsys = %{epoch}:%{version}-%{release}

%description -n kde-decoration-modernsys-i18n
Internationalization and localization files for kde-decoration-modernsys.

%description -n kde-decoration-modernsys-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kde-decoration-modernsys.

%package -n kde-decoration-quartz-i18n
Summary:	Internationalization and localization files for kde-decoration-quartz
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kde-decoration-quartz
Group:		X11/Applications
Requires:	%{name}-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-decoration-quartz = %{epoch}:%{version}-%{release}

%description -n kde-decoration-quartz-i18n
Internationalization and localization files for kde-decoration-quartz.

%description -n kde-decoration-quartz-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kde-decoration-quartz.

%package common-filemanagement-i18n
Summary:	Internationalization and localization files for common-filemanagement
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla common-filemanagement
Group:		X11/Applications
Requires:	%{name}-core-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-common-filemanagement = %{epoch}:%{version}-%{release}

%description common-filemanagement-i18n
Internationalization and localization files for common-filemanagement.

%description common-filemanagement-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla common-filemanagement.

%package desktop-libs-i18n
Summary:	Internationalization and localization files for desktop-libs
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla desktop-libs
Group:		X11/Applications
Requires:	%{name}-desktop-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description desktop-libs-i18n
Internationalization and localization files for desktop-libs.

%description desktop-libs-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla desktop-libs.

%package kappfinder-i18n
Summary:	Internationalization and localization files for kappfinder
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kappfindera
Group:		X11/Applications
Requires:	%{name}-kappfinder = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description kappfinder-i18n
Internationalization and localization files for kappfinder.

%description kappfinder-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kappfindera.

%package kdcop-i18n
Summary:	Internationalization and localization files for kdcop
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kdcopa
Group:		X11/Applications
Requires:	%{name}-kdcop = %{epoch}:%{version}-%{release}
Requires:	%{name}-core-i18n = %{epoch}:%{version}-%{release}

%description kdcop-i18n
Internationalization and localization files for kdcop.

%description kdcop-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kdcopa.

%package kdeprintfax-i18n
Summary:	Internationalization and localization files for kdeprintfax
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kdeprintfax
Group:		X11/Applications
Requires:	%{name}-kdeprintfax = %{epoch}:%{version}-%{release}
Requires:	%{name}-core-i18n = %{epoch}:%{version}-%{release}

%description kdeprintfax-i18n
Internationalization and localization files for kdeprintfax.

%description kdeprintfax-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kdeprintfax.

%package kdialog-i18n
Summary:	Internationalization and localization files for kdialog
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kdialoga
Group:		X11/Applications
Requires:	%{name}-kdialog = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description kdialog-i18n
Internationalization and localization files for kdialog.

%description kdialog-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kdialoga.

%package kicker-libs-i18n
Summary:	Internationalization and localization files for kicker-libs
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kicker-libs
Group:		X11/Applications
Requires:	%{name}-kicker-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description kicker-libs-i18n
Internationalization and localization files for kicker-libs.

%description kicker-libs-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kicker-libs.

%package kjobviewer-i18n
Summary:	Internationalization and localization files for kjobviewer
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kjobviewera
Group:		X11/Applications
Requires:	%{name}-kjobviewer = %{epoch}:%{version}-%{release}
Requires:	%{name}-core-i18n = %{epoch}:%{version}-%{release}

%description kjobviewer-i18n
Internationalization and localization files for kjobviewer.

%description kjobviewer-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kjobviewera.

%package kpersonalizer-i18n
Summary:	Internationalization and localization files for kpersonalizer
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kpersonalizera
Group:		X11/Applications
Requires:	%{name}-kpersonalizer = %{epoch}:%{version}-%{release}
Requires:	%{name}-desktop-i18n = %{epoch}:%{version}-%{release}

%description kpersonalizer-i18n
Internationalization and localization files for kpersonalizer.

%description kpersonalizer-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kpersonalizera.

%package ksystraycmd-i18n
Summary:	Internationalization and localization files for ksystraycmd
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla ksystraycmd
Group:		X11/Applications
Requires:	%{name}-ksystraycmd = %{epoch}:%{version}-%{release}
Requires:	%{name}-kicker-i18n = %{epoch}:%{version}-%{release}

%description ksystraycmd-i18n
Internationalization and localization files for ksystraycmd.

%description ksystraycmd-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla ksystraycmd.

%package libkonq-i18n
Summary:	Internationalization and localization files for libkonq
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla libkonq
Group:		X11/Applications
Requires:	%{name}-libkonq = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description libkonq-i18n
Internationalization and localization files for libkonq.

%description libkonq-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla libkonq.

%package mailnews-i18n
Summary:	Internationalization and localization files for mailnews
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla mailnews
Group:		X11/Applications
Requires:	%{name}-mailnews = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description mailnews-i18n
Internationalization and localization files for mailnews.

%description mailnews-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla mailnews.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
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
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1


%build
cp %{_datadir}/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir} \
	--with-kdm-pam=kdm \
	%{!?with_ldap:--with-ldap=no} \
	--with-pam=kdesktop

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d \
	$RPM_BUILD_ROOT%{_sysconfdir}/{X11/kdm/faces,pam.d,rc.d/init.d,security} \
	$RPM_BUILD_ROOT%{_libdir}/kde3/plugins/konqueror

# Backup generated Xsession file (we have own one)
mv $RPM_BUILD_ROOT%{_sysconfdir}/X11/kdm/Xsession{,.orig}

# Install miscleanous PLD files
install %{SOURCE1}	$RPM_BUILD_ROOT%{_sysconfdir}/pam.d/kdesktop
install %{SOURCE2}	$RPM_BUILD_ROOT%{_sysconfdir}/pam.d/kdm
install %{SOURCE3}	$RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/kdm
install %{SOURCE4}	$RPM_BUILD_ROOT%{_sysconfdir}/X11/kdm/Xsession
install %{SOURCE6}	$RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/pldlogo.png
install %{SOURCE7}	$RPM_BUILD_ROOT%{_datadir}/wallpapers/kdm_pld.png
install %{SOURCE8}	$RPM_BUILD_ROOT%{_datadir}/services/searchproviders/ircpld.desktop
install %{SOURCE9}	$RPM_BUILD_ROOT%{_datadir}/services/searchproviders/specs.desktop
install %{SOURCE11}	$RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes/QtCurve.kcsrc

# Needed for pam support
touch $RPM_BUILD_ROOT%{_sysconfdir}/security/blacklist.kdm

# For fileshare
touch $RPM_BUILD_ROOT%{_sysconfdir}/security/fileshare.conf

# Copying default faces to kdm config dir
cp $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/default1.png \
	$RPM_BUILD_ROOT%{_sysconfdir}/X11/kdm/faces/.default.face.icon
cp $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/root1.png \
	$RPM_BUILD_ROOT%{_sysconfdir}/X11/kdm/faces/root.face.icon

# Make PLD splashscreen as default
cd $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes
mv Default Default-KDE
echo -e ',s/\[KSplash Theme: Default\]/[KSplash Theme: Default-KDE]/\n,w' |\
	ed Default-KDE/Theme.rc
bzip2 -dc %{SOURCE12} | tar xf -
cd -

# konqsidebartng PLD entries
cd $RPM_BUILD_ROOT%{_datadir}/apps/konqsidebartng/virtual_folders
bzip2 -dc %{SOURCE13} | tar xf -
cd -

# konqueror/dirtree no longer supported
mv $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/dirtree/remote/smb-network.desktop \
	$RPM_BUILD_ROOT%{_datadir}/apps/konqsidebartng/virtual_folders/services

# Some desktop appearance defaults
cat > $RPM_BUILD_ROOT%{_datadir}/config/kdesktoprc << EOF
[FMSettings]
NormalTextColor=255,255,255
ShadowEnabled=true
StandardFont=Helvetica,13,-1,5,75,0,0,0,0,0
EOF

# Some kicker appearance defaults
cat > $RPM_BUILD_ROOT%{_datadir}/config/kickerrc << EOF
[General]
Alignment=1
SizePercentage=50
UseBackgroundTheme=false
EOF

# Some order with desktop files
mv $RPM_BUILD_ROOT%{_applnkdir}/System/kinfocenter.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_desktopdir}/kde/print{ers,mgr}.desktop

# Workaround for gnome menu which maps all these to "Others" dir
cd $RPM_BUILD_ROOT%{_desktopdir}/kde
for f in `grep -El 'X-KDE-settings|X-KDE-information' *`; do
	echo "OnlyShowIn=KDE" >> $f
done
cd -

%if %{with i18n}
bzip2 -dc %{SOURCE14} | tar xf - -C $RPM_BUILD_ROOT
for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
        [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done
%endif

# <find_lang>
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
	desktopbehavior \
	energy \
	kcmaccess \
	kcmlaunch \
	kcmnotify \
	kcmsmserver \
	keyboard \
	keys \
	ksplashml \
	kwindecoration \
	kxkb \
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
	panel \
	panelappearance"

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
%find_lang	kcmfontinst	--with-kde
%find_lang	kinfocenter	--with-kde
%find_lang	kioslave	--with-kde
%find_lang	klipper		--with-kde
%find_lang	kmenuedit	--with-kde
%find_lang	konsole		--with-kde
%find_lang	ksysguard	--with-kde
%find_lang	kpager		--with-kde
%find_lang	kwrite		--with-kde
%find_lang	screensaver	--with-kde

cat kcmkonsole.lang	>> konsole.lang
cat kioslave.lang	>> kinfocenter.lang

files="core \
kdebase \
kicker \
konqueror \
konsole \
kinfocenter \
kate \
kdm \
kfind \
kioslave \
klipper \
kmenuedit \
ksysguard \
kpager \
kwrite \
screensaver \
kcmfontinst"

%if %{with i18n}
%find_lang kwin_b2_config	--with-kde
%find_lang kwin_modernsys_config	--with-kde
%find_lang kwin_quartz_config	--with-kde
%find_lang kcmfileshare	--with-kde

core="kdesud \
kcmaccessibility \
kcmprintmgr \
klegacyimport \
kpartapp \
kprinter \
kcmcolors \
kcmfonts \
kcmkded \
kcmlocale \
kcontrol \
kdeprint_part \
kio_man \
kio_settings \
kstyle_keramik_config \
drkonqi"

for i in $core;
do
	%find_lang $i	--with-kde
	cat $i.lang >> core.lang
done

desktop="kcmkwintheme \
kcmkwm \
kwin \
krandr \
privacy \
kcmspellchecking \
kcminput \
kcmxinerama \
display \
ktip \
kaccess \
krdb \
kreadconfig \
ksplash \
kstart \
kwin_default_config \
kcmarts \
kcmbackground \
kcmbell \
kcmcomponentchooser \
kcmemail \
kcmenergy \
kcmkeys \
kcmkwindecoration \
khotkeys \
kdesktop \
ksmserver \
kwin_keramik_config \
kcmmidi"

for i in $desktop;
do
	%find_lang $i	--with-kde
	cat $i.lang >> %{name}.lang
done

%find_lang ksplashthemes	--with-kde

info="kcminfo \
kcmioslaveinfo \
kcmnic \
kcmsamba \
kcmusb \
kcmview1394"

for i in $info;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kinfocenter.lang
done

%find_lang kappfinder	--with-kde

%find_lang katedefaultproject	--with-kde
cat katedefaultproject.lang >> kate.lang

%find_lang kdcop	--with-kde

%find_lang kdeprintfax	--with-kde

%find_lang kdialog	--with-kde

%find_lang kfindpart	--with-kde
cat kfindpart.lang >> kfind.lang


%find_lang kfontinst	--with-kde
cat kfontinst.lang >> kcmfontinst.lang
%find_lang fontinst	--with-kde
cat fontinst.lang >> kcmfontinst.lang

kicker="kcmkclock \
kcmkicker \
lockout \
ktaskbarapplet \
libkicker \
libkickermenu_kdeprint \
libkickermenu_konsole \
libkickermenu_prefmenu \
libkickermenu_recentdocs \
ksystemtrayapplet \
childpanelextension \
clockapplet \
kmenuapplet \
kminipagerapplet \
krunapplet \
devicesapplet \
dockbarextension \
kasbarextension \
naughtyapplet \
quicklauncher \
taskbarextension"

for i in $kicker;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kicker.lang
done

%find_lang libtaskbar	--with-kde
%find_lang libtaskmanager	--with-kde
cat libtaskmanager.lang >> libtaskbar.lang

%find_lang kjobviewer	--with-kde

%find_lang kpersonalizer	--with-kde

%find_lang ksystraycmd	--with-kde

%find_lang kwriteconfig	--with-kde
cat kwriteconfig.lang >> kwrite.lang

%find_lang libkonq	--with-kde

mn="kio_imap4 \
kio_pop3 \
kio_nntp \
kio_smtp"

for i in $mn;
do
	%find_lang $i	--with-kde
	cat $i.lang >> mailnews.lang
done

screen="kscreensaver \
kcmscreensaver"

for i in $screen;
do
	%find_lang $i	--with-kde
	cat $i.lang >> screensaver.lang
done


kdm="kdmchooser \
kdmconfig \
kdmgreet"

for i in $kdm;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kdm.lang
done

konqueror="appletproxy \
nsplugin \
kcmhtmlsearch \
kcmsocks \
kcmlayout \
htmlsearch \
extensionproxy \
kfmclient \
kio_devices \
kcmcgi \
kcmcrypto \
kcmicons \
kcmkio \
kcmkonq \
kcmkonqhtml \
kcmkurifilt \
kcmperformance \
kfile_font \
kio_finger \
kio_fish \
kio_floppy \
kio_mac \
kio_nfs \
kio_print \
kio_sftp \
kio_smb \
kio_smbro"

for i in $konqueror;
do
	%find_lang $i	--with-kde
	cat $i.lang >> konqueror.lang
done


%find_lang desktop_kdebase --with-kde
mv desktop_kdebase.lang i18n.lang

for i in $RPM_BUILD_ROOT%{_datadir}/locale/* ;
do
	echo $i
	if [ -d $i ] ; then
	z=`echo $i|sed -e "s,${RPM_BUILD_ROOT}%{_datadir}/locale/,,"`
	if [ -f ${RPM_BUILD_ROOT}%{_datadir}/locale/$z/charset ] ; then
	echo %lang\($z\) %{_datadir}/locale/$z/charset >> i18n.lang
	fi
	if [ -f ${RPM_BUILD_ROOT}%{_datadir}/locale/$z/entry.desktop ] ; then
	echo %lang\($z\) %{_datadir}/locale/$z/entry.desktop >> i18n.lang
	fi
	if [ -f ${RPM_BUILD_ROOT}%{_datadir}/locale/$z/flag.png ] ; then
	echo %lang\($z\) %{_datadir}/locale/$z/flag.png >> i18n.lang
	fi
	fi
done
%endif

for i in $files; do
	echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done

durne=`ls -1 *.lang|grep -v _en`

for i in $durne;
do
	echo $i >> control
	grep -v en\/ $i|grep -v apidocs >> ${i}.1
	if [ -f ${i}.1 ] ; then
		mv ${i}.1 ${i}
	fi
done
# </find_lang>


%clean
rm -rf $RPM_BUILD_ROOT

%post common-filemanagement
cat << EOF

 *********************************************************
 *                                                       *
 * NOTE:                                                 *
 * If You want the catalogs sharing from the context     *
 * menu functionality, do as following:                  *
 * 1) Install sperl package,                             *
 * 2) Set SUID for fileshareset script.                  *
 *                                                       *
 * WARNING:                                              *
 * 1) That allows users to write to /etc/samba/smb.conf, *
 * 2) After all - using sperl is not safe.               *
 *                                                       *
 *********************************************************

EOF

%post common-konsole
/usr/bin/fontpostinst misc

%postun common-konsole
/usr/bin/fontpostinst misc

%post core
cat << EOF

 ******************************************
 *                                        *
 * NOTE:                                  *
 * Set sgid for kdesud daemon if You want *
 * superuser password caching feature.    *
 *                                        *
 ******************************************

EOF

%post	desktop-libs	-p /sbin/ldconfig
%postun	desktop-libs	-p /sbin/ldconfig

%post	kicker-libs	-p /sbin/ldconfig
%postun	kicker-libs	-p /sbin/ldconfig

%post	libkate		-p /sbin/ldconfig
%postun	libkate		-p /sbin/ldconfig

%post	libkickermain	-p /sbin/ldconfig
%postun	libkickermain	-p /sbin/ldconfig

%post	libkonq		-p /sbin/ldconfig
%postun	libkonq		-p /sbin/ldconfig

%post	libksgrd	-p /sbin/ldconfig
%postun	libksgrd	-p /sbin/ldconfig

%post -n kdm
/sbin/chkconfig --add kdm
if [ -f /var/lock/subsys/kdm ]; then
cat << EOF

 ***************************************************
 *                                                 *
 * NOTE:                                           *
 * To make sure that new version of KDM is running *
 * You should restart KDM with:                    *
 * "/etc/rc.d/init.d/kdm restart".                 *
 *                                                 *
 * WARNING:                                        *
 * Restarting KDM will terminate any X session     *
 * started by it!                                  *
 *                                                 *
 ***************************************************

EOF
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

%if %{with i18n}
%files core-i18n -f core.lang
%files desktop-i18n -f kdebase.lang
%files infocenter-i18n -f kinfocenter.lang
%files kate-i18n -f kate.lang
%files kfind-i18n -f kfind.lang
%files kfontinst-i18n -f kcmfontinst.lang
%files kicker-i18n -f kicker.lang
%files klipper-i18n -f klipper.lang
%files kmenuedit-i18n -f kmenuedit.lang
%files konsole-i18n -f konsole.lang
%files kpager-i18n -f kpager.lang
%files ksysguard-i18n -f ksysguard.lang
%files kwrite-i18n -f kwrite.lang
%files screensavers-i18n -f screensaver.lang
%files -n kdm-i18n -f kdm.lang
%files -n konqueror-i18n -f konqueror.lang
%files i18n -f i18n.lang
%files -n kde-decoration-b2-i18n -f kwin_b2_config.lang
%files -n kde-decoration-modernsys-i18n -f kwin_modernsys_config.lang
%files -n kde-decoration-quartz-i18n -f kwin_quartz_config.lang
%files common-filemanagement-i18n -f kcmfileshare.lang
%files desktop-libs-i18n -f ksplashthemes.lang
%files kappfinder-i18n -f kappfinder.lang
%files kdcop-i18n -f kdcop.lang
%files kdeprintfax-i18n -f kdeprintfax.lang
%files kdialog-i18n -f kdialog.lang
%files kicker-libs-i18n -f libtaskbar.lang
%files kjobviewer-i18n -f kjobviewer.lang
%files kpersonalizer-i18n -f kpersonalizer.lang
%files ksystraycmd-i18n -f ksystraycmd.lang
%files libkonq-i18n -f libkonq.lang
%files mailnews-i18n -f mailnews.lang
%endif

%files devel
%defattr(644,root,root,755)
##%lang(en) %{_kdedocdir}/en/%{name}-apidocs
%attr(755,root,root) %{_libdir}/libkateinterfaces.so
%attr(755,root,root) %{_libdir}/libkateutils.so
%attr(755,root,root) %{_libdir}/libkdecorations.so
%attr(755,root,root) %{_libdir}/libkickermain.so
%attr(755,root,root) %{_libdir}/libkonq.so
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so
%attr(755,root,root) %{_libdir}/libksgrd.so
%attr(755,root,root) %{_libdir}/libksplashthemes.so
#%attr(755,root,root) %{_libdir}/libsensordisplays.so
%attr(755,root,root) %{_libdir}/libtaskbar.so
%attr(755,root,root) %{_libdir}/libtaskmanager.so
%{_includedir}/*.h
%{_includedir}/kate
%{_includedir}/ksgrd
%{_includedir}/ksplash
%{_includedir}/kwin

%files -n kde-decoration-b2
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_b2.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_b2.so
%{_libdir}/kde3/kwin_b2_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_b2_config.so
%{_datadir}/apps/kwin/b2.desktop

%files -n kde-decoration-laptop
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_laptop.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_laptop.so
%{_datadir}/apps/kwin/laptop.desktop

%files -n kde-decoration-modernsys
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_modernsys.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_modernsys.so
%{_libdir}/kde3/kwin_modernsys_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_modernsys_config.so
%{_datadir}/apps/kwin/modernsystem.desktop

%files -n kde-decoration-quartz
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_quartz.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_quartz.so
%{_libdir}/kde3/kwin_quartz_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_quartz_config.so
%{_datadir}/apps/kwin/quartz.desktop

%files -n kde-decoration-redmond
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_redmond.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_redmond.so
%{_datadir}/apps/kwin/redmond.desktop

%files -n kde-decoration-web
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_web.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_web.so
%{_datadir}/apps/kwin/web.desktop

%files -n kde-kside-default
%defattr(644,root,root,755)
%{_datadir}/apps/kicker/pics/kside*.png

%files -n kde-logoutpic-default
%defattr(644,root,root,755)
%{_datadir}/apps/ksmserver/pics/shutdownkonq.png

%files -n kde-splash-Default-KDE
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/Default-KDE

%files -n kde-splash-blue-bend
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/blue-bend

%files -n kde-splashplugin-Redmond
%defattr(644,root,root,755)
%{_libdir}/kde3/ksplashredmond.la
%attr(755,root,root) %{_libdir}/kde3/ksplashredmond.so
%{_datadir}/apps/ksplash/Themes/Redmond
%{_datadir}/services/ksplashredmond.desktop

%files -n kde-splashplugin-Standard
%defattr(644,root,root,755)
%{_libdir}/kde3/ksplashstandard.la
%attr(755,root,root) %{_libdir}/kde3/ksplashstandard.so
%{_datadir}/apps/ksplash/Themes/Standard
%{_datadir}/apps/ksplash/pics/splash.png
%{_datadir}/services/ksplashstandard.desktop

%files common-filemanagement
%defattr(644,root,root,755)
%ghost %{_sysconfdir}/security/fileshare.conf
%attr(755,root,root) %{_bindir}/filesharelist
%attr(755,root,root) %{_bindir}/fileshareset
%{_libdir}/kde3/kcm_fileshare.la
%attr(755,root,root) %{_libdir}/kde3/kcm_fileshare.so
%{_libdir}/kde3/djvuthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/djvuthumbnail.so
%{_libdir}/kde3/kio_thumbnail.la
%attr(755,root,root) %{_libdir}/kde3/kio_thumbnail.so
%{_libdir}/kde3/fontthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/fontthumbnail.so
%{_libdir}/kde3/gsthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/gsthumbnail.so
%{_libdir}/kde3/htmlthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/htmlthumbnail.so
%{_libdir}/kde3/imagethumbnail.la
%attr(755,root,root) %{_libdir}/kde3/imagethumbnail.so
%{_libdir}/kde3/libkonsolepart.la
%attr(755,root,root) %{_libdir}/kde3/libkonsolepart.so
%{_libdir}/kde3/picturethumbnail.la
%attr(755,root,root) %{_libdir}/kde3/picturethumbnail.so
%{_libdir}/kde3/textthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/textthumbnail.so
%{_datadir}/services/djvuthumbnail.desktop
%{_datadir}/services/fontthumbnail.desktop
%{_datadir}/services/gsthumbnail.desktop
%{_datadir}/services/htmlthumbnail.desktop
%{_datadir}/services/imagethumbnail.desktop
%{_datadir}/services/konsolepart.desktop
%{_datadir}/services/textthumbnail.desktop
%{_datadir}/services/picturethumbnail.desktop
%{_datadir}/services/thumbnail.protocol
%{_datadir}/servicetypes/terminalemulator.desktop
%{_datadir}/servicetypes/thumbcreator.desktop
%{_desktopdir}/kde/fileshare.desktop

%files common-konsole
%defattr(644,root,root,755)
%{_fontsdir}/misc/console*.gz
%{_datadir}/apps/konsole
%{_datadir}/mimelnk/application/x-konsole.desktop
%{_iconsdir}/[!l]*/*/apps/bell.png
%{_iconsdir}/*/*/apps/key_bindings.png

%files core -f core_en.lang
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/menus/applications-merged/kde-essential.menu
%{_sysconfdir}/xdg/menus/kde-settings.menu
%attr(755,root,root) %{_bindir}/drkonqi
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcmshell
%attr(755,root,root) %{_bindir}/kcontrol
%attr(755,root,root) %{_bindir}/kdebugdialog
%attr(755,root,root) %{_bindir}/kdesu
%attr(755,root,root) %{_bindir}/kdesud
%attr(755,root,root) %{_bindir}/khc_indexbuilder
%attr(755,root,root) %{_bindir}/khelpcenter
%attr(755,root,root) %{_bindir}/kprinter
%{_libdir}/libkdeinit_kcminit.la
%attr(755,root,root) %{_libdir}/libkdeinit_kcminit.so
%{_libdir}/libkdeinit_kcmshell.la
%attr(755,root,root) %{_libdir}/libkdeinit_kcmshell.so
%{_libdir}/libkdeinit_kcontrol.la
%attr(755,root,root) %{_libdir}/libkdeinit_kcontrol.so
%{_libdir}/libkdeinit_khelpcenter.la
%attr(755,root,root) %{_libdir}/libkdeinit_khelpcenter.so
%{_libdir}/libkdeinit_kprinter.la
%attr(755,root,root) %{_libdir}/libkdeinit_kprinter.so
%{_libdir}/kde3/kcm_colors.la
%attr(755,root,root) %{_libdir}/kde3/kcm_colors.so
%{_libdir}/kde3/kcm_fonts.la
%attr(755,root,root) %{_libdir}/kde3/kcm_fonts.so
%{_libdir}/kde3/kcm_kded.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kded.so
%{_libdir}/kde3/kcm_style.la
%attr(755,root,root) %{_libdir}/kde3/kcm_style.so
%{_libdir}/kde3/kcm_locale.la
%attr(755,root,root) %{_libdir}/kde3/kcm_locale.so
%{_libdir}/kde3/kcm_printmgr.la
%attr(755,root,root) %{_libdir}/kde3/kcm_printmgr.so
%{_libdir}/kde3/kcminit.la
%attr(755,root,root) %{_libdir}/kde3/kcminit.so
%{_libdir}/kde3/kcmshell.la
%attr(755,root,root) %{_libdir}/kde3/kcmshell.so
%{_libdir}/kde3/kcontrol.la
%attr(755,root,root) %{_libdir}/kde3/kcontrol.so
%{_libdir}/kde3/khelpcenter.la
%attr(755,root,root) %{_libdir}/kde3/khelpcenter.so
%{_libdir}/kde3/kio_info.la
%attr(755,root,root) %{_libdir}/kde3/kio_info.so
%{_libdir}/kde3/kio_man.la
%attr(755,root,root) %{_libdir}/kde3/kio_man.so
%{_libdir}/kde3/kio_settings.la
%attr(755,root,root) %{_libdir}/kde3/kio_settings.so
%{_libdir}/kde3/kprinter.la
%attr(755,root,root) %{_libdir}/kde3/kprinter.so
%{_libdir}/kde3/kstyle_keramik_config.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_keramik_config.so
%{_libdir}/kde3/libkdeprint_part.la
%attr(755,root,root) %{_libdir}/kde3/libkdeprint_part.so
%{_libdir}/kde3/libkmanpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmanpart.so
%{_datadir}/apps/drkonqi
%{_datadir}/apps/kcmview1394
%{_datadir}/apps/kcontrol
%{_datadir}/apps/kdeprint/*
%{_datadir}/apps/kdeprint_part
%dir %{_datadir}/apps/kdisplay
%{_datadir}/apps/kdisplay/color-schemes
%{_datadir}/apps/khelpcenter
# For apps they store files in applets
%dir %{_datadir}/apps/kicker
%dir %{_datadir}/apps/kicker/applets
#
%dir %{_datadir}/apps/kio_info
%attr(0755,root,root) %{_datadir}/apps/kio_info/kde-info2html
%{_datadir}/apps/kio_info/kde-info2html.conf
# For apps they store files in servicemenus
%dir %{_datadir}/apps/konqueror
%dir %{_datadir}/apps/konqueror/servicemenus
#
%{_datadir}/locale/l10n
%lang(en_US) %{_datadir}/locale/en_US/entry.desktop
%{_datadir}/mimelnk/print
%{_datadir}/services/info.protocol
%{_datadir}/services/khelpcenter.desktop
%{_datadir}/services/kdeprint_part.desktop
%{_datadir}/services/man.protocol
%{_datadir}/services/programs.protocol
%{_datadir}/services/settings.protocol
%{_datadir}/services/system.protocol
%{_xdgdatadir}/kde-settings*.directory
%{_desktopdir}/kde/language.desktop
%{_desktopdir}/kde/kcmkded.desktop
%{_desktopdir}/kde/colors.desktop
%{_desktopdir}/kde/fonts.desktop
%{_desktopdir}/kde/style.desktop
%{_desktopdir}/kde/printmgr.desktop
%{_desktopdir}/kde/Help.desktop
%{_desktopdir}/kde/KControl.desktop
%{_iconsdir}/*/*/apps/colors.png
%{_iconsdir}/*/*/apps/energy.png
%{_iconsdir}/*/*/apps/fonts.png
%{_iconsdir}/*/*/apps/help_index.png
%{_iconsdir}/*/*/apps/input_devices_settings.png
%{_iconsdir}/*/*/apps/kcmdrkonqi.png
%{_iconsdir}/*/*/apps/khelpcenter.png
%{_iconsdir}/*/*/apps/kcmsystem.png
%{_iconsdir}/*/*/apps/kcontrol.png
%{_iconsdir}/*/*/apps/konqueror.png
%{_iconsdir}/*/*/apps/locale.png
%{_iconsdir}/*/*/apps/looknfeel.png
%{_iconsdir}/*/*/apps/multimedia.png
%{_iconsdir}/*/*/apps/personal.png
%{_iconsdir}/*/*/apps/printmgr.png
%{_iconsdir}/*/*/apps/style.png
%{_iconsdir}/*/*/devices/print_printer.png
%{_iconsdir}/*/*/filesystems/folder_print2.png
# infocenter & konqueror need it:
%{_iconsdir}/*/*/apps/samba.png
%{_iconsdir}/*/*/apps/usb.png

%files desktop -f %{name}_en.lang
%defattr(644,root,root,755)
%doc AUTHORS README README.pam
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pam.d/kdesktop
%attr(755,root,root) %{_bindir}/kaccess
%attr(755,root,root) %{_bindir}/kcheckpass
%attr(755,root,root) %{_bindir}/kdeeject
%attr(755,root,root) %{_bindir}/kdesktop
%attr(755,root,root) %{_bindir}/kdesktop_lock
%attr(755,root,root) %{_bindir}/kwin_killer_helper
%attr(755,root,root) %{_bindir}/khotkeys
%attr(755,root,root) %{_bindir}/krdb
%attr(755,root,root) %{_bindir}/kreadconfig
%attr(755,root,root) %{_bindir}/krandrtray
%attr(755,root,root) %{_bindir}/ksmserver
%attr(755,root,root) %{_bindir}/ksplash
%attr(755,root,root) %{_bindir}/kstart
%attr(755,root,root) %{_bindir}/ktip
%attr(755,root,root) %{_bindir}/kwebdesktop
%attr(755,root,root) %{_bindir}/kwin
#%attr(755,root,root) %{_bindir}/kwin_dialog_helper
%attr(755,root,root) %{_bindir}/kxkb
%attr(755,root,root) %{_bindir}/startkde
%attr(755,root,root) %{_libdir}/kconf_update_bin/khotkeys_update
%{_libdir}/krandrinithack.la
%attr(755,root,root) %{_libdir}/krandrinithack.so
%{_libdir}/libkdeinit_kaccess.la
%attr(755,root,root) %{_libdir}/libkdeinit_kaccess.so
%{_libdir}/libkdeinit_kdesktop.la
%attr(755,root,root) %{_libdir}/libkdeinit_kdesktop.so
%{_libdir}/libkdeinit_khotkeys.la
%attr(755,root,root) %{_libdir}/libkdeinit_khotkeys.so
%{_libdir}/libkdeinit_ksmserver.la
%attr(755,root,root) %{_libdir}/libkdeinit_ksmserver.so
%{_libdir}/libkdeinit_kwin.la
%attr(755,root,root) %{_libdir}/libkdeinit_kwin.so
%{_libdir}/libkdeinit_kxkb.la
%attr(755,root,root) %{_libdir}/libkdeinit_kxkb.so
%{_libdir}/kde3/cursorthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/cursorthumbnail.so
%{_libdir}/kde3/kaccess.la
%attr(755,root,root) %{_libdir}/kde3/kaccess.so
%{_libdir}/kde3/kcm_access.la
%attr(755,root,root) %{_libdir}/kde3/kcm_access.so
%{_libdir}/kde3/kcm_arts.la
%attr(755,root,root) %{_libdir}/kde3/kcm_arts.so
%{_libdir}/kde3/kcm_background.la
%attr(755,root,root) %{_libdir}/kde3/kcm_background.so
%{_libdir}/kde3/kcm_bell.la
%attr(755,root,root) %{_libdir}/kde3/kcm_bell.so
%{_libdir}/kde3/kcm_componentchooser.la
%attr(755,root,root) %{_libdir}/kde3/kcm_componentchooser.so
%{_libdir}/kde3/kcm_display.la
%attr(755,root,root) %{_libdir}/kde3/kcm_display.so
%{_libdir}/kde3/kcm_email.la
%attr(755,root,root) %{_libdir}/kde3/kcm_email.so
%{_libdir}/kde3/kcm_energy.la
%attr(755,root,root) %{_libdir}/kde3/kcm_energy.so
%{_libdir}/kde3/kcm_input.la
%attr(755,root,root) %{_libdir}/kde3/kcm_input.so
%{_libdir}/kde3/kcm_keyboard.la
%attr(755,root,root) %{_libdir}/kde3/kcm_keyboard.so
%{_libdir}/kde3/kcm_keys.la
%attr(755,root,root) %{_libdir}/kde3/kcm_keys.so
 %{_libdir}/kde3/kcm_khotkeys.la
%attr(755,root,root) %{_libdir}/kde3/kcm_khotkeys.so
%{_libdir}/kde3/kcm_knotify.la
%attr(755,root,root) %{_libdir}/kde3/kcm_knotify.so
%{_libdir}/kde3/kcm_ksplashthemes.la
%attr(755,root,root) %{_libdir}/kde3/kcm_ksplashthemes.so
%{_libdir}/kde3/kcm_kwindecoration.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kwindecoration.so
%{_libdir}/kde3/kcm_kwinoptions.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kwinoptions.so
%{_libdir}/kde3/kcm_launch.la
%attr(755,root,root) %{_libdir}/kde3/kcm_launch.so
%{_libdir}/kde3/kcm_nsplugins.la
%attr(755,root,root) %{_libdir}/kde3/kcm_nsplugins.so
%{_libdir}/kde3/kcm_passwords.la
%attr(755,root,root) %{_libdir}/kde3/kcm_passwords.so
%{_libdir}/kde3/kcm_privacy.la
%attr(755,root,root) %{_libdir}/kde3/kcm_privacy.so
%{_libdir}/kde3/kcm_randr.la
%attr(755,root,root) %{_libdir}/kde3/kcm_randr.so
%{_libdir}/kde3/kcm_smserver.la
%attr(755,root,root) %{_libdir}/kde3/kcm_smserver.so
%{_libdir}/kde3/kcm_spellchecking.la
%attr(755,root,root) %{_libdir}/kde3/kcm_spellchecking.so
%{_libdir}/kde3/kcm_xinerama.la
%attr(755,root,root) %{_libdir}/kde3/kcm_xinerama.so
%{_libdir}/kde3/kdesktop.la
%attr(755,root,root) %{_libdir}/kde3/kdesktop.so
%{_libdir}/kde3/khotkeys.la
%attr(755,root,root) %{_libdir}/kde3/khotkeys.so
%{_libdir}/kde3/ksmserver.la
%attr(755,root,root) %{_libdir}/kde3/ksmserver.so
%{_libdir}/kde3/ksplashdefault.la
%attr(755,root,root) %{_libdir}/kde3/ksplashdefault.so
%{_libdir}/kde3/kwin.la
%attr(755,root,root) %{_libdir}/kde3/kwin.so
%{_libdir}/kde3/kwin_default_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_default_config.so
%{_libdir}/kde3/kwin_keramik_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_keramik_config.so
%{_libdir}/kde3/kwin3_default.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_default.so
%{_libdir}/kde3/kwin3_keramik.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_keramik.so
%{_libdir}/kde3/kxkb.la
%attr(755,root,root) %{_libdir}/kde3/kxkb.so
%{_datadir}/apps/clockapplet
%{_datadir}/apps/kcm_componentchooser/*
%dir %{_datadir}/apps/kcminput
%{_datadir}/apps/kcminput/pics
%{_datadir}/apps/kcmkeys
%{_datadir}/apps/kcmlocale
%{_datadir}/apps/kconf_update/*
%{_datadir}/apps/kdcop
%{_datadir}/apps/kdesktop
%{_datadir}/apps/kdewizard
%{_datadir}/apps/kdisplay/app-defaults
%{_datadir}/apps/khotkeys
%dir %{_datadir}/apps/ksmserver
%dir %{_datadir}/apps/ksmserver/pics
%dir %{_datadir}/apps/ksplash
%dir %{_datadir}/apps/ksplash/Themes
%dir %{_datadir}/apps/ksplash/pics
%{_datadir}/apps/ksplash/Themes/Default
%dir %{_datadir}/apps/kwin
%{_datadir}/apps/kwin/eventsrc
%{_datadir}/apps/kwin/keramik.desktop
%dir %{_datadir}/apps/kwin/pics
%{_datadir}/apps/kwin/pics/*
%{_datadir}/autostart/kdesktop.desktop
%{_datadir}/autostart/khotkeys.desktop
%{_datadir}/autostart/ktip.desktop
%{_datadir}/config/kdesktoprc
%{_datadir}/config/kdesktop_custom_menu1
%{_datadir}/config/kdesktop_custom_menu2
%{_datadir}/config/kxkb_groups
%{_datadir}/services/cursorthumbnail.desktop
%{_datadir}/services/kaccess.desktop
%{_datadir}/services/ksplash.desktop
%{_datadir}/services/ksplashdefault.desktop
%{_datadir}/services/kxkb.desktop
%{_datadir}/servicetypes/ksplashplugins.desktop
%{_datadir}/sounds/*
%{_datadir}/templates
%{_datadir}/wallpapers/All-Good-People-1.jpg
%{_datadir}/wallpapers/Blkmarble.jpg
%{_datadir}/wallpapers/Chicken-Songs-2.jpg
%{_datadir}/wallpapers/Circuit.jpg
%{_datadir}/wallpapers/Foggy1.jpg
%{_datadir}/wallpapers/Marble01.jpg
%{_datadir}/wallpapers/No-Ones-Laughing-3.jpg
%{_datadir}/wallpapers/Paper01.jpg
%{_datadir}/wallpapers/Planning-And-Probing-1.jpg
%{_datadir}/wallpapers/Time-For-Lunch-2.jpg
%{_datadir}/wallpapers/Totally-New-Product-1.jpg
%{_datadir}/wallpapers/Won-Ton-Soup-3.jpg
%{_datadir}/wallpapers/default_blue.jpg
%{_datadir}/wallpapers/default_gears.jpg
%{_datadir}/wallpapers/fulmine.jpg
%{_datadir}/wallpapers/kde_box.png
%{_datadir}/wallpapers/kde_passion.jpg
#%{_datadir}/wallpapers/kdm_bg.jpg
%{_datadir}/wallpapers/only_k.jpg
%{_datadir}/wallpapers/seaofconero.jpg
%{_datadir}/wallpapers/triplegears.jpg
%{_datadir}/wallpapers/blue-bend.jpg
%{_datadir}/wallpapers/Island-of-Elba.jpg
%{_datadir}/xsessions/kde.desktop
%{_datadir}/applnk/.hidden/battery.desktop
%{_datadir}/applnk/.hidden/bwarning.desktop
%{_datadir}/applnk/.hidden/cwarning.desktop
%{_datadir}/applnk/.hidden/kcmkxmlrpcd.desktop
%{_datadir}/applnk/.hidden/kwinactions.desktop
%{_datadir}/applnk/.hidden/kwinadvanced.desktop
%{_datadir}/applnk/.hidden/kwinfocus.desktop
%{_datadir}/applnk/.hidden/kwinmoving.desktop
%{_datadir}/applnk/.hidden/power.desktop
%{_datadir}/applnk/.hidden/randr.desktop
%{_datadir}/applnk/.hidden/socks.desktop
%{_datadir}/applnk/.hidden/virtualdesktops.desktop
%{_datadir}/applnk/.hidden/xinerama.desktop
%{_desktopdir}/kde/arts.desktop
%{_desktopdir}/kde/background.desktop
%{_desktopdir}/kde/bell.desktop
%{_desktopdir}/kde/componentchooser.desktop
%{_desktopdir}/kde/desktop.desktop
%{_desktopdir}/kde/desktopbehavior.desktop
%{_desktopdir}/kde/desktoppath.desktop
%{_desktopdir}/kde/display.desktop
%{_desktopdir}/kde/email.desktop
%{_desktopdir}/kde/energy.desktop
%{_desktopdir}/kde/kcmaccess.desktop
%{_desktopdir}/kde/kcmlaunch.desktop
%{_desktopdir}/kde/kcmsmserver.desktop
%{_desktopdir}/kde/kcmnotify.desktop
%{_desktopdir}/kde/keyboard.desktop
%{_desktopdir}/kde/keyboard_layout.desktop
%{_desktopdir}/kde/keys.desktop
%{_desktopdir}/kde/khotkeys.desktop
%{_desktopdir}/kde/krandrtray.desktop
%{_desktopdir}/kde/ksplashthememgr.desktop
%{_desktopdir}/kde/ktip.desktop
%{_desktopdir}/kde/kwindecoration.desktop
%{_desktopdir}/kde/kwinoptions.desktop
%{_desktopdir}/kde/mouse.desktop
%{_desktopdir}/kde/passwords.desktop
%{_desktopdir}/kde/privacy.desktop
%{_desktopdir}/kde/spellchecking.desktop
%{_iconsdir}/*/*/apps/access.png
%{_iconsdir}/*/*/apps/acroread.png
%{_iconsdir}/*/*/apps/alevt.png
%{_iconsdir}/*/*/apps/applixware.png
%{_iconsdir}/*/*/apps/arts.png
%{_iconsdir}/*/*/apps/background.png
%{_iconsdir}/*/*/apps/blender.png
%{_iconsdir}/*/*/apps/clanbomber.png
%{_iconsdir}/*/*/apps/designer.png
%{_iconsdir}/*/*/apps/dlgedit.png
%{_iconsdir}/*/*/apps/emacs.png
%{_iconsdir}/*/*/apps/email.png
%{_iconsdir}/*/*/apps/energy_star.png
%{_iconsdir}/*/*/apps/error.png
%{_iconsdir}/*/*/apps/galeon.png
%{_iconsdir}/*/*/apps/gimp.png
#%{_iconsdir}/*/*/apps/gnome_app.png
%{_iconsdir}/*/*/apps/gnome_apps.png
%{_iconsdir}/*/*/apps/gvim.png
%{_iconsdir}/*/*/apps/gv.png
%{_iconsdir}/*/*/apps/kcmdf.png
%{_iconsdir}/*/*/apps/kcmkwm.png
%{_iconsdir}/*/*/apps/kcmmidi.png
%{_iconsdir}/*/*/apps/kdisknav.png
%{_iconsdir}/*/*/apps/keyboard_layout.png
%{_iconsdir}/*/*/apps/keyboard.png
%{_iconsdir}/*/*/apps/khotkeys.png
%{_iconsdir}/*/*/apps/knotify.png
%{_iconsdir}/*/*/apps/ksplash.png
%{_iconsdir}/*/*/apps/ktip.png
%{_iconsdir}/*/*/apps/kvirc.png
%{_iconsdir}/*/*/apps/kwin.png
%{_iconsdir}/*/*/apps/kxkb.png
%{_iconsdir}/*/*/apps/licq.png
%{_iconsdir}/*/*/apps/linuxconf.png
%{_iconsdir}/*/*/apps/lyx.png
%{_iconsdir}/*/*/apps/mathematica.png
%{_iconsdir}/*/*/apps/mozilla.png
%{_iconsdir}/*/*/apps/mozilla_m.png
%{_iconsdir}/*/*/apps/mozilla_mail.png
%{_iconsdir}/*/*/apps/nedit.png
%{_iconsdir}/*/*/apps/netscape.png
%{_iconsdir}/*/*/apps/opera.png
%{_iconsdir}/*/*/apps/password.png
%{_iconsdir}/*/*/apps/penguin.png
%{_iconsdir}/*/*/apps/phppg.png
%{_iconsdir}/*/*/apps/plan.png
%{_iconsdir}/*/*/apps/pybliographic.png
%{_iconsdir}/*/*/apps/pysol.png
%{_iconsdir}/*/*/apps/qtella.png
%{_iconsdir}/*/*/apps/randr.png
%{_iconsdir}/*/*/apps/realplayer.png
%{_iconsdir}/*/*/apps/remote.png
%{_iconsdir}/*/*/apps/soffice.png
%{_iconsdir}/*/*/apps/staroffice.png
%{_iconsdir}/*/*/apps/terminal.png
%{_iconsdir}/*/*/apps/tux.png
%{_iconsdir}/*/*/apps/vnc.png
%{_iconsdir}/*/*/apps/wabi.png
%{_iconsdir}/*/*/apps/window_list.png
%{_iconsdir}/*/*/apps/winprops.png
%{_iconsdir}/*/*/apps/wmaker_apps.png
%{_iconsdir}/*/*/apps/wp.png
%{_iconsdir}/*/*/apps/xapp.png
%{_iconsdir}/*/*/apps/xawtv.png
%{_iconsdir}/*/*/apps/xcalc.png
%{_iconsdir}/*/*/apps/xchat.png
%{_iconsdir}/*/*/apps/xclipboard.png
%{_iconsdir}/*/*/apps/xclock.png
%{_iconsdir}/*/*/apps/xconsole.png
%{_iconsdir}/*/*/apps/xedit.png
%{_iconsdir}/*/*/apps/xemacs.png
%{_iconsdir}/*/*/apps/xeyes.png
%{_iconsdir}/*/*/apps/xfig.png
%{_iconsdir}/*/*/apps/xfmail.png
%{_iconsdir}/*/*/apps/xload.png
%{_iconsdir}/*/*/apps/xmag.png
%{_iconsdir}/*/*/apps/xmms.png
%{_iconsdir}/*/*/apps/xosview.png
%{_iconsdir}/*/*/apps/xpaint.png
%{_iconsdir}/*/*/apps/x.png
%{_iconsdir}/*/*/apps/xv.png

%files desktop-libs
%defattr(644,root,root,755)
%{_libdir}/libkdecorations.la
%attr(755,root,root) %{_libdir}/libkdecorations.so.*.*.*
%{_libdir}/libksplashthemes.la
%attr(755,root,root) %{_libdir}/libksplashthemes.so.*.*.*

%files infocenter -f kinfocenter_en.lang
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/menus/kde-information.menu
%attr(755,root,root) %{_bindir}/kinfocenter
%{_libdir}/kde3/kcm_info.la
%attr(755,root,root) %{_libdir}/kde3/kcm_info.so
%{_libdir}/kde3/kcm_ioslaveinfo.la
%attr(755,root,root) %{_libdir}/kde3/kcm_ioslaveinfo.so
%{_libdir}/kde3/kcm_nic.la
%attr(755,root,root) %{_libdir}/kde3/kcm_nic.so
%{_libdir}/kde3/kcm_samba.la
%attr(755,root,root) %{_libdir}/kde3/kcm_samba.so
%{_libdir}/kde3/kcm_usb.la
%attr(755,root,root) %{_libdir}/kde3/kcm_usb.so
%{_libdir}/kde3/kcm_view1394.la
%attr(755,root,root) %{_libdir}/kde3/kcm_view1394.so
%{_datadir}/apps/kcmusb
%{_datadir}/apps/kinfocenter
%{_xdgdatadir}/kde-information.directory
%{_desktopdir}/kde/devices.desktop
%{_desktopdir}/kde/dma.desktop
%{_desktopdir}/kde/interrupts.desktop
%{_desktopdir}/kde/ioports.desktop
%{_desktopdir}/kde/kcmusb.desktop
%{_desktopdir}/kde/kcmview1394.desktop
%{_desktopdir}/kde/ioslaveinfo.desktop
%{_desktopdir}/kde/memory.desktop
%{_desktopdir}/kde/nic.desktop
%{_desktopdir}/kde/partitions.desktop
%{_desktopdir}/kde/pci.desktop
%{_desktopdir}/kde/processor.desktop
%{_desktopdir}/kde/scsi.desktop
%{_desktopdir}/kde/smbstatus.desktop
%{_desktopdir}/kde/sound.desktop
%{_desktopdir}/kde/xserver.desktop
%{_desktopdir}/kde/kinfocenter.desktop
%{_iconsdir}/*/*/apps/hwinfo.png
%{_iconsdir}/*/*/apps/kcmdevices.png
%{_iconsdir}/*/*/apps/kcmmemory.png
%{_iconsdir}/*/*/apps/kcmpartitions.png
%{_iconsdir}/*/*/apps/kcmpci.png
%{_iconsdir}/*/*/apps/kcmprocessor.png
%{_iconsdir}/*/*/apps/kcmscsi.png
%{_iconsdir}/*/*/apps/kcmsound.png
%{_iconsdir}/*/*/apps/kcmx.png
# !!!
%{_iconsdir}/*/*/apps/kthememgr.png

%files kappfinder
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kappfinder
%{_datadir}/apps/kappfinder
%{_desktopdir}/kde/kappfinder.desktop
%{_iconsdir}/*/*/apps/kappfinder.png

%files kate -f kate_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kate
%{_libdir}/libkdeinit_kate.la
%attr(755,root,root) %{_libdir}/libkdeinit_kate.so
%{_libdir}/kde3/kate.la
%attr(755,root,root) %{_libdir}/kde3/kate.so
%{_libdir}/kde3/katedefaultprojectplugin.la
%attr(755,root,root) %{_libdir}/kde3/katedefaultprojectplugin.so
%dir %{_datadir}/apps/kate
%{_datadir}/apps/kate/[!s]*
%dir %{_datadir}/apps/kate/scripts
%{_datadir}/apps/kate/scripts/*.desktop
%attr(755,root,root) %{_datadir}/apps/kate/scripts/*.sh
%{_datadir}/services/katedefaultproject.desktop
%{_datadir}/servicetypes/kateinitplugin.desktop
%{_datadir}/servicetypes/kateplugin.desktop
%{_datadir}/servicetypes/kateprojectplugin.desktop
%{_desktopdir}/kde/kate.desktop
# konqueror needs it ?
%{_iconsdir}/*/*/apps/kate.png

%files kdcop
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdcop

%files kdeprintfax
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdeprintfax
%dir %{_datadir}/apps/kdeprintfax
%attr(755,root,root) %{_datadir}/apps/kdeprintfax/anytops
%{_datadir}/apps/kdeprintfax/[!a]*
%{_desktopdir}/kde/kdeprintfax.desktop
%{_iconsdir}/*/*/apps/kdeprintfax.png

%files kdialog
%defattr(644,root,root,755)
%doc kdialog/{README,test}
%attr(755,root,root) %{_bindir}/kdialog

%files kfind -f kfind_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfind
%{_desktopdir}/kde/Kfind.desktop
%{_iconsdir}/*/*/apps/kfind.png

%files kfontinst -f kcmfontinst_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfontinst
%{_libdir}/kde3/libkfontviewpart.la
%attr(755,root,root) %{_libdir}/kde3/libkfontviewpart.so
%{_libdir}/kde3/kcm_fontinst.la
%attr(755,root,root) %{_libdir}/kde3/kcm_fontinst.so
%{_libdir}/kde3/kio_fonts.la
%attr(755,root,root) %{_libdir}/kde3/kio_fonts.so
#%{_datadir}/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%dir %{_datadir}/mimelnk/fonts
%{_datadir}/mimelnk/fonts/folder.desktop
%{_datadir}/mimelnk/fonts/system-folder.desktop
%{_datadir}/services/fonts.protocol
%{_datadir}/services/kfontviewpart.desktop
%{_desktopdir}/kde/kcmfontinst.desktop
%{_iconsdir}/[!l]*/*/apps/kcmfontinst.png

%files kicker -f kicker_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kicker
%{_libdir}/libkdeinit_kicker.la
%attr(755,root,root) %{_libdir}/libkdeinit_kicker.so
%{_libdir}/kde3/childpanel_panelextension.la
%attr(755,root,root) %{_libdir}/kde3/childpanel_panelextension.so*
%{_libdir}/kde3/clock_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/clock_panelapplet.so
%{_libdir}/kde3/devices_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/devices_panelapplet.so
%{_libdir}/kde3/dockbar_panelextension.la
%attr(755,root,root) %{_libdir}/kde3/dockbar_panelextension.so
%{_libdir}/kde3/kasbar_panelextension.la
%attr(755,root,root) %{_libdir}/kde3/kasbar_panelextension.so
%{_libdir}/kde3/kcm_clock.la
%attr(755,root,root) %{_libdir}/kde3/kcm_clock.so
%{_libdir}/kde3/kcm_kicker.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kicker.so
%{_libdir}/kde3/kcm_taskbar.la
%attr(755,root,root) %{_libdir}/kde3/kcm_taskbar.so
%{_libdir}/kde3/kicker.la
%attr(755,root,root) %{_libdir}/kde3/kicker.so*
%{_libdir}/kde3/kickermenu_find.la
%attr(755,root,root) %{_libdir}/kde3/kickermenu_find.so
%{_libdir}/kde3/kickermenu_kdeprint.la
%attr(755,root,root) %{_libdir}/kde3/kickermenu_kdeprint.so
%{_libdir}/kde3/kickermenu_konsole.la
%attr(755,root,root) %{_libdir}/kde3/kickermenu_konsole.so
%{_libdir}/kde3/kickermenu_prefmenu.la
%attr(755,root,root) %{_libdir}/kde3/kickermenu_prefmenu.so
%{_libdir}/kde3/kickermenu_recentdocs.la
%attr(755,root,root) %{_libdir}/kde3/kickermenu_recentdocs.so
%{_libdir}/kde3/launcher_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/launcher_panelapplet.so*
%{_libdir}/kde3/lockout_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/lockout_panelapplet.so
%{_libdir}/kde3/menu_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/menu_panelapplet.so
%{_libdir}/kde3/minipager_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/minipager_panelapplet.so
%{_libdir}/kde3/naughty_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/naughty_panelapplet.so
%{_libdir}/kde3/run_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/run_panelapplet.so
%{_libdir}/kde3/systemtray_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/systemtray_panelapplet.so
%{_libdir}/kde3/taskbar_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/taskbar_panelapplet.so
%{_libdir}/kde3/taskbar_panelextension.la
%attr(755,root,root) %{_libdir}/kde3/taskbar_panelextension.so
%{_datadir}/apps/kicker/applets/*.desktop
%{_datadir}/apps/kicker/default-apps
%{_datadir}/apps/kicker/extensions
%{_datadir}/apps/kicker/icons
%{_datadir}/apps/kicker/menuext
%dir %{_datadir}/apps/kicker/pics
%{_datadir}/apps/kicker/pics/disk*.png
%{_datadir}/apps/kicker/tiles
%{_datadir}/apps/kicker/wallpapers
%{_datadir}/apps/naughtyapplet
%{_datadir}/autostart/panel.desktop
%{_datadir}/config/kickerrc
%{_datadir}/applnk/.hidden/kicker_config.desktop
%{_datadir}/applnk/.hidden/kicker_config_appearance.desktop
%{_desktopdir}/kde/kcmtaskbar.desktop
%{_desktopdir}/kde/panel.desktop
%{_desktopdir}/kde/panel_appearance.desktop
%{_desktopdir}/kde/clock.desktop
#%{_desktopdir}/kde/kcmkicker.desktop
%{_iconsdir}/*/*/apps/clock.png
%{_iconsdir}/*/*/apps/date.png
%{_iconsdir}/*/*/apps/go.png
%{_iconsdir}/*/*/apps/kcmkicker.png
%{_iconsdir}/*/*/apps/kicker.png
%{_iconsdir}/*/*/apps/package*.png
%{_iconsdir}/*/*/apps/panel.png
%{_iconsdir}/*/*/apps/panel_settings.png

%files kicker-libs
%defattr(644,root,root,755)
%{_libdir}/libtaskbar.la
%attr(755,root,root) %{_libdir}/libtaskbar.so.*.*.*
%{_libdir}/libtaskmanager.la
%attr(755,root,root) %{_libdir}/libtaskmanager.so.*.*.*

%files kjobviewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjobviewer
%{_libdir}/libkdeinit_kjobviewer.la
%attr(755,root,root) %{_libdir}/libkdeinit_kjobviewer.so
%{_libdir}/kde3/kjobviewer.la
%attr(755,root,root) %{_libdir}/kde3/kjobviewer.so
%{_datadir}/apps/kjobviewer
%{_desktopdir}/kde/kjobviewer.desktop
%{_iconsdir}/*/*/apps/kjobviewer.png

%files klipper -f klipper_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klipper
%{_libdir}/libkdeinit_klipper.la
%attr(755,root,root) %{_libdir}/libkdeinit_klipper.so
%{_libdir}/kde3/klipper.la
%attr(755,root,root) %{_libdir}/kde3/klipper.so
%{_libdir}/kde3/klipper_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/klipper_panelapplet.so
%{_datadir}/autostart/klipper.desktop
%{_datadir}/config/klipperrc
%{_desktopdir}/kde/klipper.desktop
%{_iconsdir}/*/*/apps/klipper.png

%files kmenuedit -f kmenuedit_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmenuedit
%{_libdir}/libkdeinit_kmenuedit.la
%attr(755,root,root) %{_libdir}/libkdeinit_kmenuedit.so
%{_libdir}/kde3/kmenuedit.la
%attr(755,root,root) %{_libdir}/kde3/kmenuedit.so
%{_datadir}/apps/kmenuedit
%{_desktopdir}/kde/kmenuedit.desktop
%{_iconsdir}/*/*/apps/kmenu.png
%{_iconsdir}/*/*/apps/kmenuedit.png

%files konsole -f konsole_en.lang
%defattr(644,root,root,755)
%doc konsole/README*
%attr(755,root,root) %{_bindir}/konsole
%{_libdir}/libkdeinit_konsole.la
%attr(755,root,root) %{_libdir}/libkdeinit_konsole.so
%{_libdir}/kde3/kcm_konsole.la
%attr(755,root,root) %{_libdir}/kde3/kcm_konsole.so
%{_libdir}/kde3/konsole.la
%attr(755,root,root) %{_libdir}/kde3/konsole.so
#%{_datadir}/config/konsolerc
%{_datadir}/services/konsole-script.desktop
%{_datadir}/applnk/.hidden/kcmkonsole.desktop
%{_desktopdir}/kde/konsole*.desktop
%{_iconsdir}/*/*/apps/konsole.png

%files kpager -f kpager_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpager
%{_desktopdir}/kde/kpager.desktop
%{_iconsdir}/*/*/apps/kpager.png

%files kpersonalizer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpersonalizer
%{_datadir}/apps/kpersonalizer
%{_desktopdir}/kde/kpersonalizer.desktop
%{_iconsdir}/*/*/apps/kpersonalizer.png

%files ksysguard -f ksysguard_en.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ksysguarddrc
%attr(755,root,root) %{_bindir}/kpm
%attr(755,root,root) %{_bindir}/ksysguard
%attr(755,root,root) %{_bindir}/ksysguardd
%{_libdir}/kde3/sysguard_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/sysguard_panelapplet.so
%{_datadir}/apps/ksysguard
%{_datadir}/mimelnk/application/x-ksysguard.desktop
%{_desktopdir}/kde/ksysguard.desktop
%{_iconsdir}/*/*/apps/ksysguard.png

%files ksystraycmd
%defattr(644,root,root,755)
%doc ksystraycmd/README
%attr(755,root,root) %{_bindir}/ksystraycmd

#%files kwmtheme -f kthememgr_en.lang
#%defattr(644,root,root,755)
#%attr(0755,root,root) %{_bindir}/kdeinstallktheme
#%attr(0755,root,root) %{_bindir}/kwmtheme
#%{_libdir}/kde3/kcm_themes.la
#%attr(0755,root,root) %{_libdir}/kde3/kcm_themes.so
#%{_libdir}/kde3/kwin_kwmtheme.la
#%attr(0755,root,root) %{_libdir}/kde3/kwin_kwmtheme.so
#%{_datadir}/apps/kthememgr
#%{_datadir}/mimelnk/application/x-ktheme.desktop
#%{_desktopdir}/kde/kthememgr.desktop
#%{_iconsdir}/*/*/apps/kthememgr.png

%files kwrite -f kwrite_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwrite
%attr(755,root,root) %{_bindir}/kwriteconfig
%{_libdir}/libkdeinit_kwrite.la
%attr(755,root,root) %{_libdir}/libkdeinit_kwrite.so
%{_libdir}/kde3/kwrite.la
%attr(755,root,root) %{_libdir}/kde3/kwrite.so
%{_datadir}/apps/kwrite
%{_desktopdir}/kde/kwrite.desktop
%{_iconsdir}/*/*/apps/kwrite.png

%files kwrited
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwrited
%{_libdir}/libkdeinit_kwrited.la
%attr(755,root,root) %{_libdir}/libkdeinit_kwrited.so
%{_libdir}/kde3/kwrited.la
%attr(755,root,root) %{_libdir}/kde3/kwrited.so
%{_datadir}/autostart/kwrited.desktop
%{_datadir}/config/kwritedrc
%{_datadir}/services/kwrited.desktop

%files libkate
%defattr(644,root,root,755)
%{_libdir}/libkateinterfaces.la
%attr(755,root,root) %{_libdir}/libkateinterfaces.so.*.*.*
%{_libdir}/libkateutils.la
%attr(755,root,root) %{_libdir}/libkateutils.so.*.*.*

%files libkickermain
%defattr(644,root,root,755)
%{_libdir}/libkickermain.la
%attr(755,root,root) %{_libdir}/libkickermain.so.*.*.*

%files libkonq
%defattr(644,root,root,755)
%{_libdir}/libkonq.la
%attr(755,root,root) %{_libdir}/libkonq.so.*.*.*
%{_libdir}/kde3/konq_sound.la
%attr(755,root,root) %{_libdir}/kde3/konq_sound.so
%{_libdir}/libkonqsidebarplugin.la
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so.*.*.*

%files libksgrd
%defattr(644,root,root,755)
%{_libdir}/libksgrd.la
%attr(755,root,root) %{_libdir}/libksgrd.so.*.*.*
#%{_libdir}/libsensordisplays.la
#%attr(0755,root,root) %{_libdir}/libsensordisplays.so.*.*.*

%files mailnews
%defattr(644,root,root,755)
%{_libdir}/kde3/kio_imap4.la
%attr(755,root,root) %{_libdir}/kde3/kio_imap4.so
%{_libdir}/kde3/kio_nntp.la
%attr(755,root,root) %{_libdir}/kde3/kio_nntp.so
%{_libdir}/kde3/kio_pop3.la
%attr(755,root,root) %{_libdir}/kde3/kio_pop3.so
%{_libdir}/kde3/kio_smtp.la
%attr(755,root,root) %{_libdir}/kde3/kio_smtp.so
%{_datadir}/services/imap4.protocol
%{_datadir}/services/imaps.protocol
%{_datadir}/services/nntp.protocol
%{_datadir}/services/pop3.protocol
%{_datadir}/services/pop3s.protocol
%{_datadir}/services/smtp.protocol
%{_datadir}/services/smtps.protocol

%files screensavers -f screensaver_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.kss
%{_libdir}/kde3/kcm_screensaver.la
%attr(755,root,root) %{_libdir}/kde3/kcm_screensaver.so
%{_datadir}/apps/kscreensaver
%{_desktopdir}/kde/screensaver.desktop
%{_iconsdir}/*/*/apps/kscreensaver.png

%files -n kdm -f kdm_en.lang
%defattr(644,root,root,755)
%doc README.pam kdm/{ChangeLog,README,TODO}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pam.d/kdm
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/security/blacklist.kdm
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/kdm
%dir %{_sysconfdir}/X11/kdm
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/kdm/kdmrc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/kdm/backgroundrc
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/kdm/Xreset
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/kdm/Xsession
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/kdm/Xsetup
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/kdm/Xstartup
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/kdm/Xwilling
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/kdm/Xaccess
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/kdm/Xservers
%dir %{_sysconfdir}/X11/kdm/faces
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/kdm/faces/.default.face.icon
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/kdm/faces/root.face.icon
%attr(755,root,root) %{_bindir}/genkdmconf
%attr(755,root,root) %{_bindir}/kdm
%attr(755,root,root) %{_bindir}/kdm_config
%attr(755,root,root) %{_bindir}/kdm_greet
%attr(755,root,root) %{_bindir}/krootimage
%{_libdir}/kde3/kcm_kdm.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kdm.so
%{_libdir}/kde3/kgreet_classic.la
%attr(755,root,root) %{_libdir}/kde3/kgreet_classic.so
%{_datadir}/apps/kdm
%{_datadir}/wallpapers/kdm_pld.png
%{_desktopdir}/kde/kdm.desktop
%{_iconsdir}/*/*/apps/kdmconfig.png

%files -n konqueror -f konqueror_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/appletproxy
%attr(755,root,root) %{_bindir}/extensionproxy
%attr(755,root,root) %{_bindir}/keditbookmarks
%attr(755,root,root) %{_bindir}/keditfiletype
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/kio_devices_mounthelper
%attr(755,root,root) %{_bindir}/klocaldomainurifilterhelper
%attr(755,root,root) %{_bindir}/konqueror
%attr(755,root,root) %{_bindir}/nspluginscan
%attr(755,root,root) %{_bindir}/nspluginviewer
%{_libdir}/libkdeinit_appletproxy.la
%attr(755,root,root) %{_libdir}/libkdeinit_appletproxy.so
%{_libdir}/libkdeinit_extensionproxy.la
%attr(755,root,root) %{_libdir}/libkdeinit_extensionproxy.so
%{_libdir}/libkdeinit_keditbookmarks.la
%attr(755,root,root) %{_libdir}/libkdeinit_keditbookmarks.so
%{_libdir}/libkdeinit_kfmclient.la
%attr(755,root,root) %{_libdir}/libkdeinit_kfmclient.so
%{_libdir}/libkdeinit_konqueror.la
%attr(755,root,root) %{_libdir}/libkdeinit_konqueror.so
%{_libdir}/libkonq_sidebar_tree.la
%attr(755,root,root) %{_libdir}/libkonq_sidebar_tree.so
%{_libdir}/kde3/appletproxy.la
%attr(755,root,root) %{_libdir}/kde3/appletproxy.so
%{_libdir}/kde3/libnsplugin.la
%attr(755,root,root) %{_libdir}/kde3/libnsplugin.so
%{_libdir}/kde3/extensionproxy.la
%attr(755,root,root) %{_libdir}/kde3/extensionproxy.so
%{_libdir}/kde3/kcm_cgi.la
%attr(755,root,root) %{_libdir}/kde3/kcm_cgi.so
%{_libdir}/kde3/kcm_crypto.la
%attr(755,root,root) %{_libdir}/kde3/kcm_crypto.so
%{_libdir}/kde3/kcm_css.la
%attr(755,root,root) %{_libdir}/kde3/kcm_css.so
%{_libdir}/kde3/kcm_filetypes.la
%attr(755,root,root) %{_libdir}/kde3/kcm_filetypes.so
%{_libdir}/kde3/kcm_history.la
%attr(755,root,root) %{_libdir}/kde3/kcm_history.so
%{_libdir}/kde3/kcm_icons.la
%attr(755,root,root) %{_libdir}/kde3/kcm_icons.so
%{_libdir}/kde3/kcm_kio.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kio.so
%{_libdir}/kde3/kcm_konq.la
%attr(755,root,root) %{_libdir}/kde3/kcm_konq.so
%{_libdir}/kde3/kcm_konqhtml.la
%attr(755,root,root) %{_libdir}/kde3/kcm_konqhtml.so
%{_libdir}/kde3/kcm_kurifilt.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kurifilt.so
%{_libdir}/kde3/kcm_performance.la
%attr(755,root,root) %{_libdir}/kde3/kcm_performance.so
%{_libdir}/kde3/kded_favicons.la
%attr(755,root,root) %{_libdir}/kde3/kded_favicons.so
%{_libdir}/kde3/kded_konqy_preloader.la
%attr(755,root,root) %{_libdir}/kde3/kded_konqy_preloader.so
%{_libdir}/kde3/kded_mountwatcher.la
%attr(755,root,root) %{_libdir}/kde3/kded_mountwatcher.so
%{_libdir}/kde3/keditbookmarks.la
%attr(755,root,root) %{_libdir}/kde3/keditbookmarks.so
%{_libdir}/kde3/kfile_font.la
%attr(755,root,root) %{_libdir}/kde3/kfile_font.so
%{_libdir}/kde3/kfmclient.la
%attr(755,root,root) %{_libdir}/kde3/kfmclient.so
%{_libdir}/kde3/kio_about.la
%attr(755,root,root) %{_libdir}/kde3/kio_about.so
%{_libdir}/kde3/kio_cgi.la
%attr(755,root,root) %{_libdir}/kde3/kio_cgi.so
%{_libdir}/kde3/kio_devices.la
%attr(755,root,root) %{_libdir}/kde3/kio_devices.so
%{_libdir}/kde3/kio_filter.la
%attr(755,root,root) %{_libdir}/kde3/kio_filter.so
%{_libdir}/kde3/kio_finger.la
%attr(755,root,root) %{_libdir}/kde3/kio_finger.so
%{_libdir}/kde3/kio_fish.la
%attr(755,root,root) %{_libdir}/kde3/kio_fish.so
%{_libdir}/kde3/kio_floppy.la
%attr(755,root,root) %{_libdir}/kde3/kio_floppy.so
%if %{with ldap}
%{_libdir}/kde3/kio_ldap.la
%attr(755,root,root) %{_libdir}/kde3/kio_ldap.so
%endif
%{_libdir}/kde3/kio_mac.la
%attr(755,root,root) %{_libdir}/kde3/kio_mac.so
%{_libdir}/kde3/kio_nfs.la
%attr(755,root,root) %{_libdir}/kde3/kio_nfs.so
%{_libdir}/kde3/kio_print.la
%attr(755,root,root) %{_libdir}/kde3/kio_print.so
%{_libdir}/kde3/kio_sftp.la
%attr(755,root,root) %{_libdir}/kde3/kio_sftp.so
%{_libdir}/kde3/kio_smb.la
%attr(755,root,root) %{_libdir}/kde3/kio_smb.so
%{_libdir}/kde3/kio_tar.la
%attr(755,root,root) %{_libdir}/kde3/kio_tar.so
%{_libdir}/kde3/konq_aboutpage.la
%attr(755,root,root) %{_libdir}/kde3/konq_aboutpage.so
%{_libdir}/kde3/konq_iconview.la
%attr(755,root,root) %{_libdir}/kde3/konq_iconview.so
%{_libdir}/kde3/konq_listview.la
%attr(755,root,root) %{_libdir}/kde3/konq_listview.so
%{_libdir}/kde3/konq_shellcmdplugin.la
%attr(755,root,root) %{_libdir}/kde3/konq_shellcmdplugin.so
%{_libdir}/kde3/konq_sidebar.la
%attr(755,root,root) %{_libdir}/kde3/konq_sidebar.so
%{_libdir}/kde3/konq_sidebartree_bookmarks.la
%attr(755,root,root) %{_libdir}/kde3/konq_sidebartree_bookmarks.so
%{_libdir}/kde3/konq_sidebartree_dirtree.la
%attr(755,root,root) %{_libdir}/kde3/konq_sidebartree_dirtree.so
%{_libdir}/kde3/konq_sidebartree_history.la
%attr(755,root,root) %{_libdir}/kde3/konq_sidebartree_history.so
%{_libdir}/kde3/konqueror.la
%attr(755,root,root) %{_libdir}/kde3/konqueror.so
%{_libdir}/kde3/konqsidebar_tree.la
%attr(755,root,root) %{_libdir}/kde3/konqsidebar_tree.so
%{_libdir}/kde3/konqsidebar_web.la
%attr(755,root,root) %{_libdir}/kde3/konqsidebar_web.so
%{_libdir}/kde3/libkfindpart.la
%attr(755,root,root) %{_libdir}/kde3/libkfindpart.so
%{_libdir}/kde3/libkshorturifilter.la
%attr(755,root,root) %{_libdir}/kde3/libkshorturifilter.so
%{_libdir}/kde3/libkuriikwsfilter.la
%attr(755,root,root) %{_libdir}/kde3/libkuriikwsfilter.so
%{_libdir}/kde3/libkurisearchfilter.la
%attr(755,root,root) %{_libdir}/kde3/libkurisearchfilter.so
%{_libdir}/kde3/liblocaldomainurifilter.la
%attr(755,root,root) %{_libdir}/kde3/liblocaldomainurifilter.so
%{_libdir}/kde3/sidebar_panelextension.la
%attr(755,root,root) %{_libdir}/kde3/sidebar_panelextension.so
%dir %{_libdir}/kde3/plugins/konqueror
%{_datadir}/apps/kbookmark
%{_datadir}/apps/kcmcss
%{_datadir}/apps/keditbookmarks
%{_datadir}/apps/kfindpart
%{_datadir}/apps/kio_finger
%{_datadir}/apps/konqiconview
%{_datadir}/apps/konqlistview
%{_datadir}/apps/konqsidebartng
#%dir %{_datadir}/apps/konqsidebartng
#%{_datadir}/apps/konqsidebartng/add
#%{_datadir}/apps/konqsidebartng/dirtree
#%{_datadir}/apps/konqsidebartng/entries
#%{_datadir}/apps/konqsidebartng/kicker_entries
#%{_datadir}/apps/konqsidebartng/websidebar
#%dir %{_datadir}/apps/konqsidebartng/virtual_folders
#%{_datadir}/apps/konqsidebartng/virtual_folders/remote
#%dir %{_datadir}/apps/konqsidebartng/virtual_folders/services
#%{_datadir}/apps/konqsidebartng/virtual_folders/services/.directory
#%{_datadir}/apps/konqsidebartng/virtual_folders/services/audiocd.desktop
#%{_datadir}/apps/konqsidebartng/virtual_folders/services/devices.desktop
#%{_datadir}/apps/konqsidebartng/virtual_folders/services/lisa.desktop
#%{_datadir}/apps/konqsidebartng/virtual_folders/services/printsystem.desktop
%{_datadir}/apps/konqueror/about
#%{_datadir}/apps/konqueror/dirtree
%{_datadir}/apps/konqueror/icons
%{_datadir}/apps/konqueror/pics
%{_datadir}/apps/konqueror/profiles
%{_datadir}/apps/konqueror/servicemenus/*
%{_datadir}/apps/konqueror/tiles
%{_datadir}/apps/konqueror/konqueror.rc
%{_datadir}/autostart/konqy_preload.desktop
%{_datadir}/config/konqsidebartng.rc
%{_datadir}/config/kshorturifilterrc
%{_datadir}/config/mountwatcher.desktop
%{_datadir}/mimelnk/application/x-smb-workgroup.desktop
%{_datadir}/mimelnk/kdedevice
%{_datadir}/services/searchproviders
%{_datadir}/services/useragentstrings
%{_datadir}/services/about.protocol
%{_datadir}/services/ar.protocol
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
%{?with_ldap:%{_datadir}/services/ldap.protocol}
%{_datadir}/services/localdomainurifilter.desktop
%{_datadir}/services/mac.protocol
%{_datadir}/services/nfs.protocol
%{_datadir}/services/print.protocol
%{_datadir}/services/printdb.protocol
%{_datadir}/services/sftp.protocol
%{_datadir}/services/smb.protocol
%{_datadir}/services/tar.protocol
%{_datadir}/services/zip.protocol
%{_datadir}/servicetypes/findpart.desktop
%{_datadir}/servicetypes/konqaboutpage.desktop
%{_datadir}/servicetypes/konqpopupmenuplugin.desktop
%{_datadir}/servicetypes/searchprovider.desktop
%{_datadir}/servicetypes/uasprovider.desktop
%{_datadir}/applnk/.hidden/fileappearance.desktop
%{_datadir}/applnk/.hidden/filebehavior.desktop
%{_datadir}/applnk/.hidden/filepreviews.desktop
%{_datadir}/applnk/.hidden/kcmkonq.desktop
%{_datadir}/applnk/.hidden/kcmkonqyperformance.desktop
%{_datadir}/applnk/.hidden/konqfilemgr.desktop
%{_datadir}/applnk/.hidden/konqhtml.desktop
%{_datadir}/applnk/.hidden/smb.desktop
# Must be here!
%{_applnkdir}/konqueror.desktop
#
%{_desktopdir}/kde/filebrowser.desktop
%{_desktopdir}/kde/filetypes.desktop
%{_desktopdir}/kde/kcmperformance.desktop
%{_desktopdir}/kde/icons.desktop
%{_desktopdir}/kde/cache.desktop
%{_desktopdir}/kde/cookies.desktop
%{_desktopdir}/kde/ebrowsing.desktop
%{_desktopdir}/kde/kcmcgi.desktop
%{_desktopdir}/kde/kcmcss.desktop
%{_desktopdir}/kde/kcmhistory.desktop
%{_desktopdir}/kde/khtml_behavior.desktop
%{_desktopdir}/kde/khtml_fonts.desktop
%{_desktopdir}/kde/khtml_java_js.desktop
%{_desktopdir}/kde/khtml_plugins.desktop
%{_desktopdir}/kde/useragent.desktop
%{_desktopdir}/kde/lanbrowser.desktop
%{_desktopdir}/kde/netpref.desktop
%{_desktopdir}/kde/proxy.desktop
%{_desktopdir}/kde/crypto.desktop
%{_desktopdir}/kde/Home.desktop
%{_desktopdir}/kde/kfmclient.desktop
%{_desktopdir}/kde/kfmclient_dir.desktop
%{_desktopdir}/kde/kfmclient_html.desktop
%{_desktopdir}/kde/kfmclient_war.desktop
%{_desktopdir}/kde/konqbrowser.desktop
%{_desktopdir}/kde/konquerorsu.desktop
%{_iconsdir}/*/*/apps/agent.png
%{_iconsdir}/*/*/apps/cache.png
%{_iconsdir}/*/*/apps/cookie.png
%{_iconsdir}/*/*/apps/enhanced_browsing.png
%{_iconsdir}/*/*/apps/filetypes.png
%{_iconsdir}/*/*/apps/icons.png
%{_iconsdir}/*/*/apps/iconthemes.png
%{_iconsdir}/*/*/apps/keditbookmarks.png
%{_iconsdir}/*/*/apps/kfm_home.png
%{_iconsdir}/*/*/apps/kfm.png
%{_iconsdir}/*/*/apps/mac.png
%{_iconsdir}/*/*/apps/proxy.png
%{_iconsdir}/*/*/apps/stylesheet.png
