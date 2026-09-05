#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

if [ -x /usr/bin/minios-thunar-uca-sync ]; then
  /usr/bin/minios-thunar-uca-sync >/dev/null || true
fi

xrdb -merge .Xresources

exec xfce4-session
