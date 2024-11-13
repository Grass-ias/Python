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

# TUGAS REALISASI OPERATOR
# ElmtkeN: integer >= 0, List -> elemen
# ElmtkeN(N, L) : Mengirimkan elemen list yang ke N, N <= NbElmt(L) dan N>=0
def ElmtkeN(N,L):
    if N <= NbElmt(L) and N >= 0:
        if N == 0:
            return FirstElmt(L)
        else:
            return ElmtkeN(N-1, Tail(L))

# print(ElmtkeN(2, [3,4,5]))

# IsMember: elemen/list, List -> boolean
# IsMember(X,L) adalah benar jika X adalah elemen list L
def IsMember(x, L):
    if IsEmpty(L):
        return False
    else:
        if LastElmt(L) == x:
            return True
        else:
            return (IsMember(x, Head(L)))

# print(IsMember([3], [[6,7], 8, 3, 9, [2], [1,2,3]]))

# Copy: List -> List
# Copy(L) : Menghasilkan list yang identik dengan list asal
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), Copy(Tail(L)))

# print(Copy([2, 3, 4, 5]))

# Inverse: List -> List
# Inverse(L) : Menghasilkan list L yang dibalik, yaitu yang urutan elemennya
#   adalah kebalikan dari list asal
def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konsi(Inverse(Tail(L)), FirstElmt(L))

# print(Inverse([3, 70, 40, 55]))

# Konkat: 2 List -> List
# Konkat(L1,L2) : Menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah" list L1
def Konkat(L1, L2):
    if IsEmpty(L2):
        return L1
    else:
        return Konkat(L1 + [FirstElmt(L2)], Tail(L2))

# print(Konkat([10, 14, 60, 100], [35, 66, 90]))


# SumElmt: List of integer -> integer
# SumElmt(L) menghasilkan jumlahan dari setiap elemen di list L
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))
# print(SumElmt([1, 2, 3, 4, 5]))

# AvgElmt: List of integer -> integer
# AvgElmt(L) menghasilkan nilai rata-rata
def AvgElmt(L):
    return int(SumElmt(L)/NbElmt(L))
# print(AvgElmt([1, 2, 3, 4, 5]))


# MaxElmt: List of integer -> integer
# MaxElmt(L) mengembalikan elemen maksimun dari list L
def max2(x,y):
    return int((x+y+(abs(x-y)))/2)

def MaxElmt(L):
    if IsOneElmt(L):
        return LastElmt(L)
    else:
        return max2(FirstElmt(L), MaxElmt(Tail(L)))
# print(MaxElmt([1, 2, 10, 2, 3]))


# MaxNB: List of integer -> <integer, integer>
# MaxNB(L) menghasilkan <max,countMax>
#   Dengan max adalah elemen maksimun list L
#   Dan countMax adalah banyaknya kemunculan max di list L
def maxlist(x):
    if IsOneElmt(x):
        return LastElmt(x)
    else:
        return max2(LastElmt(x), maxlist(Head(x)))
def NbOcc(x, L):
    if IsOneElmt(L):
        if x == FirstElmt(L):
            return 1
        else:
            return 0
    else:
        if x == FirstElmt(L):
            return 1 + NbOcc(x, Tail(L))
        else:
            return NbOcc(x, Tail(L))
        
def MaxNb(L):
    return [maxlist(L), NbOcc(maxlist(L), L)]
# print(MaxNb([100, 100000, 3000000, 30000000, 30000000, 1000000000]))


# AddList: 2 List of integer -> List of integer
# AddList(L1,L2) menghasilkan list baru yang setiap elemennya
#   Adalah hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama
def AddList(L1, L2):
    if IsEmpty(L1) or IsEmpty(L2):
        return []
    else:
        return Konso((FirstElmt(L1) + FirstElmt(L2)), AddList(Tail(L1), Tail(L2)))
# print(AddList([1, 6, 10], [3, 9, 6]))


# IsPalindrom: List of character -> boolean
# IsPalindrom(L) benar jika L merupakan kata palindrom
#   Yaitu kata yang sama jika dibaca dari kiri atau kanan
def IsPalindrom(L):
    if IsEmpty(L):
        return True
    elif IsOneElmt(L):
        return True
    else:
        return FirstElmt(L) == LastElmt(L) and IsPalindrom(Head(Tail(L)))
# print(IsPalindrom(['S', 'U', 'S']))


# 6 November 2024
# DEFINISI DAN SPESIFIKASI OPERASI YANG DIBUTUHKAN UNTUK HIMPUNAN
# Rember : elemen, list -> list
# Rember(e,L) menghapus elemen e yang berada di list L
#   Jika e ada di dalam L, maka elemen e dalam L akan menghilang
#   Jika e tidak ada di dalam L, maka L akan tetap
#   Jika list L kosong tetap menjadi list kosong
def Rember(e,L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == e:
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember(Tail(L)))
# print(Rember(1,[1,2]))

def MultiRember(e,L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == e:
            return MultiRember(e,Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(e,Tail(L)))  
# print(MultiRember(2,[2,3,4,1,2]))
# print(MultiRember(4,[2,3,4,1,4,4]))

        
def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L),Tail(L)):
            return False
        else:
            return IsSet(Tail(L))
# print(IsSet([1,2,3,4,5]))
# print(IsSet([1,2,3,4,5,5]))


def MakeSet1(L):
    if IsEmpty(L):
        return []
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet1(Tail(L))
        else:
            return Konso(FirstElmt(L), MakeSet1(Tail(L)))
# print(MakeSet1([1,2,2,3,4,5,5]))


def MakeSet2(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), MakeSet2(MultiRember(FirstElmt(L), Tail(L))))
# print(MakeSet2([1,2,2,3,4,4,4,5,5]))


def KonsoSet(e,L):
    if IsEmpty(L):
        return [e]+L
    else:
        if IsMember(e,L):
            return L
        else:
            return [e]+L
# print(KonsoSet(1,[2,3,4]))


def IsSubSet(L1,L2):
    if IsEmpty(L1):
        return True
    else:
        if IsMember(FirstElmt(L1),L2):
            return IsSubSet(Tail(L1),L2)
        else:
            return False
# print(IsSubSet([],[1]))
# print(IsSubSet([1,2],[1,2]))
# print(IsSubSet([0,1],[1,2]))


def IsEqSet1(L1,L2):
    return IsSubSet(L1,L2) and IsSubSet(L2,L1)
# print(IsEqSet1([1],[1]))
# print(IsEqSet1([1,2],[1]))
# print(IsEqSet1([],[]))
# print(IsEqSet1([],[1]))
    

def IsEqSet2(L1,L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return True
    else:
        if FirstElmt(L1) != FirstElmt(L2):
            return False
        else:
            return IsEqSet2(Tail(L1),Tail(L2))
# print(IsEqSet2([1],[1]))
# print(IsEqSet2([1,2],[1]))
# print(IsEqSet2([],[]))
# print(IsEqSet2([],[1]))






