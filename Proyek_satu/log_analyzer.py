# 1. Buka file server log
# Kita pakai 'with open' supaya file otomatis tertutup setelah selesai dibaca

file_path = "server.log"
print(f"--- Memulai Analisis Log: {file_path} ---")

# Kamus (Dictionary) untuk menyimpan data penyerang
# Formatnya nanti: { "IP_ADDRESS": JUMLAH_GAGAL }
failed_logins = {}

# 2. Baca file baris demi baris
with open(file_path, 'r') as file:
    for line in file:
        # Kita hanya peduli kalau ada tulisan "Login failed"
        if "Login failed" in line:
            # Contoh baris: ... failed for user: root from IP: 203.0.113.5
            
            # Ambil bagian IP-nya (teknik slicing sederhana)
            # Kita split kalimat berdasarkan kata "IP: "
            parts = line.split("IP: ")
            # parts[1] isinya: "203.0.113.5\n" (ada enter di akhir)
            ip_address = parts[1].strip() # strip() untuk buang enter

            # 3. Hitung jumlah percobaan gagal
            # cek apakah IP sudah ada di dictionary
            if ip_address in failed_logins:
                # jika sudah ada, tambah hitungannya
                failed_logins[ip_address] += 1
            else:
                # jika belum ada, masukkan ke dictionary dengan hitungan 1
                failed_logins[ip_address] = 1

# 4. Tampilkan Hasil Peringatan
print("\n[HASIL DETEKSI]")
threshold = 3  # Batas toleransi gagal login

for ip, count in failed_logins.items():
    if count > threshold:
        print(f"🚨 BAHAYA: IP {ip} mencoba login {count} kali! (Indikasi Brute Force)")
    else:
        print(f"⚠️  Waspada: IP {ip} gagal login {count} kali.")