Summary:     K Desktop Environment - core files
Summary(pl): K Desktop Environment - pliki ¶rodowiska
Name:        kdebase
Version:     1.0
Release:     7
Copyright:   GPL
Group:       X11/KDE/Base
Vendor:      The KDE Team
Source:      ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.gz
Source2:     kdeenv
Requires:    qt >= 1.40, kdelibs = %{version}
BuildRoot:   /tmp/%{name}-%{version}-root

%description
KDE specific files. Used by core KDE applications.
Package includes:
  KDE menu hierarchy
  kappfinder - script installing some non-KDE apps in KDE menu
  krootwm - module used by KWM and KFM
  kaudio - audio server for KDE

%description -l pl
Pliki specyficzne dla ¶rodowiska KDE i wykorzystywane przez g³ówne
aplikacje KDE.
Pakiet zawiera:
  Hierarchiê menu KDE
  kappfinder - skrypt u³awiaj±cy uruchamianie niektórych programów spoza KDE
  krootwm - modu³ wykorzystywany przez kwm i kfm
  kaudio - serwer d¼wiêku dla KDE

%package -n kcontrol
Summary:     KDE Control Center
Summary(pl): Centrum Sterowania KDE
Group:       X11/KDE/Base
Requires:    qt >= 1.40, kdelibs = %{version}, %{name} = %{version}

%description -n kcontrol
KDE Control Center - easy way to access KDE configuration modules
and several useful modules.

%description -l pl -n kcontrol
Centrum sterowania KDE - program obs³ugi modu³ów konfiguracyjnych KDE
oraz kilka przydatnych modu³ów.

%package -n kdehelp
Summary:     KDE Help System	
Summary(pl): System Pomocy KDE
Group:       X11/KDE/Base
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kdehelp
This program is used for viewing KDE applications' online manual.
It is also convinient for reading system's man pages and "info" documentation.

%description -l pl -n kdehelp
Program umo¿liwiaj±cy przegl±danie dokumentacji applikacji KDE.
Jest te¿ wygodnym narzêdziem do ogl±dania stron man i dokumentacji "info".

%package -n kdm
Summary:     KDE Display Manager	
Summary(pl): KDE Display Manager
Group:       X11/KDE/Base
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kdm
It is KDE replacement for XDM.
It manages local and remote X11 displays.

%description -l pl -n kdm
Zamiennik XDM rodem z KDE.

%package -n kfind
Summary:     KDE file finder	
Summary(pl): Wyszukiwarka plików dla KDE
Group:       X11/KDE/Base
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kfind
A simple frontend to find and grep.

%description -l pl -n kfind
Prosty interfejs dla poleceñ find i grep.

%package -n kfm
Summary:     KDE file manager	
Summary(pl): Mened¿er plików KDE
Group:       X11/KDE/Base
Requires:    %{name} = %{version}, qt >= 1.40, kdelibs = %{version} 

%description -n kfm
A file manager and a web browser for KDE.

%description -l pl -n kfm
Mened¿er plików i przegl±darka WWW dla KDE.

%package -n kfontmanager
Summary:     KDE font manager	
Summary(pl): Mened¿er fontów KDE
Group:       X11/KDE/Base
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kfontmanager
A font manager for KDE.
It may be used to choose fonts which can be used by KDE.

%description -l pl -n kfm
Mened¿er fontów dla KDE.
Mo¿e byæ wykorzystany do okre¶lenia listy czcionek dostêpnych dla aplikacji KDE.

%package -n kmenuedit
Summary:     KDE Menu Editor	
Summary(pl): Edytor menu KDE
Group:       X11/KDE/Base
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kmenuedit
A system menu editor for KDE.

%description -l pl -n kmenuedit
Edytor menu systemowego KDE.

%package -n kpanel
Summary:     KDE Panel	
Summary(pl): Panel KDE
Group:       X11/KDE/Base
Requires:    kfm = %{version}, qt >= 1.40, kdelibs = %{version} 

%description -n kpanel
An easy way to start applications and swtich desktops in KDE.

%description -l pl -n kpanel
U³atwia startowanie aplikacji oraz prze³±czanie ekranów w KDE.

%package -n kscreensaver
Summary:     KDE Screen-savers
Summary(pl): Screen-savery dla KDE
Group:       X11/KDE/Base
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kscreensaver
Several screen-savers for KDE.

%description -l pl -n kscreensaver
"Oszczêdzacze ekranu" dla KDE

%package -n kvt
Summary:     KDE terminal emulator
Summary(pl): Emulator terminala dla KDE
Group:       X11/KDE/Base
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kvt
Terminal emulator for KDE.

%description -l pl -n kvt
Emulator terminala znakowego dla KDE

%package -n kwm
Summary:     KDE window manager
Summary(pl): Mened¿er okien KDE
Group:       X11/KDE/Base
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kwm
Window manager for KDE

%description -l pl -n kwm
Mened¿er okien dla KDE

%package -n kbgndwm
Summary:     KDE background manager and wallpapers
Summary(pl): Tapety oraz mened¿er t³a KDE 
Group:       X11/KDE/Base
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kbgndwm
Background manager for KDE.
It is responsible for displaying KDE wallpapers.
Sample wallpapers are also included.

%description -l pl -n kbgndwm
Mened¿er t³a dla KDE.
Odpowiedzialny za wy¶wietlanie tapet.
Przyk³adowe tapety s± tak¿e do³±czone

%prep
%setup -q

%build
export KDEDIR=/usr/X11R6
CXXFLAGS="$RPM_OPT_FLAGS -Wall" CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure --prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=/usr/X11R6
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

# create wmconfig files
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
DIR=$PWD
cd $RPM_BUILD_ROOT/etc/X11/kde/applnk
for kdelnk in `find . -name "*.kdelnk"` ; do
  PKG=kde`basename $kdelnk|sed -e "s/\.kdelnk$//"`;
  SECT=`dirname $kdelnk|sed -e "s/^\.\/*//"`;
  kdelnk2wmconfig $PKG $kdelnk $RPM_BUILD_ROOT/etc/X11/wmconfig/$PKG KDE/$SECT pl
done
cd $DIR

install -d ${RPM_BUILD_ROOT}/etc/X11/kde

install ${RPM_SOURCE_DIR}/kdeenv ${RPM_BUILD_ROOT}${KDEDIR}/bin/kdeenv

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KDEBASE
#################################################

%files
%defattr(644, root, root, 755)

#directory hierarchy
%dir /etc/X11/kde/applnk/System
%dir /etc/X11/kde/applnk/Applications
%dir /etc/X11/kde/applnk/Games
%dir /etc/X11/kde/applnk/Graphics
%dir /etc/X11/kde/applnk/Internet
%dir /etc/X11/kde/applnk/Multimedia
%dir /etc/X11/kde/applnk/Utilities
%dir /etc/X11/kde/applnk/Settings

# locale files
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/krootwm.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/krootwm.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/krootwm.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/krootwm.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/krootwm.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/krootwm.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/krootwm.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/krootwm.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/krootwm.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/krootwm.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/krootwm.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/krootwm.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/krootwm.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/krootwm.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/krootwm.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/krootwm.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/krootwm.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/krootwm.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/krootwm.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/krootwm.mo
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kdisplay.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kdisplay.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kdisplay.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kdisplay.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kdisplay.mo
%lang(en) /usr/X11R6/share/locale/en*/LC_MESSAGES/kdisplay.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kdisplay.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kdisplay.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kdisplay.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kdisplay.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kdisplay.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kdisplay.mo
%lang(mk) /usr/X11R6/share/locale/mk/LC_MESSAGES/kdisplay.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kdisplay.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kdisplay.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kdisplay.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kdisplay.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kdisplay.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kdisplay.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kdisplay.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kdisplay.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kdisplay.mo

%config(missingok) /etc/X11/kde/applnk/Settings/Desktop/
%config(missingok) /etc/X11/wmconfig/kdebackground
%config(missingok) /etc/X11/wmconfig/kdecolors
%config(missingok) /etc/X11/wmconfig/kdedesktop
%config(missingok) /etc/X11/wmconfig/kdelanguage
%config(missingok) /etc/X11/wmconfig/kdescreensaver
%config(missingok) /etc/X11/wmconfig/kdestyle
/usr/X11R6/share/kde/apps/kdisplay/

# Help files
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/kdisplay

# Applications' files
/usr/X11R6/share/kde/apps/kappfinder/*

# some icons
/usr/X11R6/share/kde/icons/*_package.xpm
/usr/X11R6/share/kde/icons/mini/*_package.xpm

/usr/X11R6/share/kde/icons/mini/mini*.xpm
/usr/X11R6/share/kde/icons/mini/background.xpm
/usr/X11R6/share/kde/icons/mini/colors.xpm
/usr/X11R6/share/kde/icons/mini/screensaver.xpm
/usr/X11R6/share/kde/icons/mini/style.xpm
/usr/X11R6/share/kde/icons/mini/mouse.xpm
/usr/X11R6/share/kde/icons/mini/keyboard.xpm
/usr/X11R6/share/kde/icons/mini/windows.xpm
/usr/X11R6/share/kde/icons/mini/titlebar.xpm
/usr/X11R6/share/kde/icons/mini/buttons.xpm
/usr/X11R6/share/kde/icons/mini/application_settings.xpm
/usr/X11R6/share/kde/icons/mini/desktop_settings.xpm
/usr/X11R6/share/kde/icons/mini/general_settings.xpm
/usr/X11R6/share/kde/icons/mini/information_settings.xpm
/usr/X11R6/share/kde/icons/mini/input_devices_settings.xpm
/usr/X11R6/share/kde/icons/mini/network_settings.xpm
/usr/X11R6/share/kde/icons/mini/panel_settings.xpm
/usr/X11R6/share/kde/icons/mini/sound_settings.xpm
/usr/X11R6/share/kde/icons/mini/exec.xpm
/usr/X11R6/share/kde/icons/mini/folder.xpm
/usr/X11R6/share/kde/icons/mini/terminal.xpm
/usr/X11R6/share/kde/icons/mini/x.xpm
/usr/X11R6/share/kde/icons/background.xpm
/usr/X11R6/share/kde/icons/palette.xpm
/usr/X11R6/share/kde/icons/application_settings.xpm
/usr/X11R6/share/kde/icons/desktop_settings.xpm
/usr/X11R6/share/kde/icons/general_settings.xpm
/usr/X11R6/share/kde/icons/information_settings.xpm
/usr/X11R6/share/kde/icons/input_devices_settings.xpm
/usr/X11R6/share/kde/icons/network_settings.xpm
/usr/X11R6/share/kde/icons/panel_settings.xpm
/usr/X11R6/share/kde/icons/sound_settings.xpm

#config files
%config /etc/X11/kde/kdisplayrc

# KDE menu
%config(missingok) /etc/X11/kde/applnk/System/.directory
%config(missingok) /etc/X11/kde/applnk/System/kappfinder.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekappfinder
%config(missingok) /etc/X11/kde/applnk/Applications/.directory
%config(missingok) /etc/X11/kde/applnk/Games/.directory
%config(missingok) /etc/X11/kde/applnk/Graphics/.directory
%config(missingok) /etc/X11/kde/applnk/Internet/.directory
%config(missingok) /etc/X11/kde/applnk/Multimedia/.directory
%config(missingok) /etc/X11/kde/applnk/Utilities/.directory
%config(missingok) /etc/X11/kde/applnk/Settings/Input_Devices/.directory
%config(missingok) /etc/X11/kde/applnk/Settings/Sound/.directory
%config(missingok) /etc/X11/kde/applnk/Settings/Windows/.directory
%config(missingok) /etc/X11/kde/applnk/Settings/Network/.directory
%config(missingok) /etc/X11/kde/applnk/Settings/Information/.directory
%config(missingok) /etc/X11/kde/applnk/Settings/Applications/.directory
%config(missingok) /etc/X11/kde/applnk/Settings/.directory

#documentation
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kmedia/*

#no go executables
%defattr(755, root, root, 755)
/usr/X11R6/bin/startkde
/usr/X11R6/bin/kdeenv
/usr/X11R6/bin/krootwm
/usr/X11R6/bin/maudio
/usr/X11R6/bin/kaudioserver
/usr/X11R6/bin/kappfinder
/usr/X11R6/bin/kappfinder_restart
/usr/X11R6/bin/krdb
/usr/X11R6/bin/kcmdisplay

#################################################
#             KWM
#################################################

%files -n kwm
%defattr(644, root, root, 755)
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kwm/
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/kcmkwm/
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/kcmsyssound/
%config(missingok) /etc/X11/kde/applnk/Settings/Windows/
%config(missingok) /etc/X11/wmconfig/kdebuttons
%config(missingok) /etc/X11/wmconfig/kdeproperties
%config(missingok) /etc/X11/wmconfig/kdetitlebar
%config(missingok) /etc/X11/kde/applnk/System/kwmpager.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekwmpager
%config(missingok) /etc/X11/kde/applnk/Settings/Sound/syssound.kdelnk
%config(missingok) /etc/X11/wmconfig/kdesyssound
/usr/X11R6/share/kde/apps/kwm/
/usr/X11R6/share/kde/icons/mini/maximize2.xpm
/usr/X11R6/share/kde/icons/mini/kwm.xpm
/usr/X11R6/share/kde/icons/mini/syssound.xpm
/usr/X11R6/share/kde/icons/syssound.xpm
/usr/X11R6/share/kde/icons/kcmkwm.xpm
/usr/X11R6/share/kde/icons/kwm.xpm

%lang(de) /usr/X11R6/share/kde/doc/HTML/de/kcontrol/kcmsyssound
%lang(no) /usr/X11R6/share/kde/doc/HTML/no/kcontrol/kcmsyssound
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kwm.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kwm.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kwm.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kwm.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kwm.mo
%lang(en) /usr/X11R6/share/locale/en*/LC_MESSAGES/kwm.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kwm.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kwm.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kwm.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kwm.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kwm.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kwm.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kwm.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kwm.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kwm.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kwm.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kwm.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kwm.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kwm.mo
%lang(sl) /usr/X11R6/share/locale/sl/LC_MESSAGES/kwm.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kwm.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kwm.mo

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kcmkwm.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kcmkwm.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kcmkwm.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kcmkwm.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kcmkwm.mo
%lang(en) /usr/X11R6/share/locale/en*/LC_MESSAGES/kcmkwm.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kcmkwm.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kcmkwm.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kcmkwm.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kcmkwm.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kcmkwm.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kcmkwm.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kcmkwm.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kcmkwm.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kcmkwm.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kcmkwm.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kcmkwm.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kcmkwm.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kcmkwm.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kcmkwm.mo

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kcmsyssound.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kcmsyssound.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kcmsyssound.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kcmsyssound.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kcmsyssound.mo
%lang(en) /usr/X11R6/share/locale/en*/LC_MESSAGES/kcmsyssound.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kcmsyssound.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kcmsyssound.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kcmsyssound.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kcmsyssound.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kcmsyssound.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kcmsyssound.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kcmsyssound.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kcmsyssound.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kcmsyssound.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kcmsyssound.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kcmsyssound.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kcmsyssound.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kcmsyssound.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kcmsyssound.mo

%defattr(755, root, root, 755)
/usr/X11R6/bin/kcmsyssound
/usr/X11R6/bin/kstartondesk
/usr/X11R6/bin/kcmkwm
/usr/X11R6/bin/kwmsound
/usr/X11R6/bin/kwmcom
/usr/X11R6/bin/kwmpager
/usr/X11R6/bin/kbgndwm
/usr/X11R6/bin/kwm

#################################################
#             KBGNDWM
#################################################

%files -n kbgndwm
%defattr(644, root, root, 755)
/usr/X11R6/share/kde/wallpapers/*

%defattr(755, root, root, 755)
/usr/X11R6/bin/kbgndwm


#################################################
#             KDEHELP
#################################################

%files -n kdehelp
%defattr(644, root, root, 755)
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kdehelp/
/usr/X11R6/share/kde/icons/mini/kdehelp.xpm
/usr/X11R6/share/kde/icons/kdehelp.xpm

%defattr(755, root, root, 755)
/usr/X11R6/lib/kde/cgi-bin
/usr/X11R6/bin/kdehelp
%config(missingok) /etc/X11/kde/applnk/Help.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeHelp

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kdehelp.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kdehelp.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kdehelp.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kdehelp.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kdehelp.mo
%lang(en) /usr/X11R6/share/locale/en*/LC_MESSAGES/kdehelp.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kdehelp.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kdehelp.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kdehelp.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kdehelp.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kdehelp.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kdehelp.mo
%lang(mk) /usr/X11R6/share/locale/mk/LC_MESSAGES/kdehelp.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kdehelp.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kdehelp.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kdehelp.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kdehelp.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kdehelp.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kdehelp.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kdehelp.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kdehelp.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kdehelp.mo

#################################################
#             KFM
#################################################

%files -n kfm
%defattr(644, root, root, 755)
%config /etc/X11/kde/mimelnk/*
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kfm/
%config(missingok) /etc/X11/kde/applnk/Krefresh.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKrefresh
%config(missingok) /etc/X11/kde/applnk/Trash.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeTrash
%config(missingok) /etc/X11/kde/applnk/Home.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeHome
%config(missingok) /etc/X11/kde/applnk/System/kfmsu.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekfmsu
%config(missingok) /etc/X11/kde/applnk/System/Arrange.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeArrange
%config /etc/X11/kde/kfmrc
%config /etc/X11/kde/desktop
/usr/X11R6/share/kde/icons/kfm.xpm
/usr/X11R6/share/kde/icons/link.xpm
/usr/X11R6/share/kde/apps/kfm/
/usr/X11R6/share/kde/icons/mini/3floppy_mount.xpm
/usr/X11R6/share/kde/icons/mini/3floppy_unmount.xpm
/usr/X11R6/share/kde/icons/mini/5floppy_mount.xpm
/usr/X11R6/share/kde/icons/mini/5floppy_unmount.xpm
/usr/X11R6/share/kde/icons/mini/binary.xpm
/usr/X11R6/share/kde/icons/mini/blockdevice.xpm
/usr/X11R6/share/kde/icons/mini/c_src.xpm
/usr/X11R6/share/kde/icons/mini/cdrom_mount.xpm
/usr/X11R6/share/kde/icons/mini/chardevice.xpm
/usr/X11R6/share/kde/icons/mini/cdrom_unmount.xpm
/usr/X11R6/share/kde/icons/mini/core.xpm
/usr/X11R6/share/kde/icons/mini/document.xpm
/usr/X11R6/share/kde/icons/mini/dvi.xpm
/usr/X11R6/share/kde/icons/mini/folder_blue.xpm
/usr/X11R6/share/kde/icons/mini/folder_cyan.xpm
/usr/X11R6/share/kde/icons/mini/folder_green.xpm
/usr/X11R6/share/kde/icons/mini/folder_locked.xpm
/usr/X11R6/share/kde/icons/mini/folder_open.xpm
/usr/X11R6/share/kde/icons/mini/folder_red.xpm
/usr/X11R6/share/kde/icons/mini/folder_yellow.xpm
/usr/X11R6/share/kde/icons/mini/font.xpm
/usr/X11R6/share/kde/icons/mini/ftp.xpm
/usr/X11R6/share/kde/icons/mini/f_src.xpm
/usr/X11R6/share/kde/icons/mini/gf.xpm
/usr/X11R6/share/kde/icons/mini/h_src.xpm
/usr/X11R6/share/kde/icons/mini/html.xpm
/usr/X11R6/share/kde/icons/mini/image.xpm
/usr/X11R6/share/kde/icons/mini/info.xpm
/usr/X11R6/share/kde/icons/mini/java_src.xpm
/usr/X11R6/share/kde/icons/mini/kfm*
/usr/X11R6/share/kde/icons/mini/l_src.xpm
/usr/X11R6/share/kde/icons/mini/library.xpm
/usr/X11R6/share/kde/icons/mini/locked.xpm
/usr/X11R6/share/kde/icons/mini/lockedfolder.xpm
/usr/X11R6/share/kde/icons/mini/log.xpm
/usr/X11R6/share/kde/icons/mini/make.xpm
/usr/X11R6/share/kde/icons/mini/man.xpm
/usr/X11R6/share/kde/icons/mini/metafont.xpm
/usr/X11R6/share/kde/icons/mini/midi.xpm
/usr/X11R6/share/kde/icons/mini/moc_src.xpm
/usr/X11R6/share/kde/icons/mini/o_src.xpm
/usr/X11R6/share/kde/icons/mini/p_src.xpm
/usr/X11R6/share/kde/icons/mini/pdf.xpm
/usr/X11R6/share/kde/icons/mini/pipe.xpm
/usr/X11R6/share/kde/icons/mini/pk.xpm
/usr/X11R6/share/kde/icons/mini/postscript.xpm
/usr/X11R6/share/kde/icons/mini/printer.xpm
/usr/X11R6/share/kde/icons/mini/readme.xpm
/usr/X11R6/share/kde/icons/mini/resource.xpm
/usr/X11R6/share/kde/icons/mini/s_src.xpm
/usr/X11R6/share/kde/icons/mini/package.xpm
/usr/X11R6/share/kde/icons/mini/script.xpm
/usr/X11R6/share/kde/icons/mini/socket.xpm
/usr/X11R6/share/kde/icons/mini/sound.xpm
/usr/X11R6/share/kde/icons/mini/tex.xpm
/usr/X11R6/share/kde/icons/mini/tgz.xpm
/usr/X11R6/share/kde/icons/mini/trash.xpm
/usr/X11R6/share/kde/icons/mini/txt.xpm
/usr/X11R6/share/kde/icons/mini/unknown.xpm
/usr/X11R6/share/kde/icons/mini/video.xpm
/usr/X11R6/share/kde/icons/mini/www.xpm
/usr/X11R6/share/kde/icons/mini/y_src.xpm
/usr/X11R6/share/kde/icons/mini/zip_mount.xpm
/usr/X11R6/share/kde/icons/mini/zip_unmount.xpm
/usr/X11R6/share/kde/icons/3floppy_mount.xpm
/usr/X11R6/share/kde/icons/3floppy_unmount.xpm
/usr/X11R6/share/kde/icons/5floppy_mount.xpm
/usr/X11R6/share/kde/icons/5floppy_unmount.xpm
/usr/X11R6/share/kde/icons/binary.xpm
/usr/X11R6/share/kde/icons/blockdevice.xpm
/usr/X11R6/share/kde/icons/c_src.xpm
/usr/X11R6/share/kde/icons/cdrom_mount.xpm
/usr/X11R6/share/kde/icons/cdrom_unmount.xpm
/usr/X11R6/share/kde/icons/chardevice.xpm
/usr/X11R6/share/kde/icons/core.xpm
/usr/X11R6/share/kde/icons/document.xpm
/usr/X11R6/share/kde/icons/dvi.xpm
/usr/X11R6/share/kde/icons/exec.xpm
/usr/X11R6/share/kde/icons/f_src.xpm
/usr/X11R6/share/kde/icons/folder.xpm
/usr/X11R6/share/kde/icons/folder_blue.xpm
/usr/X11R6/share/kde/icons/folder_cyan.xpm
/usr/X11R6/share/kde/icons/folder_green.xpm
/usr/X11R6/share/kde/icons/folder_locked.xpm
/usr/X11R6/share/kde/icons/folder_open.xpm
/usr/X11R6/share/kde/icons/folder_red.xpm
/usr/X11R6/share/kde/icons/folder_yellow.xpm
/usr/X11R6/share/kde/icons/font.xpm
/usr/X11R6/share/kde/icons/ftp.xpm
/usr/X11R6/share/kde/icons/gf.xpm
/usr/X11R6/share/kde/icons/h_src.xpm
/usr/X11R6/share/kde/icons/html.xpm
/usr/X11R6/share/kde/icons/image.xpm
/usr/X11R6/share/kde/icons/info.xpm
/usr/X11R6/share/kde/icons/java_src.xpm
/usr/X11R6/share/kde/icons/kfm_fulltrash.xpm
/usr/X11R6/share/kde/icons/kfm_home.xpm
/usr/X11R6/share/kde/icons/kfm_refresh.xpm
/usr/X11R6/share/kde/icons/kfm_trash.xpm
/usr/X11R6/share/kde/icons/l_src.xpm
/usr/X11R6/share/kde/icons/library.xpm
/usr/X11R6/share/kde/icons/lockedfolder.xpm
/usr/X11R6/share/kde/icons/log.xpm
/usr/X11R6/share/kde/icons/make.xpm
/usr/X11R6/share/kde/icons/man.xpm
/usr/X11R6/share/kde/icons/metafont.xpm
/usr/X11R6/share/kde/icons/midi.xpm
/usr/X11R6/share/kde/icons/moc_src.xpm
/usr/X11R6/share/kde/icons/o_src.xpm
/usr/X11R6/share/kde/icons/p_src.xpm
/usr/X11R6/share/kde/icons/package.xpm
/usr/X11R6/share/kde/icons/pdf.xpm
/usr/X11R6/share/kde/icons/pipe.xpm
/usr/X11R6/share/kde/icons/pk.xpm
/usr/X11R6/share/kde/icons/postscript.xpm
/usr/X11R6/share/kde/icons/printer.xpm
/usr/X11R6/share/kde/icons/readme.xpm
/usr/X11R6/share/kde/icons/readonly.xpm
/usr/X11R6/share/kde/icons/resource.xpm
/usr/X11R6/share/kde/icons/s_src.xpm
/usr/X11R6/share/kde/icons/script.xpm
/usr/X11R6/share/kde/icons/socket.xpm
/usr/X11R6/share/kde/icons/sound.xpm
/usr/X11R6/share/kde/icons/terminal.xpm
/usr/X11R6/share/kde/icons/tex.xpm
/usr/X11R6/share/kde/icons/tgz.xpm
/usr/X11R6/share/kde/icons/trash.xpm
/usr/X11R6/share/kde/icons/txt.xpm
/usr/X11R6/share/kde/icons/unknown.xpm
/usr/X11R6/share/kde/icons/video.xpm
/usr/X11R6/share/kde/icons/www.xpm
/usr/X11R6/share/kde/icons/x.xpm
/usr/X11R6/share/kde/icons/y_src.xpm
/usr/X11R6/share/kde/icons/zip_mount.xpm
/usr/X11R6/share/kde/icons/zip_unmount.xpm

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kfm.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kfm.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kfm.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kfm.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kfm.mo
%lang(en) /usr/X11R6/share/locale/en*/LC_MESSAGES/kfm.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kfm.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kfm.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kfm.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kfm.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kfm.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kfm.mo
%lang(mk) /usr/X11R6/share/locale/mk/LC_MESSAGES/kfm.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kfm.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kfm.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kfm.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kfm.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kfm.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kfm.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kfm.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kfm.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kfm.mo

%defattr(755, root, root, 755)
/usr/X11R6/bin/kfmwarn
/usr/X11R6/bin/kfmclient
/usr/X11R6/bin/kioslave
/usr/X11R6/bin/kfmexec
/usr/X11R6/bin/kfm
/usr/X11R6/bin/kfmsu
/usr/X11R6/bin/kfmsu2
/usr/X11R6/bin/unpack

#################################################
#             KFIND
#################################################

%files -n kfind
%defattr(644, root, root, 755)
/usr/X11R6/share/kde/apps/kfind/
/usr/X11R6/share/kde/icons/mini/kfind.xpm
%config(missingok) /etc/X11/kde/applnk/Kfind.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKfind
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kfind/
/usr/X11R6/share/kde/icons/kfind.xpm

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kfind.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kfind.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kfind.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kfind.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kfind.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kfind.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kfind.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kfind.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kfind.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kfind.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kfind.mo
%lang(mk) /usr/X11R6/share/locale/mk/LC_MESSAGES/kfind.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kfind.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kfind.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kfind.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kfind.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kfind.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kfind.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kfind.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kfind.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kfind.mo

%defattr(755, root, root, 755)
/usr/X11R6/bin/kfind

#################################################
#            KCONTROL 
#################################################
%files -n kcontrol
%defattr(644, root, root, 755)
/usr/X11R6/share/kde/apps/kcontrol/
/usr/X11R6/share/kde/apps/kcmlocale/
%config /etc/X11/kde/kcmlocalerc
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/kcmbell
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/kcminfo
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/kcminput
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/kcmlocale
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/kcmsamba
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/index.html
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/index-1.html
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/index-2.html
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/logotp3.gif
%config(missingok) /etc/X11/kde/applnk/Settings/Input_Devices/
%config(missingok) /etc/X11/wmconfig/kdekeyboard
%config(missingok) /etc/X11/wmconfig/kdemouse
%config(missingok) /etc/X11/kde/applnk/Settings/Sound/bell.kdelnk
%config(missingok) /etc/X11/wmconfig/kdebell
%config(missingok) /etc/X11/kde/applnk/Settings/Network/
%config(missingok) /etc/X11/wmconfig/kdesmbstatus
%config(missingok) /etc/X11/kde/applnk/Settings/Information/
%config(missingok) /etc/X11/wmconfig/kdememory
%config(missingok) /etc/X11/wmconfig/kdeprocessor
%config(missingok) /etc/X11/kde/applnk/KControl.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKControl
/usr/X11R6/share/kde/icons/mini/smbstatus.xpm
/usr/X11R6/share/kde/icons/mini/memory.xpm
/usr/X11R6/share/kde/icons/mini/processor.xpm
/usr/X11R6/share/kde/icons/kcontrol.xpm
/usr/X11R6/share/kde/icons/locale.xpm
/usr/X11R6/share/kde/icons/network.xpm
/usr/X11R6/share/kde/icons/information.xpm
/usr/X11R6/share/kde/icons/mouse.xpm
/usr/X11R6/share/kde/icons/keyboard.xpm
/usr/X11R6/share/kde/icons/smbstatus.xpm
/usr/X11R6/share/kde/icons/mini/kcontrol.xpm
/usr/X11R6/share/kde/icons/mini/locale.xpm
/usr/X11R6/share/kde/icons/bell.xpm

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kcontrol.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kcontrol.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kcontrol.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kcontrol.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kcontrol.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kcontrol.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kcontrol.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kcontrol.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kcontrol.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kcontrol.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kcontrol.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kcontrol.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kcontrol.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kcontrol.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kcontrol.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kcontrol.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kcontrol.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kcontrol.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kcontrol.mo

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kcmbell.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kcmbell.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kcmbell.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kcmbell.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kcmbell.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kcmbell.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kcmbell.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kcmbell.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kcmbell.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kcmbell.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kcmbell.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kcmbell.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kcmbell.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kcmbell.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kcmbell.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kcmbell.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kcmbell.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kcmbell.mo
%lang(sl) /usr/X11R6/share/locale/sl/LC_MESSAGES/kcmbell.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kcmbell.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kcmbell.mo

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kcminfo.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kcminfo.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kcminfo.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kcminfo.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kcminfo.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kcminfo.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kcminfo.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kcminfo.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kcminfo.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kcminfo.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kcminfo.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kcminfo.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kcminfo.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kcminfo.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kcminfo.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kcminfo.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kcminfo.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kcminfo.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kcminfo.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kcminfo.mo

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kcminput.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kcminput.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kcminput.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kcminput.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kcminput.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kcminput.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kcminput.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kcminput.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kcminput.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kcminput.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kcminput.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kcminput.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kcminput.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kcminput.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kcminput.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kcminput.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kcminput.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kcminput.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kcminput.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kcminput.mo

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kcmlocale.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kcmlocale.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kcmlocale.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kcmlocale.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kcmlocale.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kcmlocale.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kcmlocale.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kcmlocale.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kcmlocale.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kcmlocale.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kcmlocale.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kcmlocale.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kcmlocale.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kcmlocale.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kcmlocale.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kcmlocale.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kcmlocale.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kcmlocale.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kcmlocale.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kcmlocale.mo

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kcmsamba.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kcmsamba.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kcmsamba.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kcmsamba.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kcmsamba.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kcmsamba.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kcmsamba.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kcmsamba.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kcmsamba.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kcmsamba.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kcmsamba.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kcmsamba.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kcmsamba.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kcmsamba.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kcmsamba.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kcmsamba.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kcmsamba.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kcmsamba.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kcmsamba.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kcmsamba.mo

%defattr(755, root, root, 755)
/usr/X11R6/bin/kcmsamba
/usr/X11R6/bin/kcmbell
/usr/X11R6/bin/kcminput
/usr/X11R6/bin/kcminfo
/usr/X11R6/bin/kcontrol
/usr/X11R6/bin/kcmlocale

#################################################
#            KSCREENSAVER 
#################################################
%files -n kscreensaver
%defattr(644, root, root, 755)
/usr/X11R6/share/kde/icons/mini/kscreensaver.xpm
/usr/X11R6/share/kde/apps/kscreensaver/
/usr/X11R6/share/kde/icons/kscreensaver.xpm

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/klock.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/klock.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/klock.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/klock.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/klock.mo
%lang(en) /usr/X11R6/share/locale/en*/LC_MESSAGES/klock.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/klock.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/klock.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/klock.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/klock.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/klock.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/klock.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/klock.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/klock.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/klock.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/klock.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/klock.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/klock.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/klock.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/klock.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/klock.mo

%defattr(755, root, root, 755)
/usr/X11R6/bin/klock
/usr/X11R6/bin/*.kss

#################################################
#            KVT 
#################################################
%files -n kvt
%defattr(644, root, root, 755)
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kvt
/usr/X11R6/share/kde/icons/mini/kvt.xpm
%config(missingok) /etc/X11/kde/applnk/Utilities/kvt.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekvt
/usr/X11R6/share/kde/icons/kvt.xpm

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kvt.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kvt.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kvt.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kvt.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kvt.mo
%lang(en) /usr/X11R6/share/locale/en*/LC_MESSAGES/kvt.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kvt.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kvt.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kvt.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kvt.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kvt.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kvt.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kvt.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kvt.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kvt.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kvt.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kvt.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kvt.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kvt.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kvt.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kvt.mo

%defattr(755, root, root, 755)
/usr/X11R6/bin/kvt

#################################################
#            KMENUEDIT
#################################################
%files -n kmenuedit
%defattr(644, root, root, 755)
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kmenuedit/
%config(missingok) /etc/X11/kde/applnk/Utilities/KMenuEdit.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKMenuEdit
/usr/X11R6/share/kde/icons/mini/kmenuedit.xpm
/usr/X11R6/share/kde/icons/kmenuedit.xpm
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kmenuedit.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kmenuedit.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kmenuedit.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kmenuedit.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kmenuedit.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kmenuedit.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kmenuedit.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kmenuedit.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kmenuedit.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kmenuedit.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kmenuedit.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kmenuedit.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kmenuedit.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kmenuedit.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kmenuedit.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kmenuedit.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kmenuedit.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kmenuedit.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kmenuedit.mo

%defattr(755, root, root, 755)
/usr/X11R6/bin/kmenuedit

#################################################
#            KPANEL
#################################################
%files -n kpanel
%defattr(644, root, root, 755)
/usr/X11R6/share/kde/apps/kpanel/
%config /etc/X11/kde/kpanelrc
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/kcmkpanel/
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kpanel/index.html
%config(missingok) /etc/X11/kde/applnk/Settings/Applications/panel.kdelnk
%config(missingok) /etc/X11/wmconfig/kdepanel
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kpanel.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kpanel.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kpanel.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kpanel.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kpanel.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kpanel.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kpanel.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kpanel.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kpanel.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kpanel.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kpanel.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kpanel.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kpanel.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kpanel.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kpanel.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kpanel.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kpanel.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kpanel.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kpanel.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kpanel.mo
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kcmkpanel.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kcmkpanel.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kcmkpanel.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kcmkpanel.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kcmkpanel.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kcmkpanel.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kcmkpanel.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kcmkpanel.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kcmkpanel.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kcmkpanel.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kcmkpanel.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kcmkpanel.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kcmkpanel.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kcmkpanel.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kcmkpanel.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kcmkpanel.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kcmkpanel.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kcmkpanel.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kcmkpanel.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kcmkpanel.mo

%defattr(755, root, root, 755)
%attr(-,root,root) /usr/X11R6/bin/kpanel
%attr(-,root,root) /usr/X11R6/bin/kcmkpanel

#################################################
#            KDM
#################################################
%files -n kdm
%defattr(644, root, root, 755)
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kdm/
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcontrol/kdmconfig/
%config(missingok) /etc/X11/kde/applnk/Settings/Applications/kdm.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekdm
%config /etc/X11/kde/kdmrc
/usr/X11R6/share/kde/apps/kdm/
/usr/X11R6/share/kde/apps/kdmconfig/
/usr/X11R6/share/kde/icons/mini/kdmconfig.xpm
/usr/X11R6/share/kde/icons/kdmconfig.xpm
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kdm.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kdm.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kdm.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kdm.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kdm.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kdm.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kdm.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kdm.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kdm.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kdm.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kdm.mo
%lang(mk) /usr/X11R6/share/locale/mk/LC_MESSAGES/kdm.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kdm.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kdm.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kdm.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kdm.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kdm.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kdm.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kdm.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kdm.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kdm.mo
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kdmconfig.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kdmconfig.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kdmconfig.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kdmconfig.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kdmconfig.mo
%lang(en) /usr/X11R6/share/locale/en*/LC_MESSAGES/kdmconfig.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kdmconfig.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kdmconfig.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kdmconfig.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kdmconfig.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kdmconfig.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kdmconfig.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kdmconfig.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kdmconfig.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kdmconfig.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kdmconfig.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kdmconfig.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kdmconfig.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kdmconfig.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kdmconfig.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kdmconfig.mo

%attr(755, root, root) /usr/X11R6/bin/kdm
%attr(755, root, root) /usr/X11R6/bin/kdmdesktop
%attr(755, root, root) /usr/X11R6/bin/kdmconfig

#################################################
#            KFONTMANAGER
#################################################
%files -n kfontmanager
%defattr(644, root, root, 755)
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kfontmanager/
%config(missingok) /etc/X11/kde/applnk/System/Kfontmanager.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKfontmanager
/usr/X11R6/share/kde/icons/mini/kfontmanager.xpm
/usr/X11R6/share/kde/icons/kfontmanager.xpm

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kfontmanager.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kfontmanager.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kfontmanager.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kfontmanager.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kfontmanager.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kfontmanager.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kfontmanager.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kfontmanager.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kfontmanager.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kfontmanager.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kfontmanager.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kfontmanager.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kfontmanager.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kfontmanager.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kfontmanager.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kfontmanager.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kfontmanager.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kfontmanager.mo
%lang(sl) /usr/X11R6/share/locale/sl/LC_MESSAGES/kfontmanager.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kfontmanager.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kfontmanager.mo

%attr(755, root, root) /usr/X11R6/bin/kfontmanager

%changelog
* Wed Dec  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-7]
- recompiled against libstdc++.so.2.9.

* Sun Oct 4 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-5]
- startkde.PLD changed and made "kdeenv".

* Mon Sep 28 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-4]
- moved to new directory hierarchy (see kdelibs.spec).

* Sat Sep 26 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-3]
- added dependencies on kdebase to kcontrol,
- kbgndwm and wallpapers separated from kwm,
- documentation marked %lang(en),
- kdelnk files marked as %config,
- config files moved to /etc/kde/config.

* Sat Sep 19 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-3]
- changed KDEDIR to /usr/X11R6,
- removed using macros kdename, version and kderelease,
- added pl translation,
- added real %files,
- added using $RPM_OPT_FLAGS during compilation,
- split into several packages,
- added devel subpackage,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc),
- removed Distribution field (this also must be placed in private .rpmrc),
- base dir changed to /usr/X11R6,
- added -q an emoved -n %setup parameter,
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} macros in Source,
- added %lang macros for /usr/share/locale/*/LC_MESSAGES/ files,
- "rm -rf $RPM_BUILD_ROOT" moved from %prep to %install.
