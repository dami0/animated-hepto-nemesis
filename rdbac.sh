#!/usr/bin/sh

. ./conf.dat

if [ ! -d "$DIR" ]; then
  mkdir $DIR
fi

cp ./list.dat $DIR

cd $DIR

sudo rdiff-backup --include-globbing-filelist list.dat --exclude '**' / ./etc
sudo rdiff-backup / ./pkg
sudo rdiff-backup ~/Documents ./Documents

rm ./list.dat
