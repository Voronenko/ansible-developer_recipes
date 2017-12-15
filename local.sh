#!/bin/sh
stty_orig=`stty -g`
stty -echo
read -p "become pass: " BECOME_PASS
stty $stty_orig
ansible-playbook -i "localhost," -c local local.yml --extra-vars "'ansible_become_pass=${BECOME_PASS}'"
