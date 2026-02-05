import re
import time

print("=== PROJECT 4: PASSWORD STRENGTH & CRACK SIMULATION ===")

# --- BAGIAN 1: FUNGSI VALIDATOR (REGEX) ---
def cek_kekuatan(password):
    score = 0
    kriteria = []

    # 1. Cek Panjang (Minimal 8 karakter)
    if len(password) >= 8:
        score += 1
        kriteria.append("panjang pass ok")
    else:
        kriteria.append("panjang pass kurang dari 8 karakter")
    
    # 2. Cek huruf besar
    if re.search(r"[A-Z]", password):
        score += 1
        kriteria.append("huruf besar ok")
    
    # 3. Cek huruf kecil
    if re.search(r"[a-z]", password):
        score += 1
        kriteria.append("huruf kecil ok")
    
    # 4. Cek angka
    if re.search(r"\d", password):
        score += 1
        kriteria.append("angka ok")

    # 5. Cek simbol
    if re.search(r"\W", password):
        score += 1
        kriteria.append("simbol ok")

    print(f"\nAnalisis Password: '{password}'")
    print(f"Kriteria: {', '.join(kriteria)}")

    print(f"⭐ Skor Kekuatan: {score}/5")
    if score < 3:
        print("⚠️  KESIMPULAN: Password LEMAH! Gampang dihack.")
    else:
        print("🛡️  KESIMPULAN: Password KUAT.")

    return score

# --- BAGIAN 2: SIMULASI BRUTE FORCE (PIN) ---
def brute_force_pin(target_pin):
    print(f"\n[+] Memulai serangan Brute Force ke PIN: {target_pin}")
    start_time = time.time()

    for i in range(10000):
        # Format i jadi string 4 digit (misal 5 jadi "0005")
        current_pin = f"{i:04d}"

        if current_pin == target_pin:
            end_time = time.time()
            durasi = end_time - start_time
            print(f"✅ PIN DITEMUKAN: {current_pin}")
            print(f"⏱️  Waktu yang dibutuhkan: {durasi:.4f} detik")
            print(f"🔥 Jumlah percobaan: {i} kali")
            return

    print("❌ PIN TIDAK DITEMUKAN (Mungkin lebih dari 4 digit)")

# --- BAGIAN 3: SIMULASI DICTIONARY ATTACK (PASSWORD) ---
def dictionary_attack(target_password):
    print(f"\n[+] Memulai serangan Dictionary Attack ke Password: {target_password}")
    start_time = time.time()

    # Daftar kata kamus (bisa ditambahkan sesuai kebutuhan)
    wordlist = ["admin", "password", "123456", "qwerty", "admin123", "rahasia", "bismillah"]

    for word in wordlist:
        print(f"Mencoba: {word}")
        time.sleep(0.1) # Simulasi proses checking

        if word == target_password:
            end_time = time.time()
            durasi = end_time - start_time
            print(f"✅ PASSWORD DITEMUKAN: {word}")
            print(f"⏱️  Waktu yang dibutuhkan: {durasi:.4f} detik")
            print(f"🔥 Jumlah percobaan: {wordlist.index(word) + 1} kali")
            return

    print("❌ Password tidak ditemukan dalam kamus.")

# --- BAGIAN 4: EKSEKUSI PROGRAM ---
if __name__ == "__main__":
    nilai = cek_kekuatan("Admin123!")

    # 2. Tes Brute Force (PIN 4 Digit)
    # Ganti angka ini untuk tes
    brute_force_pin("8812") 

    # 3. Tes Dictionary Attack
    # Ganti kata ini untuk tes
    dictionary_attack("rahasia")