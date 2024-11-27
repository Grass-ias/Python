# Nama File : TreeNAire_24060124140145.py
# Deskripsi : Program yang berisi implementasi pohon n-aire
# Pembuat   : Ferdy Prasetya Putra
# Tanggal   : Rabu, 20 November 2024

from ListFunction import * 

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def MakePN(A, PN):
    return [A, PN]

# DEFINISI DAN SPESIFIKASI SELEKTOR
def Akar(PN):
    return PN[0]

def Anak(PN):
    return PN[1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
def IsTreeEmpty(PN):
    return PN == []

def IsOneElmt(PN):
    return (IsTreeEmpty(PN) == False) and (IsTreeEmpty(Anak(PN)) == True)

def NbElmt(PN):
    # Basis -> pohon kosong
    if IsTreeEmpty(PN):
        return 0
    # Basis -. pohon 1 elemen (akar doang)
    elif IsOneElmt(PN):
        return 1
    # Hitung 1 untuk akar, dan rekursif pada setiap anak pohon
    # Tanpa menggunakan loop, kita memanggil fungsi untuk setiap anak secara rekursif
    # Pertama pada anak pertama
    else:
        return 1 + NbElmt(Anak(PN)[0]) + NbElmtChild(Anak(PN)[1:])

# Fungsi tambahan untuk menghitung jumlah elemen pada sisa anak-anak
def NbElmtChild(PN):
    # Basis -> pohon kosong
    if IsTreeEmpty(PN):
        return 0
    # Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    else:
        return NbElmt(PN[0]) + NbElmtChild(PN[1:])

def NbDaun(PN):
    # Basis: Jika pohon kosong
    if IsTreeEmpty(PN):
        return 0
    # Jika pohon adalah daun (anak kosong)
    elif IsOneElmt(PN) and IsTreeEmpty(Anak(PN)):
        return 1
    # Rekursi pada akar dan anak-anak
    else:
        return NbDaun(Anak(PN)[0]) + NbDaunChild(Anak(PN)[1:])

# Fungsi tambahan untuk menghitung jumlah daun pada sisa anak-anak
def NbDaunChild(PN):
    # Basis: Jika tidak ada anak
    if IsTreeEmpty(PN):
        return 0
    # Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    else:
        return NbDaun(PN[0]) + NbDaunChild(PN[1:])

#Aplikasi
T1 = MakePN(2,[])
print(IsTreeEmpty(T1))
print(IsOneElmt(T1))

T2 = MakePN('A', [MakePN('B', [MakePN('D', []), MakePN('E', []), MakePN('F', [])]), MakePN('C', [MakePN('G', []), MakePN('H', [MakePN('I', [])])])])
print(T2)
print(NbElmt(T2))
print(NbDaun(T2))