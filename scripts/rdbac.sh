#!/usr/bin/sh

. ./aard.conf

cd $DIR

sudo rdiff-backup --include /etc/pacman.d --include /etc/ssh --include /etc/samba --include '**pacman.conf' --include '**vsftpd.conf' --include '**fstab' --exclude '**' /etc ./etc
sudo rdiff-backup /var/cache/pacman/pkg ./pkg
