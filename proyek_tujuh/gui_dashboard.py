import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests

print("=== PROJECT 7: CYBER DASHBOARD GUI ===")

class CyberDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("IP INTEL TRACKER v1.0")
        self.root.geometry("500x450") # Ukuran Jendela (Lebar x Tinggi)

        # --- 1. BAGIAN HEADER ---  
        # label tulisan statis 
        self.label_judul = tk.Label(root, text="IP INTEL TRACKER v1.0", font=("Arial", 16, "bold"))
        self.label_judul.pack(pady=10) # pady = padding y (jarak atas bawah)

        # --- 2. BAGIAN INPUT ---
        frame_input = tk.Frame(root)
        frame_input.pack(pady=5)

        tk.Label(frame_input, text="Masukkan IP Address: ").pack(side=tk.LEFT)

        # Entry: Kolom ketik (Input Box)
        self.entry_ip = tk.Entry(frame_input, width=20, font=("Arial", 12))
        self.entry_ip.pack(side=tk.LEFT, padx=5)

        # --- 3. TOMBOL EKSEKUSI ---
        # command=self.lacak_data -> Hubungkan tombol dengan fungsi logika
        self.btn_scan = tk.Button(root, text="SCAN LOCATION 🚀", bg="red", fg="white", command=self.lacak_data)
        self.btn_scan.pack(pady=10)

        # --- 4. LAYAR HASIL (OUTPUT) ---
        # ScrolledText: Kotak teks yang bisa discroll kalau isinya panjang
        self.layar_hasil = scrolledtext.ScrolledText(root, width=50, height=15, font=("Consolas", 10))
        self.layar_hasil.pack(pady=10)
        
        # Pesan awal
        self.update_layar("Siap melacak... Masukkan IP dan tekan SCAN.")

    def lacak_data(self):
        ip_address = self.entry_ip.get().strip()
        if not ip_address:
            messagebox.showwarning("Peringatan", "Harap masukkan alamat IP!")
            return
        
        try:
            # Setup URL dan Headers
            url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,city,isp,org,lat,lon"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
            
            # Request ke API
            response = requests.get(url, headers=headers, timeout=5)
            data = response.json()
            
            if data['status'] == 'fail':
                self.update_layar(f"❌ GAGAL: {data['message']}")
            else:
                # Format hasil laporan
                laporan = (
                    f"✅ TARGET DITEMUKAN!\n"
                    f"========================\n"
                    f"🏳️  Negara   : {data.get('country')}\n"
                    f"🏙️  Kota     : {data.get('city')}\n"
                    f"📡  ISP      : {data.get('isp')}\n"
                    f"🏢  Org      : {data.get('org')}\n"
                    f"📍  Koordinat: {data.get('lat')}, {data.get('lon')}\n"
                    f"========================\n"
                )
                self.update_layar(laporan)
                
        except Exception as e:
            self.update_layar(f"❌ ERROR SISTEM: {e}")

    # Fungsi pembantu untuk nulis di layar hitam
    def update_layar(self, teks):
        # Hapus dulu teks lama (dari baris 1.0 sampai END)
        self.layar_hasil.delete(1.0, tk.END)
        # Masukkan teks baru
        self.layar_hasil.insert(tk.END, teks)

# --- BOOTSTRAP (Pemicu Utama) ---
if __name__ == "__main__":
    # Membuat Canvas Utama
    window = tk.Tk()
    
    # Menjalankan Class Dashboard kita
    app = CyberDashboard(window)
    
    # MAIN LOOP (Jantungnya GUI)
    # Ini bikin jendela tetap terbuka dan menunggu klik mouse
    window.mainloop()