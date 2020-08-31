#!/bin/bash

#Update apt database
sudo apt update
#Installing git package
sudo apt install git -y
#Clone git-repo
git clone https://github.com/g-anikin/check_tabs.git
#Make files install.sh and check_tabs.py executable
sudo chmod +x ./check_tabs/install.sh
sudo chmod +x ./check_tabs/check_tabs.py
#Installing pip3 module
sudo apt install python3-pip -y
#Intalling requirements for python3
sudo pip3 install -r requirements.txt
