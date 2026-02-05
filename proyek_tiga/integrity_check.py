import hashlib
import time
import os
print("File tersimpan di sini:", os.path.abspath("rahasia.txt"))

print("=== PROJECT 3: FILE INTEGRITY MONITOR ===")

# --- BAGIAN 1: MEMBUAT FUNGSI SENDIRI ---
# Kita bikin "mesin" khusus penghasil Hash biar bisa dipanggil berkali-kali

def hitung_hash(nama_file):
    # Kita pakai algoritma SHA256 (Standar keamanan militer/perbankan)
    sha256_hash = hashlib.sha256()

    try:
        # Buka file dalam mode 'rb' (Read Binary)
        # Kenapa rb? Karena kita mau baca isinya murni sebagai byte, bukan teks
        with open(nama_file, "rb") as f:
            # Baca file blok demi blok (biar RAM gak meledak kalau file besar)
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        # Kembalikan hasil fingerprint-nya (bentuk kode hex)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "ERROR: File tidak ditemukan!"

# --- BAGIAN 2: MENGHITUNG HASH FILE ---
# Agar file txt tersimpan di folder yang sama dengan script ini
current_dir = os.path.dirname(os.path.abspath(__file__))
target_file = os.path.join(current_dir, "rahasia.txt")

# Kita buat dulu file awal kalau belum punya
with open(target_file, "w") as f:
    f.write("Ini adalah data rahasia negara. Jangan diubah!")

print(f"[1] Membaca kondisi awal file '{target_file}'...")
hash_awal = hitung_hash(target_file)
print(f"🔒 Sidik Jari (Hash) Asli: {hash_awal}")
print("-" * 50)

# --- BAGIAN 3: SIMULASI SERANGAN HACKER ---
input("⚠️  TANTANGAN: Minimize window ini, buka file 'rahasia.txt', ubah isinya sedikit, save, lalu kembali ke sini dan tekan ENTER.")
print("\n[2] Memeriksa ulang file...")
time.sleep(1) # Efek dramatis loading

hash_baru = hitung_hash(target_file)
print(f"🔎 Sidik Jari (Hash) Baru: {hash_baru}")

print("-" * 50)

# --- BAGIAN 4: PERIKSA PERUBAHAN ---
if hash_awal == hash_baru:
    print("✅ File TIDAK DIUBAH. Apa yang kamu lakukan?")
else:
    print("🚨 PERINGATAN! File DIUBAH! Apa yang kamu lakukan?")
    print("Seseorang telah mengubah isinya diam-diam.")


