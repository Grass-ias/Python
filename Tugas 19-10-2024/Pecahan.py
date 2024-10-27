# Program     : PecahanCampuran.py
# Deskripsi   : Membuat pecahan campuran menggunakan tipe bentukan dan mengoperasikannya dengan operator yang ditentukan serta pengecekkan melalui predikat yang telah ditentukan
# NIM/Nama    : 24060124140145/Ferdy Prasetya Putra
# Tanggal     : (19/10/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================
# type PecahanCampuran : <bil: integer, n:integer >= 0, d:integer > 0>
#   {<bil: integer, n:integer >= 0, d:integer > 0> adalah elemen dari pecahan campuran dimana bil adalah bilangan bulat disamping pecahan, n adalah pembilang dari pecahan, dan d adalah penyebut dari pecahan}
# type Pecahan: <n:integer >= 0, d:integer > 0>
#   {<n:integer >= 0, d:integer > 0> adalah elemen dari pecahan biasa dimana n adalah sebuah pembilang dan d adalah penyebut}
# Makepecahanc: <bil: integer, n:integer >= 0, d:integer > 0> -> PecahanCampuran
#   {Makepecahanc(bil,n,d) adalah sebuah konstruktor untuk mengkonversi bil, n, d menjadi tipe bentukan pecahan campuran}
# Makepecahanb: <n:integer >= 0, d:integer > 0> -> PecahanBiasa
#   {makepecahanb(n,d) adalah sebuah konstruktor untuk mengkonversi n, d menjadi tipe bentukan pecahan biasa}
# Bilangan: PecahanCampuran -> integer
#   {Bilangan(P) adalah selektor untuk mengambil data bilangan dari tipe bentukan pecahan campuran}
# Pemb: PecahanCampuran -> integer
#   {Pemp(P) adalah selektor untuk mengambil data pembilang dari tipe bentukan pecahan campuran}
# Peny: PecahanCampuran -> integer
#   {Peny(P) adalah selektor untuk mengambil data penyebut dari tipe bentukan pecahan campuran}
# PembB: PecahanBiasa -> integer
#   {PembB(P) adalah selektor untuk mengambil data penyebut dari tipe bentukan pecahan biasa}
# PenyB: PecahanBiasa -> integer
#   {PenyB(P) adalah selektor untuk mengambil data penyebut dari tipe bentukan pecahan biasa}
# KonversiPecahanB: PecahanCampuran -> PecahanBiasa
#   {KonversiPecahanB(P) adalah sebuah operator untuk mengkonversi tipe bentukan pecahan campuran menjadi pecahan biasa}
# KonversiPecahanC: PecahanBiasa -> PecahanCampuran
#   {KonversiPecahanC(P) adalah sebuah operator untuk mengkonversi tipe bentukan pecahan biasa menjadi pecahan campuran}
# KonversiReal: PecahanCampuran -> real
#   {KonversiReal(P) adalah sebuah operator untuk mengkonversi tipe bentukan pecahan campuran menjadi real}
# AddP: 2 PecahanCampuran -> PecahanBiasa
#   {AddP(P1,P2) adalah sebuah operator untuk menambahkan 2 PecahanCampuran dan mengoutputkan sebagai PecahanBiasa}
# SubP: 2 PecahanCampuran -> PecahanBiasa
#   {SubP(P1,P2) adalah sebuah operator untuk mengurangi 2 PecahanCampuran dan mengoutputkan sebagai PecahanBiasa}
# DivP: 2 PecahanCampuran -> PecahanBiasa
#   {DivP(P1,P2) adalah sebuah operator untuk membagi 2 PecahanCampuran dan mengoutputkan sebagai PecahanBiasa}
# MulP: 2 PecahanCampuran -> PecahanBiasa
#   {MulP(P1,P2) adalah sebuah operator untuk mengali 2 PecahanCampuran dan mengoutputkan sebagai PecahanBiasa}
# IsEqP?: 2 PecahanCampuran -> boolean
#   {IsEqP?(P1,P2) adalah sebuah predikat untuk mengoutput true jika kedua pecahan bernilai sama dan false jika sebaliknya}
# IsLtP?: 2 PecahanCampuran -> boolean
#   {IsLtP?(P1,P2) adalah sebuah predikat untuk mengoutput true jika pecahan pertama bernilai lebih kecil daripada pecahan kedua}
# IsGtP?: 2 PecahanCampuran -> boolean
#   {IsGtP?(P1,P2) adalah sebuah predikat untuk mengoutput true jika pecahan pertama bernilai lebih besar daripada pecahan kedua}
# ===========================================================================
# REALISASI
# ===========================================================================
def Makepecahanc(bil,n,d):
    return [bil,n,d]
def Makepecahanb(n,d):
    return [n,d]

def Bilangan(P):
    return P[0]
def Pemb(P):
    return P[1]
def Peny(P):
    return P[2]
def PembB(P):
    return P[0]
def PenyB(P):
    return P[1]
   
def KonversiPecahanB(P):
    if Pemb(P) >= 0 and Bilangan(P) > 0 and Peny(P) > 0:
        return Makepecahanb(Bilangan(P)*Peny(P)+Pemb(P),Peny(P))
    elif Pemb(P) >= 0 and Bilangan(P) < 0 and Peny(P) > 0:
        return Makepecahanb(Bilangan(P)*Peny(P)+Pemb(P)*-1,Peny(P))

def KonversiPecahanC(P):
    if PembB(P) == 0:
        return 0
    elif PembB(P) == 0:
        return "Tak Terdefinisi"
    elif PembB(P) == PenyB(P):
        return 1 
    elif PembB(P) < PenyB(P):
        return 0,PembB(P),PenyB(P)
    elif PembB(P) % PenyB(P) == 0:
        return PembB(P)//PenyB(P)
    elif PembB(P) < 0 and PenyB(P) > 0 and PembB(P) > PenyB(P):
        return ((PembB(P)*-1)//PenyB(P))*-1,((PembB(P)*-1)%PenyB(P)),PenyB(P)
    elif PembB(P) > 0 and PenyB(P) > 0 and PembB(P) > PenyB(P):
        return PembB(P)//PenyB(P),PembB(P)%PenyB(P),PenyB(P)
    elif PembB(P) > 0 and PenyB(P) < 0 and PembB(P) > PenyB(P):
        return PembB(P)//(PenyB(P)*-1)*-1,PembB(P)%(PenyB(P)*-1),PenyB(P)*-1
    elif PembB(P) < 0 and PenyB(P) < 0 and PembB(P) > PenyB(P):
        return (PembB(P)*-1)//(PenyB(P)*-1)*-1,(PembB(P)*-1)%(PenyB(P)*-1),PenyB(P)*-1
    
def KonversiReal(P):
    return PembB(KonversiPecahanB(P)) / PenyB(KonversiPecahanB(P))
    
def AddP(P1,P2):
    return KonversiPecahanC(Makepecahanb(PembB(KonversiPecahanB(P1))*PenyB(KonversiPecahanB(P2))+PembB(KonversiPecahanB(P2))*PenyB(KonversiPecahanB(P1)), (PenyB(KonversiPecahanB(P1))*PenyB(KonversiPecahanB(P2)))))                           
def SubP(P1,P2):
    return KonversiPecahanC(Makepecahanb(PembB(KonversiPecahanB(P1))*PenyB(KonversiPecahanB(P2))-PembB(KonversiPecahanB(P2))*PenyB(KonversiPecahanB(P1)), PenyB(KonversiPecahanB(P1))*PenyB(KonversiPecahanB(P2))))
def DivP(P1,P2):
    return KonversiPecahanC(Makepecahanb(PembB(KonversiPecahanB(P1))*PenyB(KonversiPecahanB(P2)), PembB(KonversiPecahanB(P2))*PenyB(KonversiPecahanB(P1))))
def MulP(P1,P2):
    return KonversiPecahanC(Makepecahanb(PembB(KonversiPecahanB(P1))*PembB(KonversiPecahanB(P2)), PenyB(KonversiPecahanB(P1))*PenyB(KonversiPecahanB(P2))))
def IsEqP(P1,P2):
    return KonversiReal(P1) == KonversiReal(P2)
def IsLtP(P1,P2): 
    return KonversiReal(P1) < KonversiReal(P2)
def IsGtP(P1,P2): 
    return KonversiReal(P1) > KonversiReal(P2)

# ===========================================================================
# APLIKASI
print(IsEqP(Makepecahanc(1,1,2), Makepecahanc(1,1,2)))
print(IsLtP(Makepecahanc(1,1,2), Makepecahanc(2,1,2)))
print(IsGtP(Makepecahanc(2,1,2), Makepecahanc(1,1,2)))
print(MulP(Makepecahanc(1,1,2), Makepecahanc(1,1,2))) 
print(DivP(Makepecahanc(1,1,2), Makepecahanc(1,1,2)))
print(SubP(Makepecahanc(1,1,2), Makepecahanc(1,1,2)))
print(AddP(Makepecahanc(1,1,2), Makepecahanc(1,1,2)))
print(KonversiReal(Makepecahanc(1,1,2)))
print(KonversiPecahanB(Makepecahanc(1,1,2)))
print(KonversiPecahanB(Makepecahanc(-1,1,2)))