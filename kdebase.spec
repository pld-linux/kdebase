#
# TODO:
# * KDM: ColorSheme=Default works properly with GUIStyle=KDE only 
# * KDM: Replacing findwm with a better solution (it's in the way)
# * Fixing 48x48 pld applnk-pixmaps scaling (konqsidebar, kicker)
# * Separating kicker, kwin, wtf
#
# Conditional build:
# _without_alsa		- without alsa support
#

%define         _state          snapshots
%define         _ver		3.2
%define         _snap		030411
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
Source2:	kdm.pamd
Source3:	kdm.init
Source4:	kdm.Xsession
Source6:	%{name}-kscreensaver.pam
Source7:	%{name}-kdm.Xservers
Source9:	%{name}-kdm_pldlogo.png
Source10:	%{name}-kdm_pldwallpaper.png
Source11:	ircpld.desktop
Source12:	specs.desktop
Source13:	kabc.desktop
Source14:	kde-settings.menu
Source15:	kde-settings.directory
#
Patch0:		%{name}-fix-mem-leak-in-kfind.patch
# obsoleted
#Patch1:	%{name}-fix-mouse.cpp.patch
Patch2:		%{name}-fontdir.patch
Patch3:		%{name}-kcm_background.patch
Patch4:		%{name}-kdm.daemon_output.patch
Patch5:		%{name}-kdm_utmpx.patch
Patch6:		%{name}-kdmconfig.patch
Patch7:		%{name}-kicker.patch
Patch8:		%{name}-konsole_all.patch
Patch9:		%{name}-nsplugins_dirs.patch
Patch10:	%{name}-startkde.patch
Patch11:        %{name}-kcm_fonts.patch
Patch12:	%{name}-gtkrc.patch
# fix it if You like it
#Patch13:	%{name}-krdb.patch
Patch14:	%{name}-pldcredits.patch
# doesn't work (Makefile.in should be patched too)
#Patch15:	%{name}-searchprov.patch
# rh stuff
Patch16:	%{name}-kicker_nodesktop.patch
Patch17:        %{name}-xfsreload.patch
Patch18:	%{name}-kdesukonsole.patch
Patch19:	%{name}-vroot.patch
# not tested yet
#Patch20:	%{name}-konsolepropfontwidth3.patch
#
Patch21:	%{name}-vcategories.patch
Patch22:	%{name}-screensavers.patch
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
BuildRequires:	qt-devel >= 3.1
BuildRequires:	zlib-devel
# TODO: sensors
#BuildRequires:	sensors-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	applnk >= 1.6
# Old ksplash is obsoleted
#Requires:	kde-splash
#
Requires:       kde-sdscreen
Requires:       kdelibs >= %{version}-%{_kdelibsminrel}
Requires:	%{name}-pam = %{version}-%{release}
Requires:	konqueror = %{version}-%{release}
#
Obsoletes:	%{name}-fonts
Obsoletes:	%{name}-khelpcenter
Obsoletes:	%{name}-screensaver
Obsoletes:	%{name}-kioslave
Obsoletes:	%{name}-konqueror
Obsoletes:	%{name}-kwin
Obsoletes:	%{name}-kxmlrpc
Obsoletes:	%{name}-kdesktop
Obsoletes:	%{name}-wallpapers
Obsoletes:	kde-splash
Obsoletes:	kde-theme-keramik
#
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
- krootwm - module used by KWM and KFM,
- kaudio - audio server for KDE.

%description -l ja
KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ÍÑ¤Î´ðËÜ¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¡£
°Ê²¼¤Î¤è¤¦¤Ê¥Ñ¥Ã¥±¡¼¥¸¤¬Æþ¤Ã¤Æ¤¤¤Þ¤¹¡£

%description -l pl
Pliki specyficzne dla ¶rodowiska KDE i wykorzystywane przez g³ówne
aplikacje KDE. Pakiet zawiera:
- Hierarchiê menu KDE,
- kappfinder - skrypt u³awiaj±cy uruchamianie niektórych programów
  spoza KDE
- krootwm - modu³ wykorzystywany przez kwm i kfm
- kaudio - serwer d¼wiêku dla KDE.

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
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-kate = %{version}-%{release}
Requires:	kdelibs-devel >= %{version}-%{_kdelibsminrel}

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe niezbêdne do programowania aplikacji
KDE.

%description devel -l pt_BR
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos que usem bibliotecas do kdebase.

%package static
Summary:	Include static libraries to develop KDE applications
Summary(pl):	Statyczne biblioteki KDE
Summary(pt_BR):	Bibliotecas estáticas do kdebase
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= %{version}

%description static
This package contains KDE static libraries.

%description static -l pl
Pakiet zawiera statyczne biblioteki KDE.

%description static -l pt_BR
Bibliotecas estáticas do kdebase.

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

#%package -n kde-splash-default
#Summary:	KDE splash screen
#Summary(pl):	Obrazek startowy KDE
#Group:		X11/Amusements
#Provides:	kde-splash
#Requires:	%{name} >= 3.0.3
#Obsoletes:	kde-splash-KDEGirl
#Obsoletes:	kde-splash-keramik

#%description -n kde-splash-default
#Default splash screen for KDE.

#%description -n kde-splash-default -l pl
#Standardowy obrazek startowy KDE.

%package common-filemanagement
Summary:	Common Files for kate and konqueror
Summary(pl):	Pliki wspólne dla kate i konquerora
Group:		X11/Libraries
Requires:	%{name}-common-konsole = %{version}-%{release}
Requires:	%{name}-kcontrol = %{version}-%{release}
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
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	%{name}-fonts

%description common-konsole
Common files for konsole and konsolepart.

%description common-konsole -l pl
Pliki wspólne dla konsole i konsolepart.

%package helpcenter
Summary:	KDE Help Center
Summary(pl):	Przegl±darka plików pomocy dla KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	%{name}-khelpcenter

%description helpcenter
KDE Help Center.

%description helpcenter -l pl
Przegl±darka plików pomocy dla KDE.

%package kate
Summary:	KDE Advanced Text Editor
Summary(pl):	Zaawansowany edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-common-filemanagement = %{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	kate

%description kate
KDE advanced text editor. 

%description kate -l pl
Zaawansowany edytor tekstu dla KDE.

%package kcontrol
Summary:	KDE Control Center
Summary(pl):	Centrum Sterowania KDE
Group:		X11/Applications
Requires:	%{name}-helpcenter = %{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4

%description kcontrol
KDE Control Center.

%description kcontrol -l pl
Narzêdzie do konfigurowania aplikacji KDE.

%package kdeprintfax
Summary:	KDE Fax Tool
Summary(pl):	Narzêdzie do faksowania dla KDE
Group:		X11/Applications
Requires:	%{name}-helpcenter = %{version}-%{release}
Requires:	kdelibs >= %{version}
Requires:	efax
Requires:	enscript
Obsoletes:	%{name} <= 3.1-9

%description kdeprintfax
KDE Fax Tool.

%description kdeprintfax -l pl
Narzêdzie do faksowania dla KDE.

%package kfind
Summary:	KDE Find Tool
Summary(pl):	Narzêdzie do wyszukiwania plików dla KDE
Group:		X11/Applications
Requires:	%{name}-helpcenter = %{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	kfind

%description kfind
KDE Find Tool.

%description kfind -l pl
Narzêdzie do wyszukiwania plików dla KDE.

%package kicker
Summary:        KDE Panel - kicker
Summary(pl):    Panel KDE - kicker
Group:          X11/Applications
Requires:       %{name} = %{version}-%{release}

%description kicker
KDE Panel - kicker.

%description kicker -l pl
Panel KDE - kicker.

%package konsole
Summary:	KDE Terminal Emulator
Summary(pl):	Emulator terminala dla KDE
Group:		X11/Applications
Requires:	%{name}-common-konsole = %{version}-%{release}
Requires:	%{name}-kcontrol = %{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	konsole

%description konsole
KDE Terminal Emulator.

%description konsole -l pl
Emulator terminala dla KDE.

%package kwrite
Summary:	KDE Text Editor
Summary(pl):	Edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-helpcenter = %{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	kwrite

%description kwrite
KDE text editor with syntax highlighting. 

%description kwrite -l pl
Edytor tekstu z pod¶wietlaniem sk³adni dla KDE.

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

%package pam
Summary:	KDE User Autentication 
Summary(pl):	Uwierzytelnianie u¿ytkowników dla KDE
Group:		X11/Applications
Obsoletes:	%{name} < 3.0.9-2.4

%description pam
KDE User Autentication.

%description pam -l pl
Uwierzytelnianie u¿ytkowników dla KDE.

%package screensavers
Summary:	KDE screensavers
Summary(pl):	Wygaszacze ekranu desktopu KDE
Summary(ru):	ÈÒÁÎÉÔÅÌÉ ÜËÒÁÎÁ ÄÌÑ KDE
Summary(uk):	ÚÂÅÒ¦ÇÁÞ¦ ÅËÒÁÎÕ ÄÌÑ KDE
Group:		X11/Applications
Requires:	OpenGL
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
Requires:	%{name}-kcontrol = %{version}-%{release}
Requires:	%{name}-pam = %{version}-%{release}
Requires:	sessreg
Requires:	xinitrc
Obsoletes:	gdm
Obsoletes:	xdm
Obsoletes:	%{name}-kdm

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
Requires:	%{name}-mailnews = %{version}-%{release}
Requires:	%{name}-konsole = %{version}-%{release}
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
# obsoleted
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
# fix it if You like it 
#%patch13 -p1
%patch14 -p1
# doesn't work (patches Makefile.am only!)
#%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
# not tested yet
#%patch20 -p1
%patch21 -p1
%patch22 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

for plik in `find ./ -name *.desktop` ; do
	echo $plik
	sed -i -e "s/\[nb\]/\[no\]/g" $plik
done

%configure \
	--with-pam=kdm
		
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

install -d $RPM_BUILD_ROOT/etc/{X11/desktop/menus,pam.d,rc.d/init.d,security} \
    $RPM_BUILD_ROOT%{_libdir}/kde3/plugins/konqueror

mv $RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xservers{,.orig}
mv $RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xsession{,.orig}

touch $RPM_BUILD_ROOT/etc/security/blacklist.kdm

install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/kdm
install %{SOURCE6}	$RPM_BUILD_ROOT/etc/pam.d/kscreensaver
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/rc.d/init.d/kdm
install %{SOURCE4}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xsession
install %{SOURCE7}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xservers
install %{SOURCE9}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/pics/pldlogo.png
install %{SOURCE10}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/pics/pldwallpaper.png

install {%{SOURCE11},%{SOURCE12}} \
    $RPM_BUILD_ROOT%{_datadir}/services/searchproviders

cp $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/dirtree/remote/smb-network.desktop \
    $RPM_BUILD_ROOT%{_datadir}/apps/konqsidebartng/virtual_folders/remote

ALD=$RPM_BUILD_ROOT%{_applnkdir}
install -d $ALD/Settings/KDE
mv -f $ALD/{Settings/[!K]*,Settings/KDE}
mv -f $ALD/Help.desktop $RPM_BUILD_ROOT%{_desktopdir}
mv -f $ALD/Settingsmenu/[!K]*.desktop $RPM_BUILD_ROOT%{_desktopdir}
mv -f $ALD/System/kinfocenter.desktop $RPM_BUILD_ROOT%{_desktopdir}

install %{SOURCE13} $ALD/Settings/KDE/Components
install %{SOURCE14} $RPM_BUILD_ROOT/etc/X11/desktop/menus

mv $RPM_BUILD_ROOT%{_vfinfodir}/kde-settings.directory{,.orig}
install %{SOURCE15} $RPM_BUILD_ROOT%{_vfinfodir}


> %{name}.lang

programs="kdebugdialog kdeprint kdesu kinfocenter \
kioslave klipper kmenuedit kpager ksysguard" 
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> %{name}.lang
done

programs="arts background bell clock colors desktop energy fonts \
helpindex.html icons kcmaccess kcmfontinst kcmlaunch kcmnotify kcmsmserver \
kcmstyle kcmtaskbar keyboard keys kthememgr kwindecoration language mouse \
panel passwords smb spellchecking windowmanagement"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> %{name}.lang
done

%find_lang	kate		--with-kde
%find_lang	kdm		--with-kde
%find_lang	kfind		--with-kde
%find_lang	khelpcenter	--with-kde
%find_lang	kicker		--with-kde
%find_lang	kcmkonsole	--with-kde
%find_lang	konsole		--with-kde
cat kcmkonsole.lang >> konsole.lang

%find_lang konqueror	--with-kde
programs="cache cookies crypto ebrowsing email filemanager filetypes \
kcmcss khtml netpref proxy useragent"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> konqueror.lang
done

%find_lang	kwrite		--with-kde
%find_lang	screensaver	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%config %{_sysconfdir}/ksysguarddrc
%attr(0755,root,root) %{_bindir}/[ades]*
%attr(0755,root,root) %{_bindir}/k[jtx]*
%attr(0755,root,root) %{_bindir}/ka[!t]*
%attr(0755,root,root) %{_bindir}/kcheckpass
%attr(0755,root,root) %{_bindir}/kdc*
%attr(0755,root,root) %{_bindir}/kde[!ps]*
%attr(0755,root,root) %{_bindir}/kdes[!u]*
%attr(2755,root,nobody) %{_bindir}/kdesud
%attr(2755,root,nobody) %{_bindir}/kdialog
%attr(2755,root,nobody) %{_bindir}/khc_indexbuilder
%attr(0755,root,root) %{_bindir}/khotkeys
%attr(0755,root,root) %{_bindir}/kinfocenter
%attr(0755,root,root) %{_bindir}/klipper
%attr(0755,root,root) %{_bindir}/kmenuedit
%attr(0755,root,root) %{_bindir}/kpager
%attr(0755,root,root) %{_bindir}/kpersonalizer
%attr(0755,root,root) %{_bindir}/kpm
%attr(0755,root,root) %{_bindir}/kprinter
%attr(0755,root,root) %{_bindir}/krdb
%attr(0755,root,root) %{_bindir}/kreadconfig
%attr(0755,root,root) %{_bindir}/ks[mty]*
%attr(0755,root,root) %{_bindir}/ksplash
%attr(0755,root,root) %{_bindir}/kw[!r]*
%attr(0755,root,root) %{_bindir}/kwrited
%{_libdir}/[ae]*.la
%attr(0755,root,root) %{_libdir}/[ae]*.so
%{_libdir}/k[dhijlmsx]*.la
%attr(0755,root,root) %{_libdir}/k[dhjlmsx]*.so
%{_libdir}/kaccess.la
%attr(0755,root,root) %{_libdir}/kaccess.so
%{_libdir}/kprinter.la
%attr(0755,root,root) %{_libdir}/kprinter.so
%{_libdir}/kw[!r]*.la
%attr(0755,root,root) %{_libdir}/kw[!r]*.so
%{_libdir}/kwrited.la
%attr(0755,root,root) %{_libdir}/kwrited.so
%{_libdir}/libksgrd.la
%attr(0755,root,root) %{_libdir}/libksgrd.so.*
%{_libdir}/libksplashthemes.la
%attr(0755,root,root) %{_libdir}/libksplashthemes.so.*
##%{_libdir}/libsensordisplays.la
##%attr(0755,root,root) %{_libdir}/libsensordisplays.so.*
%{_libdir}/libtask*.la
%attr(0755,root,root) %{_libdir}/libtask*.so.*
%{_libdir}/kde3/kcm_access.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_access.so
%{_libdir}/kde3/kcm_arts.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_arts.so
%{_libdir}/kde3/kcm_background.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_background.so
%{_libdir}/kde3/kcm_bell.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_bell.so
%{_libdir}/kde3/kcm_clock.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_clock.so
%{_libdir}/kde3/kcm_colors.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_colors.so
%{_libdir}/kde3/kcm_componentchooser.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_componentchooser.so
%{_libdir}/kde3/kcm_email.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_email.so
%{_libdir}/kde3/kcm_energy.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_energy.so
%{_libdir}/kde3/kcm_fontinst.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_fontinst.so
#%{_libdir}/kde3/kcm_helpcenter.la
#%attr(0755,root,root) %{_libdir}/kde3/kcm_helpcenter.so
%{_libdir}/kde3/kcm_icons.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_icons.so
%{_libdir}/kde3/kcm_info.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_info.so
%{_libdir}/kde3/kcm_input.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_input.so
%{_libdir}/kde3/kcm_ioslaveinfo.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_ioslaveinfo.so
%{_libdir}/kde3/kcm_keyboard.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_keyboard.so
%{_libdir}/kde3/kcm_keys.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_keys.so
%{_libdir}/kde3/kcm_khotkeys.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_khotkeys.so
%{_libdir}/kde3/kcm_knotify.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_knotify.so
%{_libdir}/kde3/kcm_kwindecoration.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kwindecoration.so
%{_libdir}/kde3/kcm_kwinoptions.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kwinoptions.so
%{_libdir}/kde3/kcm_launch.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_launch.so
%{_libdir}/kde3/kcm_locale.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_locale.so
%{_libdir}/kde3/kcm_nic.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_nic.so
%{_libdir}/kde3/kcm_passwords.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_passwords.so
%{_libdir}/kde3/kcm_performance.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_performance.so
%{_libdir}/kde3/kcm_printmgr.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_printmgr.so
%{_libdir}/kde3/kcm_samba.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_samba.so
%{_libdir}/kde3/kcm_smserver.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_smserver.so
%{_libdir}/kde3/kcm_spellchecking.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_spellchecking.so
%{_libdir}/kde3/kcm_style.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_style.so
%{_libdir}/kde3/kcm_taskbar.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_taskbar.so
%{_libdir}/kde3/kcm_themes.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_themes.so
%{_libdir}/kde3/kcm_usb.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_usb.so
%{_libdir}/kde3/kcm_xinerama.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_xinerama.so
%{_libdir}/kde3/klipper_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/klipper_panelapplet.so
%{_libdir}/kde3/kwin*.la
%attr(0755,root,root) %{_libdir}/kde3/kwin*.so
%{_libdir}/kde3/libkdeprint_part.la
%attr(0755,root,root) %{_libdir}/kde3/libkdeprint_part.so
%{_libdir}/kde3/libksplashdefault.la
%attr(755,root,root) %{_libdir}/kde3/libksplashdefault.so*
%{_libdir}/kde3/sysguard_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/sysguard_panelapplet.so
%dir %{_datadir}/apps/ksmserver
%dir %{_datadir}/apps/ksplash
%dir %{_datadir}/apps/ksplash/Themes
%{_datadir}/apps/ksplash/Themes/Default
%{_datadir}/apps/?[!acdefhiosw]*
%{_datadir}/apps/kappfinder
%{_datadir}/apps/kcm[!_c]*
%{_datadir}/apps/kcm_componentchooser/*
%{_datadir}/apps/kconf_update/*
%{_datadir}/apps/kdcop
%{_datadir}/apps/kdeprint/*
%{_datadir}/apps/kdeprint_part
%{_datadir}/apps/kdesktop
%{_datadir}/apps/kdewizard
%{_datadir}/apps/kdisplay
%{_datadir}/apps/kinfocenter
%{_datadir}/apps/kio_finger
%{_datadir}/apps/kio_info
%{_datadir}/apps/ksysguard
%{_datadir}/apps/kwin
%{_datadir}/apps/naughtyapplet
%{_datadir}/autostart/*
%{_datadir}/config/kdesktop*
%{_datadir}/config/klipperrc
%{_datadir}/config/kwritedrc
%{_datadir}/config/kxkb_groups
%{_datadir}/locale/*
%{_datadir}/services/kaccess.desktop
%{_datadir}/services/kdeprint_part.desktop
%{_datadir}/services/ksplash*.desktop
%{_datadir}/services/kwrited.desktop
%{_datadir}/services/kxkb.desktop
%{_datadir}/sounds
%{_datadir}/templates
%{_datadir}/wallpapers
%{_applnkdir}/Home.desktop
%{_applnkdir}/.hidden/[bcmspv]*.desktop
%{_applnkdir}/.hidden/k[!cio]*.desktop
%{_applnkdir}/.hidden/kcmkxmlrpcd.desktop
%{_applnkdir}/Utilities/k[!de]*.desktop
%{_applnkdir}/Settings/KDE/Accessibility
%{_applnkdir}/Settings/KDE/Components/[!f]*
%{_applnkdir}/Settings/KDE/Components/filebrowser.desktop
%{_applnkdir}/Settings/KDE/Desktop
%{_applnkdir}/Settings/KDE/Information
%dir %{_applnkdir}/Settings/KDE/LookNFeel
%{_applnkdir}/Settings/KDE/LookNFeel/[!s]*
%{_applnkdir}/Settings/KDE/LookNFeel/s[!c]*
%{_applnkdir}/Settings/KDE/Network/email.desktop
%{_applnkdir}/Settings/KDE/Peripherals
%{_applnkdir}/Settings/KDE/PowerControl
%{_applnkdir}/Settings/KDE/Security/passwords.desktop
%{_applnkdir}/Settings/KDE/Sound
%{_applnkdir}/Settings/KDE/System/[!k]*
%{_applnkdir}/Settings/KDE/System/kcmfontinst.desktop
%{_applnkdir}/Settings/KDE/WebBrowsing
%{_applnkdir}/System/k[!io]*.desktop
%{_desktopdir}/kjobviewer.desktop
%{_desktopdir}/klipper.desktop
%{_desktopdir}/kpager.desktop
%{_desktopdir}/ksysguard.desktop
%{_desktopdir}/ktip.desktop
# moved here
%{_desktopdir}/kappfinder.desktop
%{_desktopdir}/kinfocenter.desktop
%{_desktopdir}/kmenuedit.desktop
%{_desktopdir}/kpersonalizer.desktop
%{_desktopdir}/printmgr.desktop
#
%{_vfinfodir}/kde-information.directory
%{_vfinfodir}/kde-settings-[ailpw]*.directory
%{_vfinfodir}/kde-settings-desktop.directory
%{_vfinfodir}/kde-settings-sound.directory
%{_pixmapsdir}/*/*/apps/a[!g]*
%{_pixmapsdir}/*/*/apps/[dghilmnqrtuvwx]*
%{_pixmapsdir}/*/*/apps/b[!e]*
%{_pixmapsdir}/*/*/apps/c[!ao]*
%{_pixmapsdir}/*/*/apps/co[!o]*
%{_pixmapsdir}/*/*/apps/e[!n]*
%{_pixmapsdir}/*/*/apps/en[!h]*
%{_pixmapsdir}/*/*/apps/k[jlmnptvmx]*
%{_pixmapsdir}/*/*/apps/kappfinder.png
%{_pixmapsdir}/[!l]*/*/apps/kc[!o][!s]*
%{_pixmapsdir}/*/*/apps/kcms[!y]*
%{_pixmapsdir}/*/*/apps/key[!_]*
%{_pixmapsdir}/*/*/apps/ksysguard.png
%{_pixmapsdir}/*/*/apps/kdisk*
%{_pixmapsdir}/*/*/apps/kwin.png
%{_pixmapsdir}/*/*/apps/opera*
%{_pixmapsdir}/*/*/apps/p[!er]*
%{_pixmapsdir}/*/*/apps/penguin.png
%{_pixmapsdir}/*/*/apps/printmgr.png
%{_pixmapsdir}/*/*/apps/s[!t]*.png
%{_pixmapsdir}/*/*/apps/staroffice.png
%{_pixmapsdir}/*/*/apps/style.png
%{_pixmapsdir}/*/*/devices/print_[!c]*
%{_pixmapsdir}/*/*/filesystems/*

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
%{_libdir}/libtask*.so

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/libccont.a

%files -n kde-sdscreen-default                                                  
%defattr(644,root,root,755)                                                     
%{_datadir}/apps/ksmserver/* 

#%files -n kde-splash-default                                                  
#%defattr(644,root,root,755)                                                     
#%{_datadir}/apps/ksplash/pics

%files common-filemanagement
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/filesharelist
%attr(0755,root,root) %{_bindir}/fileshareset
%{_libdir}/libkmultitabbar.la
%attr(0755,root,root) %{_libdir}/libkmultitabbar.so.*
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
%dir %{_applnkdir}/Settings/KDE/Network
%{_applnkdir}/Settings/KDE/Network/fileshare.desktop
%{_vfinfodir}/kde-settings-network.directory

%files common-konsole
%defattr(644,root,root,755)
%{_fontdir}/console*.gz
%{_datadir}/apps/konsole
%{_pixmapsdir}/[!l]*/*/apps/bell.png
%{_pixmapsdir}/*/*/apps/key_bindings.png

%files helpcenter -f khelpcenter.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/khelpcenter
%{_libdir}/kde3/kio_info.la
%attr(0755,root,root) %{_libdir}/kde3/kio_info.so
%{_libdir}/kde3/kio_man.la
%attr(0755,root,root) %{_libdir}/kde3/kio_man.so
%{_libdir}/kde3/khelpcenter.la
%attr(0755,root,root) %{_libdir}/kde3/khelpcenter.so
%{_datadir}/apps/khelpcenter
%{_datadir}/services/info.protocol
%{_datadir}/services/khelpcenter.desktop
%{_datadir}/services/man.protocol
%{_desktopdir}/Help.desktop
%{_pixmapsdir}/*/*/apps/khelpcenter.png

%files kate -f kate.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kate
%{_libdir}/kate.la
%attr(0755,root,root) %{_libdir}/kate.so
%{_libdir}/libkateinterfaces.la
%attr(0755,root,root) %{_libdir}/libkateinterfaces.so.*
%{_libdir}/libkateutils.la
%attr(0755,root,root) %{_libdir}/libkateutils.so.*
%{_libdir}/kde3/katedefaultprojectplugin.la
%attr(0755,root,root) %{_libdir}/kde3/katedefaultprojectplugin.so
%{_datadir}/apps/kate
%{_datadir}/services/katedefaultproject.desktop
%{_datadir}/servicetypes/kateinitplugin.desktop
%{_datadir}/servicetypes/kateplugin.desktop
%{_datadir}/servicetypes/kateprojectplugin.desktop
%{_desktopdir}/kate.desktop
%{_pixmapsdir}/*/*/apps/kate.png

%files kcontrol
%defattr(644,root,root,755)
/etc/X11/desktop/menus/kde-settings.menu
%attr(0755,root,root) %{_bindir}/kcminit
%attr(0755,root,root) %{_bindir}/kcmshell
%attr(0755,root,root) %{_bindir}/kcontrol
%attr(0755,root,root) %{_bindir}/kdesu
%{_libdir}/kcminit.la
%attr(0755,root,root) %{_libdir}/kcminit.so
%{_libdir}/kcmshell.la
%attr(0755,root,root) %{_libdir}/kcmshell.so
%{_libdir}/kcontrol.la
%attr(0755,root,root) %{_libdir}/kcontrol.so
%{_datadir}/apps/kcontrol
%{_applnkdir}/KControl.desktop
# no idea to do with
#%{_applnkdir}/Settingsmenu/KControl.desktop
%dir %{_applnkdir}/Settings/KDE
%dir %{_applnkdir}/Settings/KDE/Components
%dir %{_applnkdir}/Settings/KDE/System
%{_vfinfodir}/kde-settings.directory
%{_vfinfodir}/kde-settings-components.directory
%{_vfinfodir}/kde-settings-system.directory
%{_pixmapsdir}/*/*/apps/kcontrol.png
%{_pixmapsdir}/*/*/apps/kcmsystem.png
%lang(en) %dir %{_htmldir}/en/kcontrol
%lang(en) %{_htmldir}/en/kcontrol/common
%lang(en) %{_htmldir}/en/kcontrol/index.*
%lang(en) %{_htmldir}/en/kcontrol/screenshot.png

%files kdeprintfax
%attr(0755,root,root) %{_bindir}/kdeprintfax
%dir %{_datadir}/apps/kdeprintfax
%attr(0755,root,root) %{_datadir}/apps/kdeprintfax/anytops
%{_datadir}/apps/kdeprintfax/[!a]*
%{_desktopdir}/kdeprintfax.desktop
%{_pixmapsdir}/*/*/apps/kdeprintfax.png

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
%attr(0755,root,root) %{_libdir}/libkickermain.so.*
%{_libdir}/kde3/kickermenu_kdeprint.la
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_kdeprint.so                         
%{_libdir}/kde3/kickermenu_konsole.la
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_konsole.so                         
%{_libdir}/kde3/kickermenu_prefmenu.la
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_prefmenu.so                         
%{_libdir}/kde3/kickermenu_recentdocs.la
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_recentdocs.so                       
%{_libdir}/kde3/kcm_kicker.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kicker.so
%{_libdir}/kde3/systemtray_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/systemtray_panelapplet.so
%{_libdir}/kde3/taskbar_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelapplet.so
%{_libdir}/kde3/taskbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelextension.so
%{_libdir}/kde3/launcher_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/launcher_panelapplet.so
%{_libdir}/kde3/lockout_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/lockout_panelapplet.so
%{_libdir}/kde3/minipager_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/minipager_panelapplet.so
%{_libdir}/kde3/naughty_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/naughty_panelapplet.so
%{_libdir}/kde3/run_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/run_panelapplet.so
%{_libdir}/kde3/childpanel_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/childpanel_panelextension.so
%{_libdir}/kde3/clock_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/clock_panelapplet.so
%{_libdir}/kde3/dockbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/dockbar_panelextension.so
%{_libdir}/kde3/kasbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/kasbar_panelextension.so 
%{_datadir}/apps/kicker
%{_pixmapsdir}/*/*/apps/*kicker*
%{_applnkdir}/.hidden/kicker*.desktop
%{_desktopdir}/kcmkicker.desktop

%files konsole -f konsole.lang
%defattr(644,root,root,755)
%doc konsole/README*
%attr(0755,root,root) %{_bindir}/konsole
#%attr(6755,root,root) %{_bindir}/konsole_grantpty
%{_libdir}/konsole.la
%attr(0755,root,root) %{_libdir}/konsole.so
%{_libdir}/kde3/kcm_konsole.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_konsole.so
%{_datadir}/config/konsolerc
%dir %{_applnkdir}/.hidden
%{_applnkdir}/.hidden/kcmkonsole.desktop
%{_applnkdir}/System/konsolesu.desktop
%{_desktopdir}/konsole*.desktop
%{_pixmapsdir}/*/*/apps/konsole.png

%files kwrite -f kwrite.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kwrite
%attr(0755,root,root) %{_bindir}/kwriteconfig
%{_libdir}/kwrite.la
%attr(0755,root,root) %{_libdir}/kwrite.so
%{_datadir}/apps/kwrite
%{_desktopdir}/kwrite.desktop
%{_pixmapsdir}/*/*/apps/kwrite.png

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

%files pam
%defattr(644,root,root,755)
%doc README.pam
# Must be here. kcheckpass needs it.
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/kdm
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.kdm

%files screensavers -f screensaver.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/*.kss
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/kscreensaver
%{_libdir}/kde3/kcm_screensaver.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_screensaver.so
%{_datadir}/apps/kscreensaver
%{_applnkdir}/Settings/KDE/LookNFeel/screensaver.desktop
%{_pixmapsdir}/*/*/apps/kscreensaver.png


%files -n kdm -f kdm.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/kdm
%attr(0754,root,root) /etc/rc.d/init.d/kdm
%config(noreplace) %{_sysconfdir}/kdm/kdmrc
%config(noreplace) %{_sysconfdir}/kdm/backgroundrc
%attr(0755,root,root) %{_sysconfdir}/kdm/Xreset
%attr(0755,root,root) %{_sysconfdir}/kdm/Xsession
%attr(0755,root,root) %{_sysconfdir}/kdm/Xsetup
%attr(0755,root,root) %{_sysconfdir}/kdm/Xstartup
%attr(0755,root,root) %{_sysconfdir}/kdm/Xwilling
%{_sysconfdir}/kdm/Xaccess
%{_sysconfdir}/kdm/Xservers
%{_sysconfdir}/kdm/pics
#%attr(0755,root,root) %{_bindir}/chooser
%attr(0755,root,root) %{_bindir}/kdm*
%attr(0755,root,root) %{_bindir}/krootimage
%{_libdir}/kde3/kcm_kdm.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kdm.so
%{_applnkdir}/Settings/KDE/System/kdm.desktop
%{_pixmapsdir}/*/*/apps/kdmconfig.png

%files -n konqueror -f konqueror.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/keditbookmarks
%attr(0755,root,root) %{_bindir}/keditfiletype
%attr(0755,root,root) %{_bindir}/kfm*
%attr(0755,root,root) %{_bindir}/kio_devices_mounthelper
%attr(0755,root,root) %{_bindir}/konqueror
%attr(0755,root,root) %{_bindir}/klocaldomainurifilterhelper
%attr(0755,root,root) %{_bindir}/nspluginscan
%attr(0755,root,root) %{_bindir}/nspluginviewer
%{_libdir}/keditbookmarks.la
%attr(0755,root,root) %{_libdir}/keditbookmarks.so
%{_libdir}/kfm*.la
%attr(0755,root,root) %{_libdir}/kfm*.so
%{_libdir}/konqueror.la
%attr(0755,root,root) %{_libdir}/konqueror.so
%{_libdir}/kde3/libkfindpart.la
%attr(0755,root,root) %{_libdir}/kde3/libkfindpart.so
%{_libdir}/libkonq.la
%attr(0755,root,root) %{_libdir}/libkonq.so.*
%{_libdir}/libkonq_sidebar_tree.la
%attr(0755,root,root) %{_libdir}/libkonq_sidebar_tree.so
%{_libdir}/libkonqsidebarplugin.la
%attr(0755,root,root) %{_libdir}/libkonqsidebarplugin.so.*
%{_libdir}/libnsplugin.la
%attr(0755,root,root) %{_libdir}/libnsplugin.so.*
%dir %{_libdir}/kde3/plugins/konqueror
%{_libdir}/kde3/kfile_font.la     
%attr(0755,root,root) %{_libdir}/kde3/kfile_font.so     
%{_libdir}/kde3/libkmanpart.la
%attr(0755,root,root) %{_libdir}/kde3/libkmanpart.so
%{_libdir}/kde3/libkshorturifilter.la
%attr(0755,root,root) %{_libdir}/kde3/libkshorturifilter.so
%{_libdir}/kde3/libkuriikwsfilter.la
%attr(0755,root,root) %{_libdir}/kde3/libkuriikwsfilter.so
%{_libdir}/kde3/libkurisearchfilter.la
%attr(0755,root,root) %{_libdir}/kde3/libkurisearchfilter.so
%{_libdir}/kde3/liblocaldomainurifilter.la
%attr(0755,root,root) %{_libdir}/kde3/liblocaldomainurifilter.so
%{_libdir}/kde3/kcm_cgi.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_cgi.so
%{_libdir}/kde3/kcm_crypto.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_crypto.so
%{_libdir}/kde3/kcm_css.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_css.so
%{_libdir}/kde3/kcm_filetypes.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_filetypes.so
%{_libdir}/kde3/kcm_fonts.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_fonts.so
%{_libdir}/kde3/kcm_history.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_history.so
%{_libdir}/kde3/kcm_kded.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kded.so
%{_libdir}/kde3/kcm_kio.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kio.so
%{_libdir}/kde3/kcm_konqhtml.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_konqhtml.so
%{_libdir}/kde3/kcm_konq.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_konq.so
%{_libdir}/kde3/kcm_kurifilt.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kurifilt.so
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
%{_libdir}/kde3/kded_*.la
%attr(0755,root,root) %{_libdir}/kde3/kded_*.so
%{_libdir}/kde3/konq*.la
%attr(0755,root,root) %{_libdir}/kde3/konq*.so
%{_datadir}/apps/kcmcss
%{_datadir}/apps/keditbookmarks
%{_datadir}/apps/kfindpart
%{_datadir}/apps/konq*
%{_datadir}/config/konqsidebartng.rc
%{_datadir}/config/kshorturifilterrc
#%{_datadir}/config/kuriikwsfilterrc
%{_datadir}/mimelnk/application/*
%{_datadir}/mimelnk/print
%{_datadir}/mimelnk/kdedevice
%{_datadir}/services/kded/*
%{_datadir}/services/searchproviders
%{_datadir}/services/useragentstrings
%{_datadir}/services/about.protocol
%{_datadir}/services/bzip2.protocol
%{_datadir}/services/bzip.protocol
%{_datadir}/services/cgi.protocol
%{_datadir}/services/devices.protocol
%{_datadir}/services/finger.protocol
%{_datadir}/services/fish.protocol
%{_datadir}/services/floppy.protocol
%{_datadir}/services/gzip.protocol
%{_datadir}/services/ldap.protocol
%{_datadir}/services/mac.protocol
%{_datadir}/services/nfs.protocol
%{_datadir}/services/print.protocol
%{_datadir}/services/sftp.protocol
%{_datadir}/services/smb.protocol
%{_datadir}/services/tar.protocol
%{_datadir}/services/zip.protocol
%{_datadir}/services/kfile_font.desktop
%{_datadir}/services/kfindpart.desktop
%{_datadir}/services/kmanpart.desktop
%{_datadir}/services/konq*.desktop
%{_datadir}/services/kshorturifilter.desktop
%{_datadir}/services/kuriikwsfilter.desktop
%{_datadir}/services/kurisearchfilter.desktop
%{_datadir}/services/localdomainurifilter.desktop
%{_datadir}/servicetypes/[!kt]*
%{_datadir}/servicetypes/k[!a]*
%{_applnkdir}/konqueror.desktop
%{_applnkdir}/.hidden/file*.desktop
%{_applnkdir}/.hidden/kcmkonq.desktop
%{_applnkdir}/.hidden/konq*.desktop
%{_applnkdir}/Settings/KDE/Components/filetypes.desktop
%{_applnkdir}/Settings/KDE/Network/WebBrowsing
%{_applnkdir}/Settings/KDE/Network/netpref.desktop
%{_applnkdir}/Settings/KDE/Network/lanbrowser.desktop
%{_applnkdir}/Settings/KDE/Network/proxy.desktop
%dir %{_applnkdir}/Settings/KDE/Security
%{_applnkdir}/Settings/KDE/Security/crypto.desktop
%{_applnkdir}/System/konq*.desktop
%{_desktopdir}/kfmclient*.desktop
%{_desktopdir}/konq*.desktop
%{_vfinfodir}/kde-settings-security.directory
%{_pixmapsdir}/*/*/apps/agent.png
%{_pixmapsdir}/*/*/apps/cache.png
%{_pixmapsdir}/*/*/apps/cookie.png
%{_pixmapsdir}/*/*/apps/enhanced_browsing.png
%{_pixmapsdir}/*/*/apps/filetypes.png
%{_pixmapsdir}/*/*/apps/fonts.png
%{_pixmapsdir}/*/*/apps/keditbookmarks.png
%{_pixmapsdir}/*/*/apps/kfm*.png
%{_pixmapsdir}/*/*/apps/konqueror.png
%{_pixmapsdir}/*/*/apps/personal.png
%{_pixmapsdir}/*/*/apps/proxy.png
%{_pixmapsdir}/*/*/apps/stylesheet.png
