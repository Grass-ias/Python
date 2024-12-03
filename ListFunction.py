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


# Nama File : LOL_24060124140145.py
# Deskripsi : Program yang berisi implementasi operasi-operasi himpunan
# Pembuat   : Ferdy Prasetya Putra
# Tanggal   : Rabu, 13 November 2024

#NOTE
# type digunakan untuk mengecek jenis input
# list adalah fungsi untuk menentukan apakah input merupakan list 

#DEFINISI DAN SPESIFIKASI TYPE PREDIKAT KHUSUS LIST
# IsEmpty : list of list -> boolean
# IsEmpty(L) true jika list of list kosong, false jika tidak
def IsEmpty(L) :
    return L == []

# IsAtom : list of list -> boolean
# IsAtom(L) true jika list of list L adalah sebuah Atom, false jika tidak
def IsAtom(L) :
    return type(L) != list

# IsList : list of list -> boolean
# IsList(L) true jika list of list L adalah sebuah List, false jika tidak
def IsList(L) :
    return type(L) == list

# KonsLo : list, list of list -> list of list
# KonsLo(L) akan menambahkan list kedalam list of list bagain pertama
def KonsLo(L,LoL):
    return [L]+LoL
    
# KonsLo : list, list of list -> list of list
# KonsLo(L) akan menambahkan list kedalam list of list bagain pertama
def KonsLi(LoL,L):
    return LoL+[L]

#DEFINISI DAN SPESIFIKASI SELECTOR
# FirstList : list of list tidak kosong -> list
# FirstList(S) mengembalikan elemen pertama dari list of list S (mungkin sebuah atom atau list).
def FirstList(S) :
    if IsEmpty(S):
        return []
    else:
        return S[0]

# LastList : list of list tidak kosong -> list
# LastList(S) mengembalikan elemen terakhir dari list of list S (mungkin sebuah atom atau list).
def LastList(S):
    if IsEmpty(S):
        return []
    else:
        return S[-1]

# TailList : list of list tidak kosong -> list of list
# TailList(S) mengembalikan list of list yang elemen pertamanya dihapus.
def TailList(S):
    if IsEmpty(S):
        return []
    else:
        return S[1:]

# HeadList : list of list tidak kosong -> list of list
# HeadList(S) mengembalikan list of list yang elemen terakhirnya dihapus.
def HeadList(S) :
    if IsEmpty(S):
        return []
    else:
        return S[:-1]

# Aplikasi Praktikum
# print("Ini adalah hasil dari fungsi KonsLo", KonsLo([1, 2, 3], [4, 5, 6])) # [[1, 2, 3], 4, 5, 6] 
# print("Ini adalah hasil dari fungsi KonsLi", KonsLi([1, 2, 3], [4, 5, 6])) # [1, 2, 3, [4, 5, 6]] 
# print("Ini adalah hasil dari fungsi FirstList", FirstList([[1, 2, 3], 4, 5, 6])) # [1, 2, 3]
# print("Ini adalah hasil dari fungsi LastList", LastList([[1, 2, 3], 4, 5, 6])) # 6
# print("Ini adalah hasil dari fungsi TailList", TailList([[1, 2, 3], 4, 5, 6])) # [4, 5, 6]
# print("Ini adalah hasil dari fungsi HeadList", HeadList([[1, 2, 3], 4, 5, 6])) # [1, 2, 3]
# print("Ini adalah hasil dari fungsi IsEmpty", IsEmpty([])) # True 
# print("Ini adalah hasil dari fungsi IsEmpty", IsEmpty([[]])) # False 
# print("Ini adalah hasil dari fungsi IsAtom", IsAtom(1)) # True
# print("Ini adalah hasil dari fungsi IsAtom", IsAtom([1, 2, 3])) # False 
# print("Ini adalah hasil dari fungsi IsList", IsList([1, 2, 3])) # True 
# print("Ini adalah hasil dari fungsi IsList", IsList(1)) # False

# 1
# IsMemberS : elemen, list of list -> boolean
# IsMemberS(x,S) mengembalikan true jika elemen x didalam LoL S
#   Contoh aplikasi
#   IsMemberS(3, []) = False
#   IsMemberS(3, [2,3, [1], [4,5]]) = True
#   IsMemberS(3, [2,3, [1], [3,5]]) = True
def IsMemberS(x,S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            if FirstElmt(S) == x:
                return True
            else:
                return IsMemberS(x,TailList(S))
        else:
            if IsMemberS(x,FirstList(S)):
                return True
            else:
                return IsMemberS(x,TailList(S))


# 2
# Rember: elemen, list of list -> list of list
# Rember(x,S) menghapus semua elemen x yang ada di list of list S
#   Contoh aplikasi:
#   Rember*(3, []) {menghasilkan []}
#   Rember*(3, [4, 3, [2,4], 3]) {menghasilkan [4, [2,4]]}
#   Rember*(3, [2, 4, [3,6,9], 5, 3]) {menghasilkan [2, 4, [6,9], 5]}
def Rember(x,S):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(FirstList(S)):
            if FirstElmt(S) == x:
                return Rember(x, Tail(S))
            else:
                return KonsLo(FirstList(S),(Rember(x ,TailList(S))))
        else:
            return KonsLo(Rember(x, FirstList(S)), Rember(x,TailList(S)))

      
# Max: list of list -> elemen
# Max(S) mengembalikan elemen maksimum di dalam list of list S
#   Contoh aplikasi:
#   Max([4, 5, 6, [8,9,10], [12,0], 8]) {menghasilkan 12}
#   Max([4, 15, 6, [8,9,10], [12,0], 8]) {menghasilkan 15}
def Max(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(FirstList(S)):
            return max2(max(FirstList(S)),Max(TailList(S)))
        else:
            return max2(FirstList(S),Max(TailList(S)))
        
# NBElmtAtom: list of list -> integer
# NBElmtAtom (S) mengembalikan banyaknya elemen list of list S yang berupa atom
def NBElmtAtom(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return NBElmtAtom(TailList(S))
    else:
        return 1 + NBElmtAtom(TailList(S))
    
# NBElmtList: list of list -> integer 
# NBElmtList(S) mengembalikan banyaknya elemen list of list S yang berupa list
def NBElmtList(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return NBElmtList(TailList(S))
    else:
        return 1 + NBElmtList(TailList(S))

# SumLoL: list of list -> integer
# SumLoL(S) mengembalikan jumlah semua elemen dalam list of list S
def SumLoL(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return SumElmt(FirstList(S)) + SumLoL(TailList(S))
    else:
        return FirstList(S) + SumLoL(TailList(S))
    
# MaxNBElmtList: list of list -> integer
# MaxNBElmtList(S) mengembalikan banyaknya elemen list maksimum yang ada pada list of list S
def MaxNBElmtList(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return max2(NbElmt(FirstList(S)),MaxNBElmtList(TailList(S)))
    else:
        return MaxNBElmtList(TailList(S))
    
# MaxSumElmt: list of list -> integer
# MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S
def MaxSumElmt(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(FirstList(S)):
            return max2(SumElmt(FirstList(S)),MaxSumElmt(TailList(S)))
        else:
            return max2(FirstList(S),MaxSumElmt(TailList(S)))

#Aplikasi Tugas
# print("Ini adalah hasil dari fungsi IsMemberS", IsMemberS(3, [2,4, [1], [5,3]])) 
# print("Ini adalah hasil dari fungsi Rember*", Rember(3, [2, 4, [3,6,9], 5, 3]))
# print("Ini adalah hasil dari fungsi Max", Max([2, 4, [3,6,9], 10]))
# print("Ini adalah hasil dari fungsi NBElmtAtom", NBElmtAtom([2, [1], [4,5]]))
# print('Ini adalah hasil dari NB List', NBElmtList([3, 4, 6, [8,1,10], [13,0],8])) 
# print('Ini adalah hasil dari SumLOL', SumLoL([4, 9, 2, [2,7,1]])) 
# print('Ini adalah hasil dari MaxNBElmtList', MaxNBElmtList([10, 4, 6, [2,3,1], [2,3,1,4]])) 
# print('Ini adalah hasil dari MaxSumElmt', MaxSumElmt([6, 5, 9, [2,4,1], [7,3,1,5]])) 

# Nama File : TreeNAire_24060124140145.py
# Deskripsi : Program yang berisi implementasi pohon n-aire
# Pembuat   : Ferdy Prasetya Putra
# Tanggal   : Rabu, 20 November 2024

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
# T1 = MakePN(2,[])
# print(IsTreeEmpty(T1))
# print(IsOneElmt(T1))

# T2 = MakePN('A', [MakePN('B', [MakePN('D', []), MakePN('E', []), MakePN('F', [])]), MakePN('C', [MakePN('G', []), MakePN('H', [MakePN('I', [])])])])
# print(T2)
# print(NbElmt(T2))
# print(NbDaun(T2))
