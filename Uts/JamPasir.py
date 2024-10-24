# Program     : Jam Pasir 
# Deskripsi   : Menetukan jam, menit, dan detik 
# NIM/Nama    : 24060124140145/Ferdy Prasetya Putra
# Tanggal     : 18/09/2024
# ===========================================================================
def jam(j,m,s):
    if j >= 0 and j <= 24:
        if m >= 0 and m <= 59:
            if s >= 0 and s <= 59:
                return (f"Jam: {j}, Menit: {m}, Detik: {s}")
            else:
                return "Waktu tidak valid"
        else:
            return "Waktu tidak valid"
    else:
        return "Waktu tidak valid"

print(jam(12,30,45))
print(jam(10,45,60))
print(jam(8,35,25)) 

