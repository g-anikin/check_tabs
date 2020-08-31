#!/bin/bash

#Update apt database
sudo apt update
#Installing pip3 module
sudo apt install python3-pip -y
#Intalling requirements for python3
sudo pip3 install -r requirements.txt
