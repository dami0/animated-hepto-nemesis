#!/usr/bin/bash

. ./aard.conf

cd $PAC

/usr/bin/pacman -Qqen > pacbac.repo
/usr/bin/pacman -Qqem > pacbac.aur
