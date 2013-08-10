#!/usr/bin/bash

cd $1

/usr/bin/pacman -Qqen > pacbac.repo
/usr/bin/pacman -Qqem > pacbac.aur
