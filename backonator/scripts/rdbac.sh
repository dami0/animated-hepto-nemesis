#!/usr/bin/sh

cp ./list.dat $1

cd $1

sudo rdiff-backup --include-globbing-filelist list.dat --exclude '**' /etc ./etc
sudo rdiff-backup /var/cache/pacman/pkg ./pkg
sudo rdiff-backup ~/Documents ./Documents

rm ./list.dat
