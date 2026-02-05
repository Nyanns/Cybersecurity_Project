peserta = [
    ("Budi", 80),
    ("Ani", 95),
    ("Citra", 88)
]

def rangking(peserta):
    return peserta[1]

peserta.sort(key=rangking, reverse=True)
peserta2 = sorted(peserta, key=rangking, reverse=True)
peserta3 = sorted(peserta, key=lambda x: x[1], reverse=True)
peserta4 = sorted(peserta, key=lambda x: x[1])

print(peserta)
print(peserta2)
print(peserta3)
print(peserta4)