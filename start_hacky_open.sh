#!/bin/bash

# الألوان
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}[*] Preparing Hacky Open Screen Environment...${NC}"

# 1. تثبيت التبعيات
sudo apt update
sudo apt install python3-tk adb fastboot python3-pip -y

# 2. تثبيت المكتبات الرسومية
pip3 install customtkinter --break-system-packages

# 3. تشغيل الـ ADB Server
sudo adb kill-server
sudo adb start-server

echo -e "${GREEN}[+] Environment Ready! Launching Tool...${NC}"
chmod +x HackyOpenScreen.py
python3 HackyOpenScreen.py
