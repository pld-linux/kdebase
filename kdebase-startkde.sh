#!/bin/sh
#
# $Id$
#
# Default KDE startup script.
#
# Author:	KDE Team
#		Modified for PLD Linux by Micha³ Zawalich <michuz@pld.org.pl>.

# Help message.
if [ $# -eq 1 ] && [ $1 = "--help" ]; then
    echo "This script starts KDE."
    echo "Usage: startkde [window_manager]"
    exit 1
fi

# Prevent an ever growing .ICEauthority file, since that will kill application
# startup performance.
rm -f $HOME/.ICEauthority*
rm -f $HOME/.DCOPserver*
rm -f $HOME/.dcop*

# Background and cursor.
xsetroot -cursor_name left_ptr -solid '#007777'

# Set KDE config directory. If $KDEHOME exist do nothing.
if [ -n $KDEHOME ]; then
    echo $KDEHOME
elif [ -n $CONFIG_DIR ] && [ ! -e $HOME/.kde ] && [ -d $HOME/$CONFIG_DIR ]; then
    export KDEHOME="$HOME/$CONFIG_DIR/kde"
    echo $KDEHOME
else
    export KDEHOME="$HOME/.kde"
    echo $KDEHOME
fi

# Add user fonts. Fonts in $OVERRIDE_FONT_DIR will be added first.
OVERRIDE_FONT_DIR="$KDEHOME/share/fonts/override"
FONT_DIR="$KDEHOME/share/fonts"

if [ -d $OVERRIDE_FONT_DIR ]; then
    mkfontdir $OVERRIDE_FONT_DIR
    xset +fp $OVERRIDE_FONT_DIR
fi

if [ -d $FONT_DIR ]; then
    mkfontdir $FONT_DIR
    xset fp+ $FONT_DIR
fi

xset fp rehash

# Link "tmp" resource to directory in /tmp
# Creates a directory /tmp/kde-$USER and links $KDEHOME/tmp-$HOSTNAME to it.
lnusertemp tmp >/dev/null

# Link "socket" resource to directory in /tmp
# Creates a directory /tmp/ksocket-$USER and links $KDEHOME/socket-$HOSTNAME 
# to it.
lnusertemp socket >/dev/null

# the splashscreen and progress indicator
ksplash

# We set LD_BIND_NOW to increase the efficiency of kdeinit.
# kdeinit unsets this variable before loading applications.
LD_BIND_NOW="true" kdeinit +kdesktop +kcminit +kicker +klipper +khotkeys kwrited

# The notification daemon. Not started with kdeinit because it uses threads
# and kdeinit doesn't.
knotify

# Start window manager.
if [ $# -eq 1 ]; then
    ksmserver --windowmanager $1
else
    ksmserver --restore
fi

# Restore saved GTK settings.
if [ -e $HOME/.gtkrc-save ]; then
    mv $HOME/.gtkrc-save $HOME/.gtkrc
fi
