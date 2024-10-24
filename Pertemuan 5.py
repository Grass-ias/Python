import math


def MakePoint(x,y):
    return (x,y)
def Absis(P):
    return P[0]
def Ordinat(P):
    return P[1]
    
P = MakePoint(1,1)

def Kuadran(P):
    if Absis(P) > 0 and Ordinat(P) > 0:
        return (f'{Absis(P)}, {Ordinat(P)} terdapat di Kuadran-1')
    elif Absis(P) < 0 and Ordinat(P) > 0:
        return (f'{Absis(P)}, {Ordinat(P)} terdapat di Kuadran-2')
    elif Absis(P) < 0 and Ordinat(P) < 0:
        return (f'{Absis(P)}, {Ordinat(P)} terdapat di Kuadran-3')
    elif Absis(P) > 0 and Ordinat(P) < 0:
        return (f'{Absis(P)}, {Ordinat(P)} terdapat di Kuadran-4')
    else:
        return "Ga di semua"
    
print(Kuadran(P))
def jalanSemut(x,y,z):
    return round(min((((x+y)**2+z**2)**0.5), (((x+z)**2+y**2)**0.5), (((y+z)**2+x**2)**0.5),3))
