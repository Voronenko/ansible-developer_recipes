#!/bin/bash

if [ "$(id -u)" == "0" ]; then
echo "Installation must NOT be done under sudo"
echo "use your regular user account"
exit 1
fi

sudo apt-get -y install git curl

SUDOERUSER="$(whoami)"
SUDOERFILE="/etc/sudoers.d/$SUDOERUSER"

sudo bash -c "touch $SUDOERFILE"
sudo bash -c "echo $SUDOERUSER ALL=\(ALL\) NOPASSWD: ALL > $SUDOERFILE"

sudo apt-get -y install -y software-properties-common git python-dev wget apt-transport-https libffi-dev libssl-dev
sudo apt-get install -y python-pip
sudo pip install -U pip
sudo pip install ansible

echo "===================================================================="
echo "current user to SUDOERS w/o password"
echo "don't  forget to remove settings after initial box configuration"
echo "by removing file $SUDOERFILE"
