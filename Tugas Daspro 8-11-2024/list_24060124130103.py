#Nama file : list_24060124130103.py
#Deskripsi : berisi type list dan operasi list
#Pembuat : Dzaki Fathul 'Alim Cahyo
#Tanggal : 30 Oktober 2024

#DEFINISI DAN SPESIFIKASI TYPE 
#Konstruktor menambahkan elemen di awal, notasi prefix
#type List: [] atau [e o List]
#Konstruktor menambahkan elemen di akhir, notasi postfix
#typw List: [] atau [List o e]

#DEFINISI DAN SPESIFIKA KONSTRUKTOR
# Konso: elemen, list -> List
# Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# Realisasi
def Konso(e,L):
    return [e] + L

# Konsi: List, elemen -> List
# Konsi(L,e) menghasilkan sebuah list dari L dan e dengan e sebagai elemen terakhir
# Realisasi
def Konsi(L,e):
    return L + [e]

#DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong -> elemen
# FirstElmt(L) menghasilkan elemen pertama list L
# Realisasi
def FirstElmt(L):
    return L[0]

# LastElmt: List tidak kosong -> elemen
# LastElmt(L) menghasilkan elemen terakhir list L
# Realisasi
def LastElmt(L):
    return L[-1]

# Tail: List tidak kosong -> List
# Tail(L) menghasilkan list tanpa elemen pertama list L, mungkin kosong
# Realisasi
def Tail(L):
    return L[1:]

# Head: List tidak kosong -> List
# Head(L) menghasilkan list tanpa elemen terakhir list L, mungkin kosong
# Realisasi
def Head(L):
    return L[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: List -> Boolean
# IsEmpty(L) true jika list kosong
# Realisasi
def IsEmpty(L):
    return L == []

# IsOneElmt: List -> Boolean
# IsOneElmt(L) true jika list hanya satu elemen
# Realisasi
def IsOneElemt(L):
    if IsEmpty(L):
        return False
    else :
        return Tail(L)==[] and Head(L)==[]
    
# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# NbElmt: List -> integer
# NbElmt(L) : Menghasilkan banyaknya elemen  list, nol jika kosong
# Realisasi
def NbElmt(L): 
    if IsEmpty(L):
        return 0
    else: 
        return 1 + NbElmt(Tail(L))
    
# ElmtkeN : integer >= 0, Lust -> elemen
# ElmtkeN (N,L): Mengirimkan elemen list yang ke N, N <= NbElmt(L) dan N>= 0
# Realisasi
def ElmtkeN(N,L):
    if N == 0:
        return FirstElmt(L)
    else:
        return ElmtkeN(N-1,Tail(L))
    
# IsMember : elemen, List -> boolean
# IsMember(X,L) true jika X adalah elemen list L
# Realisasi
def IsMember(X,L):
    if IsEmpty(L):
        return False
    elif X == FirstElmt(L):
        return True
    else:
        return IsMember(X,Tail(L))

#print(IsMember(2,[1,2,3,4]))

# Copy : List -> List
# Copy(L) : Menghasilkan list yang identik dengan list asal
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L),Copy(Tail(L)))


# Inverse : List -> List
# Inverse(L) : Menghasilkan list L yang dibalik, yaitu yang urutan elemennya adalah keballikana dari list asal
def inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(LastElmt(L),inverse(Head(L)))

#print(inverse([1,2,3,4]))
    
# Konkat : 2 List -> List
# Konkat(L1,L2) : Menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah list L1"
def Konkat(L1,L2):
    if IsEmpty(L2):
        return L1
    else:
        return Konsi(Konkat(L1,Head(L2)),LastElmt(L2))

#print(Konkat([1,2,3],[4,5,6]))

# SumElmt: List of integer -> integer
# SumElmt(L) menghasilkan jumlahan dari setiap elemen di list L
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

#print(SumElmt([1,2,3]))

    
# AvgElmt: List of integer -> integer
# AvgElmt(L) Menghasilkan nilai rata-rata
def AvgElmt(L):
    return SumElmt(L)/NbElmt(L)
    
#print(AvgElmt([1,2,3,4]))

# MaxElmt(L): List of integer -> integer
# MaxElmt(L) mengembalikan elemen maksimum dari list L
def MaxElmt(L):
    if IsOneElemt(L):
        return FirstElmt(L)
    else:
        return max(FirstElmt(L),MaxElmt(Tail(L)))

#print(MaxElmt([11,22,44,11]))

        
# MaxNB : List of integer -> <integer, integer>
# MaxNB(L) menghasilkan <max,countMax> 
# dengan max adalah elemen maksimum list L
# dan countMax adalah banyaknya kemunculan max di list L
def MaxNB(L):
    return MaxElmt(L) 


# AddList: 2 List of integer -> List of integer
# AddList(L1,L2) menghasilkan list baru yang setiap elemennya
#  adalah hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama
def AddList(L1,L2):
    if IsEmpty(L1):
        return []
    else:
        return Konso(FirstElmt(L1)+FirstElmt(L2),AddList(Tail(L1),Tail(L2)))

#print(AddList([1,1,1],[2,3,2]))

# IsPalindrom(L): List of Character -> boolean
# IsPalindrom(L) true jika L merupakan kata paindrom
# yaitu kata yang sama jika dibaca dari kiri atau kanan
# contoh: RUSAK, KASUR RUSAK, NABABAN
def IsPalindrom(L):
    return L == inverse(L)

#print(IsPalindrom([1,2,1]))

def max2(x,y):
    if x > y:
        return x
    else:
        return y

#APLIKASI
# print(Konso(2,[3]))
# print(Konsi([3,4,5],6))
# print(FirstElmt([3,4,5,6,7]))
# print(LastElmt([3,4,5,6,7]))
# print(Tail([3,4,5,6,7]))
# print(Head([3,4,5,6,7]))
# print(IsEmpty([]))
# print(IsEmpty([3,4,5,6,7]))
# print(IsOneElemt([]))
# print(IsOneElemt([3]))
# print(IsOneElemt([3,4,5,6,7]))
# print(NbElmt([3,4,5,6,7]))