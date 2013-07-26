#!/bin/bash -x
PKG=watcher
VERSION=0.5
DIR=deb_dist/$PKG-$VERSION


rm -rf deb_dist/*
mkdir -p $DIR

cp -r src $DIR/

cp -r debian $DIR/
sed -e "s/__VERSION__/$VERSION/g" debian/changelog > $DIR/debian/changelog

cd $DIR
# NOTE: You can use Debian quilt, but it requires orig.tar.gz
cd -


cd $DIR; debuild -uc -us
