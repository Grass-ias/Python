# Nama File : LOL_24060124140145.py
# Deskripsi : Program yang berisi implementasi operasi-operasi himpunan
# Pembuat   : Ferdy Prasetya Putra
# Tanggal   : Rabu, 13 November 2024

from ListFunction import * 
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

# Aplikasi
# print(KonsLo([1, 2, 3], [4, 5, 6])) # [[1, 2, 3], 4, 5, 6] 
# print(KonsLi([1, 2, 3], [4, 5, 6])) # [1, 2, 3, [4, 5, 6]] 
# print(FirstList([[1, 2, 3], 4, 5, 6])) # [1, 2, 3]
# print(LastList([[1, 2, 3], 4, 5, 6])) # 6
# print(TailList([[1, 2, 3], 4, 5, 6])) # [4, 5, 6]
# print(HeadList([[1, 2, 3], 4, 5, 6])) # [1, 2, 3]
# print(IsEmpty([])) # True 
# print(IsEmpty([[]])) # False 
# print(IsAtom(1)) # True
# print(IsAtom([1, 2, 3])) # False 
# print(IsList([1, 2, 3])) # True 
# print(IsList(1)) # False

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
print(IsMemberS(3, [2,3, [1], [4,5]]))
print(IsMemberS(3, [2,4, [1], [5,3]]))

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
                return Rember(Tail(S))
            else:
                return KonsLo(FirstList(S),(Rember(x,TailList(S))))
        else:
            return KonsLo(Rember(x, FirstList(S)), Rember(x,TailList(S)))
print(Rember*(3, [4, 3, [2,4], 3]))
print(Rember*(3, [2, 4, [3,6,9], 5, 3]))
      
# Max: list of list -> elemen
# Max(S) mengembalikan elemen maksimum di dalam list of list S
#   Contoh aplikasi:
#   Max([4, 5, 6, [8,9,10], [12,0], 8]) {menghasilkan 12}
#   Max([4, 15, 6, [8,9,10], [12,0], 8]) {menghasilkan 15}
