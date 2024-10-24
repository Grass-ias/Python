# Program     : Lalu Lintas Langit
# Deskripsi   : Menentukan status pesawat
# NIM/Nama    : 24060124140145/Ferdy Prasetya Putra
# Tanggal     : 18/09/2024
# ===========================================================================
def monitor_pesawat(x,y,z):
    if x >= 12000: return "Terlalu Tinggi"
    elif y <= 200 or y >= 900: return "Kecepatan Berbahaya"
    elif z <= 20: return "Bahan Bakar Rendah"
    elif z >= 50: return "Aman untuk Mendarat"
    else: return "Berjalan Normal"
            
print(monitor_pesawat(4000,850,55))
print(monitor_pesawat(5000,950,70))
print(monitor_pesawat(8000,500,30))
