# Program     : Belajar Tenang
# Deskripsi   : Menentukan Jarak Minimal Agar Belajar Tenang
# NIM/Nama    : 24060124140145/Ferdy Prasetya Putra
# Tanggal     : 18/09/2024/
# ===========================================================================
def BelajarTenang(x,y):
    if 15*(10**((x-40)/20)) <= y:
        return str(round(15*(10**((x-40)/20)), 3)) + " meter"
    else:
        return "Isi bensin dulu, bang"
              
print(BelajarTenang(102, 20000))
print(BelajarTenang(200, 15000))
print(BelajarTenang(30, 1000))
