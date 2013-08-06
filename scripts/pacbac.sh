#!/usr/bin/bash

. ./aard.conf

cd $DIR

/usr/bin/pacman -Qqen > pacbac.repo
/usr/bin/pacman -Qqem > pacbac.aur
