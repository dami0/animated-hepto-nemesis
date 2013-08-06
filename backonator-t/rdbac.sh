#!/usr/bin/sh

. ./conf.dat

if [ ! -d "$DIR" ]; then
  mkdir $DIR
fi

cd $DIR

sudo rdiff-backup --include-filelist list --exclude '**' /etc ./etc
sudo rdiff-backup /var/cache/pacman/pkg ./pkg
