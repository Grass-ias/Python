def IsKabisat(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def IsTanggalValid(d,m,y):
    if (d > 0 and d < 31) and (m > 0 and m < 12) and y > 0:
        if IsKabisat(y) == True and m == 2 and d == 29:
            return "valid"
        elif IsKabisat(y) == False and m == 2 and d == 29:
            return "tidak valid"
        else:
            return "valid"
    else:
        return "invalid"

print(IsTanggalValid(29,2,2021))
print(IsTanggalValid(28,2,2021))
print(IsTanggalValid(29,2,2020))

def IsKabisat(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def dpm(m):
    if m == 1: return 1
    elif m == 2: return 32
    elif m == 3: return 60
    elif m == 4: return 91
    elif m == 5: return 121
    elif m == 6: return 152
    elif m == 7: return 182
    elif m == 8: return 213
    elif m == 9: return 244
    elif m == 10: return 274
    elif m == 11: return 305
    elif m == 12: return 335

def HariTotal(d,m,y):
    if IsKabisat(y) and m > 2:
        return dpm(m)+(d-1)+1
    else:
        return dpm(m)+(d-1)

def Hariapa(d,m,y):
    if HariTotal(d,m,y) % 7 == 0: return "Senin"
    elif HariTotal(d,m,y) % 7 == 1: return "Selasa"
    elif HariTotal(d,m,y) % 7 == 2: return "Rabu"
    elif HariTotal(d,m,y) % 7 == 3: return "Kamis"
    elif HariTotal(d,m,y) % 7 == 4: return "Jumat"
    elif HariTotal(d,m,y) % 7 == 5: return "Sabtu"
    elif HariTotal(d,m,y) % 7 == 6: return "Minggu"

print(Hariapa(1,1,1900))
print(Hariapa(1,1,2000))
print(Hariapa(2,2,2000))
print(Hariapa(2,2,2001))
print(Hariapa(3,3,2001))
print(Hariapa(3,3,2000))



def BuatSegitiga(a,b,c):
    return [a,b,c]
def point1(S):
    return S[0]
def point2(S):
    return S[1]
def point3(S):
    return S[2]

def jarak(P1,P2):
    return (((P1[0] - P2[0])**2) + ((P1[1] - P2[1]) ** 2))**0.5
def GetKeliling(J1):
    return 

def GetLuas(S):
    return 




def Date(x):
    if x > 40:
        return x-40
    else:
        return x

def Month(y):
    if y == "1": return "Januari"
    elif y == "2": return "Februari"
    elif y == "3": return "Maret"
    elif y == "4": return "April"
    elif y == "5": return "Mei"
    elif y == "6": return "Juni"
    elif y == "7": return "Juli"
    elif y == "8": return "Agustus"
    elif y == "9": return "September"
    elif y == "10": return "Oktober"
    elif y == "11": return "November"
    elif y == "12": return "December"

def Year(z):
    if z + 2000 > 2024:
        return 19, {Year}
    else:
        return 20, {Year}

def Titik(x,y):
    return [x,y]

def Absis(T):
    return T[0]
def Ordinat(T):
    return T[1]

def Garis(G):
    return abs(G[0])+abs(G[1])

print(Garis(Titik(2,-3)))
