#!/usr/bin/env bash
# This Code write by Mr.nope
# Version: 1.2
if [[ "$(id -u)" -ne 0 ]]; then
  echo "Please, Run This Programm as Root!"
  echo ""
  exit 1
fi
clear
echo "Installing..."
sleep 2
chmod +x main.py
apt install python
apt install python3
apt install python3-pip
pip3 install --upgrade pip3
pip3 install PyQt5
pip3 install pygame
echo ""
echo "-------- Finish ---------"
echo ""
exit 1
