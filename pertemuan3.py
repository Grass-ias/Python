def max3(x,y,z):
    if x>y:
        if x>z:
            return x
        else:
            return z
    elif y>x:
        if y>z:
            return y
        else:
            return z
    elif z>x:
        if z>y:
            return z
        else:
            return y

def min3(x,y,z):
    if x<y:
        if x<z:
            return x
        else:
            return z
    elif y<x:
        if y<z:
            return y
        else:
            return z
    elif z<x:
        if z<y:
            return z
        else:
            return y

print("Minimum dari 4,1,5 adalah " + str(min3(4,1,5)))
print("Maximum dari 3,2,9 adalah " + str(max3(3,2,9)))
print("Maximum dari 20,20,20 adalah " + str(max3(20,20,20)))
