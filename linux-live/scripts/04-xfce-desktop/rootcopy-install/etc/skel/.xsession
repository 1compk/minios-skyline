#!/bin/sh
if [ -x /usr/bin/minios-thunar-uca-sync ]; then
    /usr/bin/minios-thunar-uca-sync >/dev/null || true
fi
exec xfce4-session
