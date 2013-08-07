#!/usr/bin/bash

. ./conf.dat

cd $DIR

/usr/bin/pacman -Qqen > pacbac.repo
/usr/bin/pacman -Qqem > pacbac.aur
