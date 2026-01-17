#!/bin/bash

echo "-----------------------------------"
echo "    Hack99y Setup & Launch        "
echo "-----------------------------------"

# 1. التحقق من صلاحيات الجذر (Root)
if [ "$EUID" -ne 0 ]; then 
  echo "Please run as root (use sudo)"
  exit
fi

# 2. تثبيت التبعيات إذا كانت مفقودة
echo "[*] Installing/Checking dependencies..."
apt-get update -y > /dev/null
apt-get install aircrack-ng python3-pip -y > /dev/null
pip3 install scapy --break-system-packages --quiet

# 3. تجهيز قائمة الأسماء
echo "[*] Generating names.txt..."
python3 -c "print('\n'.join(['Hacky' + str(i) for i in range(100)]))" > names.txt

# 4. تفعيل وضع المراقبة (Monitor Mode)
echo "[*] Optimizing network interfaces..."
airmon-ng check kill > /dev/null
airmon-ng start wlan0 > /dev/null
airmon-ng start wlan1 > /dev/null

# 5. تشغيل الأداة
echo "[+] Setup complete. Launching Hack99y..."
python3 Hack99y.py
