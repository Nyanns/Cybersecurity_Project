emails = ["ADMIN@bkn.go.id", "Budi@GMAIL.com", "SITI@yahoo.com"]

def ubah_kecil(email):
    return email.lower()

emails = list(map(ubah_kecil, emails))
emails2 = list(map(lambda x: x.lower(), emails))
emails3 = [email.lower() for email in emails]
emails4 = map(lambda x: x.lower(), emails)
print(emails)
print(emails2)
print(emails3)
print(list(emails4))
