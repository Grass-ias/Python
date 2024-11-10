# Nama file  : Koleksi Objek.py
# Deskripsi  : Tugas Koleksi Objek
# Pembuat    : Dzaki Fathul Alim Cahyo - 24060124130103
# Tanggal    : 30 Oktober 2024

from list_24060124130103 import *


# Type Mhs : < nim : String, nama : String, kelas : Character, nilai : List of Integer >
# (<nim, nama, kelas, nilai> adalah sebuah Mahasiswa, dengan:
# - Nim adalah nomor induk mahasiswa yang berbentuk string,
# - Nama adalah nama mahasiswa yang berbentuk string,
# - Kelas adalah kelas mahasiswa yang berupa karakter,
# - Nilai adalah daftar nilai kuis yang telah dikerjakan mahasiswa dalam bentuk list of integer)

# Type SetOfMhs : <setofmhs : List of Mhs>
# <setofmhs> adalah kumpulan mahasiswa di mana setiap mahasiswa diwakili oleh type Mhs (nim, nama, kelas, nilai).


# ===========================================================================
# DEFINISI DAN SPESIFIKASI SELEKTOR
# ===========================================================================
# NIMMhs: Mhs -> string
# NIMMhs(Mhs) menghasilkan NIM mahasiswa dari record mahasiswa

# NamaMhs: Mhs -> string
# NamaMhs(Mhs) menghasilkan nama mahasiswa dari record mahasiswa

# KelasMhs: Mhs -> character
# KelasMhs(Mhs) menghasilkan kelas mahasiswa dari record mahasiswa

# NilaiMhs: Mhs -> list of integer
# NilaiMhs(Mhs) menghasilkan daftar nilai mahasiswa dari record mahasiswa


# ===========================================================================
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# ===========================================================================
# MakeMhs: string, string, character, list of integer -> Mhs
# MakeMhs(NIM, Nama, Kelas, Nilai) menghasilkan record mahasiswa baru

def NIMMhs(Mhs):
    return Mhs[0]

def NamaMhs(Mhs):
    return Mhs[1]

def KelasMhs(Mhs):
    return Mhs[2]

def NilaiMhs(Mhs):
    return Mhs[3]

def MakeMhs(NIM, Nama, Kelas, Nilai):
    return [NIM, Nama, Kelas, Nilai]

# Bagian 2, No. 1

# SetOfMhs: list -> setofmhs
# SetOfMhs(L) mengembalikan daftar mahasiswa (sebagai type bentukan setofmhs)
def MakeSetOfMhs(L):
    return L
print(MakeSetOfMhs(MakeMhs('2222', 'Baskara', 'Z', [100, 100, 100]), [MakeMhs('2222', 'Putra', 'Z', [44, 33, 22]), MakeMhs('3333', 'Max', 'Z', [0, 0, 0]), MakeMhs('4444', 'Emily', 'Z', [88, 77, 99])]))


#OPERATOR
# Bagian 2, No. 2a

# MakeSetMhs: Mhs, setofmhs -> setofmhs
# MakeSetMhs(Mhs, SetMhs) menambahkan mahasiswa Mhs ke dalam SetMhs
#  - Jika belum ada mahasiswa dengan NIM yang sama
def MakeSetMhs(Mhs, SetMhs):
    if IsEmpty(SetMhs):
        return [Mhs]
    elif NIMMhs(Mhs) == NIMMhs(FirstElmt(SetMhs)):
        return SetMhs
    else:
        return Konso(FirstElmt(SetMhs), MakeSetMhs(Mhs, Tail(SetMhs)))
print(MakeSetMhs(MakeMhs('2222', 'Baskara', 'Z', [100, 100, 100]), [MakeMhs('2222', 'Putra', 'Z', [44, 33, 22]), MakeMhs('3333', 'Max', 'Z', [0, 0, 0]), MakeMhs('4444', 'Emily', 'Z', [88, 77, 99])]))


# Bagian 2, No. 2b

# MhsLulus: setofmhs -> setofmhs
# MhsLulus(SetMhs) menghasilkan daftar mahasiswa yang lulus (nilai rata-rata >= 70)
def MhsLulus(SetMhs):
    if IsEmpty(SetMhs):
        return []
    else:
        if AvgElmt(NilaiMhs(FirstElmt(SetMhs))) >= 70:
            return [FirstElmt(SetMhs)] + MhsLulus(Tail(SetMhs))
        else:
            return MhsLulus(Tail(SetMhs))
print(MhsLulus(MakeSetMhs(MakeMhs('11111', 'Baskara', 'Z', [100, 100, 100]), [MakeMhs('2222', 'Putra', 'Z', [44, 33, 22]), MakeMhs('3333', 'Max', 'Z', [0, 0, 0]), MakeMhs('4444', 'Emily', 'Z', [88, 77, 99])])))

# Bagian 2, No. 2c

# MhsnotKuis: setofmhs, string -> setofmhs
# MhsnotKuis(SetMhs, Kelas) menghasilkan daftar mahasiswa di kelas tertentu yang belum mengumpulkan kuis
def MhsnotKuis(SetMhs, Kelas):
    if IsEmpty(SetMhs):
        return []
    else:
        if KelasMhs(FirstElmt(SetMhs)) == Kelas and IsEmpty(NilaiMhs(FirstElmt(SetMhs))):
            return [FirstElmt(SetMhs)] + MhsnotKuis(Tail(SetMhs), Kelas)
        else:
            return MhsnotKuis(Tail(SetMhs), Kelas)
print(MhsnotKuis(MakeSetOfMhs([MakeMhs('11111', 'Baskara', 'Z', [100, 100, 100]),MakeMhs('2222', 'Putra', 'K', []),MakeMhs('3333', 'Max', 'Z', []),MakeMhs('4444', 'Emily', 'Z', [88, 77, 99])]),'Z'))

# Bagian 2, No. 2d

# NilaiTertinggi: setofmhs -> float
# NilaiTertinggi(SetMhs) menghasilkan nilai rata-rata tertinggi dari semua mahasiswa
def NilaiTertinggi(SetMhs):
    if IsEmpty(SetMhs):
        return 0
    elif IsOneElemt(SetMhs):
        return AvgElmt(NilaiMhs(FirstElmt(SetMhs)))
    else:
        return max2(AvgElmt(NilaiMhs(FirstElmt(SetMhs))), NilaiTertinggi(Tail(SetMhs)))
print(NilaiTertinggi(MakeSetOfMhs([MakeMhs('11111', 'Baskara', 'A', [100, 90, 90]),MakeMhs('2222', 'Putra', 'B', [0,0,0]), MakeMhs('3333', 'Max', 'C', [80,90,100]), MakeMhs('4444', 'Emily', 'Z', [88, 77, 99])])))

# Bagian 2, No. 2e

# NilaiTertinggiKelas: setofmhs, string -> setofmhs
# NilaiTertinggiKelas(SetMhs, Kelas) menghasilkan mahasiswa dengan nilai rata-rata tertinggi di kelas tertentu
def NilaiTertinggiKelas(SetMhs,Kelas):
    if IsEmpty(SetMhs):
        return []
    elif IsOneElemt(SetMhs):
        if KelasMhs(FirstElmt(SetMhs)) == Kelas:
            return FirstElmt(SetMhs)
        else:
            return []
    else:
        if KelasMhs(FirstElmt(SetMhs)) == Kelas:
            if IsEmpty(NilaiTertinggiKelas(Tail(SetMhs),Kelas)):
                return FirstElmt(SetMhs)
            
            elif AvgElmt(NilaiMhs(FirstElmt(SetMhs))) >= AvgElmt(NilaiMhs(NilaiTertinggiKelas(Tail(SetMhs), Kelas))):
                return FirstElmt(SetMhs)
            
            else:
                return NilaiTertinggiKelas(Tail(SetMhs), Kelas)
        else:
            return NilaiTertinggiKelas(Tail(SetMhs),Kelas)
print("z")
print(NilaiTertinggiKelas(MakeSetOfMhs([MakeMhs('11111', 'Baskara', 'K', [100, 100, 100]),MakeMhs('2222', 'Putra', 'Z', [44, 33, 22]), MakeMhs('3333', 'Max', 'Z', [0, 0, 0]), MakeMhs('4444', 'Emily', 'S', [100,100,100])]),'Z'))

# Bagian 2, No. 2f

# NBnotKuis: setofmhs -> integer
# NBnotKuis(SetMhs) menghasilkan jumlah mahasiswa yang belum mengumpulkan kuis
def NBnotKuis(SetMhs):
    if IsEmpty(SetMhs):
        return 0
    else:
        if NilaiMhs(FirstElmt(SetMhs)) == []:
            return 1 + NBnotKuis(Tail(SetMhs))
        else:
            return NBnotKuis(Tail(SetMhs))
print(NBnotKuis(MakeSetOfMhs([MakeMhs('11111', 'Baskara', 'Z', [100, 100, 100]),MakeMhs('2222', 'Putra', 'Z', [44, 33, 22]), MakeMhs('3333', 'Max', 'Z', [0, 0, 0]), MakeMhs('4444', 'Emily', 'Z', [88, 77, 99])])))

# Bagian 2, No. 2g

# NBLulus: setofmhs -> integer
# NBLulus(SetMhs) menghasilkan jumlah mahasiswa yang lulus (nilai rata-rata >= 70)
def NBLulus(SetMhs):
    if IsEmpty(SetMhs):
        return 0
    else:
        if AvgElmt(NilaiMhs(FirstElmt(SetMhs))) >= 70:
            return 1 + NBLulus(Tail(SetMhs))
        else:
            return NBLulus(Tail(SetMhs))
        
       
print(NBLulus(MakeSetOfMhs([MakeMhs('11111', 'Baskara', 'Z', [100, 100, 100]),MakeMhs('2222', 'Putra', 'Z', [44, 33, 22]), MakeMhs('3333', 'Max', 'Z', [0, 0, 0]), MakeMhs('4444', 'Emily', 'Z', [88, 77, 99])])))
