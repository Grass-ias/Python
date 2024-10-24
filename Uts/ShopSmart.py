# Program     : Shop Smart
# Deskripsi   : Menentukan hasil harga jika ada berbagai diskon dan pajak
# NIM/Nama    : 24060124140145/Ferdy Prasetya Putra
# Tanggal     : 18/09/2024
# ===========================================================================
def hargaAkhir(harga, kategori, VIP, lokasi, hari):
    if kategori == "elektronik":
        if VIP == True:
            harga *= 0.7
        else:
            harga *= 0.9
    elif kategori == "pakaian":
        if VIP == True:
            harga *= 0.8
        else:
            harga *= 0.95
    elif kategori == "makanan":
        if VIP == True:
            harga *= 0.85
        else:
            harga *= 0.98
    elif kategori == "lainnya":
        harga *= 1
        
    if hari == "Minggu":
        harga *= 1.05  
    elif hari == "Jumat" or hari == "Sabtu":
        harga *= 0.95  
    elif kategori == "pakaian" and hari == "Rabu":
        harga *= 0.95
        
    if lokasi == 'dalam negeri':
        harga *= 1.10
    elif lokasi == 'luar negeri':
        harga *= 1.20

    return int(harga)

print(hargaAkhir(1000000, "elektronik", True, "dalam negeri", "Senin"))
print(hargaAkhir(800000, "pakaian", False, "luar negeri", "Rabu"))
print(hargaAkhir(500000, "makanan", True, "dalam negeri", "Minggu"))
