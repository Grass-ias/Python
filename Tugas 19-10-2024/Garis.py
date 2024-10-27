# Program     : Garis.py
# Deskripsi   : Membuat garis menggunakan tipe bentukan dan mengoperasikannya dengan operator yang ditentukan serta pengecekkan melalui predikat yang telah ditentukan
# NIM/Nama    : 24060124140145/Ferdy Prasetya Putra
# Tanggal     : (19/10/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================
# type Point: <x: integer, y:integer>
#   {<x: integer, y:integer> adalah elemen dari point dimana x dan y merupakan absis dan ordinat}
# type Garis: <P1: Point, P2:Point>
#   {<P1,P2> adalah elemen dari garis dimana P1 dan P2 merupakan garis 1 dan garis 2 }
# Makegaris: <P1: Point, P2:Point> -> Garis
#   {Makegaris(<P1,P2) adalah sebuah konstruktor untuk mengkonversi x1, y1, x2, y2 menjadi tipe bentukan garis}
# Absis1: Garis -> integer
#   {Absis1(G) adalah selektor untuk mengambil data x dari tipe bentukan point dari garis}
# Ordinat1: Garis -> integer
#   {Ordinat1(G) adalah selektor untuk mengambil data y dari tipe bentukan point dari garis}
# Absis2: Garis -> integer
#   {Absis2(G) adalah selektor untuk mengambil data x dari tipe bentukan point dari garis}
# Ordinat2: Garis -> integer
#   {Ordinat2(G) adalah selektor untuk mengambil data y dari tipe bentukan point dari garis}
# Gradien: Garis -> integer
#   {Gradien(G) adalah sebuah operator untuk mencari gradien}
# PanjangGaris: Garis -> integer
#   {PanjangGaris(G) adalah sebuah operator untuk mencari panjang}
# IsSejajar: Garis,Garis -> Boolean
#   {IsSejajar(G1,G2) adalah sebuah operator untuk menentukan apakah garis 1 dan garis 2 sejajar}
# IsTegakLurus: Garis, Garis -> Boolean
#   {IsTegakLurus(G1,G2) adalah sebuah operator untuk menentukan apakah garis 1 dan garis 2 tegak lurus}
# ===========================================================================
# REALISASI
# ===========================================================================

def Point(x,y):
    return [x,y]
def Makegaris(P1,P2):
    return [P1,P2]

def Absis1(P1):
    return P1[0]
def Ordinat1(P1):
    return P1[1]
def Absis2(P2):
    return P2[0]
def Ordinat2(P2):
    return P2[1]

def Gradien(G):
    return (Ordinat2(G[1])-Ordinat1(G[0]))/(Absis2(G[1])-Absis1(G[0]))

def PanjangGaris(G):
    return ((Absis2(G[1])-Absis1(G[0]))**2+(Ordinat2(G[1])-Ordinat1(G[0]))**2)**0.5

def IsSejajar(G1,G2):
    return Gradien(G1)==Gradien(G2)
def IsTegakLurus(G1,G2):
    return Gradien(G1)*Gradien(G2)==-1
# ===========================================================================
# APLIKASI
print(Gradien(Makegaris(Point(1,-3),Point(2,-6))))
print(PanjangGaris(Makegaris(Point(1,-2),Point(4,-6))))
print(IsSejajar(Makegaris(Point(1,-3),Point(2, 5)),Makegaris(Point(1,-3),Point(2,5))))
print(IsTegakLurus(Makegaris(Point(1,-2),Point(4,-6)),Makegaris(Point(1,6),Point(2,-3))))