def tipesegitiga(x,y,z):
    if x == 0 or y == 0 or z == 0:
        return "Gini lagi gw delete System32 lu..."
    else:
        if x == y and y == z:
            return "sama sisi"
        elif x == y or x == z:
            return "sama kaki"
        else:
            return "sembarang"

print(tipesegitiga(3,3,3))
print(tipesegitiga(5,3,5))
print(tipesegitiga(2,6,3))
print(tipesegitiga(2,0,3))