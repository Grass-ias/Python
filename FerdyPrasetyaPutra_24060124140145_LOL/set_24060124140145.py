# Nama File  : set_24060124140145.py
# Deskripsi  : Program yang berisi implemtasi operasi-operasi himpunan
# NIM/Nama   : 24060124140145/Ferdy Prasetya Putra
# Tanggal    : 9/11/2024

from ListFunction import * # biar fungsi-fungsi nya bisa jalan kak :)

# 1
# Rember1: elemen, list -> list
#   Rember1(x, L) menghapus sebuah elemen x dari list L
#   Jika x ada di list L, maka elemen L berkurang 1
#   Jika x tidak ada di list L, maka L tetap
#   List kosong tetap menjadi list kosong
#REALISASI
def Rember1(x,L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember1(x,Tail(L)))     
# print("Hasil dari Rember1 adalah: ", Rember1(1,[1,2]))

# Rember2 : list, elemen -> list     
#   MultiRember(x, L) menghapus semua kemunculan elemen x dari list L
#   List baru yang dihasilkan tidak lagi memiliki elemen x.
#   List kosong tetap menjadi list kosong.
#REALISASI
def Rember2(L,x):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember2(Tail(L),x))
# print("Hasil dari Rember2 adalah: ", Rember2([3,2,1],1))


# 2
# MultiRember: elemen, list -> list
# MultiRember(x, L) menghapus semua kemunculan elemen x dari list L.
# List baru yang dihasilkan tidak lagi memiliki elemen x.
# List kosong tetap menjadi list kosong.
#REALISASI
def MultiRember(x,L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return MultiRember(x,Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x,Tail(L))) 
# print("Hasil dari MultiRember adalah: ", MultiRember(4,[2,3,4,1,4,4]))


# 3 
# MakeSet1 : list -> set     
#   {MakeSet1(L) membuat list menjadi set}
#REALISASI
def MakeSet1(L):
    if IsEmpty(L):
        return []
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet1(Tail(L))
        else:
            return Konso(FirstElmt(L), MakeSet1(Tail(L)))
# print("Hasil dari MakeSet1 adalah: ", MakeSet1([1,2,2,3,4,5,5]))  

# MakeSet2 : list -> set     
#   {MakeSet2(L) membuat list menjadi set dengan menghilangkan semua elemen yang sama secara sekaligus}
#REALISASI
def MakeSet2(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), MakeSet2(MultiRember(FirstElmt(L), Tail(L))))
# print("Hasil dari MakeSet2 adalah: ", MakeSet2([1,2,2,3,4,4,4,5,5]))


# 4
def KonsoSet(e,L):
    if IsEmpty(L):
        return [e]
    else:
        if IsMember(e,L):
            return L
        else:
            return [e]+L
# print("Hasil dari KonsoSet adalah: ", KonsoSet(1,[2,3,4]))


# 5      
# IsSet : set -> boolean     
#   {IsSet(L) menghapus semua elemen e yang berada di list L}
#REALISASI
def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L),Tail(L)):
            return False
        else:
            return IsSet(Tail(L))
# print("Hasil dari IsSet adalah: ", IsSet([1,2,3,4,5,5]))


# 6     
# IsSubSet : set, set -> boolean     
#   {IsSubSet(L1,L2) mengecek apakah L1 merupakan subset dari L2}
#REALISASI
def IsSubSet(L1,L2):
    if IsEmpty(L1):
        return True
    else:
        if IsMember(FirstElmt(L1),L2):
            return IsSubSet(Tail(L1),L2)
        else:
            return False
# print("Hasil dari IsSubSet adalah: ", IsSubSet([1,2],[1,2]))


# 7    
# IsEqSet1 : set, set -> boolean     
#   {IsEqSet1(L1,L2) mengecek apakah L1 dan L2 adalah set yang sama}
#REALISASI
def IsEqSet1(L1,L2):
    return IsSubSet(L1,L2) and IsSubSet(L2,L1)
# print("Hasil dari IsEqSet1 adalah: ", IsEqSet1([],[]))

# IsEqSet2 : set, set -> boolean     
#   {IsEqSet2(L1,L2) mengecek apakah L1 dan L2 adalah set yang sama}
#REALISASI
def IsEqSet2(L1,L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return True
    else:
        if FirstElmt(L1) != FirstElmt(L2):
            return False
        else:
            return IsEqSet2(Tail(L1),Tail(L2))
# print("Hasil dari IsEqSet2 adalah: ", IsEqSet2([1],[1]))


# 8 
# IsIntersect : set, set -> boolean     
#   {IsIntersect(L1,L2) mengecek apakah L1 dan L2 memiliki satu elemen yang sama}
#REALISASI
def IsIntersect(L1,L2):
    if IsEmpty(L1) or IsEmpty(L2):
        return False
    elif IsEmpty(L1) == False and IsEmpty(L2) == False:
        if IsMember(FirstElmt(L1),L2):
            return True
        else: 
            return IsIntersect(Tail(L1),L2)
# print("Hasil dari IsIntersect adalah: ", IsIntersect([1,2,3],[4,3,6]))


# 9 
# MakeIntersect1 : set, set -> set     
#   {MakeIntersect1(L1,L2) membuat set dengan mengkombinasi L1 dan L2}
#REALISASI
def MakeIntersect1(L1,L2):
    if IsEmpty(L1) or IsEmpty(L2):
        return []
    else:
        if IsMember(FirstElmt(L1),L2):
            return Konso(FirstElmt(L1), MakeIntersect1(Tail(L1),L2))
        else:
            return MakeIntersect1(Tail(L1),L2)
# print("Hasil dari MakeIntersect1 adalah: ", MakeIntersect1([1,2],[3,2,1,4]))

# MakeIntersect2 : set, set -> set     
#   {MakeIntersect2(L1,L2) membuat set dengan mengkombinasi L1 dan L2}
#REALISASI
def MakeIntersect2(L1, L2):
    if IsEmpty(L1) or IsEmpty(L2):
        return []
    else:
        if IsMember(FirstElmt(L2), L1):
            return Konso(FirstElmt(L2), MakeIntersect2(L1, Tail(L2)))
        else:
            return MakeIntersect2(L1, Tail(L2))
# print("Hasil dari MakeIntersect2 adalah: ", MakeIntersect2([1,2],[3,2,4,1]))

# 10
# MakeUnion1 : set, set -> set     
#   {MakeUnion1(L1,L2) membuat set baru dengan semua anggota elemen L1 dan anggota L2}
#REALISASI
def MakeUnion1(L1,L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return []
    elif not IsEmpty(L1) and IsEmpty(L2):
        return L1
    elif IsEmpty(L1) and not IsEmpty(L2):
        return L2
    else:
        if IsMember(FirstElmt(L1),L2):
            return MakeUnion1(Tail(L1),L2)
        else:
            return Konso(FirstElmt(L1),MakeUnion1(Tail(L1),L2))
# print("Hasil dari MakeUnion1 adalah: ", MakeUnion1([1,3,2],[2,3,4,5]))

# MakeUnion2 : set, set -> set     
#   {MakeUnion2(L1,L2) membuat set baru dengan semua anggota elemen L1 dan anggota L2}
#REALISASI
def MakeUnion2(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif IsEmpty(H1):
        return H2
    elif IsEmpty(H2):
        return H1
    else:
        if IsMember(FirstElmt(H2), H1):
            return MakeUnion2(H1, Tail(H2)) 
        else:
            return Konso(FirstElmt(H2), MakeUnion2(H1, Tail(H2)))
# print("Hasil dari MakeUnion2 adalah: ", MakeUnion2([1,4,2],[2,3,6,5]))
        

# 11       
# NBIntersect : set, set -> set     
#   {NBIntersect(L1,L2) mencari banyak elemen yang berintersect}
#REALISASI  
def NBIntersect(L1,L2):
    if IsEmpty(L1) or IsEmpty(L2):
        return 0
    else:
        if IsMember(FirstElmt(L1),L2):
            return 1 + NBIntersect(Tail(L1), L2)
        else:
            return NBIntersect(Tail(L1),L2)
# print("Hasil dari NBIntersect adalah: ",NBIntersect([1,3,2],[2,3,4,5]))    


# 12
# NBUnion: 2 set -> integer
# NBUnion(H1, H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2 tanpa memanfaatkan fungsi MakeUnion(H1, H2).
def NBUnion(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return 0
    elif IsEmpty(H1):
        return NbElmt(H2)
    elif IsEmpty(H2):
        return NbElmt(H1)
    else:
        if IsMember(FirstElmt(H2), H1):
            return NBUnion(H1, Tail(H2)) 
        else:
            return 1 + NBUnion(H1, Tail(H2))
# print("Hasil dari NBUnion adalah: ", NBUnion([1,3,2],[2,3,4,5]))