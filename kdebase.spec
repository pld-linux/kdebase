Summary:	K Desktop Environment - core files
Summary(es):	K Desktop Environment - archivos b�sicos
Summary(pl):	K Desktop Environment - pliki �rodowiska
Summary(pt_BR):	K Desktop Environment - arquivos b�sicos
Name:		kdebase
Version:	2.2.2
Release:	8
Epoch:		6
License:	GPL
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(it):	X11/Applicazioni
Group(ja):	X11/���ץꥱ�������
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Group(ru):	X11/����������
Group(sv):	X11/Till�mpningar
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Source1:	%{name}-startkde.sh
Source2:	kdm.pamd
Source3:	kdm.init
Source4:	kdm.Xsession
Source6:	%{name}-kscreensaver.pam
Source7:	%{name}-kdm.Xservers
Patch0:		%{name}-kdmrc.patch
Patch1:		%{name}-konsole-TERM.patch
Patch2:		%{name}-glibc-2.2.2.patch
Patch3:		%{name}-utmp.patch
Patch4:		%{name}-nsplugins_dirs.patch
Patch5:		%{name}-hardcoded_paths.patch
Patch6:		%{name}-kdm.daemon_output.patch
%ifnarch sparc sparc64 ppc
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	awk
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cups-devel
BuildRequires:	findutils
BuildRequires:	gettext-devel
BuildRequires:	glut-devel
BuildRequires:	grep
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	motif-devel
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	qt-devel >= 2.3.0
BuildRequires:	zlib-devel
BuildRequires:	db3-devel
# TODO: sensors
#BuildRequires:	sensors-devel
Prereq:		/sbin/ldconfig
Prereq:		/usr/X11R6/bin/mkfontdir
Requires:	applnk
Requires:	konqueror
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

%description
KDE specific files. Used by core KDE applications. Package includes:
- KDE menu hierarchy,
- kappfinder - script installing some non-KDE apps in KDE menu,
- krootwm - module used by KWM and KFM,
- kaudio - audio server for KDE.

%description -l pl
Pliki specyficzne dla �rodowiska KDE i wykorzystywane przez g��wne
aplikacje KDE. Pakiet zawiera:
- Hierarchi� menu KDE,
- kappfinder - skrypt u�awiaj�cy uruchamianie niekt�rych program�w
  spoza KDE
- krootwm - modu� wykorzystywany przez kwm i kfm
- kaudio - serwer d�wi�ku dla KDE.

%package devel
Summary:	Include files to develop KDE applications
Summary(es):	Header files for compiling applications that use kdebase libraries
Summary(pl):	Pliki nag��wkowe potrzebne do programowania
Summary(pt_BR):	Arquivos de inclus�o para compilar aplicativos que usem bibliotecas do kdebase
Group:		X11/Development/Libraries
Group(cs):	X11/V�vojov� prost�edky/Knihovny
Group(da):	X11/Udvikling/Biblioteker
Group(de):	X11/Entwicklung/Bibliotheken
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(it):	X11/Sviluppo/Librerie
Group(ja):	X11/��ȯ/�饤�֥��
Group(no):	X11/Applikasjoner/Biblioteker
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(pt):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(sv):	X11/Utveckling/Bibliotek
Group(uk):	X11/��������/��̦�����
Requires:	%{name}-%{version}
Requires:	qt-devel >= 2.3.0
Requires:	kdelibs-devel >= %{version}

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l es
This package includes the header files you will need to compile
applications that use kdebase libraries.

%description devel -l pl
Pakiet zawiera pliki nag��wkowe niezb�dne do programowania aplikacji
KDE.

%description devel -l pt_BR
Este pacote cont�m os arquivos de inclus�o que s�o necess�rios para
compilar aplicativos que usem bibliotecas do kdebase.

%package static
Summary:	Include static libraries to develop KDE applications
Summary(es):	kdebase static library files
Summary(pl):	Statyczne biblioteki KDE
Summary(pt_BR):	Bibliotecas est�ticas do kdebase
Group:		X11/Development/Libraries
Group(cs):	X11/V�vojov� prost�edky/Knihovny
Group(da):	X11/Udvikling/Biblioteker
Group(de):	X11/Entwicklung/Bibliotheken
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(it):	X11/Sviluppo/Librerie
Group(ja):	X11/��ȯ/�饤�֥��
Group(no):	X11/Applikasjoner/Biblioteker
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(pt):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(sv):	X11/Utveckling/Bibliotek
Group(uk):	X11/��������/��̦�����
Requires:	qt-devel >= 2.3.0
Requires:	kdelibs-devel >= %{version}

%description static
This package contains KDE static libraries.

%description -l es static
kdebase static library files.

%description static -l pl
Pakiet zawiera statyczne biblioteki KDE.

%description -l pt_BR static
Bibliotecas est�ticas do kdebase.

%package -n kdm
Summary:	KDE Display Manager	
Summary(pl):	KDE Display Manager
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(it):	X11/Applicazioni
Group(ja):	X11/���ץꥱ�������
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Group(ru):	X11/����������
Group(sv):	X11/Till�mpningar
Requires:	qt >= 2.3.0
Requires:	kdelibs >= %{version}
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
Summary(pl):	Konqueror - przegl�darka WWW i mened�er plik�w
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(it):	X11/Applicazioni
Group(ja):	X11/���ץꥱ�������
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Group(ru):	X11/����������
Group(sv):	X11/Till�mpningar
Requires:	qt >= 2.3.0
Requires:	kdelibs >= %{version}
Obsoletes:	kdebase-konqueror

%description -n konqueror
Konqueror is a web browser and file manager similar to MS Internet
Explorer.

%description -n konqueror -l pl
Konqueror jest przegl�dark� WWW i mene�derem plik�w podobnym do MS
Internet Explorer.

%package screensavers
Summary:	KDE screensavers
Summary(pl):	Wygaszacze ekranu desktopu KDE
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(it):	X11/Applicazioni
Group(ja):	X11/���ץꥱ�������
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Group(ru):	X11/����������
Group(sv):	X11/Till�mpningar
Requires:	qt >= 2.3.0
Requires:	kdelibs >= %{version}
Requires:	OpenGL

%description screensavers
KDE screensavers.

%description screensavers -l pl
Wygaszacze ekranu desktopu KDE.

%prep
%setup  -q
# patch0 is applied in %%install
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build

# workaround -- don't allow to regenerate Makefile.xx
find -name Makefile.am -exec touch {} \;
find -name Makefile.in -exec touch {} \;

kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%{__make} -f Makefile.cvs
CPPFLAGS="-I%{_includedir}"
export CPPFLAGS
%configure \
	--with-pam=kdm \
	--without-shadow \
	--disable-shadow \
	--with-xdmdir="%{_sysconfdir}/kdm" \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Network/WWW,Office/Editors,Amusements,Settings/KDE} \
	$RPM_BUILD_ROOT/etc/{pam.d,security,rc.d/init.d,X11/kdm}

%{__make} install \
 	DESTDIR="$RPM_BUILD_ROOT" \
 	fontdir="%{_fontdir}/misc"

# Patch kdmrc. It is generated so it can not be patched in %%prep.
cd $RPM_BUILD_ROOT%{_datadir}/config/kdm
patch -p0  < %{PATCH0}
cd -

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv -f $ALD/{Internet/konqbrowser.desktop,Network/WWW}
mv -f $ALD/{Internet/keditbookmarks.desktop,Network/WWW}
mv -f $ALD/{Toys/ktip.desktop,Amusements}

install %{SOURCE1}			$RPM_BUILD_ROOT%{_bindir}/startkde
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
Icon=package_settings
X-KDE-BaseGroup=settings
EOF

# removing unneeded directories
# XXX rm -rf $RPM_BUILD_ROOT%{_applnkdir}/{Editors,Toys}

for f in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory' -o -name '*.dekstop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

touch $RPM_BUILD_ROOT/etc/security/blacklist.kdm

gzip AUTHORS README*

%find_lang tmp.%{name} --with-kde --all-name
grep -vE konqueror\|kdm tmp.%{name}.lang > %{name}.lang
%find_lang konqueror --with-kde
%find_lang kdm --with-kde

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

%post	-n konqueror -p /sbin/ldconfig 
%postun	-n konqueror -p /sbin/ldconfig 

%pre -n kdm
/usr/sbin/groupadd -g 55 -r -f xdm
if [ -z "`id -u xdm 2>/dev/null`" ]; then
	/usr/sbin/useradd -u 55 -r -d /dev/null -s /bin/false -c 'X Display Manager' -g xdm xdm 1>&2
fi

%post -n kdm
/sbin/chkconfig --add kdm
if [ -f /var/lock/subsys/kdm ]; then
        /etc/rc.d/init.d/kdm restart >&2
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
%doc *gz
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
%attr(6755,root,root) %{_bindir}/kdesud
%attr(0755,root,root) %{_bindir}/konsole
%attr(6755,root,root) %{_bindir}/konsole_grantpty
%attr(0755,root,root) %{_bindir}/khelpcenter
%attr(0755,root,root) %{_bindir}/khotkeys
%attr(0755,root,root) %{_bindir}/klegacyimport
%attr(0755,root,root) %{_bindir}/klipper
%attr(0755,root,root) %{_bindir}/ks[mty]*
%attr(0755,root,root) %{_bindir}/ksplash
%attr(0755,root,root) %{_bindir}/krdb
%attr(0755,root,root) %{_bindir}/kreadconfig
%attr(0755,root,root) %{_bindir}/kpager
%attr(0755,root,root) %{_bindir}/kprinter
%attr(0755,root,root) %{_bindir}/kpersonalizer
%attr(0755,root,root) %{_bindir}/kmenuedit

%attr(0755,root,root) %{_libdir}/[ae]*.la
%attr(0755,root,root) %{_libdir}/[ae]*.so*
%attr(0755,root,root) %{_libdir}/k[dhijlmwx]*.la
%attr(0755,root,root) %{_libdir}/k[dhijlmwx]*.so*
%attr(0755,root,root) %{_libdir}/kate.??
%attr(0755,root,root) %{_libdir}/konsole.la
%attr(0755,root,root) %{_libdir}/konsole.so*
%attr(0755,root,root) %{_libdir}/lib[cdqt]*.la
%attr(0755,root,root) %{_libdir}/lib[cdqt]*.so*
%attr(0755,root,root) %{_libdir}/libk[ahmrstw]*.la
%attr(0755,root,root) %{_libdir}/libk[ahmrstw]*.so*
%attr(0755,root,root) %{_libdir}/libkcm_[ilx]*.la*
%attr(0755,root,root) %{_libdir}/libkcm_[ilx]*.so*
%attr(0755,root,root) %{_libdir}/libkonsolepart.la
%attr(0755,root,root) %{_libdir}/libkonsolepart.so*
%attr(0755,root,root) %{_libdir}/libnaughtyapplet.la
%attr(0755,root,root) %{_libdir}/libnaughtyapplet.so*
%attr(0755,root,root) %{_libdir}/libkcm_[ku]*.la
%attr(0755,root,root) %{_libdir}/libkcm_[ku]*.so

%attr(0755,root,root) %{_libdir}/kde2/[ikt]*.la
%attr(0755,root,root) %{_libdir}/kde2/[ikt]*.so*
%attr(0755,root,root) %{_libdir}/kde2/libkcm_[abcefilmptu]*.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_[abcefilmptu]*.so*
%attr(0755,root,root) %{_libdir}/kde2/libkcm_k[ehinuw]*.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_k[ehinuw]*.so*
%attr(0755,root,root) %{_libdir}/kde2/libkcm_s[amt]*.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_s[amt]*.so*
%attr(0755,root,root) %{_libdir}/kde2/libk[fsuw]*.la*
%attr(0755,root,root) %{_libdir}/kde2/libk[fsuw]*.so*

%attr(0755,root,root) %{_libdir}/kde2/libkcm_socks.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_socks.so
%attr(0755,root,root) %{_libdir}/kde2/libkcm_konsole.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_konsole.so
%attr(0755,root,root) %{_libdir}/kde2/libkcm_spellchecking.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_spellchecking.so
%attr(0755,root,root) %{_libdir}/kde2/libkded*.la
%attr(0755,root,root) %{_libdir}/kde2/libkded*.so*
%attr(0755,root,root) %{_libdir}/kde2/libkhelp*.la
%attr(0755,root,root) %{_libdir}/kde2/libkhelp*.so*
%attr(0755,root,root) %{_libdir}/kde2/gsthumbnail.la
%attr(0755,root,root) %{_libdir}/kde2/gsthumbnail.so*

# NOTE:	There are many directories created by kappfinder. They should be
#	ignored as such functionality is provided by applnk package and
#	*.dekstop files from apropriate packages.
%{_applnkdir}/Help.desktop
%{_applnkdir}/Home.desktop
%{_applnkdir}/KControl.desktop
%{_applnkdir}/.hidden/konqfilemgr.desktop
%{_applnkdir}/Amusements/*.desktop
%dir %{_applnkdir}/Settings
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
%{_applnkdir}/Settings/KDE/System/k[!d]*
%{_applnkdir}/Settings/KDE/System/[!k]*
%{_applnkdir}/Settings/KDE/System/.directory
%{_applnkdir}/System/k[!o]*.desktop
%{_applnkdir}/System/kon[!q]*.desktop
%{_applnkdir}/Utilities/*.desktop
%{_applnkdir}/Editors/*.desktop
# No idea what it is for...
%{_applnkdir}/ksysguard

%{_datadir}/apps/[cdn]*
%{_datadir}/apps/k[abcfhijmtw]*
%{_datadir}/apps/kd[cei]*
%{_datadir}/apps/konsole
%{_datadir}/apps/kpersonalizer
%{_datadir}/apps/ks[py]*

%{_datadir}/autostart
%dir %{_datadir}/config
%{_datadir}/config/[!k]*
%{_datadir}/config/k[!d]*
%{_datadir}/config/kdesktop*
%{_datadir}/locale
%{_datadir}/mimelnk
%{_datadir}/services/[abfgimnpst]*
%{_datadir}/services/k[afhsuwx]*
%{_datadir}/services/kded
%{_datadir}/services/kons*
%{_datadir}/sounds
%{_datadir}/templates
%{_datadir}/wallpapers
%{_datadir}/servicetypes/[fstu]*.desktop
%{_datadir}/servicetypes/k[!o]*.desktop

%{_pixmapsdir}/*/*/apps/[abcdefghilmnprstuwx]*
%{_pixmapsdir}/*/*/apps/k[acefhijlmnptwm]*
%{_pixmapsdir}/*/*/apps/konsole.png
%{_pixmapsdir}/*/*/apps/ksysguard.png
%{_pixmapsdir}/*/*/apps/kdisk*
%{_pixmapsdir}/*/*/apps/kdeprint*

%{_pixmapsdir}/*/*/actions/*
%{_pixmapsdir}/*/*/filesystems/*

# TODO:	file /usr/share/fonts/misc/9x15.pcf.gz from install of kdebase-2.0.1-3
# 	conflicts with file from package XFree86-fonts-4.0.1-2.
# TODO:	there is a name conflict between cursor_large and cursor from XFree86.
%{_fontdir}/misc/console8*.gz
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libccont.a

%files -f kdm.lang -n kdm
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/chooser
%attr(0755,root,root) %{_bindir}/kdm*
%attr(0755,root,root) %{_libdir}/kde2/libkcm_kdm.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_kdm.so*

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
#%{_datadir}/config/kdm/README

%{_pixmapsdir}/*/*/apps/kdmconfig.png

%files -n konqueror -f konqueror.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/keditbookmarks
%attr(0755,root,root) %{_bindir}/konqueror
%attr(0755,root,root) %{_bindir}/kfm*
%attr(0755,root,root) %{_bindir}/nspluginscan
%attr(0755,root,root) %{_bindir}/nspluginviewer

%attr(0755,root,root) %{_libdir}/keditbookmarks.la
%attr(0755,root,root) %{_libdir}/keditbookmarks.so
%attr(0755,root,root) %{_libdir}/kfm*.??
%attr(0755,root,root) %{_libdir}/konqueror.la
%attr(0755,root,root) %{_libdir}/konqueror.so*
%attr(0755,root,root) %{_libdir}/libkcm_nsplugin.la
%attr(0755,root,root) %{_libdir}/libkcm_nsplugin.so*
%attr(0755,root,root) %{_libdir}/libkonq*.la
%attr(0755,root,root) %{_libdir}/libkonq*.so*
%attr(0755,root,root) %{_libdir}/libnsplugin.la
%attr(0755,root,root) %{_libdir}/libnsplugin.so*

%attr(0755,root,root) %{_libdir}/kde2/htmlthumbnail.la
%attr(0755,root,root) %{_libdir}/kde2/htmlthumbnail.so*
%attr(0755,root,root) %{_libdir}/kde2/libkcm_konq*.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_konq*.so*
%attr(0755,root,root) %{_libdir}/kde2/libkonq*la
%attr(0755,root,root) %{_libdir}/kde2/libkonq*so.*
%attr(0755,root,root) %{_libdir}/kde2/libkonq*.so

%{_applnkdir}/Network/WWW/konq*.desktop
%{_applnkdir}/Network/WWW/keditbookmarks.desktop
%{_applnkdir}/System/konq*.desktop
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

%{_pixmapsdir}/*/*/apps/konqueror.png


%files screensavers
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/*.kss

%attr(0755,root,root) %{_libdir}/kde2/libkcm_screensaver.la
%attr(0755,root,root) %{_libdir}/kde2/libkcm_screensaver.so*

%{_applnkdir}/Settings/KDE/LookNFeel/screensaver.desktop
%{_applnkdir}/System/ScreenSavers/*

%{_datadir}/apps/kscreensaver

%{_pixmapsdir}/*/*/apps/kscreensaver.png
