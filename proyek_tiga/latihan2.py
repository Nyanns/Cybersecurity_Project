transaksi = [5, 12, 500, 8, 2, 1000, 7]

def mencurigakan(transaksi):
    return transaksi >= 100

transaksi_curiga = list(filter(mencurigakan, transaksi))
transaksi_curiga2 = list(filter(lambda x: x >= 100, transaksi))
transaksi_curiga3 = [x for x in transaksi if x >= 100]

jumlah_mencurigakan = sum(transaksi_curiga)
jumlah = 0
for i in transaksi_curiga:
    jumlah += 1
    
print(jumlah)
print(transaksi_curiga)
print(jumlah_mencurigakan)