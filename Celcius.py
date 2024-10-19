def Konversi(x,y):
    if  y == 1:
        return (x * (4/5))
    elif y == 2:
        return (x*(9/5)) + 32
    elif y == 3:
        return (x + 273)
    else:
        return "gini lagi gw delete system32 ntar..."

print(str(Konversi(20,1)) + "°R")
print(str(Konversi(-20,2)) + "°F")
print(str(Konversi(20,3)) + "°K")
