# Program     : Perpustakaan Agung
# Deskripsi   : Menetukan perkiraan pengunjung  
# NIM/Nama    : 24060124140145/Ferdy Prasetya Putra
# Tanggal     : 18/09/2024
# ===========================================================================
def datapengunjung(D): 
    if D == 'senin': 
        return (5000 + 6000 + 4000)/3
    elif D == 'selasa': 
        return (7000 + 5000 + 2000)/3
    elif D == 'rabu': 
        return (4500 + 3500 + 3000)/3
    elif D == 'kamis': 
        return (2900 + 2100 + 2000)/3
    elif D == 'jumat': 
        return (3000 + 3000 + 3000)/3
    elif D == 'sabtu': 
        return (2000 + 2500 + 2300)/3
    elif D == 'minggu': 
        return (1100 + 900 + 1000)/3

def Perkiraan(D, X, Y, AS, AM, AIP):
    return (abs(Y-X)*(max(AS, AM, AIP)-min(AS, AM, AIP)))/datapengunjung(D)

def EstimateGreatLib(D, X, Y, SS, SR, AS, AM, AIP, R):
    if X < SR and Y > SS:
           return round((Perkiraan(D, X, SR, AS, AM, AIP)*(R/100)+Perkiraan(D, SS, SR, AS, AM, AIP)+Perkiraan(D, SS, Y, AS, AM, AIP)*(R/100))/3, 5)
    elif X < SR and Y > SR:  
        return round((Perkiraan(D, X, SR, AS, AM, AIP)*(R / 100)+Perkiraan(D, SR, Y, AS, AM, AIP))/2, 5)
    elif  Y > SS and X < SS: 
        return round((Perkiraan(D, X, SS, AS, AM, AIP) + Perkiraan(D, SS, Y, AS, AM, AIP)*(R/100))/2, 5)
    elif (X < SR) or ((X > SS) and (Y < SR)) or (Y > SS):
        return round(Perkiraan(D, X, Y, AS, AM, AIP) * (R/100), 5)
    else:
        return round(Perkiraan(D,X,Y, AS, AM, AIP), 5)
    
print(EstimateGreatLib("senin", 12, 17, 18, 9, 6000, 5000, 4500, 50))
print(EstimateGreatLib("selasa", 8, 16, 20, 12, 7000, 5000, 2000, 75))
print(EstimateGreatLib("jumat", 7, 8, 17, 6, 4000, 5500, 5000, 3))
