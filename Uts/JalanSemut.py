# Program     : Jalan Semut
# Deskripsi   : Menetukan jalan terpendek
# NIM/Nama    : 24060124140145/Ferdy Prasetya Putra
# Tanggal     : 18/09/2024
# ===========================================================================
def jalanSemut(x,y,z):
    return round(min((((x+y)**2+z**2)**0.5),(((x+z)**2+y**2)**0.5), (((y+z)**2+x**2)**0.5)),3)

print(jalanSemut(3,4,5))
print(jalanSemut(1,2,7))
print(jalanSemut(9,7,3))
