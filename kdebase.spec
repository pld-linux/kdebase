# TODO:
# - make separate subpackages
# - -avoid-version for kde3/* applets/extensions?
#
# Conditional build:
# _with_pixmapsubdirs - leave different depth/resolution icons
#
Summary:	K Desktop Environment - core files
Summary(es):	K Desktop Environment - archivos b·sicos
Summary(ja):	KDE•«•π•Ø•»•√•◊¥ƒ∂≠ - ¥À‹•’•°•§•Î
Summary(ko):	KDE - ±‚∫ª ∆ƒ¿œ
Summary(pl):	K Desktop Environment - pliki ∂rodowiska
Summary(pt_BR):	K Desktop Environment - arquivos b·sicos
Summary(ru):	K Desktop Environment - ¬¡⁄œ◊Ÿ≈ ∆¡ ÃŸ
Summary(uk):	K Desktop Environment - ¬¡⁄œ◊¶ ∆¡ Ã…
Summary(zh_CN): KDE∫À–ƒ
Name:		kdebase
Version:	3.0.4
Release:	9
Epoch:		7
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	kdm.pamd
Source3:	kdm.init
Source4:	kdm.Xsession
Source5:	%{name}-extra_icons.tar.bz2
Source6:	%{name}-kscreensaver.pam
Source7:	%{name}-kdm.Xservers
Patch0:		%{name}-kdmrc.patch
Patch1:		%{name}-konsole-TERM.patch
Patch2:		%{name}-glibc-2.2.2.patch
Patch3:		%{name}-utmp.patch
Patch4:		%{name}-nsplugins_dirs.patch
Patch5:		%{name}-hardcoded_paths.patch
Patch6:		%{name}-kdm.daemon_output.patch
Patch7:		%{name}-startkde.patch
Patch8:		%{name}-dont_merge_old_kdmrc.patch
Patch9:		%{name}-konsole-defaultfonts.patch
Patch10:	%{name}-konsoleF1.patch
Patch11:	%{name}-linebreaks.patch
Patch12:	%{name}-ptsname.patch
Patch13:	%{name}-no_versioned_modules.patch
Patch14:	%{name}-desktop.patch
Patch15:	%{name}-dont_overwrite_our_desktops.patch
Patch20:	%{name}-fix-klipper-bug-41137.patch
Patch21:	%{name}-fix-konsole-bug-37890.patch
Patch22:	%{name}-fix-mem-leak-in-kdesktop.patch
Patch23:	%{name}-fix-mem-leak-in-kfind.patch
Patch24:	%{name}-fix-mem-leak-in-kxkb.patch
Patch25:	%{name}-kicker.patch
Patch26:	%{name}-dtfix.patch
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
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	zlib-devel
# TODO: sensors
#BuildRequires:	sensors-devel
Requires(post,postun):	/sbin/ldconfig
Prereq:		/usr/X11R6/bin/mkfontdir
Requires:	applnk
Requires:	kdelibs >= %{version}
Requires:	kde-splash
Requires:       kde-sdscreen
Requires:	konqueror >= %{version}
Obsoletes:	%{name}-kcontrol
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix 	/usr/X11R6
%define		_fontdir 	/usr/share/fonts
%define		_htmldir	/usr/share/doc/kde/HTML
%define		_sysconfdir	/etc/X11

%define		no_install_post_chrpath		0

%description
KDE specific files. Used by core KDE applications. Package includes:

- KDE menu hierarchy,
- kappfinder - script installing some non-KDE apps in KDE menu,
- krootwm - module used by KWM and KFM,
- kaudio - audio server for KDE.

%description -l es
Aplicaciones b·sicas para KDE. Incluidos en este paquete:

- kcontrol - herramienta de configuraciÛn,
- kdm - substituto del xdm,
- kfind - herramienta de b˙squeda,
- konqueror - administrador de archivos, browser, cliente ftp,
- kmenuedit - herramienta para adicionar aplicaciÛn al panel,
- kicker - paginador del ·rea de trabajo,
- konsole - substituto del xterm,
- kwin - administrador de ventanas del kde.

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

%description -l pt_BR
AplicaÁıes b·sicas para o KDE. IncluÌdos neste pacote:

- kcontrol - ferramenta de configuraÁ„o,
- kdm - substituto do xdm,
- kfind - ferramenta de busca,
- konqueror - gerenciador de arquivos, browser, cliente ftp,
- kmenuedit - ferramenta para adicionar aplicaÁ„o ao painel,
- kicker - paginador da ·rea de trabalho,
- konsole - substituto do xterm,
- kwin - gerenciador de janelas do kde.

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

%package -n kdm
Summary:	KDE Display Manager
Summary(pl):	KDE Display Manager
Group:		X11/Applications
Requires:	qt >= 3.0.5
Requires:	kdelibs >= %{version}
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

%package -n konqueror
Summary:	Konqueror - web browser and file manager
Summary(pl):	Konqueror - przegl±darka WWW i menedøer plikÛw
Group:		X11/Applications
Requires:	qt >= 3.0.5
Requires:	kdelibs >= %{version}
Obsoletes:	kdebase-konqueror

%description -n konqueror
Konqueror is a web browser and file manager similar to MS Internet
Explorer.

%description -n konqueror -l pl
Konqueror jest przegl±dark± WWW i meneøderem plikÛw podobnym do MS
Internet Explorer.

%package screensavers
Summary:	KDE screensavers
Summary(pl):	Wygaszacze ekranu desktopu KDE
Summary(ru):	»“¡Œ…‘≈Ã… ‹À“¡Œ¡ ƒÃ— KDE
Summary(uk):	⁄¬≈“¶«¡ﬁ¶ ≈À“¡Œ’ ƒÃ— KDE
Group:		X11/Applications
Requires:	qt >= 3.0.5
Requires:	kdelibs >= %{version}
Requires:	OpenGL

%description screensavers
KDE screensavers.

%description screensavers -l pl
Wygaszacze ekranu desktopu KDE.

%description screensavers -l ru
Ó≈Àœ‘œ“Ÿ≈ 3D »“¡Œ…‘≈Ã… ‹À“¡Œ¡ ƒÃ— K Desktop Environment.

%package -n kde-splash-default
Summary:	KDE splash screen
Summary(pl):	Obrazek startowy KDE
Group:		X11/Amusements
Provides:	kde-splash
Obsoletes:	kde-splash
Obsoletes:	kde-splash-KDEGirl
Obsoletes:	kde-splash-keramik

%description -n kde-splash-default
Default splash screen for KDE.

%description -n kde-splash-default -l pl
Standardowy obrazek startowy KDE.

%package -n kde-sdscreen-default
Summary:        KDE "Logout" picture
Summary(pl):    Obrazek okna "Wyloguj" KDE
Group:          X11/Amusements
Provides:       kde-sdscreen
Obsoletes:      kde-sdscreen
Obsoletes:	kde-sdscreen-KDEGirl

%description -n kde-sdscreen-default
Default KDE "Logout" picture.

%description -n kde-sdscreen-default -l pl
Standardowy obrazek okna "Wyloguj" KDE. 

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
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1

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
	--disable-rpath \
	--with-xdmdir="%{_sysconfdir}/kdm" \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Amusements,Editors,Help,Network/WWW,Utilities,Settings/KDE,System/Administration,Terminals} \
	$RPM_BUILD_ROOT/etc/{pam.d,security,rc.d/init.d,X11/kdm}

%{__make} install \
 	DESTDIR="$RPM_BUILD_ROOT" \
 	fontdir="%{_fontdir}/misc"

# remove icons corresponding to ones used by applnk
%{!?_with_pixmapsubdirs:rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/apps/package_{applications,editors,edutainment,games{,_arcade,_board,_card,_strategy},graphics,multimedia,network,settings,system,toys,utilities,wordprocessing}.png}

# rename to avoid conflict with netscape icon
for i in $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/apps/netscape.png
do
	mv $i `echo $i | sed 's:/netscape:/netscape-plugins:'`
done

# create in toplevel %%{_pixmapsdir} links to icons
for i in $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/{access,agent,bell,colors,cookie,date,designer,email,energy,energy_star,enhanced_browsing,filetypes,fonts,go,gvim,help_index,hwinfo,icons,input_devices_settings}.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/{kaddressbook,kappfinder,kate,kcmdevices,kcmfontinst,kcmkwm,kcmmemory,kcmmidi,kcmpartitions,kcmpci,kcmprocessor,kcmscsi,kcmsystem,kcontrol,kdmconfig,key_bindings}.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/{keyboard,kfind,kfm,kfm_home,khelpcenter,klipper,kmenuedit,knotify,konqueror,konsole,kpager,kscreensaver,ksysguard,kthememgr,ktip,kwrite,licq,locale,looknfeel,mouse}.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/{multimedia,netscape-plugins,password,personal,proxy,samba,style,stylesheet,usb,window_list}.png
do
%if %{?_with_pixmapsubdirs:1}%{!?_with_pixmapsubdirs:0}
	ln -sf `echo $i | sed "s:^$RPM_BUILD_ROOT%{_pixmapsdir}/::"` $RPM_BUILD_ROOT%{_pixmapsdir}	
%else
	cp -af $i $RPM_BUILD_ROOT%{_pixmapsdir}
%endif
done

bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}

%if %{!?_with_pixmapsubdirs:1}%{?_with_pixmapsubdirs:0}
# we have own
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{emacs,gimp,mozilla,netscape,opera,xedit,xemacs,xmag,xv}.png
# moved
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{access,agent,bell,colors,cookie,date,designer,email,energy,energy_star,enhanced_browsing,filetypes,fonts,go,gvim,help_index,hwinfo,icons,input_devices_settings}.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{kaddressbook,kappfinder,kate,kcmdevices,kcmfontinst,kcmkwm,kcmmemory,kcmmidi,kcmpartitions,kcmpci,kcmprocessor,kcmscsi,kcmsystem,kcontrol,kdmconfig,key_bindings}.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{keyboard,kfind,kfm,kfm_home,khelpcenter,klipper,kmenuedit,knotify,konqueror,konsole,kpager,kscreensaver,ksysguard,kthememgr,ktip,kwrite,licq,locale,looknfeel,mouse}.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{multimedia,netscape-plugins,password,personal,proxy,samba,style,stylesheet,usb,window_list}.png \
# resized
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{background,kcmsound,printmgr,cache,kcmx,kcmkicker,keditbookmarks}.png
# moved to kdelibs
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/arts.png
%endif

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

# Patch kdmrc. It is generated so it can not be patched in %%prep.
cd $RPM_BUILD_ROOT%{_datadir}/config/kdm
patch -p0  < %{PATCH0}
cd -

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv -f $ALD/{Internet/konqbrowser.desktop,Network/WWW}
mv -f $ALD/{Internet/keditbookmarks.desktop,Network/WWW}
mv -f $ALD/{Toys/ktip.desktop,Amusements}
mv -f $ALD/{System/konsole.desktop,Terminals}
mv -f $ALD/{System/{konquerorsu,konsolesu}.desktop,System/Administration}
mv -f $ALD/{System/{kappfinder,kmenuedit,kpersonalizer}.desktop,Utilities}
mv -f $ALD/{Help.desktop,Help}

install %{SOURCE2}			$RPM_BUILD_ROOT/etc/pam.d/kdm
install %{SOURCE6}			$RPM_BUILD_ROOT/etc/pam.d/kscreensaver
install %{SOURCE3}			$RPM_BUILD_ROOT/etc/rc.d/init.d/kdm

mv \
	$RPM_BUILD_ROOT%{_datadir}/config/kdm/{Xaccess,Xreset,Xservers,Xsession,Xsetup,Xstartup,Xwilling} \
	$RPM_BUILD_ROOT%{_sysconfdir}/kdm/

install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xservers

# This file is referenced in several dozens places in code and
# documentation. Maintaining patch wich changes all these places would
# be a real PITA.
ln -s ../../../%{_datadir}/config/kdm/kdmrc $RPM_BUILD_ROOT%{_sysconfdir}/kdm/kdmrc

install %{SOURCE4}			$RPM_BUILD_ROOT%{_sysconfdir}/kdm/Xsession

# Make Control Center a subdirectory of Settings. Control Center applets can
# not be mixed with normal programs or CC will die on startup.
mv -f $RPM_BUILD_ROOT%{_applnkdir}/Settings/{[!K]*,KDE}
cat > $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/.directory << EOF
[Desktop Entry]
Name=KDE
Icon=go
X-KDE-BaseGroup=settings
EOF

# removing unneeded directories
# XXX rm -rf $RPM_BUILD_ROOT%{_applnkdir}/{Editors,Toys}

for f in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory' -o -name '*.desktop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.xpm$/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done
for f in `find $RPM_BUILD_ROOT%{_datadir}/apps/kappfinder/apps -name '*.desktop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.xpm$/&& !/\.png$/ { $0 = $0 ".png";} { print $0; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

touch $RPM_BUILD_ROOT/etc/security/blacklist.kdm
mkdir konsole-doc
cp konsole/README* konsole-doc/


> %{name}.lang
programs="appletproxy childpanelextension clockapplet cupsdconf desktop drkonqi extensionproxy filetypes fontinst htmlsearch kaccess kaddressbook kappfinder kasbarextension kate kcontrol kdcop kdebugdialog kdeprintfax kdesktop kdesktop_lock kdesu kdesud kfind kfindpart kfmclient kfmexec khelpcenter khotkeys kicker kjobviewer klegacyimport kless klipper klock kmcop kmenuedit kminipagerapplet knotify konsole kpager kpartapp kpersonalizer kpm kprinter kreadconfig krunapplet ksmserver ksplash kstart ksysguard ksystemtrayapplet ksystraycmd ktaskbarapplet ktip kxkb libkicker libkickermenu_kdeprint libtaskbar libtaskmanager lockout naughtyapplet nsplugin passwords ppdtranslations quicklauncher taskbarextension"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> %{name}.lang
done

> kcm.lang
programs="kcmaccess kcmarts kcmaudiocd kcmbackground kcmbell kcmcolors kcmcrypto kcmcss kcmemail kcmenergy kcmfonts kcmhtmlsearch kcmicons kcminfo kcminput kcmioslaveinfo kcmkclock kcmkdb kcmkeys kcmkicker kcmkio kcmkonq kcmkonqhtml kcmkonsole kcmkurifilt kcmkwindecoration kcmkwintheme kcmkwm kcmlaunch kcmlayout kcmlocale kcmmidi kcmnic kcmnotify kcmsamba kcmscreensaver kcmsmartcard kcmsmserver kcmsocks kcmspellchecking kcmstyle kcmtaskbar kcmthemes kcmusb kcmwidgetsettings"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kcm.lang
done

%find_lang kwin --with-kde
programs="kwin_b2_config kwin_default_config kwin_icewm_config kwin_modernsys_config kwin_quartz_config libkwinb2_config libkwindefault_config libkwinmodernsys_config libkwinquartz_config "
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kwin.lang
done

> kio.lang
programs="kio_audiocd kio_finger kio_floppy kio_help kio_imap4 kio_man kio_nfs kio_nntp kio_pop3 kio_print kio_sftp kio_smb kio_smbro kio_smtp"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kio.lang
done

## KDM:
%find_lang kdm		--with-kde
%find_lang kdmchooser	--with-kde
%find_lang kdmconfig	--with-kde
%find_lang kdmgreet	--with-kde
cat kdmchooser.lang kdmconfig.lang kdmgreet.lang >> kdm.lang

## KONQUEROR:
%find_lang konqueror	--with-kde
%find_lang libkonq	--with-kde
cat libkonq.lang >> konqueror.lang

## SCREENSAVER:
%find_lang libkscreensaver --with-kde

# Maybe these things should be separated, but now it goes to kdebase:
cat kcm.lang >> %{name}.lang
cat kwin.lang >> %{name}.lang
cat kio.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun
/sbin/ldconfig
cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir

%post   -n konqueror -p /sbin/ldconfig
%postun	-n konqueror -p /sbin/ldconfig

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
%doc AUTHORS README* konsole-doc
%config %{_sysconfdir}/ksysguarddrc
%attr(0755,root,root) %{_bindir}/[ades]*
%attr(0755,root,root) %{_bindir}/conttest
%attr(0755,root,root) %{_bindir}/k[aijtwx]*
%attr(0755,root,root) %{_bindir}/kc[!h]*
%attr(6755,root,root) %{_bindir}/kcheckpass
%attr(0755,root,root) %{_bindir}/keditfiletype
%attr(0755,root,root) %{_bindir}/kdc*
%attr(0755,root,root) %{_bindir}/kde[!s]*
%attr(0755,root,root) %{_bindir}/kdes[!u]*
%attr(0755,root,root) %{_bindir}/kdesu
%attr(2755,root,nobody) %{_bindir}/kdesud
%attr(0755,root,root) %{_bindir}/kfind
%attr(0755,root,root) %{_bindir}/kpm
%attr(0755,root,root) %{_bindir}/konsole
%attr(6755,root,root) %{_bindir}/konsole_grantpty
%attr(0755,root,root) %{_bindir}/khelpcenter
%attr(0755,root,root) %{_bindir}/khotkeys
%attr(0755,root,root) %{_bindir}/klipper
%attr(0755,root,root) %{_bindir}/ks[mty]*
%attr(0755,root,root) %{_bindir}/ksplash
%attr(0755,root,root) %{_bindir}/krdb
%attr(0755,root,root) %{_bindir}/kreadconfig
%attr(0755,root,root) %{_bindir}/kpager
%attr(0755,root,root) %{_bindir}/kprinter
%attr(0755,root,root) %{_bindir}/kpersonalizer
%attr(0755,root,root) %{_bindir}/kmenuedit

%attr(0755,root,root) %{_libdir}/[ae]*.so*
%attr(0755,root,root) %{_libdir}/k[dhijlmswx]*.so*
%attr(0755,root,root) %{_libdir}/kaccess.??
%attr(0755,root,root) %{_libdir}/kate.so
%attr(0755,root,root) %{_libdir}/kcminit.??
%attr(0755,root,root) %{_libdir}/kcmshell.??
%attr(0755,root,root) %{_libdir}/kcontrol.??
%attr(0755,root,root) %{_libdir}/konsole.so*
%attr(0755,root,root) %{_libdir}/lib[cdqt]*.so*
%attr(0755,root,root) %{_libdir}/libk[ahmrstw]*.so*
%attr(0755,root,root) %{_libdir}/libkickermain.so.*.*.*
%attr(0755,root,root) %{_libdir}/libkfindpart.??
%attr(0755,root,root) %{_libdir}/libsensordisplays.so.*.*.*
%attr(0755,root,root) %{_libdir}/libkonsolepart.so*

# We have to include *.so.1 sym-links, as ldconfig doesn't touch
# %{_libdir}/kde3
%attr(0755,root,root) %{_libdir}/kde3/childpanel_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/childpanel_panelextension.so
%attr(0755,root,root) %{_libdir}/kde3/clock_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/clock_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/dockbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/dockbar_panelextension.so
%attr(0755,root,root) %{_libdir}/kde3/kasbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/kasbar_panelextension.so*
%attr(0755,root,root) %{_libdir}/kde3/launcher_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/launcher_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/lockout_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/lockout_panelapplet.so*
%attr(0755,root,root) %{_libdir}/kde3/minipager_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/minipager_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/naughty_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/naughty_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/run_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/run_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/sysguard_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/sysguard_panelapplet.so*
%attr(0755,root,root) %{_libdir}/kde3/systemtray_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/systemtray_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelapplet.so
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelextension.la
%attr(0755,root,root) %{_libdir}/kde3/taskbar_panelextension.so
%attr(0755,root,root) %{_libdir}/kde3/i*.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_[!k]*.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_k[ehinuw]*.??
%attr(0755,root,root) %{_libdir}/kde3/kcm_konsole.??
%attr(0755,root,root) %{_libdir}/kde3/kded_*.??
%attr(0755,root,root) %{_libdir}/kde3/khelpcenter.??
%attr(0755,root,root) %{_libdir}/kde3/kio_*.??
%attr(0755,root,root) %{_libdir}/kde3/kickermenu_kdeprint.??
%attr(0755,root,root) %{_libdir}/kde3/klipper_panelapplet.??
%attr(0755,root,root) %{_libdir}/kde3/kwin*.??
%attr(0755,root,root) %{_libdir}/kde3/libkcm_[abcefilmptu]*.la
%attr(0755,root,root) %{_libdir}/kde3/libkcm_[abcefilmptu]*.so
%attr(0755,root,root) %{_libdir}/kde3/libk[fsuw]*.la
%attr(0755,root,root) %{_libdir}/kde3/libk[fsuw]*.so

%attr(0755,root,root) %{_libdir}/kde3/lib*kdeprint*.la
%attr(0755,root,root) %{_libdir}/kde3/lib*kdeprint*.so
%attr(0755,root,root) %{_libdir}/kde3/libkhelp*.la
%attr(0755,root,root) %{_libdir}/kde3/libkhelp*.so
%attr(0755,root,root) %{_libdir}/kde3/gsthumbnail.la
%attr(0755,root,root) %{_libdir}/kde3/gsthumbnail.so
%attr(0755,root,root) %{_libdir}/kde3/textthumbnail.??

# NOTE:	There are many directories created by kappfinder. They should be
#	ignored as such functionality is provided by applnk package and
#	*.dekstop files from apropriate packages.
%{_applnkdir}/Help/Help.desktop
%{_applnkdir}/Home.desktop
%{_applnkdir}/KControl.desktop
%{_applnkdir}/Kfind.desktop
%{_applnkdir}/.hidden/konqfilemgr.desktop
%{_applnkdir}/Amusements/*.desktop
%{_applnkdir}/Editors/k*.desktop
%{_applnkdir}/Settings/KDE/Help
%{_applnkdir}/Settings/KDE/Databases
%{_applnkdir}/Settings/KDE/Information
%dir %{_applnkdir}/Settings/KDE/LookNFeel
%{_applnkdir}/Settings/KDE/LookNFeel/s[!c]*
%{_applnkdir}/Settings/KDE/LookNFeel/[!s]*
%{_applnkdir}/Settings/KDE/LookNFeel/.directory
%{_applnkdir}/Settings/KDE/Network
%{_applnkdir}/Settings/KDE/Peripherals
%{_applnkdir}/Settings/KDE/Personalization
%{_applnkdir}/Settings/KDE/PowerControl
%{_applnkdir}/Settings/KDE/Sound
%dir %{_applnkdir}/Settings/KDE/System
%{_applnkdir}/Settings/KDE/System/[!k]*
%{_applnkdir}/Settings/KDE/System/kcm*
%{_applnkdir}/Settings/KDE/System/.directory
%{_applnkdir}/System/k[!o]*.desktop
%{_applnkdir}/System/Administration/konsolesu.desktop
%{_applnkdir}/Terminals/*.desktop
%{_applnkdir}/Utilities/[!o]*.desktop
# No idea what it is for...
#%{_applnkdir}/ksysguard

%{_datadir}/apps/[cdn]*
%{_datadir}/apps/k[bfhijmtw]*
%{_datadir}/apps/ka[dp]*
%{_datadir}/apps/kate/*
%{_datadir}/apps/kcm*
%{_datadir}/apps/kconf_update/*
%{_datadir}/apps/kcontrol
%{_datadir}/apps/kd[ci]*
%{_datadir}/apps/kde[sw]*
%{_datadir}/apps/kdeprint[_f]*
%{_datadir}/apps/kdeprint/*
%{_datadir}/apps/konsole
%{_datadir}/apps/kpersonalizer
%dir %{_datadir}/apps/ksplash
%{_datadir}/apps/ksysguard
%{_datadir}/apps/klipper

%{_datadir}/autostart/*
%{_datadir}/config/k[!d]*
%{_datadir}/config/kdesktop*
%dir %{_datadir}/locale/l10n
%dir %{_datadir}/locale/l10n/C
%dir %{_datadir}/locale/l10n/??
#%{_datadir}/locale/en_US
%{_datadir}/locale/l10n/*/entry.desktop
%{_datadir}/locale/l10n/*/flag.png
%{_datadir}/locale/*/*.desktop
%{_datadir}/locale/*/*.png
%{_datadir}/locale/*/charset
%{_datadir}/mimelnk/application/*
%{_datadir}/mimelnk/print
%{_datadir}/services/[abfgimnpst]*
%{_datadir}/services/k[afhsuwx]*
%{_datadir}/services/kded/*
%{_datadir}/services/kdeprint_part.desktop
%{_datadir}/services/kons*
%{_datadir}/sounds/*
%{_datadir}/templates
%{_datadir}/wallpapers
%{_datadir}/servicetypes/[fstu]*.desktop

%{_pixmapsdir}/*/*/apps/[a-il-npr-uwx]*.png
%{_pixmapsdir}/[a-il-npr-uwx]*.png
%{_pixmapsdir}/*/*/apps/k[acefhijlmnptwm]*.png
%{_pixmapsdir}/k[acefhijlmnptwm]*.png
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/konsole.png}
%{_pixmapsdir}/konsole.png
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/ksysguard.png}
%{_pixmapsdir}/ksysguard.png
%{_pixmapsdir}/*/*/apps/kdisk*
%{_pixmapsdir}/*/*/apps/kdeprint*
#%{_pixmapsdir}/*/*/apps/opera*

%{_pixmapsdir}/*/*/actions/*
%{_pixmapsdir}/*/*/devices/*
%{_pixmapsdir}/*/*/filesystems/*

# Few docs:
#/usr/share/doc/kde/HTML/*/*/*

# TODO:	file /usr/share/fonts/misc/9x15.pcf.gz from install of kdebase-3.0.3
# 	conflicts with file from package XFree86-fonts-4.2.0.
%{_fontdir}/misc/console8*.gz
#%{_fontdir}/misc/cursor_large*.gz
#%{_fontdir}/misc/*.gz

%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/kscreensaver
# Must be here. kcheckpass needs it.
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/kdm
%attr(0640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.kdm

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/kwin
%{_includedir}/*.h
%{_includedir}/kwin/*.h
%{_includedir}/kate/*.h
%{_includedir}/ksgrd
%attr(0755,root,root) %{_libdir}/libkickermain.so
%attr(0755,root,root) %{_libdir}/libsensordisplays.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libccont.a

%files -f kdm.lang -n kdm
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/chooser
%attr(0755,root,root) %{_bindir}/kdm*
%attr(0755,root,root) %{_libdir}/kde3/kcm_kdm.??
%dir %{_sysconfdir}/kdm
%{_sysconfdir}/kdm/kdmrc
%{_sysconfdir}/kdm/Xaccess
%{_sysconfdir}/kdm/Xservers
%attr(0755,root,root) %{_sysconfdir}/kdm/Xreset
%attr(0755,root,root) %{_sysconfdir}/kdm/Xsession
%attr(0755,root,root) %{_sysconfdir}/kdm/Xsetup
%attr(0755,root,root) %{_sysconfdir}/kdm/Xstartup
%attr(0755,root,root) %{_sysconfdir}/kdm/Xwilling
%attr(0754,root,root) /etc/rc.d/init.d/kdm
%{_applnkdir}/Settings/KDE/System/kdm.desktop
%{_datadir}/apps/kdm
%dir %{_datadir}/config/kdm
%config(noreplace) %{_datadir}/config/kdm/kdmrc

%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kdmconfig.png}
%{_pixmapsdir}/kdmconfig.png

%files -n konqueror -f konqueror.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/keditbookmarks
%attr(0755,root,root) %{_bindir}/konqueror
%attr(0755,root,root) %{_bindir}/kfm*
%attr(0755,root,root) %{_bindir}/nspluginscan
%attr(0755,root,root) %{_bindir}/nspluginviewer

%attr(0755,root,root) %{_libdir}/keditbookmarks.so
%attr(0755,root,root) %{_libdir}/kfm*.??
%attr(0755,root,root) %{_libdir}/konqueror.so*
%attr(0755,root,root) %{_libdir}/kde3/kcm_konq*.??
%attr(0755,root,root) %{_libdir}/kde3/konq*.??
%attr(0755,root,root) %{_libdir}/kde3/libkcm_nsplugin.la
%attr(0755,root,root) %{_libdir}/kde3/libkcm_nsplugin.so
%attr(0755,root,root) %{_libdir}/libkonq*.so*
%attr(0755,root,root) %{_libdir}/libnsplugin.so*

%attr(0755,root,root) %{_libdir}/kde3/htmlthumbnail.la
%attr(0755,root,root) %{_libdir}/kde3/htmlthumbnail.so

%{_applnkdir}/Network/WWW/konq*.desktop
%{_applnkdir}/Network/WWW/keditbookmarks.desktop
%{_applnkdir}/System/Administration/konq*.desktop
%dir %{_applnkdir}/Settings/KDE
%{_applnkdir}/Settings/KDE/.directory
%{_applnkdir}/Settings/KDE/FileBrowsing
%{_applnkdir}/Settings/KDE/WebBrowsing

%{_datadir}/apps/konq*
%{_datadir}/apps/keditbookmarks
%{_datadir}/services/htmlthumbnail.desktop
%{_datadir}/services/konq*.desktop
%{_datadir}/services/useragentstrings
%{_datadir}/servicetypes/konqaboutpage.desktop
%{_datadir}/servicetypes/konqpopupmenuplugin.desktop

%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/konqueror.png}
%{_pixmapsdir}/konqueror.png

%files screensavers -f libkscreensaver.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/*.kss
%{_applnkdir}/Settings/KDE/LookNFeel/screensaver.desktop
%{_applnkdir}/System/ScreenSavers/*

%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kscreensaver.png}
%{_pixmapsdir}/kscreensaver.png

%files -n kde-splash-default
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/*

%files -n kde-sdscreen-default                                                  
%defattr(644,root,root,755)                                                     
%{_datadir}/apps/ksmserver/* 
