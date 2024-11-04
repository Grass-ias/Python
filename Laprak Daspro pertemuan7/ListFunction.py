# Program   : ListFunction.py
# Deskripsi : Fungsi-fungsi untuk operasi list
# NIM/Nama  : 24060124140145/Ferdy Prasetya Putra
# Tanggal   : 30/10/2024

# Ini fungsi biar gak rusak
def IsEmpty(L):
    return L == []

# Realisasi Konstruktor
# Konso: elemen, List -> List
def Konso(e,L):
    return [e]+L

# Konsi: List, elemen -> List
def Konsi(L,e):
    return L+[e]

# Aplikasi Konstruktor
# print("Hasil Konso:", Konso(1,[2,3,4,5]))
# print("Hasil Konsi:", Konsi([5,4,3,2],1))

# Realisasi Selektor
# FirstElmt: List tidak kosong -> elemen
def FirstElmt(L):
    if IsEmpty(L):
        return None
    else:
        return L[0]

# LastElmt: List tidak kosong -> elemen
def LastElmt(L):
    if IsEmpty(L):
        return None 
    else:
        return L[-1]

# Tail: List tidak kosong -> elemen
def Tail(L):
    if IsEmpty(L):
        return []
    else:
        return L[1:]

# Head: List tidak kosong -> elemen
def Head(L):
    if IsEmpty(L):
        return []
    else:
        return L[:-1]

# Aplikasi Selektor
# print("Hasil Tail:", Tail([0]))
# print("Hasil Tail:", Tail([1,2]))
# print("Hasil Tail:", Head([1,2,3]))
# print("Hasil Tail:", Head([0]))

# Realisasi Predikat
# IsEmpty: List -> boolean
def IsEmpty(L):
    return L == []

# IsOneElmt: List -> boolean
def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []
    
# Aplikasi Predikat
# print("Hasil IsEmpty:", IsEmpty([]))
# print("Hasil IsEmpty:", IsEmpty([1,2,3]))
# print("Hasil IsOneElmt:", IsOneElmt([]))
# print("Hasil IsOneElmt:", IsOneElmt([0]))

# Realisasi Operator
# NbElmt: List -> integer
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))
    
# Aplikasi Operator
# print("Hasil NbElmt:", NbElmt([]))
# print("Hasil NbElmt:", NbElmt([1,2]))
# print("Hasil NbElmt:", NbElmt([2,3,4,5,4,5,4,2]))
# print("Hasil NbElmt:", NbElmt([1,2,3,4,5,6]))






