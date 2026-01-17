#!/bin/bash
echo -e "\e[32m[*] Hack99y: Installing Dual-Interface Dependencies...\e[0m"
sudo apt-get update
sudo apt-get install -y python3-pip python3-tk airmon-ng tcpdump macchanger
pip3 install customtkinter scapy psutil --break-system-packages

# تفعيل وضع المراقبة للكرتين تلقائياً
echo -e "\e[34m[*] Activating Monitor Mode for wlan0 and wlan1...\e[0m"
sudo airmon-ng start wlan0
sudo airmon-ng start wlan1

echo -e "\e[32m[+] Ready. Starting Hack99y...\e[0m"
sudo python3 Hack99y.py
