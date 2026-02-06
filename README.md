# Belajar Py - Cybersecurity Learning Journey

Repository ini berisi kumpulan proyek hasil belajar Python saya yang berfokus pada cybersecurity dan automasi.

## Daftar Proyek

### 1. Proyek Satu: Log Analyzer
Folder: `Proyek_satu`
- **Deskripsi:** Script untuk menganalisis file log server (`server.log`).
- **File Utama:** `log_analyzer.py`
- **Fungsi:** Membaca, memfilter, dan mengekstrak informasi penting dari file log.

### 2. Proyek Dua: Network Scanner
Folder: `Proyek_dua`
- **Deskripsi:** Alat pemindai port sederhana untuk memeriksa keamanan jaringan.
- **File Utama:** `scanner.py`
- **Fungsi:** Memindai port yang terbuka pada target IP tertentu.

### 3. Proyek Tiga: File Integrity Monitor & Latihan
Folder: `proyek_tiga`
- **Deskripsi:** Script demonstrasi konsep Hashing dan latihan logika Python (Functional Programming).
- **File Utama:** `integrity_check.py`
- **File Latihan:** `latihan1.py`, `latihan2.py`, `latihan3.py`
- **Fungsi:** Menghitung hash SHA-256 untuk integritas data dan latihan filter/map/reduce.

### 4. Proyek Empat: Password Strength & Crack Simulation
Folder: `Proyek_empat`
- **Deskripsi:** Tool all-in-one untuk menilai kekuatan password dan simulasi serangan (Brute Force & Dictionary Attack).
- **File Utama:** `password_tool.py`
- **Fungsi:** 
    - `cek_kekuatan()`: Menilai password berdasarkan panjang, huruf, angka, dan simbol.
    - `brute_force_pin()`: Simulasi cracking PIN 4 angka.
    - `dictionary_attack()`: Simulasi serangan tebak kata sandi menggunakan kamus.

### 5. Proyek Lima: Ransomware Simulator (OOP)
Folder: `proyek_lima`
- **Deskripsi:** Simulasi cara kerja Ransomware menggunakan konsep Object Oriented Programming (OOP).
- **File Utama:** `ransomware_sim.py`
- **Fungsi:** 
    - Mendemonstrasikan enkripsi file sederhana (XOR/Base64 scheme).
    - Mekanisme penguncian dan pembukaan kembali file menggunakan "kunci".
    - **PENTING:** Hanya untuk tujuan edukasi di lingkungan terkontrol.

### 6. Proyek Enam: IP Geolocation Tracker (OSINT)
Folder: `proyek_enam`
- **Deskripsi:** Script untuk melacak lokasi fisik dari alamat IP menggunakan API publik (OSINT).
- **File Utama:** `ip_tracker.py`
- **Fungsi:** 
    - Melacak Negara, Kota, ISP, dan Koordinat dari sebuah IP Address.
    - Menggunakan teknik **User-Agent Spoofing** untuk menghindari deteksi bot.
    - Menghasilkan laporan otomatis ke file `laporan_ip.txt`.

---
*Repository ini dibuat untuk tujuan dokumentasi dan pembelajaran.*
