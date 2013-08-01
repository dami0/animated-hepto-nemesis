#!/usr/bin/sh

cd $PAC

/usr/bin/pacman -Qqen > pacbac.repo
/usr/bin/pacman -Qqem > pacbac.aur
