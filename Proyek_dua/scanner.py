import socket  # 1. Kita impor alat komunikasi jaringan

print("=== PROJECT 2: MINI PORT SCANNER ===")

# 2. Minta input dari User
target = input("Masukkan alamat IP contoh (8.8.8.8): ")

print(f"\nSedang Memindai Target: {target}")
print("=" * 40)

# Daftar port umum yang mau dicek
# 21=FTP, 22=SSH, 80=Web, 443=Web Aman, 3306=Database
ports_to_scan = [21, 22, 53, 80, 443, 3306, 8080, 8443]

for port in ports_to_scan:
    # 3. Membuat objek socket (ibarat telepon)
    # AF_INET = IPv4, SOCK_STREAM = TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Kita set waktu tunggu (timeout) 1 detik biar gak kelamaan
    s.settimeout(1)
    
    # 4. Error Handling (Jurus Anti-Crash)
    try:
        # Coba ketuk pintu (connect)
        # connect_ex mengembalikan 0 kalau BERHASIL (Pintu Terbuka)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port}: TERBUKA (OPEN) ✅")
        else:
            print(f"[-] Port {port}: TERTUTUP (CLOSED) ❌")
    except:
        print(f"[-] Terjadi kesalahan saat memindai port {port}")
    finally:
        # 5. Selalu tutup telepon setelah selesai (sopan santun)
        s.close()
    
print("-" * 40)
print("Pemindaian Selesai.")

    # Ganti list manual tadi dengan range
# range(75, 85) artinya angka 75 sampai 84 (angka terakhir gak ikut)
print("Memindai port 75 sampai 85...")

for port in range(75, 86):  # Kita set sampai 86 biar 85 ikut kena
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Kita percepat dikit timeoutnya jadi 0.5 detik
    
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port}: TERBUKA! ✅")
        else:
            # Kita cuma print kalau terbuka saja biar layar gak penuh
            # pass artinya "jangan lakukan apa-apa"
            pass 
            
    except:
        pass
    finally:
        s.close()

