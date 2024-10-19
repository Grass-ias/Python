datapengunjung = {
    "senin" : [5000, 6000, 4000],
    "selasa": [7000, 5000, 2000],
    "rabu"  : [4500, 3500, 3000],
    "kamis" : [2900, 2100, 2000],
    "jumat" : [3000, 3000, 3000],
    "sabtu" : [2000, 2500, 2300],
    "minggu": [1100, 900 , 1000]
}

def Perkiraan(D, X, Y, AS, AM, AIP):
    rata2pengunjung = sum(datapengunjung[D]) / 3
    return (abs(Y-X)*(max(AS, AM, AIP)-min(AS, AM, AIP)))/rata2pengunjung 

def EstimateGreatLib(D, X, Y, SS, SR, AS, AM, AIP, R):
    if X < SR and Y > SS:
           return round((Perkiraan(D, X, SR, AS, AM, AIP) * (R / 100) + Perkiraan(D, SS, SR, AS, AM, AIP) + Perkiraan(D, SS, Y, AS, AM, AIP) * (R/ 100)) / 3 , 5)
    elif X < SR and Y > SR:  
        return round((Perkiraan(D, X, SR, AS, AM, AIP) * (R / 100) + Perkiraan(D, SR, Y, AS, AM, AIP)) / 2 , 5)
    elif  Y > SS and X < SS: 
        return round((Perkiraan(D, X, SS, AS, AM, AIP) + Perkiraan(D, SS, Y, AS, AM, AIP) * (R / 100)) /2 , 5)
    elif (X < SR) or ((X > SS) and (Y < SR)) or (Y > SS):
        return round(Perkiraan(D, X, Y, AS, AM, AIP) * (R / 100)  , 5)
    else:
        return round(Perkiraan(D,X,Y, AS, AM, AIP) , 5)


print(eval(input()))