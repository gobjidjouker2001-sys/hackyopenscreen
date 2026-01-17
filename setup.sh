#!/bin/bash

# الألوان للتنسيق
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}[*] جاري تجهيز بيئة Hack99y...${NC}"

# التأكد من صلاحيات الـ Root
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}[!] يرجى التشغيل باستخدام sudo./setup.sh${NC}"
   exit 1
fi

# تثبيت أدوات النظام الضرورية
echo -e "${GREEN}[1/3] تثبيت أدوات الشبكة...${NC}"
apt-get update
apt-get install -y python3-pip python3-tk airmon-ng tcpdump iw net-tools

# تثبيت مكتبات البايثون
echo -e "${GREEN}[2/3] تثبيت مكتبات Python...${NC}"
pip3 install customtkinter scapy psutil --break-system-packages

# إعداد الكروت (اختياري هنا لأن الواجهة تقوم بذلك، لكن نجهرها للنظام)
echo -e "${GREEN}[3/3] تهيئة أذونات الملفات...${NC}"
chmod +x Hack99y.py

echo -e "${CYAN}=======================================${NC}"
echo -e "${GREEN}[+] تم التثبيت بنجاح!${NC}"
echo -e "${GREEN}[+] لتشغيل الأداة: sudo python3 Hack99y.py${NC}"
echo -e "${CYAN}=======================================${NC}"
