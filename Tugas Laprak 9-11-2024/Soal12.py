# Program   : Daspro.py
# Deskripsi : Menjawab 12 soal yang diberikan King Vino
# NIM/Nama  : 24060124140145/Ferdy Prasetya Putra
# Tanggal   : 9/11/2024

from ListFunction import * # biar fungsi bisa jalan kak :)

# 1
# Rember : elemen, list -> list
#   {Rember(e,L) menghapus elemen e yang berada di list L dari depan}
#REALISASI
def Rember(x,L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember(x,Tail(L)))
        
# Rember2 : list, elemen -> list     
#   {Rember2(L,e) menghapus elemen e yang berada di list L dari belakang}
#REALISASI
def Rember2(L,x):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember2(Tail(L),x))


# 2
# MultiRember : elemen, list -> list     
#   {MultiRember(e,L) menghapus semua elemen e yang berada di list L}
#REALISASI
def MultiRember(x,L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return MultiRember(x,Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x,Tail(L))) 


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

# MakeSet2 : list -> set     
#   {MakeSet2(L) membuat list menjadi set dengan menghilangkan semua elemen yang sama secara sekaligus}
#REALISASI
def MakeSet2(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), MakeSet2(MultiRember(FirstElmt(L), Tail(L))))


# 4
def KonsoSet(e,L):
    if IsEmpty(L):
        return [e]+L
    else:
        if IsMember(e,L):
            return L
        else:
            return [e]+L


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


# 7    
# IsEqSet1 : set, set -> boolean     
#   {IsEqSet1(L1,L2) mengecek apakah L1 dan L2 adalah set yang sama}
#REALISASI
def IsEqSet1(L1,L2):
    return IsSubSet(L1,L2) and IsSubSet(L2,L1)

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

# MakeUnion2 : set, set -> set     
#   {MakeUnion2(L1,L2) membuat set baru dengan semua anggota elemen L1 dan anggota L2}
#REALISAI
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

#APLIKASI
print(Rember(1,[1,2]))
print(Rember2([3,2,1],1))
print(MultiRember(4,[2,3,4,1,4,4]))
print(MakeSet1([1,2,2,3,4,5,5]))  
print(MakeSet2([1,2,2,3,4,4,4,5,5]))
print(KonsoSet(1,[2,3,4]))
print(IsSet([1,2,3,4,5,5]))
print(IsSubSet([1,2],[1,2]))
print(IsEqSet1([],[]))
print(IsEqSet2([1],[1]))
print(IsIntersect([1,2,3],[4,3,6]))
print(MakeIntersect1([1,2],[3,2,1,4]))
print(MakeIntersect2([1,2],[3,2,4,1]))
print(MakeUnion1([1,3,2],[2,3,4,5]))