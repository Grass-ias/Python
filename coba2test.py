# def Titik(x,y):
#     return [x,y]

# def Absis(T):
#     return T[0]
# def Ordinat(T):
#     return T[1]

# def Garis1(G1):
#     return abs(G1[0])+abs(G1[1])
# def Garis2(G2):
#     return abs(G2[0])+abs(G2[1])
# def Jarak(G1,G2):
#     return (abs(G2[0])-abs((G1[0]))**2)+(abs((G2[1])-abs((G1[1])))**2)**0.5

# print(Garis1(Titik(2,-3)))
# print(Jarak(Titik(2,-3),Titik(-4,2)))

# def IsKabisat(y):
#     return (y % 4 ==  0 and y % 100 != 0) or y % 400 == 0

# def dpm(m):
#     if m == 1: return 1
#     elif m == 2: return 32
#     elif m == 3: return 60
#     elif m == 4: return 91
#     elif m == 5: return 121
#     elif m == 6: return 152
#     elif m == 7: return 182
#     elif m == 8: return 213
#     elif m == 9: return 244
#     elif m == 10: return 274
#     elif m == 11: return 305
#     elif m == 12: return 335

# def HariTotal(d,m,y):
#     if IsKabisat(y) and m>2:
#         return dpm(m)+(d-1)+1
#     else:
#         return dpm(m)+(d-1)
    
# def Hariapa(d,m,y):
#     if HariTotal(d,m,y) % 7 == 1: return "Senin"
#     elif HariTotal(d,m,y) % 7 == 2: return "Selasa"
#     elif HariTotal(d,m,y) % 7 == 3: return "Rabu"
#     elif HariTotal(d,m,y) % 7 == 4: return "Kamis"
#     elif HariTotal(d,m,y) % 7 == 5: return "Jumat"
#     elif HariTotal(d,m,y) % 7 == 6: return "Sabtu"
#     elif HariTotal(d,m,y) % 7 == 0: return "Minggu"

# print(Hariapa(1,1,1900))
# print(Hariapa(3,1,2000))
# print(Hariapa(2,1,2000))
# print(Hariapa(2,2,2001))
# print(Hariapa(3,3,2001))
# print(Hariapa(3,3,2000))

def IsKabisat(y):
    return (y % 4 ==  0 and y % 100 != 0) or y % 400 == 0

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

def ApakahHariRabu(d,m,y):
    if IsKabisat(y) and m>2:
        if (dpm(m) + (d-1) + 1) % 7 == 3:
            return True
        else:
            return False
    else:
        if (dpm(m) + (d-1)) % 7 == 3:
            return True
        else:
            return False
        
def ApakahBesokKamis(d,m,y):
    if IsKabisat(y) and m>2:
        if (dpm(m) + (d-1) + 2) % 7 == 4:
            return True
        else:
            return False
    else:
        if (dpm(m) + (d-1) + 1) % 7 == 4:
            return True
        else:
            return False
        
print(ApakahHariRabu(1,1,1900))
print(ApakahHariRabu(1,1,2000))
print(ApakahHariRabu(2,1,2000))
print(ApakahHariRabu(2,2,2001))
print(ApakahBesokKamis(3,3,2001))
print(ApakahBesokKamis(3,3,2000))
print(ApakahBesokKamis(3,1,2000))
print(ApakahBesokKamis(3,1,2024))
