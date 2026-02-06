import requests
import json
import os
import sys

# Paksa output terminal menggunakan UTF-8 agar emoji tidak error di Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

print("=== PROJECT 6: IP GEOLOCATION TRACKER (OSINT) ===")

class IPTracker:
    def __init__(self):
        # API Gratisan (ip-api.com)
        self.base_url = "http://ip-api.com/json/"

    # TEKNIK SPOOFING (Menyamar)
        # Kita memalsukan identitas (User-Agent) supaya dikira Browser Chrome
        # Kalau tidak pakai ini, server akan melihat kita sebagai "python-requests/2.x"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    
    def lacak_ip(self, ip_address):
        print(f"\n[+] sedang melacak IP {ip_address}...")

        # Gabung URL + IP + Parameter
        # ?fields=status,message,country,city,lat,lon,isp,org,as,query
        # Contoh: http://ip-api.com/json/8.8.8.8
        # Tambahkan 'regionName' di sini
        url_lengkap = f"{self.base_url}{ip_address}?fields=status,message,country,countryCode,regionName,city,lat,lon,isp,org,timezone,query"
        
        try:
            #lakukan permintaan GET
            response = requests.get(url_lengkap, headers=self.headers, timeout=10)
            data = response.json()

            #cek apakah berhasil
            if data.get("status") == "success":
                self.tampilkan_info(data)
                self.tulis_laporan(data)
            else:
                print(f"❌ Gagal konek ke API. Status: {response.status_code}")
                print(f"Pesan: {data.get('message')}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Error Koneksi: {e}")
        except json.JSONDecodeError:
            print(f"❌ Format data tidak valid (Bukan JSON)")
        except Exception as e:
            print(f"❌ Error Tak Terduga: {e}")
    
    def tampilkan_info(self, data):
        # Karena 'data' sudah jadi Dictionary, kita tinggal panggil kuncinya
        print("\n" + "="*40)
        print(f"🔍 HASIL PELACAKAN")
        print("="*40)
        print(f"🏳️  Negara    : {data.get('country')} ({data.get('countryCode')})")
        print(f"🏙️  Kota      : {data.get('city')}")
        print(f"📍  Region    : {data.get('regionName')}")
        print(f"📡  ISP       : {data.get('isp')}")
        print(f"🏢  Org       : {data.get('org')}")
        print(f"⏰  Timezone  : {data.get('timezone')}")
        print(f"🌍  Koordinat : {data.get('lat')}, {data.get('lon')}")
        print("="*40)
        print("="*40)
        
        # Fitur Tambahan: Link Google Maps
        maps_link = f"https://www.google.com/maps/place/{data.get('lat')},{data.get('lon')}"
        print(f"🗺️  Lihat di Peta: {maps_link}")

    def tulis_laporan(self, data):
        nama_file = "laporan_ip.txt"

        # cek apakah file sudah ada
        if os.path.exists(nama_file):
            mode = "a" # append
        else:
            mode = "w" # Write

        with open(nama_file, mode, encoding="utf-8") as f:
            f.write("="*40)
            f.write("\n[+] LAPORAN PELACAKAN IP")
            f.write("\n" + "="*40)
            f.write(f"\n🏳️  Negara    : {data.get('country')} ({data.get('countryCode')})")
            f.write(f"\n🏙️  Kota      : {data.get('city')}")
            f.write(f"\n📍  Region    : {data.get('regionName')}")
            f.write(f"\n📡  ISP       : {data.get('isp')}")
            f.write(f"\n🏢  Org       : {data.get('org')}")
            f.write(f"\n⏰  Timezone  : {data.get('timezone')}")
            f.write(f"\n🌍  Koordinat : {data.get('lat')}, {data.get('lon')}")
            f.write("\n" + "="*40)
            f.write("\n\n")

        print(f"\n[+] Laporan disimpan ke {nama_file}")

# --- MAIN PROGRAM ---
tracker = IPTracker()

daftar_ip = ["8.8.8.8", "1.1.1.1"]

for i in range(len(daftar_ip)):
    target = daftar_ip[i]
    tracker.lacak_ip(target)