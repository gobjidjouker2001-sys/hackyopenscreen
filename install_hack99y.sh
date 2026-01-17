#!/bin/bash
# الألوان
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}[*] Installing Hack99y Wireless Tools...${NC}"

# تثبيت أدوات النظام
sudo apt update
sudo apt install -y python3-pip python3-tk airmon-ng mdk4 tcpdump

# تثبيت مكتبات بايثون
pip3 install customtkinter scapy psutil --break-system-packages

# إعطاء صلاحية التشغيل
chmod +x Hack99y.py

echo -e "${GREEN}[+] Everything is installed. Run 'sudo python3 Hack99y.py' to start.${NC}"
