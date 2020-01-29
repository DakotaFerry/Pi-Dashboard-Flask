#!/bin/sh

#Ensure chromium is installed

PKG_OK=$(dpkg-query -W --showformat='${Status}\n' chromium|grep "install ok installed")
echo Checking for somelib: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "No chromium. Setting up chromium."
  sudo apt-get install chromium ttf-mscorefonts-installer
fi


chromium --kiosk https://share.geckoboard.com/loop/PMFF3VHG4D3RFZOI --incognito
