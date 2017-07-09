#!/bin/bash

rm -rf build dist

NAME=sermonuploader

mkdir -p build/lib
mkdir -p build/app
mkdir build/src
mkdir build/tmp

cp ./$NAME.py ./build/app/$NAME.py
cp -R ./windows_libs/python ./build/lib/python

git add -A; snapshot=`git stash create`; git archive -o ./build/tmp/snapshot.zip ${snapshot:-HEAD}

unzip ./build/tmp/snapshot.zip -d ./build/src
cp LICENSE build/LICENSE

wine ./windows_libs/bat2exe.exe -bat ./bootstrap.bat -save ./build/$NAME.exe

rm -rf ./build/tmp

if [ -z "$DEVMODE" ]
then
  mkdir dist
  cd build
  zip -r ../dist/$NAME.zip *
else
  wineserver -k
  wine ./build/sermonuploader.exe
fi


