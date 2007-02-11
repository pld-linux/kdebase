# TODO:
# - Look at kdm and possibilities of using it with:
#   * sun's secure rpc (--with-rpcauth)
#   * builting console (--with-kdm-xconsole)
#   * afs support (--with afs)
# - fix kerberos support (kdm segfaults)
# - warning: Installed (but unpackaged) file(s) found:
#   /etc/xdg/menus/kde-screensavers.menu
#
# Conditional build:
%bcond_without	apidocs		# Do not prepare API documentation
%bcond_without	ldap		# build or not ldap ioslave
%bcond_with	kerberos5	# kerberos 5 support
%bcond_without	hidden_visibility	# pass '--fvisibility=hidden' & '--fvisibility-inlines-hidden' to g++
%bcond_with	groupwindows	# raise all windows belonging to program together
#
%define		_state		stable
%define		_minlibsevr	9:%{version}

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
Version:	3.5.6
Release:	6
Epoch:		9
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	a53f589f58012e655a52220a6a151019
Source1:	%{name}-kdesktop.pam
Source2:	%{name}-kdm.pam
Source3:	%{name}-kdm-np.pam
Source4:	%{name}-kdm.init
Source5:	%{name}-kdm.Xsession
Source6:	%{name}-kdm_pldlogo.png
Source7:	%{name}-kdm_pldwallpaper.png
Source8:	%{name}-searchproviders.tar.bz2
# Source8-md5:	582b29204e85c01a91799ed72f845312
Source10:	%{name}-servicemenus.tar.bz2
# Source10-md5:	f48ac7af286f4c87961de4bb24d07772
Source13:	ftp://ftp.pld-linux.org/software/kde/%{name}-konqsidebartng-PLD-entries-0.1.tar.bz2
# Source13-md5:	c8b947bc3e8a2ac050d9e9548cf585fc
# Temporary taken from kde svn
Patch100:	%{name}-branch.diff
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-fontdir.patch
# http://www.icefox.net/articles/kdeosx/grouplayer.diff
Patch2:		%{name}-grouplayer.patch
Patch3:		%{name}-kdm_utmpx.patch
Patch4:		%{name}-kdmconfig.patch
Patch5:		%{name}-kicker.patch
Patch7:		%{name}-nsplugins_dirs.patch
Patch8:		%{name}-startkde.patch
Patch9:		%{name}-kcm_fonts.patch
Patch10:	%{name}-kdesukonsole.patch
Patch12:	%{name}-screensavers.patch
Patch13:	%{name}-prefmenu.patch
Patch14:	%{name}-session.patch
Patch16:	%{name}-vmenus.patch
Patch18:	%{name}-kio_settings.patch
Patch19:	%{name}-konsole-default-keytab.patch
Patch20:	%{name}-seesar.patch
Patch21:	%{name}-konsole-wordseps.patch
Patch22:	%{name}-tango.patch
Patch24:	kde-ac260-lt.patch
Patch25:	%{name}-konsole-history_clear.patch
Patch26:	%{name}-kdm-default_background.patch
BuildRequires:	OpenEXR-devel >= 1.4.0.a
BuildRequires:	OpenGL-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cups-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	db-devel
BuildRequires:	dbus-qt-devel >= 0.70
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	ed
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gettext-devel
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	hal-devel
%{?with_kerberos5:BuildRequires: heimdal-devel}
BuildRequires:	jasper-devel
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libraw1394-devel >= 1.2.0
BuildRequires:	libsmbclient-devel >= 1:3.0.23d-3
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libusb-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	lm_sensors-devel
BuildRequires:	motif-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
%{?with_hidden_visibility:BuildRequires:	qt-devel >= 6:3.3.5.051113-1}
%{?with_apidocs:BuildRequires:	qt-doc}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.356
BuildRequires:	sed >= 4.0
#BuildRequires:	unsermake >= 040511
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel
BuildRequires:	xorg-util-imake
BuildConflicts:	kdebase-konqueror-libs
Conflicts:	kdelibs < 9:3.1.94.040110-1
# TODO: sensors
#BuildRequires:	sensors-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xdgdatadir	%{_datadir}/desktop-directories
# openexr detection fails
%undefine	configure_cache

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
Summary(pl):	Pliki nag³ówkowe potrzebne do tworzenia aplikacji KDE
Summary(pt_BR):	Arquivos de inclusão para compilar aplicativos que usem bibliotecas do kdebase
Group:		X11/Development/Libraries
Requires:	%{name}-desktop-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-kfontinst = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Requires:	%{name}-libksgrd = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= %{_minlibsevr}
Obsoletes:	kdebase-ksysguard-libs

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

%package -n kde-decoration-keramik
Summary:	KDE Window Decoration - keramik
Summary(pl):	Dekoracja okna dla KDE - keramik
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Conflicts:	kdebase-desktop < 9:3.3.91

%description -n kde-decoration-keramik
KDE Window Decoration - keramik.

%description -n kde-decoration-keramik -l pl
Dekoracja okna dla KDE - keramik.

%package -n kde-decoration-laptop
Summary:	KDE Window Decoration - Laptop
Summary(pl):	Dekoracja okna dla KDE - Laptop
Group:		X11/Amusements
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
Group:		X11/Amusements
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
Group:		X11/Amusements
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
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-redmond
A window decoration resembling the one from Windows 98.

%description -n kde-decoration-redmond -l pl
Dekoracja okna przypominaj±ca tê z Windows 98.

%package -n kde-decoration-web
Summary:	KDE Window Decoration - Web
Summary(pl):	Dekoracja okna dla KDE - Web
Group:		X11/Amusements
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
Requires:	kdelibs >= %{_minlibsevr}
Provides:	kde-kgreet
Conflicts:	kdm <= 3.2.90.040503-1

%description -n kde-kgreet-classic
Tools for asking for passwords in the classic, default look.

%description -n kde-kgreet-classic -l pl
Narzêdzia s³u¿±ce do zapytañ o has³o - klasyczny, domy¶lny motyw
wygl±du.

%package -n kde-kgreet-winbind
Summary:	KDE greeter libraries
Summary(pl):	Biblioteki s³u¿±ce do zapytañ o has³o
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Provides:	kde-kgreet
Conflicts:	kdm <= 3.2.90.040503-1

%description -n kde-kgreet-winbind
Tools for asking for passwords - winbind.

%description -n kde-kgreet-winbind -l pl
Narzêdzia s³u¿±ce do zapytañ o has³o - winbind.

%package -n kde-kio-ldap
Summary:	KDE LDAP protocol service
Summary(pl):	Obs³uga protoko³u LDAP
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Conflicts:	konqueror < 9:3.2.90.040210

%description -n kde-kio-ldap
KDE LDAP protocol service.

%description -n kde-kio-ldap -l pl
Obs³uga protoko³u LDAP.

%package -n kde-kio-nntp
Summary:	KDE NNTP protocol service
Summary(pl):	Obs³uga protoko³u NNTP
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase-mailnews

%description -n kde-kio-nntp
KDE NNTP protocol service.

%description -n kde-kio-nntp -l pl
Obs³uga protoko³u NNTP.

%package -n kde-kio-pop3
Summary:	KDE POP3 protocol service
Summary(pl):	Obs³uga protoko³u POP3
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase-mailnews

%description -n kde-kio-pop3
KDE POP3 protocol service.

%description -n kde-kio-pop3 -l pl
Obs³uga protoko³u POP3.

%package -n kde-kio-smtp
Summary:	KDE SMTP protocol service
Summary(pl):	Obs³uga protoko³u SMTP
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase-mailnews

%description -n kde-kio-smtp
KDE SMTP protocol service.

%description -n kde-kio-smtp -l pl
Obs³uga protoko³u SMTP.

%package -n kde-kside-default
Summary:	Default kicker sidebar
Summary(pl):	Domy¶lny boczny pasek do menu KDE
Group:		Themes
Requires:	kdebase-desktop >= 9:3.2.90.040424-2
Provides:	kde-kside
Obsoletes:	kde-kside

%description -n kde-kside-default
Default kicker sidebar with a gear and the K Desktop Environment text.

%description -n kde-kside-default -l pl
Domy¶lny boczny pasek do menu KDE z turbink± oraz napisem K Desktop
Environment.

%package -n kde-logoutpic-default
Summary:	KDE "Logout" picture
Summary(pl):	Obrazek okna "Wyloguj" KDE
Group:		X11/Amusements
Requires:	%{name}-desktop
Provides:	kde-logoutpic
Obsoletes:	kde-logoutpic-PLD

%description -n kde-logoutpic-default
Default "Logout" picture with a KDE logo.

%description -n kde-logoutpic-default -l pl
Standardowy obrazek okna "Wyloguj" z logiem KDE.

%package -n kde-splash-Default
Summary:	Default clasic KDE splashscreen
Summary(pl):	Domy¶lny klasyczny ekran startowy KDE
Group:		X11/Amusements
# DONT PUT STRICT R: HERE
Requires:	%{name}-desktop >= %{epoch}:%{version}-%{release}
# Because of incorrectly added strict deps there
Obsoletes:	kde-splash-Default-KDE

%description -n kde-splash-Default
Default splashscreen that came with this version of KDE.

%description -n kde-splash-Default -l pl
Domy¶lny ekran powitalny dostarczony w tej wersji KDE.

%package -n kde-splash-blue-bend
Summary:	KDE blue-bend splashscreen
Summary(pl):	Ekran powitalny KDE blue-bend
Group:		X11/Amusements
# DONT PUT STRICT R: HERE
Requires:	%{name}-desktop >= %{epoch}:%{version}-%{release}

%description -n kde-splash-blue-bend
KDE blue-bend splashcreen.

%description -n kde-splash-blue-bend -l pl
Ekran powitalny KDE blue-bend.

%package -n kde-splashplugin-Redmond
Summary:	ksplash plugin Redmond
Summary(pl):	Wtyczka ksplash Redmond
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Obsoletes:	kde-splashplugin-XpLike

%description -n kde-splashplugin-Redmond
A splash screen plugin that resembles the Windows XP post login
animations.

%description -n kde-splashplugin-Redmond -l pl
Wtyczka ekranu powitalnego KDE, podobna do animacji, które w Windows
XP maj± miejsce po zalogowaniu.

%package -n kde-splashplugin-Standard
Summary:	ksplash plugin Standard
Summary(pl):	Wtyczka ksplash Standard
Group:		X11/Amusements
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
Requires:	kdelibs >= %{_minlibsevr}
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
Requires:	kdelibs >= %{_minlibsevr}
Requires:	sudo
Requires:	xdg-menus
Obsoletes:	kdebase < 8:3.2-0.030428.1
Obsoletes:	kdebase-helpcenter
Obsoletes:	kdebase-kcontrol
Obsoletes:	kdebase-khelpcenter
Conflicts:	kttsd <= 040609

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
Requires:	%{name}-desktop-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-kdialog = %{epoch}:%{version}-%{release}
Requires:	%{name}-kfind = %{epoch}:%{version}-%{release}
Requires:	%{name}-kjobviewer = %{epoch}:%{version}-%{release}
Requires:	%{name}-kpager = %{epoch}:%{version}-%{release}
Requires:	eject
Requires:	kde-kgreet
Requires:	kde-kside
Requires:	kde-logoutpic
Requires:	kde-splash-Default
Requires:	konqueror = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.99.7.1
Provides:	kdebase-kicker
Obsoletes:	kde-decoration-plastik
Obsoletes:	kde-theme-keramik
Obsoletes:	kdebase
Obsoletes:	kdebase-fonts
Obsoletes:	kdebase-kcheckpass
Obsoletes:	kdebase-kdesktop
Obsoletes:	kdebase-kdesktop_lock
Obsoletes:	kdebase-khelpcenter
Obsoletes:	kdebase-kicker
Obsoletes:	kdebase-kioslave
Obsoletes:	kdebase-kmenuedit
Obsoletes:	kdebase-konqueror
Obsoletes:	kdebase-ksystraycmd
Obsoletes:	kdebase-kwin
Obsoletes:	kdebase-kwin_plugin
Obsoletes:	kdebase-kwmtheme
Obsoletes:	kdebase-kxmlrpc
Obsoletes:	kdebase-screensaver
Obsoletes:	kdebase-static
Obsoletes:	kdebase-wallpapers
Obsoletes:	khotkeys
Conflicts:	kdeedu-libkdeeduui < 8:3.4.0

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
Requires:	konqueror-libs = %{epoch}:%{version}-%{release}
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
Requires:	pciutils

%description infocenter
Application for displaying information about your system.

%description infocenter -l pl
Centrum informacji o systemie dla KDE.

%package kappfinder
Summary:	Menu Updating Tool
Summary(pl):	Narzêdzie do aktualizacji menu
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
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
Conflicts:	kttsd <= 040609

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
Requires:	kdelibs >= %{_minlibsevr}
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
# for /usr/share/doc/kde/HTML/en/kcontrol, probably stupid
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
Summary(pl):	Prze³±cznik biurek
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase =< 8:3.2-0.030418.2

%description kpager
KDE Desktop Pager.

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
KDE System Guard.

%description ksysguard -l pl
Stra¿nik systemu dla KDE.

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
Requires:	kdelibs >= %{_minlibsevr}
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
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase-ksysguard-libs
Obsoletes:	ksysguard < 9:3.1.92.031012

%description libksgrd
A library containing functions for the system monitor KSysGuard.

%description libksgrd -l pl
Biblioteka zawieraj±ce funkcje monitora systemu - KSysGuard.

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
Wygaszacze ekranu desktopu KDE.

%description screensavers -l ru
îÅËÏÔÏÒÙÅ 3D ÈÒÁÎÉÔÅÌÉ ÜËÒÁÎÁ ÄÌÑ K Desktop Environment.

%package useraccount
Summary:	User Account
Summary(pl):	Konto u¿ytkownika
Group:		X11/Applications
Obsoletes:	kdeutils-kdepasswd
Obsoletes:	kdeutils-userinfo

%description useraccount
useraccount changes user account information. This module contains
kdepasswd program functionality.

%description useraccount -l pl
useraccount zmienia informacje o koncie u¿ytkownika. Ten modu³ zawiera
funkcjonalno¶æ programu kdepasswd.

%package -n kdm
Summary:	KDE Display Manager
Summary(pl):	Zarz±dca ekranów KDE
Group:		X11/Applications
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	kde-kgreet
Requires:	pam >= 0.99.7.1
Requires:	rc-scripts
Requires:	xorg-app-sessreg
Obsoletes:	X11-xdm
Obsoletes:	entrance
Obsoletes:	gdm
Obsoletes:	kdebase-kdm
Obsoletes:	kdebase-pam
Obsoletes:	slim
Obsoletes:	wdm
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
Requires:	browser-plugins >= 2.0
Requires:	konqueror-libs = %{epoch}:%{version}-%{release}
Provides:	wwwbrowser
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
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase-konqueror-libs
Obsoletes:	kdebase-libkickermain
Obsoletes:	kdebase-libkonq
Obsoletes:	kdebase-libkonqsidebarplugin
Obsoletes:	konqueror < 9:3.1.92.031006

%description -n konqueror-libs
Konqueror shared libraries.

%description -n konqueror-libs -l pl
Biblioteki wspó³dzielone konquerora.

%package apidocs
Summary:	API documentation
Summary(pl):	Dokumentacja API
Group:		Documentation
Requires:	kdelibs >= 9:3.2.90

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
%setup -q
%patch100 -p0
%patch0 -p1
%patch1 -p1
%{?with_groupwindows:%patch2 -p1}
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
# Outdated but some things
# must be revised (AA default settings)
#%patch9 -p1
%patch10 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch16 -p1
%patch18 -p1
# FIXME (still needed?)
#%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p0
%patch24 -p1
%patch25 -p1
%patch26 -p1

cd kcontrol/ebrowsing/plugins/ikws/searchproviders
for i in  google*.desktop
do
	url=`grep 'Query=' $i|sed -e 's,google.com,google.pl,g'|cut -c 7-`
	echo "Query[pl]=${url}" >> $i
done
cd -

%{__sed} -i -e 's/Categories=.*/Categories=Audio;Mixer;/' \
	kappfinder/apps/Multimedia/alsamixergui.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Audio;Recorder;/' \
	kappfinder/apps/Multimedia/rezound.desktop \
	kappfinder/apps/Multimedia/sweep.desktop \
	kappfinder/apps/Multimedia/audacity.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Office;PDA;/' \
	kappfinder/apps/Utilities/xgnokii.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;TerminalEmulator;/' \
	konsole/konsole-script.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;TerminalEmulator;/' \
	konsole/konsole.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Amusement;/' \
	ksplashml/ksplash.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;System;Monitor;/' \
	ksysguard/gui/ksysguard.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Settings;/' \
	kcontrol/kcontrol/KControl.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;X-KDE-settings-desktop;/' \
	kcontrol/konq/desktoppath.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;TrayIcon;/' \
	kcontrol/randr/krandrtray.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;X-Help;/' \
	-e 's/Name=/Name=KDE/g' -e s'/Name[pl]=Pomoc/Name[pl]=Pomoc KDE/g' \
	-e 's/OnlyShowIn=KDE;//g' khelpcenter/Help.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;/' \
	-e 's/OnlyShowIn=KDE;//g' kfind/Kfind.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;SystemSetup;/' \
	konqueror/konquerorsu.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;SystemSetup;/' \
	konsole/konsolesu.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Network;WebBrowser;/' \
	konqueror/konqbrowser.desktop
%{__sed} -i -e 's/\(^Categories=.*$\)/\1;/' kioslave/media/kcmodule/media.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

cp /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%{__sed} -i -e 's#krb5/##g' configure* */configure* */*.c */*/*.c

%build
%if %{with apidocs}
	if [ ! -f "%{_kdedocdir}/en/common/kde-common.css" ]; then
		echo "ERROR: Building kdebase with apidocs requires kdelibs"
		echo "	   to be installed _without_ excluding documentation."
		exit 1
	fi
%endif

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--disable-final \
	%{?with_hidden_visibility:--enable-gcc-hidden-visibility} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-distribution="PLD Linux Distribution" \
	--with-kdm-pam=kdm \
	--with-pam=kdesktop \
	--with-openexr \
	--with-qt-libraries=%{_libdir} \
	--with%{!?with_kerberos5:out}-krb5auth \
	--without-java \
	%{!?with_ldap:--without-ldap}



%{__make}

%{?with_apidocs:%{__make} apidox}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf *.lang

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d \
	$RPM_BUILD_ROOT/etc/{X11/kdm/faces,pam.d,rc.d/init.d,security} \
	$RPM_BUILD_ROOT%{_libdir}/kde3/plugins/konqueror \
	$RPM_BUILD_ROOT%{_datadir}/apps/kate/{scripts,plugins}

%browser_plugins_add_browser konqueror -p %{_libdir}/kde3/plugins/konqueror

if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/en/%{name}-%{version}-apidocs" ] ; then
	mv -f $RPM_BUILD_ROOT{%{_kdedocdir}/en/%{name}-%{version}-apidocs,%{_kdedocdir}/en/%{name}-apidocs}
fi

# Drop generated Xsession file (we have own one)
rm -f $RPM_BUILD_ROOT/etc/X11/kdm/Xsession

# Install miscleanous PLD files
install %{SOURCE1}	$RPM_BUILD_ROOT/etc/pam.d/kdesktop
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/kdm
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/pam.d/kdm-np
install %{SOURCE4}	$RPM_BUILD_ROOT/etc/rc.d/init.d/kdm
install %{SOURCE5}	$RPM_BUILD_ROOT/etc/X11/kdm/Xsession
install %{SOURCE6}	$RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/pldlogo.png
install %{SOURCE7}	$RPM_BUILD_ROOT%{_datadir}/wallpapers/kdm_pld.png

%{__tar} xfj %{SOURCE8} -C $RPM_BUILD_ROOT%{_datadir}/services/searchproviders/
%{__tar} xfj %{SOURCE10} -C $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/
mv $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/scripts/* $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/scripts
%{__tar} xfj %{SOURCE13} -C $RPM_BUILD_ROOT%{_datadir}/apps/konqsidebartng/virtual_folders/

# Needed for pam support
touch $RPM_BUILD_ROOT/etc/security/blacklist.kdm

# Copying default faces to kdm config dir
cp $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/default1.png \
	$RPM_BUILD_ROOT/etc/X11/kdm/faces/.default.face.icon
cp $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/root1.png \
	$RPM_BUILD_ROOT/etc/X11/kdm/faces/root.face.icon

# konqueror/dirtree no longer supported
rm $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/dirtree/remote/smb-network.desktop

# Workaround for gnome menu which maps all these to "Others" dir
cd $RPM_BUILD_ROOT%{_desktopdir}/kde
for f in $(grep -El 'X-KDE-settings|X-KDE-information' *); do
	echo "OnlyShowIn=KDE" >> $f
done
cd -

# find_lang
> core.lang
programs="
colors
fonts
kcmstyle
kdebugdialog
kdeprint
kdesu
khelpcenter
knetattach
kompmgr
language
"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> core.lang
	rm -f $i.lang
done

> %{name}.lang
programs="
arts
background
bell
clock
desktop
desktopbehavior
energy
kcmaccess
kcmlaunch
kcmnotify
kcmsmserver
kcmtaskbar
keyboard
keys
kicker
kmenuedit
ksplashml
kwindecoration
kxkb
mouse
panel
panelappearance
passwords
performance
spellchecking
windowmanagement
"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> %{name}.lang
	rm -f $i.lang
done

%find_lang konqueror	--with-kde
programs="
cache
cookies
crypto
ebrowsing
email
filemanager
filetypes
icons
kcmcss
khtml
netpref
proxy
smb
useragent
"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> konqueror.lang
	rm -f $i.lang
done

%find_lang kappfinder	--with-kde
%find_lang kate		--with-kde
%find_lang kcmkonsole	--with-kde
%find_lang kdm		--with-kde
%find_lang kfind	--with-kde
%find_lang kcmfontinst	--with-kde
%find_lang kdcop	--with-kde
%find_lang kinfocenter	--with-kde
%find_lang kioslave	--with-kde
%find_lang klipper	--with-kde
%find_lang konsole	--with-kde
%find_lang ksysguard	--with-kde
%find_lang kpager	--with-kde
%find_lang kwrite	--with-kde
%find_lang screensaver	--with-kde
cat kcmkonsole.lang	>> konsole.lang
rm -f kcmkonsole.lang
cat kioslave.lang	>> kinfocenter.lang
rm -f kioslave.lang

# Omit apidocs entries
sed -i 's/.*apidocs.*//' *.lang

if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/en/%{name}-%{version}-apidocs" ] ; then
	mv -f $RPM_BUILD_ROOT%{_kdedocdir}/en/%{name}-{%{version}-,}apidocs
fi

rm -f $RPM_BUILD_ROOT/etc/X11/kdm/README
rm -f $RPM_BUILD_ROOT%{_docdir}/kdm/README
rm -f $RPM_BUILD_ROOT%{_desktopdir}/kde/kcmkicker.desktop # see r1.328
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Internet/keditbookmarks.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Settings/LookNFeel/Themes/iconthemes.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Settings/LookNFeel/kcmtaskbar.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Settings/LookNFeel/panel.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Settings/LookNFeel/panel_appearance.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Settings/WebBrowsing/khtml_appearance.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Settings/WebBrowsing/nsplugin.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Settings/WebBrowsing/smb.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/System/kappfinder.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/System/kmenuedit.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/System/kpersonalizer.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Toys/ktip.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/kpager.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/fonts/override/fonts.dir
rm -f $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/app-defaults/*.ad # dunno. not packaged
# apparently in applnk package
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-development-translation.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-development-webdevelopment.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-development.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-editors.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-edutainment.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-games-arcade.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-games-board.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-games-card.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-games-kids.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-games-roguelikes.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-games-strategy.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-games.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-graphics.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-internet-terminal.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-internet.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-main.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-more.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-multimedia.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-office.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-science.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-system-screensavers.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-system-terminal.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-system.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-toys.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-unknown.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-utilities-accessibility.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-utilities-desktop.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-utilities-file.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-utilities-peripherals.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-utilities-pim.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-utilities-xutils.directory
rm -f $RPM_BUILD_ROOT%{_datadir}/desktop-directories/kde-utilities.directory

# cleanup *.la
rm $RPM_BUILD_ROOT%{_libdir}/kde3/*.la
rm $RPM_BUILD_ROOT%{_libdir}/libkdeinit_*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post common-konsole
/usr/bin/fontpostinst misc

%postun common-konsole
/usr/bin/fontpostinst misc

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig

%post	desktop-libs	-p /sbin/ldconfig
%postun	desktop-libs	-p /sbin/ldconfig

%post	libkate		-p /sbin/ldconfig
%postun	libkate		-p /sbin/ldconfig

%post	libksgrd	-p /sbin/ldconfig
%postun	libksgrd	-p /sbin/ldconfig

%post	-n konqueror-libs	-p /sbin/ldconfig
%postun	-n konqueror-libs	-p /sbin/ldconfig

%post -n kdm
/sbin/chkconfig --add kdm
if [ -f /var/lock/subsys/kdm ]; then
	%banner kdm -e <<EOF
 ***************************************************
 *                                                 *
 * NOTE:                                           *
 * To make sure that new version of KDM is running *
 * You should restart KDM with:                    *
 * "/sbin/service kdm restart".                    *
 *                                                 *
 * WARNING:                                        *
 * Restarting KDM will terminate any X session     *
 * started by it!                                  *
 *                                                 *
 ***************************************************

EOF
else
	%banner kdm -e <<EOF
Run "/sbin/service kdm start" to start kdm.

EOF
fi

%preun -n kdm
if [ "$1" = "0" ]; then
	%service kdm stop
	/sbin/chkconfig --del kdm
fi

%post -n konqueror
%update_browser_plugins

%postun -n konqueror
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_includedir}/kate
%{_includedir}/ksgrd
%{_includedir}/ksplash
%{_includedir}/kwin
%{_libdir}/libkasbar.la
%attr(755,root,root) %{_libdir}/libkasbar.so
%{_libdir}/libkateinterfaces.la
%attr(755,root,root) %{_libdir}/libkateinterfaces.so
%{_libdir}/libkateutils.la
%attr(755,root,root) %{_libdir}/libkateutils.so
%{_libdir}/libkdecorations.la
%attr(755,root,root) %{_libdir}/libkdecorations.so
%{_libdir}/libkfontinst.la
%attr(755,root,root) %{_libdir}/libkfontinst.so
%{_libdir}/libkhotkeys_shared.la
%attr(755,root,root) %{_libdir}/libkhotkeys_shared.so
%{_libdir}/libkickermain.la
%attr(755,root,root) %{_libdir}/libkickermain.so
%{_libdir}/libkonq.la
%attr(755,root,root) %{_libdir}/libkonq.so
%{_libdir}/libkonqsidebarplugin.la
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so
%{_libdir}/libksgrd.la
%attr(755,root,root) %{_libdir}/libksgrd.so
%{_libdir}/libksplashthemes.la
%attr(755,root,root) %{_libdir}/libksplashthemes.so
%{_libdir}/libtaskbar.la
%attr(755,root,root) %{_libdir}/libtaskbar.so
%{_libdir}/libtaskmanager.la
%attr(755,root,root) %{_libdir}/libtaskmanager.so

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_kdedocdir}/en/%{name}-apidocs
%endif

%files -n kde-decoration-b2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_b2.so
%attr(755,root,root) %{_libdir}/kde3/kwin_b2_config.so
%{_datadir}/apps/kwin/b2.desktop

%files -n kde-decoration-keramik
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_keramik.so
%attr(755,root,root) %{_libdir}/kde3/kwin_keramik_config.so
%{_datadir}/apps/kwin/keramik.desktop

%files -n kde-decoration-laptop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_laptop.so
%{_datadir}/apps/kwin/laptop.desktop

%files -n kde-decoration-modernsys
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_modernsys.so
%attr(755,root,root) %{_libdir}/kde3/kwin_modernsys_config.so
%{_datadir}/apps/kwin/modernsystem.desktop

%files -n kde-decoration-quartz
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_quartz.so
%attr(755,root,root) %{_libdir}/kde3/kwin_quartz_config.so
%{_datadir}/apps/kwin/quartz.desktop

%files -n kde-decoration-redmond
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_redmond.so
%{_datadir}/apps/kwin/redmond.desktop

%files -n kde-decoration-web
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_web.so
%{_datadir}/apps/kwin/web.desktop

%files -n kde-kgreet-classic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kgreet_classic.so

%files -n kde-kgreet-winbind
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kgreet_winbind.so

%if %{with ldap}
%files -n kde-kio-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kio_ldap.so
%{_datadir}/services/ldap.protocol
%{_datadir}/services/ldaps.protocol
%endif

%files -n kde-kio-nntp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kio_nntp.so
%{_datadir}/services/nntp.protocol
%{_datadir}/services/nntps.protocol

%files -n kde-kio-pop3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kio_pop3.so
%{_datadir}/services/pop3.protocol
%{_datadir}/services/pop3s.protocol

%files -n kde-kio-smtp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kio_smtp.so
%{_datadir}/services/smtp.protocol
%{_datadir}/services/smtps.protocol

%files -n kde-kside-default
%defattr(644,root,root,755)
%{_datadir}/apps/kicker/pics/kside*.png

%files -n kde-logoutpic-default
%defattr(644,root,root,755)
%{_datadir}/apps/ksmserver/pics/shutdownkonq.png

%files -n kde-splash-Default
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/Default

%files -n kde-splash-blue-bend
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/blue-bend

%files -n kde-splashplugin-Redmond
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/ksplashredmond.so
%{_datadir}/apps/ksplash/Themes/Redmond
%{_datadir}/services/ksplashredmond.desktop

%files -n kde-splashplugin-Standard
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/ksplashstandard.so
%{_datadir}/apps/ksplash/Themes/Standard
%{_datadir}/apps/ksplash/pics/splash.png
%{_datadir}/services/ksplashstandard.desktop

%files common-filemanagement
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/djvuthumbnail.so
%attr(755,root,root) %{_libdir}/kde3/exrthumbnail.so
%attr(755,root,root) %{_libdir}/kde3/kio_thumbnail.so
%attr(755,root,root) %{_libdir}/kde3/fontthumbnail.so
%attr(755,root,root) %{_libdir}/kde3/htmlthumbnail.so
%attr(755,root,root) %{_libdir}/kde3/imagethumbnail.so
%attr(755,root,root) %{_libdir}/kde3/libkonsolepart.so
%attr(755,root,root) %{_libdir}/kde3/textthumbnail.so
%{_datadir}/services/djvuthumbnail.desktop
%{_datadir}/services/exrthumbnail.desktop
%{_datadir}/services/fontthumbnail.desktop
%{_datadir}/services/htmlthumbnail.desktop
%{_datadir}/services/imagethumbnail.desktop
%{_datadir}/services/konsolepart.desktop
%{_datadir}/services/textthumbnail.desktop
#%{_datadir}/services/picturethumbnail.desktop
%{_datadir}/services/thumbnail.protocol
%{_datadir}/servicetypes/terminalemulator.desktop
%{_datadir}/servicetypes/thumbcreator.desktop

%files common-konsole
%defattr(644,root,root,755)
%{_fontsdir}/misc/console*.gz
%{_datadir}/apps/konsole
%{_datadir}/mimelnk/application/x-konsole.desktop
%{_iconsdir}/[!l]*/*/apps/bell.png
%{_iconsdir}/*/*/apps/key_bindings.png

%files core -f core.lang
%defattr(644,root,root,755)
%lang(en) %dir %{_kdedocdir}/en/kcontrol
%lang(en) %{_kdedocdir}/en/kcontrol/common
%lang(en) %{_kdedocdir}/en/kcontrol/helpindex.html
%lang(en) %{_kdedocdir}/en/kcontrol/index.*
%lang(en) %{_kdedocdir}/en/kcontrol/screenshot.png
%{_sysconfdir}/xdg/menus/applications-merged/kde-essential.menu
%{_sysconfdir}/xdg/menus/kde-settings.menu
%attr(755,root,root) %{_bindir}/drkonqi
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcminit_startup
%attr(755,root,root) %{_bindir}/kcontrol
%attr(755,root,root) %{_bindir}/kdebugdialog
%attr(755,root,root) %{_bindir}/kdesu
%attr(755,root,root) %{_bindir}/khc_indexbuilder
%attr(755,root,root) %{_bindir}/khelpcenter
%attr(755,root,root) %{_bindir}/knetattach
%attr(755,root,root) %{_bindir}/kprinter
%attr(2755,root,root) %{_bindir}/kdesud
%attr(755,root,root) %{_bindir}/multiple-attachments-servicemenu
%attr(755,root,root) %{_libdir}/libkdeinit_kcminit.so
%attr(755,root,root) %{_libdir}/libkdeinit_kcminit_startup.so
%attr(755,root,root) %{_libdir}/libkdeinit_kcontrol.so
%attr(755,root,root) %{_libdir}/libkdeinit_khelpcenter.so
%attr(755,root,root) %{_libdir}/libkdeinit_kprinter.so
%attr(755,root,root) %{_libdir}/kde3/kcm_colors.so
%attr(755,root,root) %{_libdir}/kde3/kcm_fonts.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kded.so
%attr(755,root,root) %{_libdir}/kde3/kcm_style.so
%attr(755,root,root) %{_libdir}/kde3/kcm_locale.so
%attr(755,root,root) %{_libdir}/kde3/kcm_printmgr.so
%attr(755,root,root) %{_libdir}/kde3/kcminit.so
%attr(755,root,root) %{_libdir}/kde3/kcminit_startup.so
%attr(755,root,root) %{_libdir}/kde3/kcontrol.so
%attr(755,root,root) %{_libdir}/kde3/khelpcenter.so
%attr(755,root,root) %{_libdir}/kde3/kio_info.so
%attr(755,root,root) %{_libdir}/kde3/kio_man.so
# Move it to konqueror?
%attr(755,root,root) %{_libdir}/kde3/kio_settings.so
#
%attr(755,root,root) %{_libdir}/kde3/kprinter.so
# Should be moved to kdelibs
%attr(755,root,root) %{_libdir}/kde3/kstyle_keramik_config.so
#
%attr(755,root,root) %{_libdir}/kde3/libkdeprint_part.so
%attr(755,root,root) %{_libdir}/kde3/libkhtmlkttsdplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkmanpart.so
%{_datadir}/apps/drkonqi
%{_datadir}/apps/kcmview1394
%{_datadir}/apps/kcontrol
%{_datadir}/apps/kdeprint/*
%{_datadir}/apps/kdeprint_part
%dir %{_datadir}/apps/kdisplay
%{_datadir}/apps/kdisplay/color-schemes
%{_datadir}/apps/kio_man
%{_datadir}/apps/khelpcenter
%{_datadir}/apps/khtml/kpartplugins/*
%{_datadir}/apps/remoteview
%{_datadir}/apps/systemview
# For apps they store files in applets
%dir %{_datadir}/apps/kicker
%dir %{_datadir}/apps/kicker/applets
#
%dir %{_datadir}/apps/kio_info
%attr(755,root,root) %{_datadir}/apps/kio_info/kde-info2html
%{_datadir}/apps/kio_info/kde-info2html.conf
# For apps they store files in servicemenus
%dir %{_datadir}/apps/konqueror
%dir %{_datadir}/apps/konqueror/servicemenus
#
%{_datadir}/config.kcfg/khelpcenter.kcfg
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
%{_desktopdir}/kde/printers.desktop
%{_desktopdir}/kde/Help.desktop
%{_desktopdir}/kde/KControl.desktop
%{_iconsdir}/*/*/apps/colors.png
%{_iconsdir}/*/*/apps/energy.png
%{_iconsdir}/*/*/apps/fonts.png
%{_iconsdir}/*/*/apps/help_index.png
%{_iconsdir}/*/*/apps/ieee1394.png
%{_iconsdir}/*/*/apps/input_devices_settings.png
%{_iconsdir}/*/*/apps/kcmdrkonqi.png
%{_iconsdir}/*/*/apps/khelpcenter.*
%{_iconsdir}/*/*/apps/knetattach.*
%{_iconsdir}/*/*/apps/kcmsystem.png
%{_iconsdir}/*/*/apps/kcontrol.png
%{_iconsdir}/*/*/apps/locale.png
%{_iconsdir}/*/*/apps/looknfeel.png
%{_iconsdir}/*/*/apps/multimedia.png
%{_iconsdir}/*/*/apps/personal.png
%{_iconsdir}/*/*/apps/pinguin.png
%{_iconsdir}/*/*/apps/printmgr.*
%{_iconsdir}/*/*/apps/style.png
# infocenter & konqueror need it:
%{_iconsdir}/*/*/apps/samba.png
%{_iconsdir}/*/*/apps/usb.png

%files desktop -f kdebase.lang
%defattr(644,root,root,755)
%doc AUTHORS README README.pam
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdesktop
# New
%attr(755,root,root) %{_bindir}/attach-to-email
%attr(755,root,root) %{_bindir}/iconvert
%attr(755,root,root) %{_bindir}/jpegtran-rotate
#
%attr(755,root,root) %{_bindir}/kaccess
%attr(755,root,root) %{_bindir}/kasbar
%attr(755,root,root) %{_bindir}/kapplymousetheme
%attr(755,root,root) %{_bindir}/kcheckpass
%attr(755,root,root) %{_bindir}/kdeeject
%attr(755,root,root) %{_bindir}/kdesktop
%attr(755,root,root) %{_bindir}/kdesktop_lock
%attr(755,root,root) %{_bindir}/kio_media_mounthelper
%attr(755,root,root) %{_bindir}/kwin_killer_helper
%attr(755,root,root) %{_bindir}/khotkeys
%attr(755,root,root) %{_bindir}/krdb
# TODO: move kreadconfig/kwriteconfig to some smaller package,
# for development i don't need big kdebase-desktop, just kreadconfig/kwriteconfig scripts.
# 12.3(kdebase-desktop)+3.4(konqueror)+4(kdebase-core) ~ 20mb!!
%attr(755,root,root) %{_bindir}/kreadconfig
%attr(755,root,root) %{_bindir}/kwriteconfig
%attr(755,root,root) %{_bindir}/krandrtray
%attr(755,root,root) %{_bindir}/ksmserver
%attr(755,root,root) %{_bindir}/ksplash
%attr(755,root,root) %{_bindir}/ksplashsimple
%attr(755,root,root) %{_bindir}/kstart
%attr(755,root,root) %{_bindir}/ktip
%attr(755,root,root) %{_bindir}/ktrash
%attr(755,root,root) %{_bindir}/kwebdesktop
%attr(755,root,root) %{_bindir}/kwin
%attr(755,root,root) %{_bindir}/kwin_rules_dialog
%attr(755,root,root) %{_bindir}/kxkb
%attr(755,root,root) %{_bindir}/startkde
%attr(755,root,root) %{_libdir}/kconf_update_bin/khotkeys_update
%attr(755,root,root) %{_libdir}/kconf_update_bin/kicker-3.4-reverseLayout
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin_update_window_settings
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin_update_default_rules
# New
%attr(755,root,root) %{_bindir}/kbookmarkmerger
%attr(755,root,root) %{_bindir}/kcheckrunning
%attr(755,root,root) %{_bindir}/khc_docbookdig.pl
%attr(755,root,root) %{_bindir}/khc_htdig.pl
%attr(755,root,root) %{_bindir}/khc_htsearch.pl
%attr(755,root,root) %{_bindir}/khc_mansearch.pl
%attr(755,root,root) %{_bindir}/kompmgr
#
%attr(755,root,root) %{_libdir}/libkdeinit_kaccess.so
%attr(755,root,root) %{_libdir}/libkdeinit_kdesktop.so
%attr(755,root,root) %{_libdir}/libkdeinit_khotkeys.so
%attr(755,root,root) %{_libdir}/libkdeinit_ksmserver.so
%attr(755,root,root) %{_libdir}/libkdeinit_kwin.so
%attr(755,root,root) %{_libdir}/libkdeinit_kwin_rules_dialog.so
%attr(755,root,root) %{_libdir}/libkdeinit_kxkb.so
%attr(755,root,root) %{_libdir}/kde3/cursorthumbnail.so
%attr(755,root,root) %{_libdir}/kde3/kaccess.so
%attr(755,root,root) %{_libdir}/kde3/kcm_access.so
%attr(755,root,root) %{_libdir}/kde3/kcm_arts.so
%attr(755,root,root) %{_libdir}/kde3/kcm_background.so
%attr(755,root,root) %{_libdir}/kde3/kcm_bell.so
%attr(755,root,root) %{_libdir}/kde3/kcm_componentchooser.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kdnssd.so
%attr(755,root,root) %{_libdir}/kde3/kcm_display.so
%attr(755,root,root) %{_libdir}/kde3/kcm_energy.so
%attr(755,root,root) %{_libdir}/kde3/kcm_input.so
%attr(755,root,root) %{_libdir}/kde3/kcm_joystick.so
%attr(755,root,root) %{_libdir}/kde3/kcm_keyboard.so
%attr(755,root,root) %{_libdir}/kde3/kcm_keys.so
%attr(755,root,root) %{_libdir}/kde3/kcm_khotkeys.so
%attr(755,root,root) %{_libdir}/kde3/kcm_khotkeys_init.so
%attr(755,root,root) %{_libdir}/kde3/khotkeys_arts.so
%attr(755,root,root) %{_libdir}/kde3/kcm_knotify.so
%attr(755,root,root) %{_libdir}/kde3/kcm_ksplashthemes.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kwindecoration.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kwinoptions.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kwinrules.so
%attr(755,root,root) %{_libdir}/kde3/kcm_launch.so
%attr(755,root,root) %{_libdir}/kde3/kcm_nsplugins.so
%attr(755,root,root) %{_libdir}/kde3/kcm_privacy.so
%attr(755,root,root) %{_libdir}/kde3/kcm_randr.so
%attr(755,root,root) %{_libdir}/kde3/kcm_smserver.so
%attr(755,root,root) %{_libdir}/kde3/kcm_spellchecking.so
%attr(755,root,root) %{_libdir}/kde3/kcm_xinerama.so
%attr(755,root,root) %{_libdir}/kde3/kded_khotkeys.so
%attr(755,root,root) %{_libdir}/kde3/kdesktop.so
%attr(755,root,root) %{_libdir}/kde3/khotkeys.so
%attr(755,root,root) %{_libdir}/kde3/ksmserver.so
%attr(755,root,root) %{_libdir}/kde3/ksplashdefault.so
%attr(755,root,root) %{_libdir}/kde3/kwin.so
%attr(755,root,root) %{_libdir}/kde3/kwin_default_config.so
%attr(755,root,root) %{_libdir}/kde3/kwin_plastik_config.so
%attr(755,root,root) %{_libdir}/kde3/kwin_rules_dialog.so
%attr(755,root,root) %{_libdir}/kde3/kwin3_default.so
%attr(755,root,root) %{_libdir}/kde3/kwin3_plastik.so
%attr(755,root,root) %{_libdir}/kde3/kxkb.so
%attr(755,root,root) %{_libdir}/kde3/kcm_media.so
%attr(755,root,root) %{_libdir}/kde3/kded_medianotifier.so
%attr(755,root,root) %{_libdir}/kde3/kded_homedirnotify.so
%attr(755,root,root) %{_libdir}/kde3/kio_home.so
%{_datadir}/apps/clockapplet
%{_datadir}/apps/kaccess
%{_datadir}/apps/kcm_componentchooser/*
%dir %{_datadir}/apps/kcminput
%{_datadir}/apps/kcminput/cursor*.pcf*
%{_datadir}/apps/kcminput/pics
%{_datadir}/apps/kcmkeys
%{_datadir}/apps/kcmlocale
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.sh
%{_datadir}/apps/kconf_update/*.upd
%{_datadir}/apps/kdesktop
%{_datadir}/apps/kdewizard
# Do not include this!
#%{_datadir}/apps/kdisplay/app-defaults
%{_datadir}/apps/khotkeys
%dir %{_datadir}/apps/ksmserver
%dir %{_datadir}/apps/ksmserver/pics
%dir %{_datadir}/apps/ksplash
%dir %{_datadir}/apps/ksplash/Themes
%dir %{_datadir}/apps/ksplash/pics
%{_datadir}/apps/ksplash/Themes/None
%{_datadir}/apps/ksplash/Themes/Simple
%dir %{_datadir}/apps/kwin
%{_datadir}/apps/kwin/eventsrc
%{_datadir}/apps/kwin/plastik.desktop
%dir %{_datadir}/apps/kwin/pics
%{_datadir}/apps/kwin/pics/*
%dir %{_datadir}/apps/kwin/default_rules
%{_datadir}/apps/kwin/default_rules/fsp_workarounds_1
%{_datadir}/autostart/kdesktop.desktop
%{_datadir}/autostart/khotkeys.desktop
%{_datadir}/autostart/ktip.desktop
%{_datadir}/config/kdesktop_custom_menu1
%{_datadir}/config/kdesktop_custom_menu2
%{_datadir}/config/kxkb_groups
%{_datadir}/config.kcfg/kdesktop.kcfg
%{_datadir}/config.kcfg/keditbookmarks.kcfg
%{_datadir}/config.kcfg/kickerSettings.kcfg
%{_datadir}/config.kcfg/klaunch.kcfg
%{_datadir}/config.kcfg/konq_listview.kcfg
%{_datadir}/config.kcfg/kwebdesktop.kcfg
%{_datadir}/config.kcfg/kwin.kcfg
%{_datadir}/config.kcfg/mediamanagersettings.kcfg
%{_datadir}/services/cursorthumbnail.desktop
%{_datadir}/services/kaccess.desktop
%{_datadir}/services/kded/khotkeys.desktop
%{_datadir}/services/ksplash.desktop
%{_datadir}/services/ksplashdefault.desktop
%{_datadir}/services/kxkb.desktop
%{_datadir}/services/kfile_trash_system.desktop
%{_datadir}/services/media_propsdlgplugin.desktop
%{_datadir}/services/home.protocol
%{_datadir}/services/kded/homedirnotify.desktop
%{_datadir}/services/kded/medianotifier.desktop
%{_datadir}/services/nxfish.protocol
%{_datadir}/servicetypes/ksplashplugins.desktop
%{_datadir}/sounds/*
%{_datadir}/templates
%{_datadir}/wallpapers/All-Good-People-1.jpg
%{_datadir}/wallpapers/Chicken-Songs-2.jpg
%{_datadir}/wallpapers/KDE34.png
%{_datadir}/wallpapers/No-Ones-Laughing-3.jpg
%{_datadir}/wallpapers/Time-For-Lunch-2.jpg
%{_datadir}/wallpapers/Totally-New-Product-1.jpg
%{_datadir}/wallpapers/Won-Ton-Soup-3.jpg
%{_datadir}/wallpapers/default_blue.jpg
%{_datadir}/wallpapers/default_gears.jpg
%{_datadir}/wallpapers/alta-badia.jpg
%{_datadir}/wallpapers/floating-leaves.jpg
%{_datadir}/wallpapers/soft-green.jpg
%{_datadir}/wallpapers/stelvio.jpg
%{_datadir}/wallpapers/sunshine-after-the-rain.jpg
%{_datadir}/wallpapers/seaofconero.jpg
%{_datadir}/wallpapers/triplegears.jpg
%{_datadir}/wallpapers/blue-bend.jpg
%{_datadir}/wallpapers/*.svgz
%{_datadir}/wallpapers/*.desktop
%{_datadir}/xsessions/kde.desktop
%{_datadir}/applnk/.hidden/.directory
%{_datadir}/applnk/.hidden/battery.desktop
%{_datadir}/applnk/.hidden/bwarning.desktop
%{_datadir}/applnk/.hidden/cwarning.desktop
%{_datadir}/applnk/.hidden/email.desktop
%{_datadir}/applnk/.hidden/energy.desktop
%{_datadir}/applnk/.hidden/kcmkxmlrpcd.desktop
%{_datadir}/applnk/.hidden/kicker_config_arrangement.desktop
%{_datadir}/applnk/.hidden/kicker_config_hiding.desktop
%{_datadir}/applnk/.hidden/kicker_config_menus.desktop
%{_datadir}/applnk/.hidden/kwinactions.desktop
%{_datadir}/applnk/.hidden/kwinadvanced.desktop
%{_datadir}/applnk/.hidden/kwinfocus.desktop
%{_datadir}/applnk/.hidden/kwinmoving.desktop
%{_datadir}/applnk/.hidden/kwintranslucency.desktop
%{_datadir}/applnk/.hidden/passwords.desktop
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
%{_desktopdir}/kde/joystick.desktop
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
%{_desktopdir}/kde/kwinrules.desktop
%{_desktopdir}/kde/media.desktop
%{_desktopdir}/kde/mouse.desktop
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
%{_iconsdir}/*/*/apps/ktip.*
%{_iconsdir}/*/*/apps/kvirc.png
%{_iconsdir}/*/*/apps/kwin.png
%{_iconsdir}/*/*/apps/kxkb.png
%{_iconsdir}/*/*/apps/licq.png
%{_iconsdir}/*/*/apps/linuxconf.png
%{_iconsdir}/*/*/apps/lyx.png
%{_iconsdir}/*/*/apps/mathematica.png
%{_iconsdir}/*/*/apps/nedit.png
%{_iconsdir}/*/*/apps/netscape.png
%{_iconsdir}/*/*/apps/opera.png
%{_iconsdir}/*/*/apps/penguin.png
%{_iconsdir}/*/*/apps/phppg.png
%{_iconsdir}/*/*/apps/plan.png
%{_iconsdir}/*/*/apps/pybliographic.png
%{_iconsdir}/*/*/apps/pysol.png
%{_iconsdir}/*/*/apps/qtella.png
%{_iconsdir}/*/*/apps/randr.png
%{_iconsdir}/*/*/apps/realplayer.png
%{_iconsdir}/*/*/apps/remote.png
%{_iconsdir}/*/*/apps/staroffice.png
%{_iconsdir}/*/*/apps/terminal.png
%{_iconsdir}/*/*/apps/tux.png
%{_iconsdir}/*/*/apps/vnc.png
%{_iconsdir}/*/*/apps/wabi.png
%{_iconsdir}/*/*/apps/window_list.png
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
# new
%{_iconsdir}/crystalsvg/*/actions/newfont.png
%{_iconsdir}/crystalsvg/*/apps/abiword.png
%{_iconsdir}/crystalsvg/*/apps/assistant.png
%{_iconsdir}/crystalsvg/*/apps/bluefish.png
%{_iconsdir}/crystalsvg/*/apps/dia.png
%{_iconsdir}/crystalsvg/*/apps/eclipse.png
%{_iconsdir}/crystalsvg/*/apps/edu_*.png
%{_iconsdir}/crystalsvg/*/apps/evolution.png
%{_iconsdir}/crystalsvg/*/apps/gabber.png
%{_iconsdir}/crystalsvg/*/apps/gaim.png
%{_iconsdir}/crystalsvg/*/apps/gnomemeeting.png
%{_iconsdir}/crystalsvg/*/apps/gnucash.png
%{_iconsdir}/crystalsvg/*/apps/gnumeric.png
%{_iconsdir}/crystalsvg/*/apps/linguist.png
%{_iconsdir}/crystalsvg/*/apps/pan.png
%{_iconsdir}/crystalsvg/*/apps/planner.png
%{_iconsdir}/crystalsvg/*/apps/scribus.png
%{_iconsdir}/crystalsvg/*/apps/sodipodi.png
%{_iconsdir}/crystalsvg/*/apps/wine.png
%{_iconsdir}/crystalsvg/scalable/apps
# New
%{_iconsdir}/crystalsvg/*/apps/fifteenpieces.png
%{_iconsdir}/crystalsvg/*/apps/kbinaryclock.png
%{_iconsdir}/crystalsvg/*/apps/runprocesscatcher.png
%{_iconsdir}/crystalsvg/*/apps/systemtray.png
%{_iconsdir}/crystalsvg/*/apps/taskbar.png
%{_iconsdir}/crystalsvg/*/devices/laptop.*
# kcontroledit
%attr(755,root,root) %{_bindir}/kcontroledit
%attr(755,root,root) %{_libdir}/libkdeinit_kcontroledit.so
%attr(755,root,root) %{_libdir}/kde3/kcontroledit.so
%{_datadir}/apps/kcontroledit
# Merged kicker
%attr(755,root,root) %{_bindir}/kicker
%attr(755,root,root) %{_bindir}/ksystraycmd
%attr(755,root,root) %{_libdir}/libkdeinit_kicker.so
%attr(755,root,root) %{_libdir}/kde3/clock_panelapplet.so
%attr(755,root,root) %{_libdir}/kde3/dockbar_panelextension.so
%attr(755,root,root) %{_libdir}/kde3/kasbar_panelextension.so
%attr(755,root,root) %{_libdir}/kde3/kcm_clock.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kicker.so
%attr(755,root,root) %{_libdir}/kde3/kcm_taskbar.so
%attr(755,root,root) %{_libdir}/kde3/kicker.so*
%attr(755,root,root) %{_libdir}/kde3/kickermenu_find.so
%attr(755,root,root) %{_libdir}/kde3/kickermenu_kate.so
%attr(755,root,root) %{_libdir}/kde3/kickermenu_kdeprint.so
%attr(755,root,root) %{_libdir}/kde3/kickermenu_konqueror.so
%attr(755,root,root) %{_libdir}/kde3/kickermenu_konsole.so
%attr(755,root,root) %{_libdir}/kde3/kickermenu_prefmenu.so
%attr(755,root,root) %{_libdir}/kde3/kickermenu_recentdocs.so
%attr(755,root,root) %{_libdir}/kde3/kickermenu_remotemenu.so
%attr(755,root,root) %{_libdir}/kde3/kickermenu_systemmenu.so
%attr(755,root,root) %{_libdir}/kde3/launcher_panelapplet.so*
%attr(755,root,root) %{_libdir}/kde3/lockout_panelapplet.so
%attr(755,root,root) %{_libdir}/kde3/media_panelapplet.so
%attr(755,root,root) %{_libdir}/kde3/media_propsdlgplugin.so
%attr(755,root,root) %{_libdir}/kde3/menu_panelapplet.so
%attr(755,root,root) %{_libdir}/kde3/minipager_panelapplet.so
%attr(755,root,root) %{_libdir}/kde3/naughty_panelapplet.so
%attr(755,root,root) %{_libdir}/kde3/run_panelapplet.so
%attr(755,root,root) %{_libdir}/kde3/systemtray_panelapplet.so
%attr(755,root,root) %{_libdir}/kde3/taskbar_panelapplet.so
%attr(755,root,root) %{_libdir}/kde3/taskbar_panelextension.so
%attr(755,root,root) %{_libdir}/kde3/trash_panelapplet.so
%{_datadir}/apps/kicker/applets/*.desktop
%{_datadir}/apps/kicker/builtins
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
%{_datadir}/applnk/.hidden/kicker_config.desktop
%{_datadir}/applnk/.hidden/kicker_config_appearance.desktop
%{_datadir}/config.kcfg/taskbar.kcfg
%{_datadir}/config.kcfg/launcherapplet.kcfg
%{_desktopdir}/kde/cdinfo.desktop
%{_desktopdir}/kde/kcm_kdnssd.desktop
%{_desktopdir}/kde/kcmtaskbar.desktop
%{_desktopdir}/kde/panel.desktop
%{_desktopdir}/kde/panel_appearance.desktop
%{_desktopdir}/kde/clock.desktop
%{_desktopdir}/kde/knetattach.desktop
%{_iconsdir}/*/*/apps/clock.png
%{_iconsdir}/*/*/apps/date.png
%{_iconsdir}/*/*/apps/kcmkicker.png
%{_iconsdir}/*/*/apps/kicker.png
%{_iconsdir}/*/*/apps/package*.png
%{_iconsdir}/*/*/apps/panel.png
%{_iconsdir}/*/*/apps/panel_settings.png
# kmenuedit part
%attr(755,root,root) %{_bindir}/kmenuedit
%attr(755,root,root) %{_libdir}/libkdeinit_kmenuedit.so
%attr(755,root,root) %{_libdir}/kde3/kmenuedit.so
%{_datadir}/apps/kmenuedit
%{_desktopdir}/kde/kmenuedit.desktop
%{_iconsdir}/*/*/apps/kmenuedit.png
# thememgr is back?
%attr(755,root,root) %{_bindir}/kdeinstallktheme
%attr(755,root,root) %{_libdir}/kde3/kcm_kthememanager.so
%{_datadir}/apps/kthememanager
%{_datadir}/mimelnk/application/x-ktheme.desktop
%{_desktopdir}/kde/installktheme.desktop
%{_desktopdir}/kde/kthememanager.desktop

%files desktop-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkhotkeys_shared.so.*.*.*
%attr(755,root,root) %{_libdir}/libkasbar.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdecorations.so.*.*.*
%attr(755,root,root) %{_libdir}/libksplashthemes.so.*.*.*
# Merged kicker
%attr(755,root,root) %{_libdir}/libtaskbar.so.*.*.*
%attr(755,root,root) %{_libdir}/libtaskmanager.so.*.*.*

%files infocenter -f kinfocenter.lang
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/menus/kde-information.menu
%attr(755,root,root) %{_bindir}/kinfocenter
%attr(755,root,root) %{_libdir}/kde3/kcm_info.so
%attr(755,root,root) %{_libdir}/kde3/kcm_ioslaveinfo.so
%attr(755,root,root) %{_libdir}/kde3/kcm_nic.so
%attr(755,root,root) %{_libdir}/kde3/kcm_samba.so
%attr(755,root,root) %{_libdir}/kde3/kcm_usb.so
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
%{_desktopdir}/kde/opengl.desktop
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
%{_iconsdir}/*/*/apps/kcmopengl.png
# !!!
%{_iconsdir}/*/*/apps/kthememgr.png

%files kappfinder -f kappfinder.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kappfinder
%{_datadir}/apps/kappfinder
%{_desktopdir}/kde/kappfinder.desktop
%{_iconsdir}/*/*/apps/kappfinder.png

%files kate -f kate.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kate
%attr(755,root,root) %{_libdir}/libkdeinit_kate.so
%attr(755,root,root) %{_libdir}/kde3/kate.so
%{_datadir}/apps/kate
%{_datadir}/config/katerc
%{_datadir}/servicetypes/kateplugin.desktop
%{_desktopdir}/kde/kate.desktop
# konqueror needs it ?
%{_iconsdir}/*/*/apps/kate*

%files kdcop -f kdcop.lang
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
%{_iconsdir}/*/*/apps/kdeprintfax.*

%files kdialog
%defattr(644,root,root,755)
%doc kdialog/{README,test}
%attr(755,root,root) %{_bindir}/kdialog

%files kfind -f kfind.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfind
%{_desktopdir}/kde/Kfind.desktop
%{_iconsdir}/*/*/apps/kfind.png

%files kfontinst -f kcmfontinst.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfontinst
%attr(755,root,root) %{_bindir}/kfontview
%attr(755,root,root) %{_libdir}/libkfontinst.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/libkfontviewpart.so
%attr(755,root,root) %{_libdir}/kde3/kcm_fontinst.so
%attr(755,root,root) %{_libdir}/kde3/kio_fonts.so
%{_datadir}/apps/kfontview
%dir %{_datadir}/mimelnk/fonts
%{_datadir}/mimelnk/fonts/folder.desktop
%{_datadir}/mimelnk/fonts/system-folder.desktop
%{_datadir}/mimelnk/fonts/package.desktop
%{_datadir}/services/fonts.protocol
%{_datadir}/services/kfontviewpart.desktop
%{_desktopdir}/kde/kcmfontinst.desktop
%{_desktopdir}/kde/kfontview.desktop

%files kjobviewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjobviewer
%attr(755,root,root) %{_libdir}/libkdeinit_kjobviewer.so
%attr(755,root,root) %{_libdir}/kde3/kjobviewer.so
%{_datadir}/apps/kjobviewer
%{_desktopdir}/kde/kjobviewer.desktop
%{_iconsdir}/*/*/apps/kjobviewer.*

%files klipper -f klipper.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klipper
%attr(755,root,root) %{_libdir}/libkdeinit_klipper.so
%attr(755,root,root) %{_libdir}/kde3/klipper.so
%attr(755,root,root) %{_libdir}/kde3/klipper_panelapplet.so
%{_datadir}/autostart/klipper.desktop
%{_datadir}/config/klipperrc
%{_desktopdir}/kde/klipper.desktop
%{_iconsdir}/*/*/apps/klipper.*

%files konsole -f konsole.lang
%defattr(644,root,root,755)
%doc konsole/README*
%attr(755,root,root) %{_bindir}/konsole
%attr(755,root,root) %{_libdir}/libkdeinit_konsole.so
%attr(755,root,root) %{_libdir}/kde3/kcm_konsole.so
%attr(755,root,root) %{_libdir}/kde3/konsole.so
%{_datadir}/services/konsole-script.desktop
%{_datadir}/applnk/.hidden/kcmkonsole.desktop
%{_desktopdir}/kde/konsole*.desktop
%{_iconsdir}/*/*/apps/konsole.png
%{_iconsdir}/*/*/apps/konsole.svgz

%files kpager -f kpager.lang
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

%files ksysguard -f ksysguard.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ksysguarddrc
%attr(755,root,root) %{_bindir}/kpm
%attr(755,root,root) %{_bindir}/ksysguard
%attr(755,root,root) %{_bindir}/ksysguardd
%attr(755,root,root) %{_libdir}/kde3/sysguard_panelapplet.so
%{_datadir}/apps/ksysguard
%{_datadir}/mimelnk/application/x-ksysguard.desktop
%{_desktopdir}/kde/ksysguard.desktop
%{_iconsdir}/*/*/apps/ksysguard.png

%files kwrite -f kwrite.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwrite
%attr(755,root,root) %{_libdir}/libkdeinit_kwrite.so
%attr(755,root,root) %{_libdir}/kde3/kwrite.so
%{_datadir}/apps/kwrite
%{_desktopdir}/kde/kwrite.desktop
%{_iconsdir}/*/*/apps/kwrite*

%files kwrited
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kded_kwrited.so
%{_datadir}/services/kded/kwrited.desktop
%{_datadir}/services/kwrited.desktop

%files libkate
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkateinterfaces.so.*.*.*
%attr(755,root,root) %{_libdir}/libkateutils.so.*.*.*

%files libksgrd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libksgrd.so.*.*.*

%files screensavers -f screensaver.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.kss
%attr(755,root,root) %{_libdir}/kde3/kcm_screensaver.so
%{_datadir}/apps/kscreensaver
%{_desktopdir}/kde/screensaver.desktop
%{_iconsdir}/*/*/apps/kscreensaver.png

%files useraccount
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdepasswd
%attr(755,root,root) %{_libdir}/kde3/kcm_useraccount.so
%{_datadir}/applnk/.hidden/userinfo.desktop
%{_datadir}/apps/kdm/pics/users/*
%{_datadir}/config.kcfg/kcm_useraccount.kcfg
%{_datadir}/config.kcfg/kcm_useraccount_pass.kcfg
%{_desktopdir}/kde/kcm_useraccount.desktop
%{_desktopdir}/kde/kdepasswd.desktop

%files -n kdm -f kdm.lang
%defattr(644,root,root,755)
%doc README.pam kdm/{ChangeLog,README,TODO}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdm
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdm-np
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.kdm
%attr(754,root,root) /etc/rc.d/init.d/kdm
%dir /etc/X11/kdm
%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/kdmrc
%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/backgroundrc
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xreset
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xsession
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xsetup
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xstartup
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xwilling
%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xaccess
%dir /etc/X11/kdm/faces
%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/faces/.default.face.icon
%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/faces/root.face.icon
%attr(755,root,root) %{_bindir}/genkdmconf
%attr(755,root,root) %{_bindir}/kdm
%attr(755,root,root) %{_bindir}/kdmctl
%attr(755,root,root) %{_bindir}/kdm_config
%attr(755,root,root) %{_bindir}/kdm_greet
%attr(755,root,root) %{_bindir}/krootimage
%attr(755,root,root) %{_libdir}/kde3/kcm_kdm.so
%{_datadir}/apps/kdm
%{_datadir}/wallpapers/kdm_pld.png
%{_desktopdir}/kde/kdm.desktop
%{_iconsdir}/*/*/apps/kdmconfig.png

%files -n konqueror -f konqueror.lang
%defattr(644,root,root,755)

# browser plugins v2
%{_browserpluginsconfdir}/browsers.d/konqueror.*
%config(noreplace) %verify(not md5 mtime size) %{_browserpluginsconfdir}/blacklist.d/konqueror.*.blacklist

%attr(755,root,root) %{_bindir}/appletproxy
%attr(755,root,root) %{_bindir}/extensionproxy
%attr(755,root,root) %{_bindir}/keditbookmarks
%attr(755,root,root) %{_bindir}/keditfiletype
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/kio_system_documenthelper
%attr(755,root,root) %{_bindir}/klocaldomainurifilterhelper
%attr(755,root,root) %{_bindir}/konqueror
%attr(755,root,root) %{_bindir}/nspluginscan
%attr(755,root,root) %{_bindir}/nspluginviewer
%attr(755,root,root) %{_libdir}/libkdeinit_appletproxy.so
%attr(755,root,root) %{_libdir}/libkdeinit_extensionproxy.so
%attr(755,root,root) %{_libdir}/libkdeinit_keditbookmarks.so
%attr(755,root,root) %{_libdir}/libkdeinit_kfmclient.so
%attr(755,root,root) %{_libdir}/libkdeinit_konqueror.so
%attr(755,root,root) %{_libdir}/kde3/appletproxy.so
%attr(755,root,root) %{_libdir}/kde3/extensionproxy.so
%attr(755,root,root) %{_libdir}/kde3/kcm_cgi.so
%attr(755,root,root) %{_libdir}/kde3/kcm_crypto.so
%attr(755,root,root) %{_libdir}/kde3/kcm_css.so
%attr(755,root,root) %{_libdir}/kde3/kcm_filetypes.so
%attr(755,root,root) %{_libdir}/kde3/kcm_history.so
%attr(755,root,root) %{_libdir}/kde3/kcm_icons.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kio.so
%attr(755,root,root) %{_libdir}/kde3/kcm_konq.so
%attr(755,root,root) %{_libdir}/kde3/kcm_konqhtml.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kurifilt.so
%attr(755,root,root) %{_libdir}/kde3/kcm_performance.so
%attr(755,root,root) %{_libdir}/kde3/kded_favicons.so
%attr(755,root,root) %{_libdir}/kde3/kded_konqy_preloader.so
%attr(755,root,root) %{_libdir}/kde3/kded_mediamanager.so
%attr(755,root,root) %{_libdir}/kde3/kded_remotedirnotify.so
%attr(755,root,root) %{_libdir}/kde3/kded_systemdirnotify.so
%attr(755,root,root) %{_libdir}/kde3/keditbookmarks.so
%attr(755,root,root) %{_libdir}/kde3/kfile_font.so
%attr(755,root,root) %{_libdir}/kde3/kfile_media.so
%attr(755,root,root) %{_libdir}/kde3/kfile_trash.so
%attr(755,root,root) %{_libdir}/kde3/kfmclient.so
%attr(755,root,root) %{_libdir}/kde3/kio_about.so
%attr(755,root,root) %{_libdir}/kde3/kio_cgi.so
%attr(755,root,root) %{_libdir}/kde3/kio_filter.so
%attr(755,root,root) %{_libdir}/kde3/kio_finger.so
%attr(755,root,root) %{_libdir}/kde3/kio_fish.so
%attr(755,root,root) %{_libdir}/kde3/kio_floppy.so
%attr(755,root,root) %{_libdir}/kde3/kio_mac.so
%attr(755,root,root) %{_libdir}/kde3/kio_media.so
%attr(755,root,root) %{_libdir}/kde3/kio_nfs.so
%attr(755,root,root) %{_libdir}/kde3/kio_print.so
%attr(755,root,root) %{_libdir}/kde3/kio_remote.so
%attr(755,root,root) %{_libdir}/kde3/kio_sftp.so
%attr(755,root,root) %{_libdir}/kde3/kio_smb.so
%attr(755,root,root) %{_libdir}/kde3/kio_system.so
%attr(755,root,root) %{_libdir}/kde3/kio_tar.so
%attr(755,root,root) %{_libdir}/kde3/kio_trash.so
%attr(755,root,root) %{_libdir}/kde3/konq_aboutpage.so
%attr(755,root,root) %{_libdir}/kde3/konq_iconview.so
%attr(755,root,root) %{_libdir}/kde3/konq_listview.so
%attr(755,root,root) %{_libdir}/kde3/konq_remoteencoding.so
%attr(755,root,root) %{_libdir}/kde3/konq_shellcmdplugin.so
%attr(755,root,root) %{_libdir}/kde3/konq_sidebar.so
%attr(755,root,root) %{_libdir}/kde3/konq_sidebartree_bookmarks.so
%attr(755,root,root) %{_libdir}/kde3/konq_sidebartree_dirtree.so
%attr(755,root,root) %{_libdir}/kde3/konq_sidebartree_history.so
%attr(755,root,root) %{_libdir}/kde3/konq_sound.so
%attr(755,root,root) %{_libdir}/kde3/konqueror.so
%attr(755,root,root) %{_libdir}/kde3/libkfindpart.so
%attr(755,root,root) %{_libdir}/kde3/libkshorturifilter.so
%attr(755,root,root) %{_libdir}/kde3/libkuriikwsfilter.so
%attr(755,root,root) %{_libdir}/kde3/libkurisearchfilter.so
%attr(755,root,root) %{_libdir}/kde3/liblocaldomainurifilter.so
%attr(755,root,root) %{_libdir}/kde3/libnsplugin.so
%attr(755,root,root) %{_libdir}/kde3/sidebar_panelextension.so
%attr(755,root,root) %{_libdir}/kde3/konqsidebar_*.so
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
%{_datadir}/apps/konqueror/icons
%{_datadir}/apps/konqueror/pics
%{_datadir}/apps/konqueror/profiles
%{_datadir}/apps/konqueror/servicemenus/*
%{_datadir}/apps/konqueror/tiles
%{_datadir}/apps/konqueror/konqueror.rc
%{_datadir}/apps/konqueror/konq-simplebrowser.rc
# TODO
%dir %{_datadir}/apps/plugin
%{_datadir}/apps/plugin/nspluginpart.rc
%{_datadir}/autostart/konqy_preload.desktop
%{_datadir}/config/konqsidebartng.rc
%{_datadir}/config/kshorturifilterrc
%{_datadir}/config.kcfg/konqueror.kcfg
%{_datadir}/mimelnk/application/x-smb-server.desktop
%{_datadir}/mimelnk/application/x-smb-workgroup.desktop
%{_datadir}/mimelnk/media
%{_datadir}/mimelnk/inode/system_directory.desktop
%{_datadir}/services/searchproviders
%{_datadir}/services/useragentstrings
%{_datadir}/services/about.protocol
%{_datadir}/services/applications.protocol
%{_datadir}/services/ar.protocol
%{_datadir}/services/bzip.protocol
%{_datadir}/services/bzip2.protocol
%{_datadir}/services/cgi.protocol
%{_datadir}/services/finger.protocol
%{_datadir}/services/fish.protocol
%{_datadir}/services/floppy.protocol
%{_datadir}/services/gzip.protocol
%{_datadir}/services/kded/favicons.desktop
%{_datadir}/services/kded/konqy_preloader.desktop
%{_datadir}/services/kded/mediamanager.desktop
%{_datadir}/services/kded/remotedirnotify.desktop
%{_datadir}/services/kded/systemdirnotify.desktop
%{_datadir}/services/kfile_font.desktop
%{_datadir}/services/kfile_media.desktop
%{_datadir}/services/kfile_trash.desktop
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
%{_datadir}/services/kshorturifilter.desktop
%{_datadir}/services/kuriikwsfilter.desktop
%{_datadir}/services/kurisearchfilter.desktop
%{_datadir}/services/localdomainurifilter.desktop
%{_datadir}/services/mac.protocol
%{_datadir}/services/media.protocol
%{_datadir}/services/nfs.protocol
%{_datadir}/services/print.protocol
%{_datadir}/services/printdb.protocol
%{_datadir}/services/remote.protocol
%{_datadir}/services/sftp.protocol
%{_datadir}/services/smb.protocol
%{_datadir}/services/tar.protocol
%{_datadir}/services/trash.protocol
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
%{_desktopdir}/kde/khtml_filter.desktop
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
%{_iconsdir}/*/*/apps/konqueror.*
%{_iconsdir}/*/*/apps/mac.png
%{_iconsdir}/*/*/apps/proxy.png
%{_iconsdir}/*/*/apps/stylesheet.png

%files -n konqueror-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkickermain.so.*.*.*
%attr(755,root,root) %{_libdir}/libkonq.so.*.*.*
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so.*.*.*
