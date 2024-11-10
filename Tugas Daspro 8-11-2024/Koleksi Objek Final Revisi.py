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


