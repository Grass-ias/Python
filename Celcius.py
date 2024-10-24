def Konversi(x,y):
    if  y == 1:
        return (x * (4/5))
    elif y == 2:
        return (x*(9/5)) + 32
    elif y == 3:
        return (x + 273)
    else:
        return "gini lagi gw delete system32 ntar..."

print(Konversi(54,1))
print(Konversi(-20,2))
print(Konversi(22,3))