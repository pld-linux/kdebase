# Conditional build:
%bcond_without	ldap	# build without LDAP support
%bcond_without	apidocs	# build without apidocs
#
%define		_state		stable
%define		_ver		3.2.3
%define		qtver		6:3.3.2-5
#%%define		_snap		040110

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
Release:	5
Epoch:		9
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	fd05a338d155610856b06988d8dff117
#Source0:	http://download.kde.org/%{_state}/%{_ver}/src/%{name}-%{_ver}.tar.bz2
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
Source1:	%{name}-kdesktop.pam
Source2:	%{name}-kdm.pam
Source3:	%{name}-kdm.init
Source4:	%{name}-kdm.Xsession
Source6:	%{name}-kdm_pldlogo.png
Source7:	%{name}-kdm_pldwallpaper.png
Source8:	%{name}-searchproviders.tar.bz2
# Source8-md5:	c6d9045d9c99abce93232c7ab231fabb
Source9:	%{name}-colorschemes.tar.bz2
# Source9-md5:	2102f4a5f78f66bb86e5ab81f9ec686d
Source10:	%{name}-servicemenus.tar.bz2
# Source10-md5:	5b113fe35bd3a46de31e451e285e86d3
Source11:	%{name}-sidebarext.tar.bz2
# Source11-md5:	a79489053e6720305d6d989411aaba56
Source12:	http://ep09.pld-linux.org/~adgor/kde/%{name}-splash-Default-PLD-0.2.tar.bz2
# Source12-md5:	24f9c6a4b711be36437639c410b400b2
Source13:	http://ep09.pld-linux.org/~adgor/kde/%{name}-konqsidebartng-PLD-entries-0.1.tar.bz2
# Source13-md5:	c8b947bc3e8a2ac050d9e9548cf585fc
Icon:		kde-icon.xpm
Patch100:	%{name}-branch.diff
Patch0:		%{name}-fontdir.patch
Patch1:		%{name}-kcm_background.patch
Patch2:		%{name}-kdm_utmpx.patch
Patch3:		%{name}-kdmconfig.patch
Patch4:		%{name}-kicker.patch
Patch5:		%{name}-konsole_all.patch
Patch6:		%{name}-nsplugins_dirs.patch
Patch7:		%{name}-startkde.patch
Patch8:		%{name}-kcm_fonts.patch
Patch9:		%{name}-kdesukonsole.patch
Patch10:	%{name}-vcategories.patch
Patch11:	%{name}-screensavers.patch
Patch12:	%{name}-prefmenu.patch
Patch13:	%{name}-session.patch
Patch14:	%{name}-bgdefaults.patch
Patch15:	%{name}-vmenus.patch
Patch16:	kde-common-utmpx.patch
Patch17:	%{name}-fileshareset.patch
Patch18:	%{name}-kio_settings.patch
Patch19:	%{name}-vt-numbers-fix.patch
Patch20:	%{name}-konsole-default-keytab.patch
Patch21:	kde-common-QTDOCDIR.patch
Patch22:	%{name}-svgsupport.patch
Patch23:	%{name}-kwin_delayfocus.patch
BuildRequires:	unsermake >= 040511
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
BuildRequires:	arts-qt-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libsmbclient-devel >= 1:3.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	motif-devel
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	pam-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xcursor-devel
%if %{with apidocs}
BuildRequires:	qt-doc >= %{qtver}
BuildRequires:	doxygen
BuildRequires:	graphviz
%endif
Conflicts:	kdelibs < 9:3.1.94.040110-1
# TODO: sensors
#BuildRequires:	sensors-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	pcre-devel
BuildConflicts:	kdebase-libkickermain
BuildConflicts:	kdebase-libkonq
BuildConflicts:	kdebase-kicker-libs
BuildConflicts:	kdebase-konqueror-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xdgdatadir	%{_datadir}/desktop-directories

%define 	_noautoreqdep			libGL.so.1 libGLU.so.1

%description
This package contains KDE base system which includes:
- KDE Control Centre with modules
- KDesktop (a desktop) and Kicker (a panel)
- KWin window manager and several decorations
- KDE splash themes and plugins
- thumbnail creation, mail, news and terminal emulation support
- many more.

%description -l ja
KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ÍÑ¤Î´ðËÜ¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¡£
°Ê²¼¤Î¤è¤¦¤Ê¥Ñ¥Ã¥±¡¼¥¸¤¬Æþ¤Ã¤Æ¤¤¤Þ¤¹¡£

%description -l pl
Ten pakiet zawiera podstawowe aplikacje KDE:
- Centrum sterowania z modu³ami
- KDesktop (pulpit) i Kicker (panel)
- mened¿er okien Kwin i dekoracje
- ekrany startowe KDE
- obs³ugê podgl±du plików, protoko³ów poczty i news oraz emulacji
  terminala

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
Requires:	%{name}-desktop-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Requires:	%{name}-libksgrd = %{epoch}:%{version}-%{release}
Requires:	konqueror-libs = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= 9:%{version}

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
Group:		Themes
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-b2
A Beos like window decoration with rectangular window title to the
left. The actual window decoration does not take more than 20-30% of
the screen width and if two window titles overlap each other, they are
aligned next to each other.

%description -n kde-decoration-b2 -l pl
Podobna do Beos dekoracja okien z prostok±tnym tytu³em okna po lewej
stronie. Nie zajmuje ona wiêcej ni¿ 20-30% szeroko¶ci ekranu, a w
przypadkach gdyby dwie dekoracje siê zas³ania³y, s± one uk³adane obok
siebie.

%package -n kde-decoration-laptop
Summary:	KDE Window Decoration - Laptop
Summary(pl):	Dekoracja okna dla KDE - Laptop
Group:		Themes
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-laptop
A window decoration with stripped window title and lightly convex
window buttons.

%description -n kde-decoration-laptop -l pl
Dekoracja okna z paskowanym tytu³em okna oraz lekko wypuk³ymi
przyciskami okna.

%package -n kde-decoration-modernsys
Summary:	KDE Window Decoration - ModernSys
Summary(pl):	Dekoracja okna dla KDE - ModernSys
Group:		Themes
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-modernsys
A window decoration with small, top-aligned window buttons and a
window title with gray lines surronding the text of the title. Also
with a convex resize handle on the bottom-right window corner.

%description -n kde-decoration-modernsys -l pl
Dekoracja okna z ma³ymi, wyrównanymi do góry przyciskami okna oraz
tytu³em okna otoczonym szarymi liniami. Ma równie¿ wypuk³y uchwyt
s³u¿±cy do zmiany rozmiaru w prawym dolnym rogu okna.

%package -n kde-decoration-quartz
Summary:	KDE Window Decoration - Quartz
Summary(pl):	Dekoracja okna dla KDE - Quartz
Group:		Themes
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-quartz
A window decoration with solid borders. The window caption consists of
a lighter area for the window title and a darker area for window
buttons. Between the two area there is a stylish transition.

%description -n kde-decoration-quartz -l pl
Dekoracja okna z pe³nymi krawêdziami. Nag³ówek okna sk³ada siê z
jasnego obszaru dla tytu³u okna i ciemniejszego dla przycisków. Miêdzy
obszarami jest stylowy przej¶cie.

%package -n kde-decoration-redmond
Summary:	KDE Window Decoration - Redmond
Summary(pl):	Dekoracja okna dla KDE - Redmond
Group:		Themes
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-redmond
A window decoration resembling the one from Windows 98.

%description -n kde-decoration-redmond -l pl
Dekoracja okna przypominaj±ca tê z Windows 98.

%package -n kde-decoration-web
Summary:	KDE Window Decoration - Web
Summary(pl):	Dekoracja okna dla KDE - Web
Group:		Themes
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-web
A completely flat window decoration with rounded corners and visible,
thin borders.

%description -n kde-decoration-web -l pl
Zupe³nie p³aska dekoracja okna z zaokr±glonymi brzegami oraz
widocznymi, cienkimi krawêdziami.

%package -n kde-kgreet-classic
Summary:	KDE greeter libraries
Summary(pl):	Biblioteki s³u¿±ce do zapytañ o has³o
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Provides:	kde-kgreet
Conflicts:	kdm < 3.2.2-2

%description -n kde-kgreet-classic
Tools for asking for passwords in the classic, default look.

%description -n kde-kgreet-classic -l pl
Narzêdzia s³u¿±ce do zapytañ o has³o - klasyczny, domy¶lny motyw
wygl±du.

%package -n kde-kside-default
Summary:	Default kicker sidebar
Summary(pl):	Domy¶lny boczny pasek do menu KDE
Group:		Themes
Requires:	kdebase-desktop >= 9:%{version}
Provides:	kde-kside

%description -n kde-kside-default
Default kicker sidebar with a gear and the K Desktop Environment text.

%description -n kde-kside-default -l pl
Domy¶lny boczny pasek do menu KDE z turbink± oraz napisem K Desktop
Environment.

%package -n kde-logoutpic-default
Summary:	KDE "Logout" picture
Summary(pl):	Obrazek okna "Wyloguj" KDE
Group:		Themes
Requires:	%{name}-desktop
Provides:	kde-logoutpic
Obsoletes:	kde-logoutpic-PLD

%description -n kde-logoutpic-default
Default "Logout" picture with a KDE logo.

%description -n kde-logoutpic-default -l pl
Standardowy obrazek okna "Wyloguj" z logiem KDE.

%package -n kde-splash-Default-KDE
Summary:	Default clasic KDE splashscreen
Summary(pl):	Domy¶lny klasyczny ekran startowy KDE
Group:		Themes
Requires:	kde-splashplugin-Standard = %{epoch}:%{version}-%{release}

%description -n kde-splash-Default-KDE
Default classic KDE splashscreen with a photo of the KDE team from the
Nove Hrady KDE Conference and standard icons.

%description -n kde-splash-Default-KDE -l pl
Domy¶lny klasyczny ekran startowy KDE ze standardowymi ikonami oraz
fotografi± zespo³u twórców KDE z konferencji w Novych Hradach.

%package -n kde-splash-blue-bend
Summary:	KDE blue-bend splashscreen
Summary(pl):	Ekran startowy KDE blue-bend
Group:		Themes
Requires:	kde-splashplugin-Standard = %{epoch}:%{version}-%{release}

%description -n kde-splash-blue-bend
KDE blue-bend splashscreen.

%description -n kde-splash-blue-bend -l pl
Ekran startowy KDE blue-bend.

%package -n kde-splashplugin-Redmond
Summary:	ksplash plugin Redmond
Summary(pl):	Wtyczka ksplash Redmond
Group:		Themes
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Obsoletes:	kde-splashplugin-XpLike

%description -n kde-splashplugin-Redmond
A splash screen plugin that resembles the Windows XP post login
animations.

%description -n kde-splashplugin-Redmond -l pl
Wtyczka ekranu startowego KDE, podobna do animacji, które w Windows XP
maj± miejsce po zalogowaniu.

%package -n kde-splashplugin-Standard
Summary:	ksplash plugin Standard
Summary(pl):	Wtyczka ksplash Standard
Group:		Themes
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-splashplugin-Standard
A standard splash screen plugin for KDE. It is themable and shows
splashscreens on the center of the screen. The splash themes for this
plugin consist of a main picture and two icon bars that are shown
under it. For every step of the loading process a different icon is
highlighted.

%description -n kde-splashplugin-Standard -l pl
Standardowa wtyczka uruchamiana podczas startu KDE. Obs³uguje motywy i
pokazuje ekrany startowe na ¶rodku ekranu. Motywy startowe dla tej
wtyczki sk³adaj± siê z g³ównego obrazka i dwóch pasków ikon pod nim
pokazywanych. Dla ka¿dego kroku procesu ³adowania pod¶wietlana jest
inna ikona.

%package common-filemanagement
Summary:	Common Files for kate and konqueror
Summary(pl):	Pliki wspólne dla kate i konquerora
Group:		X11/Libraries
Requires:	%{name}-common-konsole = %{epoch}:%{version}-%{release}
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description common-filemanagement
Thumbnail and file sharing libraries for kate and konqueror.

%description common-filemanagement -l pl
Biblioteki s³u¿±ce do tworzenia podgl±du i wymiany plików dla kate i
konquerora.

%package common-konsole
Summary:	Common files for konsole and konsolepart
Summary(pl):	Pliki wspólne dla konsole i konsolepart
Group:		X11/Applications
Requires(post,postun):	fontpostinst
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdebase < 3.0.9-2.4
Obsoletes:	kdebase-fonts

%description common-konsole
Color schemes, icons, fonts and shell profiles for konsole.

%description common-konsole -l pl
Schematy kolorów, ikony, czcionki oraz profile sesji dla konsole.

%package core
Summary:	KDE Core Apps
Summary(pl):	Podstawowe aplikacje KDE
Group:		X11/Applications
Requires:	applnk >= 1.9.0
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdebase < 8:3.2-0.030428.1
Obsoletes:	kdebase-kcontrol
Obsoletes:	kdebase-khelpcenter
Obsoletes:	kdebase-helpcenter

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

%package desktop
Summary:	KDesktop - handling of desktop icons, popup menus etc.
Summary(pl):	KDesktop - obs³uga ikon na pulpicie, menu itp.
Group:		X11/Applications
Provides:	kdebase-kicker
Requires:	kde-logoutpic
Requires:	%{name}-desktop-libs = %{epoch}:%{version}-%{release}
Requires:	konqueror = %{epoch}:%{version}-%{release}
Requires:	kde-kside
Requires:	kde-kgreet
Requires:	%{name}-kfind = %{epoch}:%{version}-%{release}
Requires:	%{name}-kjobviewer = %{epoch}:%{version}-%{release}
Requires:	%{name}-kpager = %{epoch}:%{version}-%{release}
Obsoletes:	kde-theme-keramik
Obsoletes:	kdebase-kwin_plugin
Obsoletes:	kdebase
Obsoletes:	kdebase-fonts
Obsoletes:	kdebase-kcheckpass
Obsoletes:	kdebase-kdesktop
Obsoletes:	kdebase-kdesktop_lock
Obsoletes:	kdebase-khelpcenter
Obsoletes:	kdebase-kicker
Obsoletes:	kdebase-kioslave
Obsoletes:	kdebase-konqueror
Obsoletes:	kdebase-ksystraycmd
Obsoletes:	kdebase-kwin
Obsoletes:	kdebase-kwmtheme
Obsoletes:	kdebase-kxmlrpc
Obsoletes:	kdebase-screensaver
Obsoletes:	kdebase-static
Obsoletes:	kdebase-wallpapers

%description desktop
KDesktop is the program that handles the desktop icons, the popup
menus for the desktop, the mac menubar, and the screensaver system.

%description desktop -l pl
KDesktop to program obs³uguj±cy ikony na pulpicie, menu dla pulpitu,
pasek menu oraz system wygaszacza ekranu.

%package desktop-libs
Summary:	KDesktop libraries
Summary(pl):	Biblioteki KDesktop
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdebase-desktop < 9:3.1.92.031006
Obsoletes:	kdebase-kicker-libs

%description desktop-libs
KDesktop libraries (taskbar, splash themes and window decorations).

%description desktop-libs -l pl
Biblioteki KDesktop (pasek zadañ, obs³uga motywów obrazków startowych
i dekoracji okna).

%package infocenter
Summary:	KDE Info Center
Summary(pl):	Centrum informacji o systemie dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description infocenter
Application for displaying information about your system.

%description infocenter -l pl
Centrum informacji o systemie dla KDE.

%package kappfinder
Summary:	Menu updating tool
Summary(pl):	Narzêdzie do aktualizacji menu
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdebase =< 8:3.2-0.030418.2

%description kappfinder
The tool for finding installed application and adding them to your
menu.

%description kappfinder -l pl
Narzêdzie do wyszukiwania zainstalowanych aplikacji i dodawania ich do
menu.

%package kate
Summary:	KDE Advanced Text Editor
Summary(pl):	Zaawansowany edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-common-filemanagement = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Obsoletes:	kate

%description kate
KDE advanced text editor featuring among others:
- fast opening/editing of files even the big ones (opens a 50MB file
  in a few seconds)
- powerful syntaxhighlighting engine, extensible via XML files
- Code Folding capabilities for C++, C, PHP and more
- Dynamic Word Wrap - long lines are wrapped at the window border on
  the fly for better overview
- multiple views allows you to view more instances of the same
  document and/or more documents at one time
- support for different encodings globally and at write time
- built in dockable terminal emulation
- sidebars with a list of open documents, a directory viewer with a
  directory chooser, a filter chooser and more
- a plugin interface to allow third party plugins
- a "Filter" command allows you to run selected text through a shell
  command

%description kate -l pl
Kate (KDE advanced text editor) to zaawansowany edytor tekstu KDE o
mo¿liwo¶ciach obejmuj±cych m.in.:
- szybkie otwieranie i edycjê nawet du¿ych plików (otwiera plik 50MB w
  parê sekund)
- potê¿ny silnik pod¶wietlania sk³adni, rozszerzalny za pomoc± plików
  XML
- mo¿liwo¶æ zwijania kodu dla C++, C, PHP i innych jêzyków
- dynamiczne zawijanie wierszy - d³ugie linie s± zawijane na granicy
  okna w locie dla lepszej widoczno¶ci
- wiele widoków pozwalaj±cych ogl±daæ wiêcej instancji tego samego
  dokumentu i/lub wiêcej dokumentów w tym samym czasie
- obs³ugê ró¿nych kodowañ globalnie i w czasie zapisu
- wbudowan± emulacjê dokowalnego terminala
- paski z list± otwartych dokumentów, przegl±darkê katalogów z
  mo¿liwo¶ci± wybierania katalogu i filtrów
- interfejs wtyczek obs³uguj±cy zewnêtrzne wtyczki
- polecenie "Filtr" pozwalaj±ce przepuszczaæ zaznaczony tekst przez
  polecenie pow³oki

%package kdeprintfax
Summary:	KDE Fax Tool
Summary(pl):	Narzêdzie do faksowania dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	efax
Requires:	enscript

%description kdeprintfax
Support for sending faxes via the KDE print system.

%description kdeprintfax -l pl
Wsparcie wysy³ania faksów dla systemu drukowania KDE.

%package kdcop
Summary:	Graphic DCOP browser/client
Summary(pl):	Graficzna przegladarka/klient DCOP
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase-desktop < 9:3.1.91.030911

%description kdcop
Graphic DCOP browser/client. Actually useful only for developers and
very advanced users.

%description kdcop -l pl
Graficzna przegl±darka/klient DCOP. Przydatna g³ównie developerom i
bardzo zaawansowanym u¿ytkownikom.

%package kdialog
Summary:	A KDE version of dialog
Summary(pl):	Wersja KDE dialogu
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdebase < 8:3.2-0.030423.2

%description kdialog
Kdialog allows to display window dialogs with KDE widgets from shell
scripts.

%description kdialog -l pl
Kdialog umo¿liwia wy¶wietlanie komunikatów w okienkach KDE z poziomu
skryptów pow³oki.

%package kfind
Summary:	KDE Find Tool
Summary(pl):	Narzêdzie do wyszukiwania plików dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	kfind

%description kfind
A tool for find files for KDE.

%description kfind -l pl
Narzêdzie do wyszukiwania plików dla KDE.

%package kfontinst
Summary:	K Font Installer
Summary(pl):	Instalator fontów dla KDE
Group:		X11/Applications
#Requires:	konqueror = %{epoch}:%{version}-%{release}
Requires:	kdebase-core = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase-desktop < 3.1.90.030720

%description kfontinst
KDE font installer.

%description kfontinst -l pl
Instalator czcionek dla KDE.

%package kjobviewer
Summary:	Print Job Viewer
Summary(pl):	Podgl±d zadañ drukowania
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description kjobviewer
KDE print queue viewer.

%description kjobviewer -l pl
Przegl±darka kolejki drukowania dla KDE.

%package klipper
Summary:	Clipboard Tool
Summary(pl):	Narzêdzie schowka
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description klipper
A tool extending the clipboard support for KDE. Note that it requires
a powerful computer.

%description klipper -l pl
Narzêdzie rozszerzaj±ce obs³ugê schowka dla KDE. Wymaga ono szybkiego
systemu.

%package kmenuedit
Summary:	Menu Editor
Summary(pl):	Edytor menu
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description kmenuedit
KDE menu editor.

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
KDE terminal emulator.

%description konsole -l pl
Emulator terminala dla KDE.

%package kpager
Summary:	Desktop Pager
Summary(pl):	Prze³±cznik biurek
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdebase =< 8:3.2-0.030418.2

%description kpager
KDE desktop pager.

%description kpager -l pl
Prze³±cznik biurek dla KDE.

%package kpersonalizer
Summary:	KDE desktop settings wizard
Summary(pl):	Kreator ustawieñ ¶rodowiska KDE
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Requires:	%{name}-klipper = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase < 9:3.1.92.031021

%description kpersonalizer
KDE desktop settings wizard.

%description kpersonalizer -l pl
Kreator ustawieñ ¶rodowiska KDE.

%package ksysguard
Summary:	System Guard
Summary(pl):	Stra¿nik systemu
Group:		X11/Applications
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-libksgrd = %{epoch}:%{version}-%{release}

%description ksysguard
A system monitoring tool (CPU load, memory usage, etc.).

%description ksysguard -l pl
Narzêdzie do monitorowania systemu (wykorzystania procesora, pamiêci,
itp.).

%package kwrite
Summary:	KDE Text Editor
Summary(pl):	Edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Obsoletes:	kwrite

%description kwrite
KWrite is a simple texteditor, with syntaxhighlighting, codefolding,
dynamic word wrap and more, it's the lightweight version of Kate,
providing more speed for minor tasks.

%description kwrite -l pl
KWrite to prosty edytor tekstu z pod¶wietlaniem sk³adni, zwijaniem
kodu, dynamicznym zawijaniem wierszy itp. Jest l¿ejsz± wersj± Kate,
szybsz± dla mniejszych zadañ.

%package kwrited
Summary:	KDE write messaging daemon
Summary(pl):	Demon do KDE obs³uguj±cy wymianê wiadomo¶ci za pomoc± write
Group:		X11/Applications
# With functional reasons
Requires:	kdebase-core = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase < 8:3.2-0.030423.1

%description kwrited
A kde daeomn that watches for messages from local users sent with
write or wall.

%description kwrited -l pl
Demon KDE, który monitoruje wiadomo¶ci jakie lokalni u¿ytkownicy
wysy³aj± za pomoc± komend write lub wall.

%package libkate
Summary:	A libraries for KDE text editors
Summary(pl):	Biblioteki dla edytorów tekstu KDE
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdebase-kate < 8:3.2-0.030423.1
Obsoletes:	kdebase-libkmultitabbar

%description libkate
A libraries shared between KDE text editors. They provide an
embeddable kate interface.

%description libkate -l pl
Biblioteki wspó³dzielone miêdzy edytorami tekstu w KDE. Dostarczaj±
interfejs kate, który mo¿na osadzaæ w innych aplikacjach.

%package libksgrd
Summary:	ksgrd library
Summary(pl):	Biblioteka ksgrd
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= 9:%{version}
Obsoletes:	ksysguard < 9:3.1.92.031012

%description libksgrd
A library containing functions for the system monitor KSysGuard.

%description libksgrd -l pl
Biblioteka zawieraj±ce funkcje monitora systemu - KSysGuard.

%package mailnews
Summary:	KDE Mail and News Services
Summary(pl):	Obs³uga protoko³ów pocztowych i news dla KDE
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdebase < 8:3.0.9-2.4
Obsoletes:	kdebase-kioslave

%description mailnews
KDE Mail (ex. POP3 and IMAP) and News (NNTP) protocols support.

%description mailnews -l pl
Obs³uga protoko³ów pocztowych (np. POP3 and IMAP) i news (NNTP) dla
KDE.

%package screensavers
Summary:	KDE screensavers
Summary(pl):	Wygaszacze ekranu desktopu KDE
Summary(ru):	ÈÒÁÎÉÔÅÌÉ ÜËÒÁÎÁ ÄÌÑ KDE
Summary(uk):	ÚÂÅÒ¦ÇÁÞ¦ ÅËÒÁÎÕ ÄÌÑ KDE
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description screensavers
KDE screensavers.

%description screensavers -l pl
Wygaszacze ekranu dla KDE.

%description screensavers -l ru
îÅËÏÔÏÒÙÅ 3D ÈÒÁÎÉÔÅÌÉ ÜËÒÁÎÁ ÄÌÑ K Desktop Environment.

%package -n kdm
Summary:	KDE Display Manager
Summary(pl):	Zarz±dca ekranów KDE
Group:		X11/Applications
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	pam
Requires:	sessreg
Requires:	xinitrc-ng
Requires:	kde-kgreet
Obsoletes:	gdm
Obsoletes:	kdebase-kdm
Obsoletes:	kdebase-pam
Obsoletes:	xdm

%description -n kdm
A program used for managing X11 sessions on local or remote computers.
Also provides graphical login method.

%description -n kdm -l pl
Program s³u¿±cy do zarz±dzania zarówno lokalnymi jak i zdalnymi
sesjami X11. Udostêpnia tak¿e graficzny tryb logowania.

%package -n konqueror
Summary:	Konqueror - web browser and file manager
Summary(pl):	Konqueror - przegl±darka WWW i zarz±dca plików
Group:		X11/Applications
Requires:	%{name}-common-filemanagement = %{epoch}:%{version}-%{release}
Requires:	konqueror-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase-konqueror
Obsoletes:	kdebase-libkmultitabbar

%description -n konqueror
Konqueror is the file manager for the K Desktop Environment. It
supports basic file management on local UNIX filesystems, from simple
cut/copy and paste operations to advanced remote and local network
file browsing.

Konqueror is the canvas for all the latest KDE technology, from KIO
slaves (which provide mechanisms for file access) to component
embedding via the KParts object interface, and it is one of the most
customizable applications available.

Konqueror is an Open Source web browser with HTML4.0 compliance,
supporting Java applets, JavaScript, CSS1 and (partially) CSS2, as
well as Netscape plugins (for example, Flash or RealVideo plugins).

Konqueror is a universal viewing application, capable of embedding
read-only viewing components in itself to view documents without ever
launching another application.

%description -n konqueror -l pl
Konqueror to zarz±dca plików dla ¶rodowiska KDE. Obs³uguje podstawowe
zarz±dzanie plikami w lokalnych uniksowych systemach plików, od
prostych operacji wycinania/kopiowania i wklejania do zaawansowanego
przegl±dania plików z sieci zdalnych i lokalnych.

Konqueror to podstawa dla wszystkich nowych technologii KDE, od us³ug
KIO (dostarczaj±cych mechanizmy dostêpu do plików) po osadzanie
komponentów poprzez interfejs obiektowy KParts i jest jedn± z
najbardziej poddaj±cych siê dostosowaniu do w³asnych potrzeb
dostêpnych aplikacji.

Konqueror jest tak¿e przegl±dark± WWW o otwartych ¼ród³ach, zgodn± z
HTML 4.0, obs³uguj±c± aplety Javy, JavaScript, CSS1 i (czê¶ciowo)
CSS2, a tak¿e wtyczki Netscape'a (na przyk³ad Flash i RealAudio).

Konqueror jest uniwersaln± aplikacj± do przegl±dania, umo¿liwiaj±c±
osadzenie w niej komponentów do przegl±dania aby ogl±daæ dokumenty bez
uruchamiania innej aplikacji.

%package -n konqueror-libs
Summary:	konqueror shared libraries
Summary(pl):	Biblioteki wspó³dzielone konquerora
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdebase-libkickermain
Obsoletes:	kdebase-libkonq
Obsoletes:	kdebase-libkonqsidebarplugin
Obsoletes:	kdebase-konqueror-libs
Obsoletes:	konqueror < 9:3.1.92.031006

%description -n konqueror-libs
Konqueror shared libraries.

%description -n konqueror-libs -l pl
Biblioteki wspó³dzielone konquerora.

%package apidocs
Summary:	API documentation
Summary(pl):	Dokumentacja API
Group:		Documentation
Requires:	kdelibs >= 9:3.2.2

%description apidocs
Annotated reference of konqueror,kate,kicker,kcontrol and other
kdebase programming interfaces including:
- class lists
- class members
- namespaces

%description apidocs -l pl
Dokumentacja interfejsów programowania konquerora, kate, kickera,
kcontrol i innych z kdebase z przypisami. Zawiera:
- listy klas i ich sk³adników
- listê przestrzeni nazw (namespace)

%prep
%setup -q -n %{name}-%{version}
%patch100 -p1
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
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

%{__tar} xfj %{SOURCE11} -C konqueror/sidebar/
%{__sed} -i -e "s,trees web_module,trees web_module infobar speedbar,g" \
	konqueror/sidebar/Makefile.am

for f in `find . -name *.desktop | xargs grep -l '^Terminal=[01]'`; do
	%{__sed} -i -e 's/^Terminal=1/Terminal=true/' \
		-e 's/^Terminal=0/Terminal=false/' $f
done
for f in `find . -name *.desktop | xargs grep -l '^Type=Application'`; do
	if ! grep '^Encoding=' $f >/dev/null; then
		%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' $f
	fi
done

%build
cp %{_datadir}/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir} \
	--with-kdm-pam=kdm \
	%{!?with_ldap:--with-ldap=no} \
	--with-pam=kdesktop

%{__make}

%{?with_apidocs:%{__make} apidox}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_libs_htmldir=%{_kdedocdir} \
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
%{__tar} xfj %{SOURCE8} -C $RPM_BUILD_ROOT%{_datadir}/services/searchproviders/
%{__tar} xfj %{SOURCE9} -C $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes/
%{__tar} xfj %{SOURCE10} -C $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/
mv $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/scripts/* $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/scripts

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
mv $RPM_BUILD_ROOT%{_datadir}/applnk/System/kinfocenter.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_desktopdir}/kde/print{ers,mgr}.desktop

# Workaround for gnome menu which maps all these to "Others" dir
cd $RPM_BUILD_ROOT%{_desktopdir}/kde
for f in `grep -El 'X-KDE-settings|X-KDE-information' *`; do
	echo "OnlyShowIn=KDE" >> $f
done
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%post common-filemanagement
cat << EOF

 *********************************************************
 *                                                       *
 * NOTE:                                                 *
 * If You want the directories sharing from the context  *
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

%post	libkate		-p /sbin/ldconfig
%postun	libkate		-p /sbin/ldconfig

%post	-n konqueror-libs	-p /sbin/ldconfig
%postun	-n konqueror-libs	-p /sbin/ldconfig

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

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_kdedocdir}/en/%{name}-apidocs
%endif

%files devel
%defattr(644,root,root,755)
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

%files core
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
%attr(755,root,root) %{_bindir}/iconvert
%attr(755,root,root) %{_bindir}/attach-to-email
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
%{_libdir}/kde3/kcm_icons.la
%attr(755,root,root) %{_libdir}/kde3/kcm_icons.so
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
%{_desktopdir}/kde/icons.desktop
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
%dir %{_kdedocdir}/en/kcontrol
%{_kdedocdir}/en/kcontrol/helpindex.html
%{_kdedocdir}/en/kcontrol/index.*
%{_kdedocdir}/en/kcontrol/*.png
%{_kdedocdir}/en/kcontrol/colors
%{_kdedocdir}/en/kcontrol/fonts
%{_kdedocdir}/en/kcontrol/kcmstyle
%{_kdedocdir}/en/kcontrol/language
%{_kdedocdir}/en/kcontrol/icons
%{_kdedocdir}/en/kdebugdialog
%{_kdedocdir}/en/kdeprint
%{_kdedocdir}/en/kdesu
%{_kdedocdir}/en/khelpcenter



%files desktop
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
%attr(755,root,root) %{_bindir}/krandrinithack
#%attr(755,root,root) %{_bindir}/kwin_dialog_helper
%attr(755,root,root) %{_bindir}/kxkb
%attr(755,root,root) %{_bindir}/startkde
%attr(755,root,root) %{_libdir}/kconf_update_bin/khotkeys_update
%{_libdir}/libkdeinit_krandrinithack.la
%attr(0755,root,root) %{_libdir}/libkdeinit_krandrinithack.so
%{_libdir}/kde3/krandrinithack.la
%attr(755,root,root) %{_libdir}/kde3/krandrinithack.so
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
%{_iconsdir}/crystalsvg/*/actions/newfont.png
%{_iconsdir}/crystalsvg/*/*/abiword.png
%{_iconsdir}/crystalsvg/*/*/assistant.png
%{_iconsdir}/crystalsvg/*/*/bluefish.png
%{_iconsdir}/crystalsvg/*/*/dia.png
%{_iconsdir}/crystalsvg/*/*/eclipse.png
%{_iconsdir}/crystalsvg/*/*/evolution.png
%{_iconsdir}/crystalsvg/*/*/firefox.png
%{_iconsdir}/crystalsvg/*/*/gabber.png
%{_iconsdir}/crystalsvg/*/*/gaim.png
%{_iconsdir}/crystalsvg/*/*/gnomemeeting.png
%{_iconsdir}/crystalsvg/*/*/gnucash.png
%{_iconsdir}/crystalsvg/*/*/gnumeric.png
%{_iconsdir}/crystalsvg/*/*/linguist.png
%{_iconsdir}/crystalsvg/*/*/pan.png
%{_iconsdir}/crystalsvg/*/*/planner.png
%{_iconsdir}/crystalsvg/*/*/scribus.png
%{_iconsdir}/crystalsvg/*/*/sodipodi.png
%{_iconsdir}/crystalsvg/*/*/thunderbird.png
%{_iconsdir}/crystalsvg/*/*/wine.png
%doc ksystraycmd/README
%attr(755,root,root) %{_bindir}/ksystraycmd
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
%{_kdedocdir}/en/kcontrol/arts
%{_kdedocdir}/en/kcontrol/background
%{_kdedocdir}/en/kcontrol/bell
%{_kdedocdir}/en/kcontrol/clock
%{_kdedocdir}/en/kcontrol/desktop
%{_kdedocdir}/en/kcontrol/desktopbehavior
%{_kdedocdir}/en/kcontrol/energy
%{_kdedocdir}/en/kcontrol/kcmaccess
%{_kdedocdir}/en/kcontrol/kcmlaunch
%{_kdedocdir}/en/kcontrol/kcmnotify
%{_kdedocdir}/en/kcontrol/kcmsmserver
%{_kdedocdir}/en/kcontrol/kcmtaskbar
%{_kdedocdir}/en/kcontrol/keyboard
%{_kdedocdir}/en/kcontrol/keys
%{_kdedocdir}/en/kcontrol/kwindecoration
%{_kdedocdir}/en/kicker
%{_kdedocdir}/en/ksplashml
%{_kdedocdir}/en/kxkb
%{_kdedocdir}/en/kcontrol/mouse
%{_kdedocdir}/en/kcontrol/panel
%{_kdedocdir}/en/kcontrol/panelappearance
%{_kdedocdir}/en/kcontrol/passwords
%{_kdedocdir}/en/kcontrol/spellchecking
%{_kdedocdir}/en/kcontrol/windowmanagement

%files desktop-libs
%defattr(644,root,root,755)
%{_libdir}/libkdecorations.la
%attr(755,root,root) %{_libdir}/libkdecorations.so.*.*.*
%{_libdir}/libksplashthemes.la
%attr(755,root,root) %{_libdir}/libksplashthemes.so.*.*.*
%{_libdir}/libtaskbar.la
%attr(755,root,root) %{_libdir}/libtaskbar.so.*.*.*
%{_libdir}/libtaskmanager.la
%attr(755,root,root) %{_libdir}/libtaskmanager.so.*.*.*

%files infocenter
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
%{_kdedocdir}/en/kinfocenter
%{_kdedocdir}/en/kioslave

%files kappfinder
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kappfinder
%{_datadir}/apps/kappfinder
%{_desktopdir}/kde/kappfinder.desktop
%{_iconsdir}/*/*/apps/kappfinder.png

%files kate
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
%{_kdedocdir}/en/kate

%files kdcop
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdcop
%{_datadir}/apps/kdcop

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

%files kfind
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfind
%{_desktopdir}/kde/Kfind.desktop
%{_iconsdir}/*/*/apps/kfind.png
%{_kdedocdir}/en/kfind

%files kfontinst
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
%{_kdedocdir}/en/kcontrol/kcmfontinst

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

%files klipper
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
%{_kdedocdir}/en/klipper

%files kmenuedit
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
%{_kdedocdir}/en/kmenuedit

%files konsole
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
%{_kdedocdir}/en/kcontrol/kcmkonsole
%{_kdedocdir}/en/konsole

%files kpager
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpager
%{_desktopdir}/kde/kpager.desktop
%{_iconsdir}/*/*/apps/kpager.png
%{_kdedocdir}/en/kpager

%files kpersonalizer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpersonalizer
%{_datadir}/apps/kpersonalizer
%{_desktopdir}/kde/kpersonalizer.desktop
%{_iconsdir}/*/*/apps/kpersonalizer.png

%files ksysguard
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
%{_kdedocdir}/en/ksysguard

%files -n konqueror-libs
%defattr(644,root,root,755)
%{_libdir}/libkickermain.la
%attr(755,root,root) %{_libdir}/libkickermain.so.*.*.*
%{_libdir}/libkonq.la
%attr(755,root,root) %{_libdir}/libkonq.so.*.*.*
%{_libdir}/kde3/konq_sound.la
%attr(755,root,root) %{_libdir}/kde3/konq_sound.so
%{_libdir}/libkonqsidebarplugin.la
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so.*.*.*

#%files kwmtheme
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

%files kwrite
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
%{_kdedocdir}/en/kwrite

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

%files screensavers
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.kss
%{_libdir}/kde3/kcm_screensaver.la
%attr(755,root,root) %{_libdir}/kde3/kcm_screensaver.so
%{_datadir}/apps/kscreensaver
%{_desktopdir}/kde/screensaver.desktop
%{_iconsdir}/*/*/apps/kscreensaver.png
%{_kdedocdir}/en/kcontrol/screensaver

%files -n kde-kgreet-classic
%defattr(644,root,root,755)
%{_libdir}/kde3/kgreet_classic.la
%attr(0755,root,root) %{_libdir}/kde3/kgreet_classic.so

%files -n kdm
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
%{_datadir}/apps/kdm
%{_datadir}/wallpapers/kdm_pld.png
%{_desktopdir}/kde/kdm.desktop
%{_iconsdir}/*/*/apps/kdmconfig.png
%{_kdedocdir}/en/kdm
%{_kdedocdir}/en/kcontrol/kdm

%files -n konqueror
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
%{_libdir}/kde3/konqsidebar_speedbar.la
%attr(755,root,root) %{_libdir}/kde3/konqsidebar_speedbar.so
%{_libdir}/kde3/konqsidebar_ksidebar.la
%attr(755,root,root) %{_libdir}/kde3/konqsidebar_ksidebar.so
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
%{_datadir}/applnk/konqueror.desktop
#
%{_desktopdir}/kde/filebrowser.desktop
%{_desktopdir}/kde/filetypes.desktop
%{_desktopdir}/kde/kcmperformance.desktop
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
%{_kdedocdir}/en/konqueror
%{_kdedocdir}/en/kcontrol/cache
%{_kdedocdir}/en/kcontrol/cookies
%{_kdedocdir}/en/kcontrol/crypto
%{_kdedocdir}/en/kcontrol/ebrowsing
%{_kdedocdir}/en/kcontrol/email
%{_kdedocdir}/en/kcontrol/filemanager
%{_kdedocdir}/en/kcontrol/filetypes
%{_kdedocdir}/en/kcontrol/kcmcss
%{_kdedocdir}/en/kcontrol/khtml
%{_kdedocdir}/en/kcontrol/netpref
%{_kdedocdir}/en/kcontrol/proxy
%{_kdedocdir}/en/kcontrol/smb
%{_kdedocdir}/en/kcontrol/useragent
