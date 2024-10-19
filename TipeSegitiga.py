def tipesegitiga(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        if x == y == z:
            return "sama sisi"
        elif x == y or y == z or z == x:
            return "sama kaki"
        else:
            return "sembarang"
    else:
        return "gak kebentuk lah..."
    
print(tipesegitiga(3,3,3))
print(tipesegitiga(5,3,5))
print(tipesegitiga(2,4,3))
print(tipesegitiga(2,0,3))