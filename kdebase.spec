# TODO:
# - make separate subpackages

%define		_state		unstable
%define		_kdever		kde-3.1-rc1

Summary:	K Desktop Environment - core files
Summary(es):	K Desktop Environment - archivos b·sicos
Summary(ja):	KDE•«•π•Ø•»•√•◊¥ƒ∂≠ - ¥À‹•’•°•§•Î
Summary(ko):    KDE - ±‚∫ª ∆ƒ¿œ
Summary(pl):	K Desktop Environment - pliki ∂rodowiska
Summary(pt_BR):	K Desktop Environment - arquivos b·sicos
Summary(ru):	K Desktop Environment - ¬¡⁄œ◊Ÿ≈ ∆¡ ÃŸ
Summary(uk):	K Desktop Environment - ¬¡⁄œ◊¶ ∆¡ Ã…
Summary(zh_CN): KDE∫À–ƒ
Name:		kdebase
Version:	3.0.9
Release:	2.2
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
Source8:	%{name}-kdm.findwm
Patch0:		%{name}-kdmrc.patch
Patch1:		%{name}-fix-mem-leak-in-kfind.patch
Patch2:		%{name}-dont_merge_old_kdmrc.patch
Patch3:		%{name}-glibc-2.2.2.patch
Patch4:		%{name}-hardcoded_paths.patch
Patch5:		%{name}-kdm.daemon_output.patch
Patch6:		%{name}-kicker.patch
Patch7:		%{name}-konsole_all.patch
Patch8:		%{name}-nsplugins_dirs.patch
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
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
Requires:	applnk >= 1.5.11
Requires:	kdelibs >= %{version}
Requires:	kde-splash
Requires:       kde-sdscreen
Requires:	kfind = %{version}
Requires:	konqueror >= %{version}
Requires:	%{name}-fonts
Requires:	%{name}-kcontrol
Requires:	%{name}-pam
Requires:	%{name}-wallpapers
#
Obsoletes:	%{name}-khelpcenter
Obsoletes:	%{name}-konsole
Obsoletes:	%{name}-screensaver
Obsoletes:	%{name}-kicker
Obsoletes:	%{name}-kioslave
Obsoletes:	%{name}-konqueror
Obsoletes:	%{name}-kwin
Obsoletes:	%{name}-kxmlrpc
Obsoletes:	%{name}-kdesktop
Obsoletes:	%{name}-kwrite
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
KDE•«•π•Ø•»•√•◊¥ƒ∂≠Õ—§Œ¥À‹•¢•◊•Í•±°º•∑•Á•Û°£
∞ ≤º§Œ§Ë§¶§ •—•√•±°º•∏§¨∆˛§√§∆§§§ﬁ§π°£

%description -l pl
Pliki specyficzne dla ∂rodowiska KDE i wykorzystywane przez g≥Ûwne
aplikacje KDE. Pakiet zawiera:
- HierarchiÍ menu KDE,
- kappfinder - skrypt u≥awiaj±cy uruchamianie niektÛrych programÛw
  spoza KDE
- krootwm - modu≥ wykorzystywany przez kwm i kfm
- kaudio - serwer dºwiÍku dla KDE.

%description -l ru
‚¡⁄œ◊Ÿ≈ –“œ«“¡ÕÕŸ ƒÃ— K Desktop Environment. ˜ÀÃ¿ﬁ≈ŒŸ: kdm (⁄¡Õ≈Œ¡
xdm), kwin (œÀœŒŒŸ  Õ≈Œ≈ƒ÷≈“), konqueror (∆¡ Ãœ◊Ÿ  Õ≈Œ≈ƒ÷≈“,
web-¬“¡’⁄≈“, ftp-ÀÃ…≈Œ‘, ...), konsole (⁄¡Õ≈Œ¡ xterm), kicker
(⁄¡–’”À¡ÃÀ¡ –“œ«“¡ÕÕ … –≈ ƒ÷≈“ “¡¬œﬁ≈«œ ”‘œÃ¡), kaudio (¡’ƒ…œ”≈“◊≈“),
kdehelp (–“œ«“¡ÕÕ¡ ƒÃ— –“œ”Õœ‘“¡ ”–“¡◊œﬁŒŸ» ∆¡ Ãœ◊ kde, ∆¡ Ãœ◊ info …
man), kthememgr (”…”‘≈Õ¡ ƒÃ— ’–“¡◊Ã≈Œ…— ¡Ãÿ‘≈“Œ¡‘…◊ŒŸÕ… –¡À≈‘¡Õ… ‘≈Õ)
… ƒ“’«…≈ ÀœÕ–œŒ≈Œ‘Ÿ KDE (kcheckpass, kikbd, kscreensaver, kcontrol,
kfind, kfontmanager, kmenuedit, kappfinder).

%description -l uk
‚¡⁄œ◊¶ –“œ«“¡Õ… ƒÃ— K Desktop Environment. ˜ÀÃ¿ﬁ≈Œ¶: kdm (⁄¡Õ¶Œ¡ xdm),
kwin (◊¶ÀœŒŒŸ  Õ≈Œ≈ƒ÷≈“), konqueror (∆¡ Ãœ◊…  Õ≈Œ≈ƒ÷≈“, web-¬“¡’⁄≈“,
ftp-ÀÃ¶≈Œ‘, ...), konsole (⁄¡Õ¶Œ¡ xterm), kicker (⁄¡–’”À¡ÃÀ¡ –“œ«“¡Õ
‘¡ –≈ ƒ÷≈“ “œ¬œﬁœ«œ ”‘œÃ’), kaudio (¡’ƒ¶œ”≈“◊≈“), kdehelp (–“œ«“¡Õ¡
ƒÃ— –≈“≈«Ã—ƒ’ ∆¡ Ã¶◊ ƒœ◊¶ƒÀ… kde, ∆¡ Ã¶◊ info ‘¡ man), kthememgr
(”…”‘≈Õ¡ ƒÃ— À≈“’◊¡ŒŒ— ¡Ãÿ‘≈“Œ¡‘…◊Œ…Õ… –¡À≈‘¡Õ… ‘≈Õ) ‘¡ ¶Œ€¶
ÀœÕ–œŒ≈Œ‘… KDE (kcheckpass, kikbd, kscreensaver, kcontrol, kfind,
kfontmanager, kmenuedit, kappfinder).

%package devel
Summary:	Include files to develop KDE applications
Summary(pl):	Pliki nag≥Ûwkowe potrzebne do programowania
Summary(pt_BR):	Arquivos de inclus„o para compilar aplicativos que usem bibliotecas do kdebase
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	qt-devel >= 3.0.5
Requires:	kdelibs-devel >= %{version}

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l pl
Pakiet zawiera pliki nag≥Ûwkowe niezbÍdne do programowania aplikacji
KDE.

%description devel -l pt_BR
Este pacote contÈm os arquivos de inclus„o que s„o necess·rios para
compilar aplicativos que usem bibliotecas do kdebase.

%package static
Summary:	Include static libraries to develop KDE applications
Summary(pl):	Statyczne biblioteki KDE
Summary(pt_BR):	Bibliotecas est·ticas do kdebase
Group:		X11/Development/Libraries
Requires:	qt-devel >= 3.0.5
Requires:	kdelibs-devel >= %{version}

%description static
This package contains KDE static libraries.

%description static -l pl
Pakiet zawiera statyczne biblioteki KDE.

%description static -l pt_BR
Bibliotecas est·ticas do kdebase.

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

%package fonts
Summary:	KDE Font Set
Summary(pl):	Zestaw czcionek dla KDE
Group:		X11/Applications
Obsoletes:	%{name} < 3.0.9-2

%description fonts
KDE Font Set

%description fonts -l pl
Zestaw czcionek dla KDE

%package kcontrol
Summary:	KDE Control Center
Summary(pl):	Centrum Sterowania KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	qt >= 3.1
Obsoletes:	%{name} < 3.0.9-2.2

%description kcontrol
KDE Control Center

%description kcontrol -l pl
NarzÍdzie do konfigurowania aplikacji KDE


%package mailnews
Summary:	KDE Mail and News Services
Summary(pl):	Obs≥uga protoko≥Ûw pocztowych i news dla KDE
Group:		X11/Libraries
Requires:	kdelibs >= %{version}
Requires:	qt >= 3.1
Obsoletes:	%{name} < 3.0.9-2
Obsoletes:	%{name}-kioslave

%description mailnews
KDE Mail and News Services

%description mailnews -l pl
Obs≥uga protoko≥Ûw pocztowych i news dla KDE

%package pam
Summary:        KDE User Autentication 
Summary(pl):    Autentykacja uøytkownika dla KDE
Group:          X11/Applications
Obsoletes:	%{name} < 3.0.9-2

%description pam
KDE User Autentication

%description pam -l pl
Autentykacja uøytkownika dla KDE

%package screensavers
Summary:	KDE screensavers
Summary(pl):	Wygaszacze ekranu desktopu KDE
Summary(ru):	»“¡Œ…‘≈Ã… ‹À“¡Œ¡ ƒÃ— KDE
Summary(uk):	⁄¬≈“¶«¡ﬁ¶ ≈À“¡Œ’ ƒÃ— KDE
Group:		X11/Applications
Requires:	OpenGL
Requires:	%{name}-pam
Requires:	kdelibs >= %{version}
Requires:	qt >= 3.1

%description screensavers
KDE screensavers.

%description screensavers -l pl
Wygaszacze ekranu desktopu KDE.

%description screensavers -l ru
Ó≈Àœ‘œ“Ÿ≈ 3D »“¡Œ…‘≈Ã… ‹À“¡Œ¡ ƒÃ— K Desktop Environment.

%package wallpapers
Summary:	KDE Wallpapers
Summary(pl):	Tapety pulpitu dla KDE
Group:		X11/Amusements
Obsoletes:	%{name} < 3.0.9-2

%description wallpapers
KDE Wallpapers

%description wallpapers -l pl
Tapety pulpitu dla KDE.

%package -n kdm
Summary:	KDE Display Manager
Summary(pl):	KDE Display Manager
Group:		X11/Applications
Requires:	%{name}-kcontrol
Requires:	%{name}-pam
Requires:	%{name}-wallpapers
Requires:	kdelibs >= %{version}
Requires:	qt >= 3.1
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

%package -n kfind
Summary:	KDE Find Tool
Summary(pl):	NarzÍdzie do wyszukiwania plikÛw dla KDE
Group:		X11/Applications
Requires:	qt >= 3.1
Requires:	kdelibs >= %{version}
Obsoletes:	%{name} < 3.0.9-2

%description -n kfind
KDE Find Tool

%description -n kfind -l pl
NarzÍdzie do wyszukiwania plikÛw dla KDE

%package -n konqueror
Summary:	Konqueror - web browser and file manager
Summary(pl):	Konqueror - przegl±darka WWW i menedøer plikÛw
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	konsole = %{version}
Requires:	qt >= 3.1
Obsoletes:	kdebase-konqueror

%description -n konqueror
Konqueror is a web browser and file manager similar to MS Internet
Explorer.

%description -n konqueror -l pl
Konqueror jest przegl±dark± WWW i meneøderem plikÛw podobnym do MS
Internet Explorer.

%package -n konsole
Summary:	KDE Terminal Emulator
Summary(pl):	Emulator terminala dla KDE
Group:		X11/Applications
Requires:	%{name}-fonts
Requires:	%{name}-kcontrol
Requires:	kdelibs >= %{version}
Requires:	qt >= 3.1
Obsoletes:	%{name}-konsole
Obsoletes:	%{name} < 3.0.9-2

%description -n konsole
KDE Terminal Emulator

%description -n konsole -l pl
Emulator terminala dla KDE

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
	--enable-final

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
install %{SOURCE8}	$RPM_BUILD_ROOT%{_bindir}/findwm

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

#rm -rf konsole-doc
#mkdir konsole-doc
#cp konsole/README* konsole-doc/

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

> %{name}.lang
#programs="appletproxy childpanelextension clockapplet cupsdconf desktop drkonqi extensionproxy filetypes fontinst htmlsearch kaccess kaddressbook kappfinder kasbarextension kate kcontrol kdcop kdebugdialog kdeprintfax kdesktop kdesktop_lock kdesu kdesud kfind kfindpart kfmclient kfmexec khelpcenter khotkeys kicker kjobviewer klegacyimport kless klipper klock kmcop kmenuedit kminipagerapplet knotify konsole kpager kpartapp kpersonalizer kpm kprinter kreadconfig krunapplet ksmserver ksplash kstart ksysguard ksystemtrayapplet ksystraycmd ktaskbarapplet ktip kxkb libkicker libkickermenu_kdeprint libtaskbar libtaskmanager lockout naughtyapplet nsplugin passwords ppdtranslations quicklauncher taskbarextension"
programs="kate kcontrol kdebugdialog kdeprint kdesu kfind khelpcenter kicker \
kinfocenter kioslave klipper kmenuedit konsole kpager ksysguard kwrite" 
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> %{name}.lang
done

#> kcm.lang
#programs="kcmaccess kcmarts kcmaudiocd kcmbackground kcmbell kcmcolors kcmcrypto kcmcss kcmemail kcmenergy kcmfonts kcmhtmlsearch kcmicons kcminfo kcminput kcmioslaveinfo kcmkclock kcmkdb kcmkeys kcmkicker kcmkio kcmkonq kcmkonqhtml kcmkonsole kcmkurifilt kcmkwindecoration kcmkwintheme kcmkwm kcmlaunch kcmlayout kcmlocale kcmmidi kcmnic kcmnotify kcmsamba kcmscreensaver kcmsmartcard kcmsmserver kcmsocks kcmspellchecking kcmstyle kcmtaskbar kcmthemes kcmusb kcmwidgetsettings"
#for i in $programs; do
#	%find_lang $i --with-kde
#	cat $i.lang >> kcm.lang
#done

#%find_lang kwin --with-kde
#programs="kwin_b2_config kwin_default_config kwin_icewm_config kwin_modernsys_config kwin_quartz_config libkwinb2_config libkwindefault_config libkwinmodernsys_config libkwinquartz_config "
#for i in $programs; do
#	%find_lang $i --with-kde
#	cat $i.lang >> kwin.lang
#done

#> kio.lang
#programs="kio_audiocd kio_finger kio_floppy kio_help kio_imap4 kio_man kio_nfs kio_nntp kio_pop3 kio_print kio_sftp kio_smb kio_smbro kio_smtp"
#for i in $programs; do
#	%find_lang $i --with-kde
#	cat $i.lang >> kio.lang
#done

## KDM:
%find_lang kdm		--with-kde
#%find_lang kdmchooser	--with-kde
#%find_lang kdmconfig	--with-kde
#%find_lang kdmgreet	--with-kde
#cat kdmchooser.lang kdmconfig.lang kdmgreet.lang >> kdm.lang

## KONQUEROR:
%find_lang konqueror	--with-kde
#%find_lang libkonq	--with-kde
#cat libkonq.lang >> konqueror.lang

## SCREENSAVER:
#%find_lang libkscreensaver --with-kde

# Maybe these things should be separated, but now it goes to kdebase:
#cat kcm.lang >> %{name}.lang
#cat kwin.lang >> %{name}.lang
#cat kio.lang >> %{name}.lang

%post
/sbin/ldconfig
if [ -x %{_bindir}/findwm ]; then
	%{_bindir}/findwm
fi

%postun
/sbin/ldconfig
if [ -x %{_bindir}/findwm ]; then
	%{_bindir}/findwm
fi

%post fonts
cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir
%{_bindir}/xset fp rehash
if [ -x %{_bindir}/xftcache ]; then
	%{_bindir}/xftcache .
fi

%postun fonts
cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir
%{_bindir}/xset fp rehash
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
/usr/X11R6/bin/findwm

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
#rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%config %{_sysconfdir}/ksysguarddrc
%attr(0755,root,root) %{_bindir}/[ades]*
%attr(0755,root,root) %{_bindir}/k[aijltwx]*
%attr(0755,root,root) %{_bindir}/kcheckpass
%attr(0755,root,root) %{_bindir}/kdc*
%attr(0755,root,root) %{_bindir}/kde[!s]*
%attr(0755,root,root) %{_bindir}/kdes[!u]*
%attr(0755,root,root) %{_bindir}/kdesu
%attr(2755,root,nobody) %{_bindir}/kdesud
%attr(2755,root,nobody) %{_bindir}/kdialog
%attr(0755,root,root) %{_bindir}/khelpcenter
%attr(0755,root,root) %{_bindir}/khotkeys
%attr(0755,root,root) %{_bindir}/kmenuedit
%attr(0755,root,root) %{_bindir}/kpager
%attr(0755,root,root) %{_bindir}/kpersonalizer
%attr(0755,root,root) %{_bindir}/kpm
%attr(0755,root,root) %{_bindir}/kprinter
%attr(0755,root,root) %{_bindir}/krdb
%attr(0755,root,root) %{_bindir}/kreadconfig
%attr(0755,root,root) %{_bindir}/ks[mty]*
%attr(0755,root,root) %{_bindir}/ksplash

%attr(0755,root,root) %{_libdir}/[ae]*.la
%attr(0755,root,root) %{_libdir}/[ae]*.so*
%attr(0755,root,root) %{_libdir}/k[dhijlmswx]*.la
%attr(0755,root,root) %{_libdir}/k[dhijlmswx]*.so*
%attr(0755,root,root) %{_libdir}/kaccess.??
%attr(0755,root,root) %{_libdir}/kate.la
%attr(0755,root,root) %{_libdir}/kate.so
%attr(0755,root,root) %{_libdir}/kprinter.la
%attr(0755,root,root) %{_libdir}/kprinter.so*
%attr(0755,root,root) %{_libdir}/lib[cdqt]*.la
%attr(0755,root,root) %{_libdir}/lib[cdqt]*.so*
%attr(0755,root,root) %{_libdir}/libk[ahrstw]*.la
%attr(0755,root,root) %{_libdir}/libk[ahrstw]*.so*
%attr(0755,root,root) %{_libdir}/libkickermain.la
%attr(0755,root,root) %{_libdir}/libkickermain.so.*.*.*
%attr(0755,root,root) %{_libdir}/libsensordisplays.la
%attr(0755,root,root) %{_libdir}/libsensordisplays.so.*.*.*

%attr(0755,root,root) %{_libdir}/kde3/childpanel_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/childpanel_panelextension.so.*
%attr(0755,root,root) %{_libdir}/kde3/clock_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/clock_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/dockbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/dockbar_panelextension.so.*
%attr(0755,root,root) %{_libdir}/kde3/fontthumbnail.la                                                          
%attr(0755,root,root) %{_libdir}/kde3/fontthumbnail.so      
%attr(0755,root,root) %{_libdir}/kde3/gsthumbnail.la
%attr(0755,root,root) %{_libdir}/kde3/gsthumbnail.so*
%attr(0755,root,root) %{_libdir}/kde3/i*.??
%attr(0755,root,root) %{_libdir}/kde3/kasbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/kasbar_panelextension.so.*                                   

%attr(0755,root,root) %{_libdir}/kde3/kcm_access.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_arts.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_background.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_bell.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_clock.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_colors.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_componentchooser.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_energy.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_fontinst.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_helpcenter.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_icons.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_info.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_input.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_ioslaveinfo.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_kded.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_keyboard.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_keys.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_khotkeys.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_kicker.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_kio.??
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

%attr(0755,root,root) %{_libdir}/kde3/kded_*.??
%attr(0755,root,root) %{_libdir}/kde3/kfile_font.la                                                             
%attr(0755,root,root) %{_libdir}/kde3/kfile_font.so     
%attr(0755,root,root) %{_libdir}/kde3/khelpcenter.??
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_kdeprint.??                                                    
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_konsole.la                                                     
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_konsole.so                                                     
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_prefmenu.la                                                    
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_prefmenu.so                                                    
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_recentdocs.la                                                  
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_recentdocs.so   
%attr(0755,root,root) %{_libdir}/kde3/klipper_panelapplet.??
%attr(0755,root,root) %{_libdir}/kde3/kwin*.??
%attr(0755,root,root) %{_libdir}/kde3/launcher_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/launcher_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/lockout_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/lockout_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/minipager_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/minipager_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/naughty_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/naughty_panelapplet.so.*
%attr(0755,root,root) %{_libdir}/kde3/picturethumbnail.la                                                       
%attr(0755,root,root) %{_libdir}/kde3/picturethumbnail.so 
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
%attr(0755,root,root) %{_libdir}/kde3/textthumbnail.??

%dir %{_datadir}/apps/ksmserver
%dir %{_datadir}/apps/ksplash
%{_datadir}/apps/?[!cefos]*
%{_datadir}/apps/?c[!mo]*
%{_datadir}/apps/?cm[!c]*
%{_datadir}/apps/kconf_update/*
%{_datadir}/apps/ksysguard
%{_datadir}/autostart/*
%{_datadir}/config/kdesktop*
%{_datadir}/config/klipperrc
%{_datadir}/config/kwritedrc
%{_datadir}/locale/*
%{_datadir}/sounds
%{_datadir}/templates

%{_applnkdir}/Home.desktop
%{_applnkdir}/.hidden/[kms][!c]*
%{_applnkdir}/Editors/*.desktop
%{_applnkdir}/Help/Help.desktop
%{_applnkdir}/System/k[!o]*.desktop
%{_applnkdir}/Utilities/k[!e]*.desktop
%{_applnkdir}/Settings/*.desktop
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
%{_applnkdir}/Settings/KDE/Peripherals
%{_applnkdir}/Settings/KDE/Personalization
%{_applnkdir}/Settings/KDE/PowerControl
%{_applnkdir}/Settings/KDE/Security/passwords.desktop
%{_applnkdir}/Settings/KDE/Sound
%{_applnkdir}/Settings/KDE/System/.directory
%{_applnkdir}/Settings/KDE/System/[!k]*
%{_applnkdir}/Settings/KDE/System/kcm*
%{_applnkdir}/Settings/KDE/WebBrowsing

%{_pixmapsdir}/[!l]*/*/apps/[abcdefghilmnpqrstuvwx]*
%{_pixmapsdir}/[!l]*/*/apps/k[aehijlmnptvwmx]*
%{_pixmapsdir}/[!l]*/*/apps/kc[!o]*
%{_pixmapsdir}/*/*/apps/ksysguard.png
%{_pixmapsdir}/*/*/apps/kdisk*
%{_pixmapsdir}/*/*/apps/kdeprint*
%{_pixmapsdir}/*/*/apps/opera*
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

%files fonts
%defattr(644,root,root,755)
# TODO: file /usr/share/fonts/misc/9x15.pcf.gz from install of kdebase-3.0.3
# conflicts with file from package XFree86-fonts-4.2.0.
#%{_fontdir}/misc/*.gz
%{_fontdir}/misc/console*.gz
%{_fontdir}/misc/cursor_large*.gz
%{_fontdir}/misc/cursor_small*.gz

%files kcontrol
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kcminit
%attr(0755,root,root) %{_bindir}/kcmshell
%attr(0755,root,root) %{_bindir}/kcontrol
%attr(0755,root,root) %{_libdir}/kcminit.??
%attr(0755,root,root) %{_libdir}/kcmshell.??
%attr(0755,root,root) %{_libdir}/kcontrol.??
%{_datadir}/apps/kcontrol
%{_applnkdir}/KControl.desktop
%{_applnkdir}/Settings/KDE/.directory
%{_pixmapsdir}/*/*/apps/kcontrol.png

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
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/kdm
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.kdm

#%files screensavers -f libkscreensaver.lang
%files screensavers
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/*.kss
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/kscreensaver
%attr(0755,root,root) %{_libdir}/kde3/kcm_screensaver.??
%{_applnkdir}/Settings/KDE/LookNFeel/screensaver.desktop
%{_applnkdir}/System/ScreenSavers
%{_pixmapsdir}/*/*/apps/kscreensaver.png

%files wallpapers
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/krootimage
%{_datadir}/wallpapers

%files -f kdm.lang -n kdm
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/chooser
%attr(0755,root,root) %{_bindir}/findwm
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

%files -n kfind
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kfind
%{_applnkdir}/Kfind.desktop
%{_pixmapsdir}/*/*/apps/kfind.png

%files -n konqueror -f konqueror.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/filesharelist
%attr(0755,root,root) %{_bindir}/fileshareset
%attr(0755,root,root) %{_bindir}/keditbookmarks
%attr(0755,root,root) %{_bindir}/keditfiletype
%attr(0755,root,root) %{_bindir}/konqueror
%attr(0755,root,root) %{_bindir}/kfm*
%attr(0755,root,root) %{_bindir}/nspluginscan
%attr(0755,root,root) %{_bindir}/nspluginviewer
%attr(0755,root,root) %{_libdir}/keditbookmarks.la
%attr(0755,root,root) %{_libdir}/keditbookmarks.so
%attr(0755,root,root) %{_libdir}/kfm*.??
%attr(0755,root,root) %{_libdir}/konqueror.la
%attr(0755,root,root) %{_libdir}/konqueror.so*
%attr(0755,root,root) %{_libdir}/libkfindpart.la
%attr(0755,root,root) %{_libdir}/libkfindpart.so
%attr(0755,root,root) %{_libdir}/libkmultitabbar.la
%attr(0755,root,root) %{_libdir}/libkmultitabbar.so*
%attr(0755,root,root) %{_libdir}/libkonq*.la
%attr(0755,root,root) %{_libdir}/libkonq*.so*
%attr(0755,root,root) %{_libdir}/libkonsolepart.la
%attr(0755,root,root) %{_libdir}/libkonsolepart.so
%attr(0755,root,root) %{_libdir}/libnsplugin.la
%attr(0755,root,root) %{_libdir}/libnsplugin.so*

%attr(0755,root,root) %{_libdir}/kde3/htmlthumbnail.la
%attr(0755,root,root) %{_libdir}/kde3/htmlthumbnail.so*

%attr(0755,root,root) %{_libdir}/kde3/kcm_cgi.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_crypto.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_css.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_email.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_fileshare.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_filetypes.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_fonts.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_history.??
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
%attr(0755,root,root) %{_libdir}/kde3/kio_info.??
%attr(0755,root,root) %{_libdir}/kde3/kio_mac.??
%attr(0755,root,root) %{_libdir}/kde3/kio_man.??
%attr(0755,root,root) %{_libdir}/kde3/kio_nfs.??
%attr(0755,root,root) %{_libdir}/kde3/kio_print.??
%attr(0755,root,root) %{_libdir}/kde3/kio_sftp.??
%attr(0755,root,root) %{_libdir}/kde3/kio_smb.??
%attr(0755,root,root) %{_libdir}/kde3/kio_tar.??
%attr(0755,root,root) %{_libdir}/kde3/kio_thumbnail.??
%attr(0755,root,root) %{_libdir}/kde3/kio_zip.??

%attr(0755,root,root) %{_libdir}/kde3/konq*.??

%attr(0755,root,root) %{_libdir}/kde3/lib*     
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
%{_datadir}/services/fontthumbnail.desktop
%{_datadir}/services/gsthumbnail.desktop
%{_datadir}/services/gzip.protocol
%{_datadir}/services/htmlthumbnail.desktop
%{_datadir}/services/imagethumbnail.desktop
%{_datadir}/services/info.protocol
%{_datadir}/services/kaccess.desktop
%{_datadir}/services/kdeprint_part.desktop
%{_datadir}/services/kfile_font.desktop
%{_datadir}/services/kfindpart.desktop
%{_datadir}/services/khelpcenter.desktop
%{_datadir}/services/kmanpart.desktop
%{_datadir}/services/konq*
%{_datadir}/services/konsolepart.desktop
%{_datadir}/services/kshorturifilter.desktop
%{_datadir}/services/kuriikwsfilter.desktop
%{_datadir}/services/kurisearchfilter.desktop
%{_datadir}/services/kwrited.desktop
%{_datadir}/services/kxkb.desktop
%{_datadir}/services/localdomainurifilter.desktop
%{_datadir}/services/mac.protocol
%{_datadir}/services/man.protocol
%{_datadir}/services/nfs.protocol
%{_datadir}/services/picturethumbnail.desktop
%{_datadir}/services/print.protocol
%{_datadir}/services/sftp.protocol
%{_datadir}/services/smb.protocol
%{_datadir}/services/tar.protocol
%{_datadir}/services/textthumbnail.desktop
%{_datadir}/services/thumbnail.protocol
%{_datadir}/services/zip.protocol
%{_datadir}/servicetypes/*

%{_applnkdir}/.hidden/f*
%{_applnkdir}/Network/WWW/konq*.desktop
%{_applnkdir}/Utilities/keditbookmarks.desktop
%{_applnkdir}/Settings/KDE/Components/.directory
%{_applnkdir}/Settings/KDE/Components/filetypes.desktop
%{_applnkdir}/Settings/KDE/Network
%dir %{_applnkdir}/Settings/KDE/Security
%{_applnkdir}/Settings/KDE/Security/.directory
%{_applnkdir}/Settings/KDE/Security/crypto.desktop
%{_applnkdir}/System/konq*.desktop
%{_applnkdir}/System/Administration/konq*.desktop

%{_pixmapsdir}/*/*/apps/kfm*.png
%{_pixmapsdir}/*/*/apps/konqueror.png

%files -n konsole
%defattr(644,root,root,755)
%doc konsole/README*
%attr(0755,root,root) %{_bindir}/konsole
%attr(6755,root,root) %{_bindir}/konsole_grantpty
%attr(0755,root,root) %{_libdir}/konsole.la
%attr(0755,root,root) %{_libdir}/konsole.so
%attr(0755,root,root) %{_libdir}/kde3/kcm_konsole.??
%{_datadir}/apps/konsole
%{_datadir}/config/konsolerc
%dir %{_applnkdir}/.hidden
%{_applnkdir}/.hidden/kcmkonsole.desktop
%{_applnkdir}/System/konsolesu.desktop
%{_applnkdir}/System/Administration/konsolesu.desktop
%{_applnkdir}/Terminals/*.desktop
%{_pixmapsdir}/*/*/apps/konsole.png
