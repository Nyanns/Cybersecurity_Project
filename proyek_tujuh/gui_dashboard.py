import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests

print("=== PROJECT 7: CYBER DASHBOARD GUI ===")

class CyberDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("MIKU INTEL TRACKER v3.9") # 39 = Miku
        self.root.geometry("600x500")
        
        # --- THEME COLORS (HATSUNE MIKU PALETTE) ---
        self.warna_bg = "#1a1a1a"       # Dark Grey (Backdrop)
        self.warna_miku = "#39C5BB"     # Miku Teal (Primary)
        self.warna_teks = "#E0FFFF"     # Light Cyan (Text)
        self.warna_tombol = "#ff0066"   # Pink Accent (Button)
        self.font_utama = ("Consolas", 12)
        self.font_judul = ("Segoe UI", 20, "bold")

        # Konfigurasi Window Utama
        self.root.configure(bg=self.warna_bg)

        # --- 1. BAGIAN HEADER ---  
        self.label_judul = tk.Label(
            root, 
            text="🎵 MIKU CYBER TRACKER 🎵", 
            font=self.font_judul, 
            bg=self.warna_bg, 
            fg=self.warna_miku
        )
        self.label_judul.pack(pady=20)

        # --- 2. BAGIAN INPUT ---
        frame_input = tk.Frame(root, bg=self.warna_bg)
        frame_input.pack(pady=10)

        tk.Label(
            frame_input, 
            text="Target IP Address >", 
            font=self.font_utama, 
            bg=self.warna_bg, 
            fg=self.warna_teks
        ).pack(side=tk.LEFT)

        self.entry_ip = tk.Entry(
            frame_input, 
            width=25, 
            font=("Consolas", 12, "bold"), 
            bg="#333333",   # Darker input bg
            fg=self.warna_miku, # Miku color text
            insertbackground="white" # Cursor color
        )
        self.entry_ip.pack(side=tk.LEFT, padx=10)

        # --- 3. TOMBOL EKSEKUSI ---
        self.btn_scan = tk.Button(
            root, 
            text="⚡ INITIALIZE SCAN ⚡", 
            font=("Segoe UI", 12, "bold"),
            bg=self.warna_tombol, 
            fg="white", 
            activebackground=self.warna_miku,
            activeforeground="black",
            relief=tk.FLAT,
            command=self.lacak_data,
            cursor="hand2"
        )
        self.btn_scan.pack(pady=15, ipadx=20, ipady=5)

        # --- 4. LAYAR HASIL (OUTPUT) ---
        self.layar_hasil = scrolledtext.ScrolledText(
            root, 
            width=60, 
            height=15, 
            font=("Consolas", 11),
            bg="#0d0d0d",       # Almost black
            fg=self.warna_miku, # Teal text
            insertbackground="white",
            relief=tk.FLAT,
            bd=2
        )
        self.layar_hasil.pack(pady=10)
        
        # Border Fancy untuk Layar Hasil
        self.layar_hasil.config(highlightbackground=self.warna_miku, highlightcolor=self.warna_tombol, highlightthickness=2)
        
        self.update_layar(">>> SYSTEM READY...\n>>> WAITING FOR INPUT...")

    def lacak_data(self):
        ip_address = self.entry_ip.get().strip()
        if not ip_address:
            messagebox.showwarning("⚠️ ACCESS DENIED", "Harap masukkan alamat IP!")
            return
        
        try:
            self.update_layar(f">>> CONNECTING TO SATELLITE... \n>>> TRACKING {ip_address}...")
            self.root.update() # Force update UI biar teks muncul dulu
            
            # Setup URL dan Headers
            url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,city,isp,org,lat,lon,timezone,as"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
            
            # Request ke API
            response = requests.get(url, headers=headers, timeout=5)
            data = response.json()
            
            if data['status'] == 'fail':
                self.update_layar(f"❌ CONNECTION FAILED: {data['message']}")
            else:
                # Format hasil laporan a la Hacker/Miku style
                laporan = (
                    f"\n✅ TARGET LOCKED!\n"
                    f"==================================================\n"
                    f"🏳️  COUNTRY     : {data.get('country')}\n"
                    f"🏙️  CITY        : {data.get('city')}\n"
                    f"📡  ISP         : {data.get('isp')}\n"
                    f"🏢  ORG         : {data.get('org')}\n"
                    f"⏰  ZONE        : {data.get('timezone')}\n"
                    f"📍  COORDINATES : {data.get('lat')}, {data.get('lon')}\n"
                    f"==================================================\n"
                    f">>> DATA ACQUISITION COMPLETE.\n"
                )
                self.update_layar(laporan)
                
        except Exception as e:
            self.update_layar(f"❌ SYSTEM ERROR: {e}")

    def update_layar(self, teks):
        self.layar_hasil.delete(1.0, tk.END)
        self.layar_hasil.insert(tk.END, teks)

# --- BOOTSTRAP ---
if __name__ == "__main__":
    window = tk.Tk()
    app = CyberDashboard(window)
    window.mainloop()