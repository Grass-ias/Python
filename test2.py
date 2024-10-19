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