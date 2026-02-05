import base64
import os

print("=== PROJECT 5: OOP RANSOMWARE SIMULATOR ===")

# --- BAGIAN 1: BLUEPRINT (CETAKAN) ---
class Ransomware:
    # 1. __init__ adalah "Constructor"
    # Ini dijalankan PERTAMA KALI saat virus 'dihidupkan'
    def __init__(self, nama_virus, target_file):
        self.nama = nama_virus      # Menyimpan nama ke memori diri sendiri
        self.target = target_file   # Menyimpan target ke memori diri sendiri
        self.kunci = None           # Kunci belum ada saat baru lahir
        print(f"🤖 Virus '{self.nama}' telah lahir! Mengincar: {self.target}")
    
    # 2. Method untuk MENGUNCI (Encrypt)
    def lock_file(self):
        print(f"\n[{self.nama}] Sedang mengenkripsi {self.target}...")

        if not os.path.exists(self.target):
            print("❌ Error: Target tidak ditemukan!")
            return
        
        # Baca file asli
        with open(self.target, "rb") as f:
            data_asli = f.read()
        
        # Proses Enkripsi (Pura-pura pakai Base64 biar bisa dibalikin)
        # Di dunia nyata, hacker pakai AES/RSA
        data_encrypted = base64.b64encode(data_asli)

        # Timpa file dengan data acak
        with open(self.target, "wb") as f:
            f.write(data_encrypted)
        
        print(f"🔒 FILE TERKUNCI! Isinya sekarang jadi acak.")

    def unlock_file(self, password_input):
        print(f"\n[{self.nama}] Mencoba Membuka Kunci...")

        # Cek Password (Hardcoded untuk latihan)
        if password_input != "rahasia123":
            print("❌ PASSWORD SALAH! File tetap terkunci.")
            return

        # Kalau password benar, kita balikin
        with open(self.target, "rb") as f:
            data_encrypted = f.read()
        
        try:
            data_asli = base64.b64decode(data_encrypted)
            with open(self.target, "wb") as f:
                f.write(data_asli)
            print("✅ FILE BERHASIL DIBUKA KEMBALI!")
        except:
            print("❌ Gagal mendekripsi. File mungkin sudah rusak atau bukan file saya.")

# --- BAGIAN 2: MAIN PROGRAM (SIMULASI) ---

# A. Kita buat dulu file korban pura-pura
file_korban = "data_kantor.txt"
with open(file_korban, "w") as f:
    f.write("Laporan Keuangan: Profit 1 Milyar Rupiah.")

print(f"📄 File korban dibuat: {file_korban}")
print("-" * 40)

# B. INSTANSIASI (Melahirkan Virus dari Cetakan)
# Kita bikin virus bernama 'WannaCry-V2'

virus_ku = Ransomware("WannaCry-V2", file_korban)

# C. Jalankan Aksi
# Perhatikan: Kita panggil method pakai titik (.)
virus_ku.lock_file()

# D. Coba Buka (Pasti Gagal)
virus_ku.unlock_file("password_salah")

# E. Coba Buka (Pasti Berhasil)
virus_ku.unlock_file("0000000")# D. Cek isi file (Membuktikan file rusak)
with open(file_korban, "r") as f:
    print(f"\n[BUKTI] Isi file sekarang: {f.read()}")

print("-" * 40)

# E. Minta Tebusan
tebusan = input("Masukkan password untuk dekripsi: ")
virus_ku.unlock_file(tebusan)

# F. Cek lagi
with open(file_korban, "r") as f:
    print(f"\n[FINAL] Isi file sekarang: {f.read()}")