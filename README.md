# check_tabs
**List ip-addresses of all opened tabs in Mozilla Firefox browser on OS Ubuntu(maybe it will work on other debian-based OS).**

## About:
1. Script is parsing a file, which is generated by Mozilla Firefox browser. This file is updating every 15 seconds, so you need to wait some time after opening a new site in a tab and then run this script to view all opened sites.
2. All tests was made with configuration:
   - OS: Ubuntu 20.04.1-desktop
   - Mozilla Firefox version: 79.0
   - Python version: 3.8.2
   
### To make script work you need:
First of all, you need to download files from a web-interface of github.com or by using a git package on your OS. 

This instruction was written for a case with using a git package.

1. Install git package to your PC.
```
sudo apt install git -y
```

2. Clone this repo to your OS Ubuntu:
```
git clone https://github.com/g-anikin/check_tabs.git
```

3. Go to the directory "check_tabs".
```
cd ./check_tabs
```

4. Make files install.sh and check_tabs.py executable:
```
sudo chmod +x install.sh
sudo chmod +x check_tabs.py
```

5. Run install.sh
```
./install.sh
```

6. Open Mozilla Firefox browser and go to some sites in new tabs.

7. Run script check_tabs.py from user, with whom you opened a Mozilla Firefox browser:
```
./check_tabs.py
```

8. You will see unique ip-addresses of sites you opened and a number of this ip-addresses.
