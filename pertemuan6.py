def faciter(n, count, hasil):
    if n == count:
        return hasil * count
    else:
        return faciter(n, count + 1, hasil * count)

def fac(n):
    return faciter(n, 1 ,1)

print(fac(3))
print(fac(1))
print(fac(7))

def perkalian(x,y):
    if y == 1:
        return x
    else:
        return x + perkalian(x,y-1)

print(perkalian(2,3))
print(perkalian(3,4))
print(perkalian(4,2))

def fibbonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonnaci(n-1)+fibbonnaci(n-2)
    
print(fibbonnaci(0))
print(fibbonnaci(1))
print(fibbonnaci(2))
print(fibbonnaci(10))

def plus(x,y):
    if y == 0:
        return x
    else:
        return 1 + plus(x,y-1)
    
print(plus(1,2))
print(plus(5,9))
print(plus(3,2))

def pengurangan(x,y):
    if y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return pengurangan(x,y-1)-1
    
print(pengurangan(2,0))
print(pengurangan(5,2))
print(pengurangan(4,3))

def pembagian(x,y):
    if y == 0:
        return "Infinite"
    elif y == 1:
        return x
    else:
        return 1 + pembagian(x-y,y)
    
print(pembagian(2,1))
print(pembagian(4,2))
print(pembagian(4,2))