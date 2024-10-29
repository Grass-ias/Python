# Program     : Garis.py
# Deskripsi   : Membuat garis menggunakan tipe bentukan dan mengoperasikannya dengan operator yang ditentukan serta pengecekkan melalui predikat yang telah ditentukan
# NIM/Nama    : 24060124140145/Ferdy Prasetya Putra
# Tanggal     : (19/10/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI TIPE
# ===========================================================================
# type point: <x: integer, y:integer>
#   {<x,y> adalah elemen dari point dimana x dan y merupakan absis dan ordinat}
# type garis: <P1: point, P2:point>
#   {<P1,P2> adalah elemen dari garis dimana P1 dan P2 merupakan garis 1 dan garis 2 }
# ===========================================================================
# DEFINISI DAN SPESIFIKASI SELEKTOR
# ===========================================================================
# Tujung: garis -> point
#   {Tujung(G) adalah selektor untuk mengambil data point (titik ujung) dari tipe bentukan point dari garis}
# Tpangkal: garis -> point
#   {Tpangkal(G) adalah selektor untuk mengambil data point (titik pangkal) dari tipe bentukan point dari garis}
# Absis: point -> real
#   {Absis(G) adalah selektor untuk mengambil data x dari tipe bentukan point}
# Ordinat: point -> real
#   {Ordinat(G) adalah selektor untuk mengambil data y dari tipe bentukan point}
# ===========================================================================
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# ===========================================================================
# MakePoint: <x: integer, y: integer> -> point
#   {MakePoint(x,y) adalah sebuah konstruktor untuk mengkonversi x dan y menjadi tipe bentukan point}
# MakeGaris: <P1: point, P2:point> -> garis
#   {MakeGaris(P1,P2) adalah sebuah konstruktor untuk mengkonversi P1 dan P2 menjadi tipe bentukan garis}
# ===========================================================================
# DEFINISI DAN SPESIFIKASI OPERASI
# ===========================================================================
# Gradien: garis -> integer
#   {Gradien(G) adalah sebuah operator untuk mencari gradien}
# PanjangGaris: garis -> integer
#   {PanjangGaris(G) adalah sebuah operator untuk mencari panjang}
# ===========================================================================
# DEFINISI DAN SPESIFIKASI PREDIKAT
# ===========================================================================
# IsSejajar: 2 garis -> Boolean
#   {IsSejajar(G1,G2) digunakan untuk menentukan apakah garis 1 dan garis 2 sejajar}
# IsTegakLurus: 2 garis -> Boolean
#   {IsTegakLurus(G1,G2) digunakan untuk menentukan apakah garis 1 dan garis 2 tegak lurus}
# ===========================================================================
# REALISASI
# ===========================================================================

def MakePoint(x,y):
    return [x,y]
def MakeGaris(P1,P2):
    return [P1,P2]

def Tujung(G):
    return G[0]
def Tpangkal(G):
    return G[1]
def Absis(G):
    return G[0]
def Ordinat(G):
    return G[1]

def Gradien(G):
    return (Ordinat(Tujung(G))-Ordinat(Tpangkal(G))/(Absis(Tujung(G))-Absis(Tpangkal(G))

def PanjangGaris(G):
    return ((Absis(TitikPangkal(G))-Absis(TitikUjung(G)))**2+(Ordinat(TitikPangkal(G))-Ordinat(TitikUjung(G)))**2)**0.5

def IsSejajar(G1,G2):
    return Gradien(G1)==Gradien(G2)
def IsTegakLurus(G1,G2):
    return Gradien(G1)*Gradien(G2)==-1
# ===========================================================================
# APLIKASI
print(Gradien(MakeGaris(MakePoint(1,-3),MakePoint(2,-6))))
print(PanjangGaris(MakeGaris(MakePoint(1,-2),MakePoint(4,-6))))
print(IsSejajar(MakeGaris(MakePoint(1,-3),MakePoint(2, 5)),MakeGaris(MakePoint(1,-3),MakePoint(2,5))))
print(IsTegakLurus(MakeGaris(MakePoint(1,-2),MakePoint(4,-6)),MakeGaris(MakePoint(1,6),MakePoint(2,-3))))
