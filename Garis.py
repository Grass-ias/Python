def MakeGaris(x1,y1,x2,y2):
    return [x1,y1,x2,y2]

def Absis1(G):
    return G[0]
def Ordinat1(G):
    return G[1]
def Absis2(G):
    return G[2]
def Ordinat2(G):
    return G[3]

def Gradien(G):
    return G[3]+G[1]/G[2]+G[0]

def PanjangGaris(G):
    return ((G[2]-G[0])**2+(G[3]-G[1])**2)**0.5

def IsSejajar(G1,G2):
    return Gradien(G1)==Gradien(G2)
def sTegakLurus(G1,G2):
    return Gradien(G1)*Gradien(G2)==-1

 