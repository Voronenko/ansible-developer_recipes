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
sudo bash -c "echo $SUDOERUSER ALL=\(ALL\) NOPASSWD: /usr/bin/truecrypt >> $SUDOERFILE"
sudo bash -c "echo $SUDOERUSER ALL=\(ALL\) NOPASSWD: /bin/systemctl >> $SUDOERFILE"
sudo bash -c "echo $SUDOERUSER ALL=\(ALL\) NOPASSWD: /sbin/poweroff, /sbin/reboot, /sbin/shutdown >> $SUDOERFILE"
sudo bash -c "echo $SUDOERUSER ALL=\(ALL\) NOPASSWD: /etc/init.d/nginx, /etc/init.d/mysql, /etc/init.d/mongod, /etc/init.d/redis, /etc/init.d/php-fpm >> $SUDOERFILE"
sudo bash -c "echo $SUDOERUSER ALL=\(ALL\) NOPASSWD:SETENV: /usr/bin/docker, /usr/sbin/docker-gc >> $SUDOERFILE"

echo "===================================================================="
echo "current user to SUDOERS w/o password"
echo "don't  forget to remove settings after initial box configuration"
echo "by removing file $SUDOERFILE"


