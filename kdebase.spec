#
# FIXME: infinite loop in symlinks to kdmrc
#
# _without_alsa - disable alsa

%define		_state		unstable
%define		_kdever		kde-3.1-rc5

Summary:	K Desktop Environment - core files
Summary(es):	K Desktop Environment - archivos básicos
Summary(ja):	KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ - ´ðËÜ¥Õ¥¡¥¤¥ë
Summary(ko):    KDE - ±âº» ÆÄÀÏ
Summary(pl):	K Desktop Environment - pliki ¶rodowiska
Summary(pt_BR):	K Desktop Environment - arquivos básicos
Summary(ru):	K Desktop Environment - ÂÁÚÏ×ÙÅ ÆÁÊÌÙ
Summary(uk):	K Desktop Environment - ÂÁÚÏ×¦ ÆÁÊÌÉ
Summary(zh_CN): KDEºËÐÄ
Name:		kdebase
Version:	3.1
Release:	3.2
Epoch:		7
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	kdm.pamd
Source3:	kdm.init
Source4:	kdm.Xsession
Source6:	%{name}-kscreensaver.pam
Source7:	%{name}-kdm.Xservers
#Source8:	%{name}-kdm.findwm
Patch0:		%{name}-kdmrc.patch
Patch1:		%{name}-fix-mem-leak-in-kfind.patch
Patch2:		%{name}-dont_merge_old_kdmrc.patch
Patch3:		%{name}-glibc-2.2.2.patch
Patch4:		%{name}-startkde.patch
Patch5:		%{name}-kdm.daemon_output.patch
Patch6:		%{name}-kicker.patch
Patch7:		%{name}-konsole_all.patch
Patch8:		%{name}-nsplugins_dirs.patch
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:        alsa-lib-devel}
%endif
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
BuildRequires:	db3-devel
BuildRequires:	findutils
BuildRequires:	gettext-devel
BuildRequires:	glut-devel
BuildRequires:	grep
BuildRequires:	kdelibs-devel >= %{version}
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
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	qt-devel >= 3.1
BuildRequires:	zlib-devel
# TODO: sensors
#BuildRequires:	sensors-devel
Requires(post,postun):	/sbin/ldconfig
Prereq:		/usr/X11R6/bin/mkfontdir
Requires:	applnk >= 1.5.14
Requires:	kde-splash
Requires:       kde-sdscreen
Requires:	konqueror = %{version}-%{release}
Requires:	%{name}-pam = %{version}-%{release}
Requires:	%{name}-wallpapers = %{version}-%{release}
#
Obsoletes:	%{name}-fonts
Obsoletes:	%{name}-khelpcenter
Obsoletes:	%{name}-screensaver
Obsoletes:	%{name}-kicker
Obsoletes:	%{name}-kioslave
Obsoletes:	%{name}-konqueror
Obsoletes:	%{name}-kwin
Obsoletes:	%{name}-kxmlrpc
Obsoletes:	%{name}-kdesktop
#
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix 	/usr/X11R6
%define		_fontdir 	/usr/share/fonts
%define		_htmldir	/usr/share/doc/kde/HTML
%define		_sysconfdir	/etc/X11

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
Requires:	kdelibs-devel >= %{version}

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
Requires:	%{name}-common-konsole = %{version}-%{release}
Requires:	%{name}-kcontrol = %{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4

%description common-filemanagement
Common files - needed by kate and konqueror

%description common-filemanagement -l pl
Pliki wspólne - u¿ywane przez kate i konquerora

%package common-konsole
Summary:	Common files for konsole and konsolepart
Summary(pl):	Pliki wspólne dla konsole i konsolepart
Group:		X11/Applications
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	%{name}-fonts

%description common-konsole
Common files for konsole and konsolepart

%description common-konsole -l pl
Pliki wspólne dla konsole i konsolepart

%package helpcenter
Summary:	KDE Help Center
Summary(pl):	Przegladarka plików pomocy dla KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	%{name}-khelpcenter

%description helpcenter
KDE Help Center

%description helpcenter -l pl
Przegladarka plików pomocy dla KDE

%package kcontrol
Summary:	KDE Control Center
Summary(pl):	Centrum Sterowania KDE
Group:		X11/Applications
Requires:	%{name}-helpcenter = %{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4

%description kcontrol
KDE Control Center

%description kcontrol -l pl
Narzêdzie do konfigurowania aplikacji KDE

%package mailnews
Summary:	KDE Mail and News Services
Summary(pl):	Obs³uga protoko³ów pocztowych i news dla KDE
Group:		X11/Libraries
Requires:	kdelibs >= %{version}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	%{name}-kioslave

%description mailnews
KDE Mail and News Services

%description mailnews -l pl
Obs³uga protoko³ów pocztowych i news dla KDE


%package pam
Summary:        KDE User Autentication 
Summary(pl):    Autentykacja u¿ytkownika dla KDE
Group:          X11/Applications
Obsoletes:	%{name} < 3.0.9-2.4

%description pam
KDE User Autentication

%description pam -l pl
Autentykacja u¿ytkownika dla KDE

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

%package wallpapers
Summary:	KDE Wallpapers
Summary(pl):	Tapety pulpitu dla KDE
Group:		X11/Amusements
Requires:	kdelibs >= %{version}
Obsoletes:	%{name} < 3.0.9-2.4

%description wallpapers
KDE Wallpapers

%description wallpapers -l pl
Tapety pulpitu dla KDE.

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
Zaawansowany edytor tekstu dla KDE

%package -n kdm
Summary:	KDE Display Manager
Summary(pl):	KDE Display Manager
Group:		X11/Applications
Requires:	%{name}-kcontrol = %{version}-%{release}
Requires:	%{name}-pam = %{version}-%{release}
Requires:	%{name}-wallpapers = %{version}-%{release}
Requires:	sessreg
Requires:	xinitrc
Prereq:		/sbin/chkconfig
Obsoletes:	gdm
Obsoletes:	xdm
Obsoletes:	%{name}-kdm

%description -n kdm
It is KDE replacement for XDM. It manages local and remote X11
displays.

%description -n kdm -l pl
Zamiennik XDM rodem z KDE.

%package kfind
Summary:	KDE Find Tool
Summary(pl):	Narzêdzie do wyszukiwania plików dla KDE
Group:		X11/Applications
Requires:	%{name}-helpcenter = %{version}-%{release}
Requires:	kdelibs >= %{version}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	kfind

%description kfind
KDE Find Tool

%description kfind -l pl
Narzêdzie do wyszukiwania plików dla KDE

%package -n konqueror
Summary:	Konqueror - web browser and file manager
Summary(pl):	Konqueror - przegl±darka WWW i mened¿er plików
Group:		X11/Applications
Requires:	%{name}-common-filemanagement = %{version}-%{release}
Requires:	%{name}-mailnews = %{version}-%{release}
Requires:	%{name}-konsole = %{version}-%{release}
Obsoletes:	%{name}-konqueror

%description -n konqueror
Konqueror is a web browser and file manager similar to MS Internet
Explorer.

%description -n konqueror -l pl
Konqueror jest przegl±dark± WWW i mene¿derem plików podobnym do MS
Internet Explorer.

%package konsole
Summary:	KDE Terminal Emulator
Summary(pl):	Emulator terminala dla KDE
Group:		X11/Applications
Requires:	%{name}-common-konsole = %{version}-%{release}
Requires:	%{name}-kcontrol = %{version}-%{release}
Obsoletes:	%{name} < 3.0.9-2.4
Obsoletes:	konsole

%description konsole
KDE Terminal Emulator

%description konsole -l pl
Emulator terminala dla KDE

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
Edytor tekstu z pod¶wietlaniem sk³adni dla KDE

%prep
%setup -q
# patch0 is applied in %%install
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build

kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CPPFLAGS="-I%{_includedir}"
export CPPFLAGS
%configure \
	--with-pam=kdm \
	--without-ldap \
	--without-shadow \
	--disable-shadow \
	--with-xdmdir="%{_sysconfdir}/kdm" \
	--enable-final \
        --with%{?_without_alsa:out}-alsa
	

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Help,Network/WWW,Settings/KDE,System/Administration,Terminals} \
	$RPM_BUILD_ROOT{/etc/{pam.d,security,rc.d/init.d,X11/kdm},%{_libdir}/kde3/plugins/konqueror}
install -d $RPM_BUILD_ROOT

%{__make} install \
 	DESTDIR="$RPM_BUILD_ROOT" \
 	fontdir="%{_fontdir}/misc"

mv $RPM_BUILD_ROOT%{_datadir}/config/kdm/{Xaccess,Xreset,Xsetup,Xstartup,Xwilling,kdmrc,backgroundrc} \
	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/

install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/kdm
install %{SOURCE6}	$RPM_BUILD_ROOT/etc/pam.d/kscreensaver
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/rc.d/init.d/kdm
install %{SOURCE4}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xsession
install %{SOURCE7}	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xservers
#install %{SOURCE8}	$RPM_BUILD_ROOT%{_bindir}/findwm

touch $RPM_BUILD_ROOT/etc/security/blacklist.kdm

cd $RPM_BUILD_ROOT%{_sysconfdir}/kdm
patch -p0  < %{PATCH0}
cd -

ln -s %{_sysconfdir}/kdm/kdmrc $RPM_BUILD_ROOT%{_datadir}/config/kdm/kdmrc

cp -r $RPM_BUILD_ROOT%{_datadir}/apps/{konqueror/dirtree,konqsidebartng/virtual_folders}

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv -f $ALD/{Help.desktop,Help}
mv -f $ALD/{Internet/konqbrowser.desktop,Network/WWW}
mv -f $ALD/{Internet/keditbookmarks.desktop,Utilities}
mv -f $ALD/{System/konsole.desktop,Terminals}
mv -f $ALD/{System/More/{konquerorsu,konsolesu}.desktop,System/Administration}
mv -f $ALD/{Utilities/More/*.desktop,Utilities}
mv -f $ALD/{Settings/[!K]*,Settings/KDE}
mv -f $ALD/{System/kinfocenter.desktop,Settings}
mv -f $ALD/{Settingsmenu/*.desktop,Settings}

cat > $ALD/Settings/KDE/.directory << EOF
[Desktop Entry]
Name=KDE
Icon=kcontrol
X-KDE-BaseGroup=settings
EOF

cat $ALD/Help/Help.desktop |sed 's/Help/KDE Help/' |sed 's/Pomoc/Pomoc KDE/' \
	> Help.desktop.tmp
cat Help.desktop.tmp > $ALD/Help/Help.desktop
rm -f Help.desktop.tmp     

for f in `find $ALD -name '.directory' -o -name '*.dekstop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

> %{name}.lang

programs="kdebugdialog kdeprint kdesu kicker kinfocenter \
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

%post
/sbin/ldconfig
cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir
if [ -x %{_bindir}/xftcache ]; then
    %{_bindir}/xftcache .
fi

%postun
/sbin/ldconfig
cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir
if [ -x %{_bindir}/xftcache ]; then
    %{_bindir}/xftcache .
fi

%post common-konsole
cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir
if [ -x %{_bindir}/xftcache ]; then
    %{_bindir}/xftcache .
fi

%postun common-konsole
cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir
if [ -x %{_bindir}/xftcache ]; then
    %{_bindir}/xftcache .
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

%post   -n konqueror -p /sbin/ldconfig
%postun	-n konqueror -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%config %{_sysconfdir}/ksysguarddrc
%attr(0755,root,root) %{_bindir}/[ades]*
%attr(0755,root,root) %{_bindir}/k[jtx]*
%attr(0755,root,root) %{_bindir}/ka[!t]*
%attr(0755,root,root) %{_bindir}/kcheckpass
%attr(0755,root,root) %{_bindir}/kdc*
%attr(0755,root,root) %{_bindir}/kde[!s]*
%attr(0755,root,root) %{_bindir}/kdes[!u]*
%attr(2755,root,nobody) %{_bindir}/kdesud
%attr(2755,root,nobody) %{_bindir}/kdialog
%attr(0755,root,root) %{_bindir}/khotkeys
%attr(0755,root,root) %{_bindir}/kicker
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

%attr(0755,root,root) %{_libdir}/[ae]*.*
%attr(0755,root,root) %{_libdir}/k[dhijlmsx]*.*
%attr(0755,root,root) %{_libdir}/kaccess.??
%attr(0755,root,root) %{_libdir}/kprinter.??
%attr(0755,root,root) %{_libdir}/kw[!r]*
%attr(0755,root,root) %{_libdir}/kwrited.??

%attr(0755,root,root) %{_libdir}/lib[cdqt]*.*
%attr(0755,root,root) %{_libdir}/libk[hrstw]*.*
%attr(0755,root,root) %{_libdir}/libkickermain.la
%attr(0755,root,root) %{_libdir}/libkickermain.so.*
%attr(0755,root,root) %{_libdir}/libsensordisplays.la
%attr(0755,root,root) %{_libdir}/libsensordisplays.so.*

%attr(0755,root,root) %{_libdir}/kde3/childpanel_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/childpanel_panelextension.so.*
%attr(0755,root,root) %{_libdir}/kde3/clock_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/clock_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/dockbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/dockbar_panelextension.so.*
%attr(0755,root,root) %{_libdir}/kde3/kasbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/kasbar_panelextension.so.*                                   

%attr(0755,root,root) %{_libdir}/kde3/kcm_access.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_arts.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_background.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_bell.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_clock.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_colors.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_componentchooser.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_email.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_energy.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_fontinst.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_helpcenter.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_icons.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_info.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_input.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_ioslaveinfo.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_keyboard.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_keys.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_khotkeys.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_kicker.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_knotify.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_kwindecoration.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_kwinoptions.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_launch.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_locale.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_nic.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_passwords.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_printmgr.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_samba.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_smserver.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_spellchecking.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_style.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_taskbar.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_themes.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_usb.??

%attr(0755,root,root) %{_libdir}/kde3/kickermenu_kdeprint.??                                                    
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_konsole.??                                                     
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_prefmenu.??                                                    
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_recentdocs.??                                                  
%attr(0755,root,root) %{_libdir}/kde3/klipper_panelapplet.??
%attr(0755,root,root) %{_libdir}/kde3/kwin*.??
%attr(0755,root,root) %{_libdir}/kde3/launcher_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/launcher_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/libkdeprint_part.??
%attr(0755,root,root) %{_libdir}/kde3/lockout_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/lockout_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/minipager_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/minipager_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/naughty_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/naughty_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/run_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/run_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/sysguard_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/sysguard_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/systemtray_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/systemtray_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelextension.so.*

%dir %{_datadir}/apps/ksmserver
%dir %{_datadir}/apps/ksplash
%{_datadir}/apps/?[!acdefhosw]*
%{_datadir}/apps/kappfinder
%{_datadir}/apps/kcm[!_c]*
%{_datadir}/apps/kcm_componentchooser/*
%{_datadir}/apps/kconf_update/*
%{_datadir}/apps/kdcop
%{_datadir}/apps/kdeprint/*
%{_datadir}/apps/kdeprint_part
%{_datadir}/apps/kdeprintfax
%{_datadir}/apps/kdesktop
%{_datadir}/apps/kdewizard
%{_datadir}/apps/kdisplay
%{_datadir}/apps/ksysguard
%{_datadir}/apps/kwin
%{_datadir}/apps/naughtyapplet

%{_datadir}/autostart/*
%{_datadir}/config/kdesktop*
%{_datadir}/config/klipperrc
%{_datadir}/config/kwritedrc

%{_datadir}/locale/*

%{_datadir}/services/kaccess.desktop
%{_datadir}/services/kdeprint_part.desktop
%{_datadir}/services/kwrited.desktop
%{_datadir}/services/kxkb.desktop

%{_datadir}/sounds
%{_datadir}/templates

# Font 9x15.pcf.gz conflicts with file from package XFree86-fonts
#%{_fontdir}/misc/9x15.pcf.gz
%{_fontdir}/misc/cursor_large*.gz
%{_fontdir}/misc/cursor_small*.gz

%{_applnkdir}/Home.desktop
%{_applnkdir}/.hidden/[kms][!c]*
%{_applnkdir}/System/k[!o]*.desktop
%{_applnkdir}/Utilities/k[!e]*.desktop
%{_applnkdir}/Settings/[!K]*.desktop
%{_applnkdir}/Settings/KDE/email.desktop
%{_applnkdir}/Settings/KDE/Accessibility
%{_applnkdir}/Settings/KDE/Components/[!f]*
%{_applnkdir}/Settings/KDE/Components/filebrowser.desktop
%{_applnkdir}/Settings/KDE/Desktop
%{_applnkdir}/Settings/KDE/Information
%dir %{_applnkdir}/Settings/KDE/LookNFeel
%{_applnkdir}/Settings/KDE/LookNFeel/.directory
%{_applnkdir}/Settings/KDE/LookNFeel/[!s]*
%{_applnkdir}/Settings/KDE/LookNFeel/s[!c]*
%{_applnkdir}/Settings/KDE/Network/email.desktop
%{_applnkdir}/Settings/KDE/Peripherals
%{_applnkdir}/Settings/KDE/Personalization
%{_applnkdir}/Settings/KDE/PowerControl
%{_applnkdir}/Settings/KDE/Security/passwords.desktop
%{_applnkdir}/Settings/KDE/Sound
%{_applnkdir}/Settings/KDE/System/[!k]*
%{_applnkdir}/Settings/KDE/System/kcmfontinst.desktop
%{_applnkdir}/Settings/KDE/System/kcmhelpcenter.desktop
%{_applnkdir}/Settings/KDE/WebBrowsing

%{_pixmapsdir}/*/*/apps/a[!g]*
%{_pixmapsdir}/*/*/apps/[dghilmnqrtuvwx]*
%{_pixmapsdir}/*/*/apps/b[!e]*
%{_pixmapsdir}/*/*/apps/c[!ao]*
%{_pixmapsdir}/*/*/apps/co[!o]*
%{_pixmapsdir}/*/*/apps/e[!n]*
%{_pixmapsdir}/*/*/apps/en[!h]*
%{_pixmapsdir}/*/*/apps/k[ijlmnptvmx]*
%{_pixmapsdir}/*/*/apps/kappfinder.png
%{_pixmapsdir}/[!l]*/*/apps/kc[!o][!s]*
%{_pixmapsdir}/*/*/apps/kcms[!y]*
%{_pixmapsdir}/*/*/apps/key[!_]*
%{_pixmapsdir}/*/*/apps/ksysguard.png
%{_pixmapsdir}/*/*/apps/kdisk*
%{_pixmapsdir}/*/*/apps/kdeprint*
%{_pixmapsdir}/*/*/apps/kwin.png
%{_pixmapsdir}/*/*/apps/opera*
%{_pixmapsdir}/*/*/apps/p[!er]*
%{_pixmapsdir}/*/*/apps/penguin.png
%{_pixmapsdir}/*/*/apps/printmgr.png
%{_pixmapsdir}/*/*/apps/s[!t]*.png
%{_pixmapsdir}/*/*/apps/staroffice.png
%{_pixmapsdir}/*/*/apps/style.png
#%{_pixmapsdir}/*/*/actions/*
%{_pixmapsdir}/*/*/devices/print_[!c]*
%{_pixmapsdir}/*/*/filesystems/*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/kwin
%{_includedir}/*.h
%{_includedir}/kwin/*.h
%{_includedir}/kate
%{_includedir}/ksgrd
%attr(0755,root,root) %{_libdir}/libkickermain.so
%attr(0755,root,root) %{_libdir}/libsensordisplays.so
%attr(0755,root,root) %{_libdir}/kde3/childpanel_panelextension.so
%attr(0755,root,root) %{_libdir}/kde3/clock_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/dockbar_panelextension.so
%attr(0755,root,root) %{_libdir}/kde3/launcher_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/kasbar_panelextension.so
%attr(0755,root,root) %{_libdir}/kde3/lockout_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/minipager_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/naughty_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/run_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/sysguard_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/systemtray_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelextension.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libccont.a

%files -n kde-sdscreen-default                                                  
%defattr(644,root,root,755)                                                     
%{_datadir}/apps/ksmserver/* 

%files -n kde-splash-default                                                  
%defattr(644,root,root,755)                                                     
%{_datadir}/apps/ksplash/* 

%files common-filemanagement
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/filesharelist
%attr(0755,root,root) %{_bindir}/fileshareset
%attr(0755,root,root) %{_libdir}/libkmultitabbar.*
%attr(0755,root,root) %{_libdir}/libkonsolepart.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_fileshare.??
%attr(0755,root,root) %{_libdir}/kde3/kio_thumbnail.??
%attr(0755,root,root) %{_libdir}/kde3/fontthumbnail.??
%attr(0755,root,root) %{_libdir}/kde3/gsthumbnail.??
%attr(0755,root,root) %{_libdir}/kde3/htmlthumbnail.??
%attr(0755,root,root) %{_libdir}/kde3/imagethumbnail.??
%attr(0755,root,root) %{_libdir}/kde3/picturethumbnail.?? 
%attr(0755,root,root) %{_libdir}/kde3/textthumbnail.??
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
%{_applnkdir}/Settings/KDE/Network/fileshare.desktop

%files common-konsole
%defattr(644,root,root,755)
%{_fontdir}/misc/console*.gz
%{_datadir}/apps/konsole
%{_pixmapsdir}/[!l]*/*/apps/bell.png
%{_pixmapsdir}/*/*/apps/key_bindings.png

%files helpcenter -f khelpcenter.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/khelpcenter
%attr(0755,root,root) %{_libdir}/kde3/kio_info.??
%attr(0755,root,root) %{_libdir}/kde3/kio_man.??
%attr(0755,root,root) %{_libdir}/kde3/khelpcenter.??
%{_datadir}/apps/khelpcenter
%{_datadir}/services/info.protocol
%{_datadir}/services/khelpcenter.desktop
%{_datadir}/services/man.protocol
%{_applnkdir}/Help/Help.desktop
%{_pixmapsdir}/*/*/apps/khelpcenter.png

%files kcontrol
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kcminit
%attr(0755,root,root) %{_bindir}/kcmshell
%attr(0755,root,root) %{_bindir}/kcontrol
%attr(0755,root,root) %{_libdir}/kcminit.??
%attr(0755,root,root) %{_libdir}/kcmshell.??
%attr(0755,root,root) %{_libdir}/kcontrol.??
%attr(0755,root,root) %{_bindir}/kdesu
%{_datadir}/apps/kcontrol
%{_applnkdir}/KControl.desktop
%{_applnkdir}/Settings/KControl.desktop
# At this time owned by kdelibs
#%dir %{_applnkdir}/Settings/KDE
%{_applnkdir}/Settings/KDE/.directory
# At this time owned by kdelibs
#%dir %{_applnkdir}/Settings/KDE/Components
%{_applnkdir}/Settings/KDE/Components/.directory
%dir %{_applnkdir}/Settings/KDE/System
%{_applnkdir}/Settings/KDE/System/.directory
%{_pixmapsdir}/*/*/apps/kcontrol.png
%{_pixmapsdir}/*/*/apps/kcmsystem.png

%lang(en) %dir %{_htmldir}/en/kcontrol
%lang(en) %{_htmldir}/en/kcontrol/common
%lang(en) %{_htmldir}/en/kcontrol/index.*
%lang(en) %{_htmldir}/en/kcontrol/screenshot.png

%files mailnews
%defattr(644,root,root,755)
%attr(0755,root,root) %{_libdir}/kde3/kio_imap4.??
%attr(0755,root,root) %{_libdir}/kde3/kio_nntp.??
%attr(0755,root,root) %{_libdir}/kde3/kio_pop3.??
%attr(0755,root,root) %{_libdir}/kde3/kio_smtp.??
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

#%files screensavers -f libkscreensaver.lang
%files screensavers -f screensaver.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/*.kss
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/kscreensaver
%attr(0755,root,root) %{_libdir}/kde3/kcm_screensaver.??
%{_applnkdir}/Settings/KDE/LookNFeel/screensaver.desktop
%{_applnkdir}/System/ScreenSavers/*
%{_pixmapsdir}/*/*/apps/kscreensaver.png

%files wallpapers
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/krootimage
%{_datadir}/wallpapers

%files kate -f kate.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kate
%attr(0755,root,root) %{_libdir}/kate.??
%attr(0755,root,root) %{_libdir}/libkateinterfaces.??
%{_datadir}/apps/kate
%{_datadir}/servicetypes/kateplugin.desktop
%{_applnkdir}/Editors/kate.desktop
%{_pixmapsdir}/*/*/apps/kate.png

%files -n kdm -f kdm.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/chooser
#%attr(0755,root,root) %{_bindir}/findwm
%attr(0755,root,root) %{_bindir}/kdm*
%attr(0755,root,root) %{_libdir}/kde3/kcm_kdm.??
%dir %{_sysconfdir}/kdm
%config(noreplace) %{_sysconfdir}/kdm/kdmrc
%config(noreplace) %{_sysconfdir}/kdm/backgroundrc
%attr(0755,root,root) %{_sysconfdir}/kdm/Xreset
%attr(0755,root,root) %{_sysconfdir}/kdm/Xsession
%attr(0755,root,root) %{_sysconfdir}/kdm/Xsetup
%attr(0755,root,root) %{_sysconfdir}/kdm/Xstartup
%attr(0755,root,root) %{_sysconfdir}/kdm/Xwilling
%attr(0754,root,root) /etc/rc.d/init.d/kdm
%{_sysconfdir}/kdm/Xaccess
%{_sysconfdir}/kdm/Xservers
%{_datadir}/apps/kdm
%dir %{_datadir}/config/kdm
%{_datadir}/config/kdm/kdmrc
%{_pixmapsdir}/*/*/apps/kdmconfig.png
%{_applnkdir}/Settings/KDE/System/kdm.desktop

%files kfind -f kfind.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kfind
%{_applnkdir}/Kfind.desktop
%{_pixmapsdir}/*/*/apps/kfind.png

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

%attr(0755,root,root) %{_libdir}/keditbookmarks.??
%attr(0755,root,root) %{_libdir}/kfm*.??
%attr(0755,root,root) %{_libdir}/konqueror.??
%attr(0755,root,root) %{_libdir}/libkfindpart.??
%attr(0755,root,root) %{_libdir}/libkonq*.la
%attr(0755,root,root) %{_libdir}/libkonq*.so*
%attr(0755,root,root) %{_libdir}/libnsplugin.la
%attr(0755,root,root) %{_libdir}/libnsplugin.so*

%attr(0755,root,root) %{_libdir}/kde3/kfile_font.??     
%attr(0755,root,root) %{_libdir}/kde3/libkmanpart.??
%attr(0755,root,root) %{_libdir}/kde3/libkshorturifilter.??
%attr(0755,root,root) %{_libdir}/kde3/libkuriikwsfilter.??
%attr(0755,root,root) %{_libdir}/kde3/libkurisearchfilter.??
%attr(0755,root,root) %{_libdir}/kde3/liblocaldomainurifilter.??

%attr(0755,root,root) %{_libdir}/kde3/kcm_cgi.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_crypto.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_css.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_filetypes.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_fonts.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_history.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_kded.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_kio.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_konqhtml.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_konq.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_kurifilt.??

%attr(0755,root,root) %{_libdir}/kde3/kio_about.??
%attr(0755,root,root) %{_libdir}/kde3/kio_cgi.??
%attr(0755,root,root) %{_libdir}/kde3/kio_devices.??
%attr(0755,root,root) %{_libdir}/kde3/kio_filter.??
%attr(0755,root,root) %{_libdir}/kde3/kio_finger.??
%attr(0755,root,root) %{_libdir}/kde3/kio_fish.??
%attr(0755,root,root) %{_libdir}/kde3/kio_floppy.??
%attr(0755,root,root) %{_libdir}/kde3/kio_mac.??
%attr(0755,root,root) %{_libdir}/kde3/kio_nfs.??
%attr(0755,root,root) %{_libdir}/kde3/kio_print.??
%attr(0755,root,root) %{_libdir}/kde3/kio_sftp.??
%attr(0755,root,root) %{_libdir}/kde3/kio_smb.??
%attr(0755,root,root) %{_libdir}/kde3/kio_tar.??
%attr(0755,root,root) %{_libdir}/kde3/kio_zip.??

%attr(0755,root,root) %{_libdir}/kde3/kded_*.??
%attr(0755,root,root) %{_libdir}/kde3/konq*.??

%attr(0755,root,root) %{_libdir}/kde3/plugins/konqueror

%{_datadir}/apps/kcmcss
%{_datadir}/apps/keditbookmarks
%{_datadir}/apps/kfindpart
%{_datadir}/apps/konq*
%{_datadir}/config/konqsidebartng.rc
%{_datadir}/config/kshorturifilterrc
%{_datadir}/config/kuriikwsfilterrc
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

%{_applnkdir}/.hidden/f*
%{_applnkdir}/Network/WWW/konq*.desktop
%{_applnkdir}/Utilities/keditbookmarks.desktop
%{_applnkdir}/Settings/KDE/Components/filetypes.desktop
%{_applnkdir}/Settings/KDE/Network/WebBrowsing
%{_applnkdir}/Settings/KDE/Network/netpref.desktop
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
%{_pixmapsdir}/*/*/apps/fonts.png
%{_pixmapsdir}/*/*/apps/keditbookmarks.png
%{_pixmapsdir}/*/*/apps/kfm*.png
%{_pixmapsdir}/*/*/apps/konqueror.png
%{_pixmapsdir}/*/*/apps/personal.png
%{_pixmapsdir}/*/*/apps/proxy.png
%{_pixmapsdir}/*/*/apps/stylesheet.png

%files konsole -f konsole.lang
%defattr(644,root,root,755)
%doc konsole/README*
%attr(0755,root,root) %{_bindir}/konsole
%attr(6755,root,root) %{_bindir}/konsole_grantpty
%attr(0755,root,root) %{_libdir}/konsole.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_konsole.??
%{_datadir}/config/konsolerc
%dir %{_applnkdir}/.hidden
%{_applnkdir}/.hidden/kcmkonsole.desktop
%{_applnkdir}/System/konsolesu.desktop
%{_applnkdir}/System/Administration/konsolesu.desktop
%{_applnkdir}/Terminals/*.desktop
%{_pixmapsdir}/*/*/apps/konsole.png

%files kwrite -f kwrite.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kwrite
%attr(0755,root,root) %{_libdir}/kwrite.??
%{_datadir}/apps/kwrite
%{_applnkdir}/Editors/kwrite.desktop
%{_pixmapsdir}/*/*/apps/kwrite.png
