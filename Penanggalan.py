def Makedate(d,m,y):
    return [d,m,y]
def Hr(D):
    return D[0]
def Bln(D):
    return D[1]
def Thn(D):
    return D[2]
def IsKabisat(D):
    return (Thn(D)%4 == 0 and Thn(D)%100 != 0) or Thn(D)%400 == 0
def NextDay(D):
    if Bln(D) == 1 or Bln(D) == 3 or Bln(D) == 7 or Bln(D) == 8 or Bln(D) == 10: # bulan dengan 31 hari
        if Hr(D)<31: 
            return Makedate(Hr(D)+1,Bln(D),Thn(D))
        else:
            return Makedate(1,Bln(D)+1,Thn(D))
    elif Bln(D) == 2:
        if IsKabisat(D)== False:
            if Hr(D)<28: 
                return Makedate(Hr(D)+1,Bln(D),Thn(D))
            else:
                return Makedate(1,Bln(D)+1,Thn(D))
        elif IsKabisat(D) == True:
            if Hr(D) == 28: 
                return Makedate(Hr(D)+1,Bln(D),Thn(D))
            elif Hr(D)>28:
                return Makedate(1,Bln(D)+1,Thn(D))    
            elif Hr(D)<28: 
                return Makedate(Hr(D)+1,Bln(D),Thn(D))   
    elif Bln(D) == 4 or Bln(D) == 6 or Bln(D) == 9 or Bln(D) == 11: # bulan dengan 30 hari
        if Hr(D)<30: 
            return Makedate(Hr(D)+1,Bln(D),Thn(D))
        else:
            return Makedate(1,Bln(D)+1,Thn(D))
    elif Bln(D) == 12:
        if Hr(D)<31:
            return Makedate(Hr(D)+1,Bln(D),Thn(D))
        else: 
            return Makedate(1,1,Thn(D)+1)

def Yesterday(D):
    if Hr(D) == 1:
        if Bln(D) == 12 or Bln(D) == 5 or Bln(D) == 7 or Bln(D) == 8 or Bln(D) == 10:
            return Makedate(30,Bln(D)-1,Thn(D))
        elif Bln(D) == 3:
            if IsKabisat(D) == True:
                return Makedate(29,Bln(D)-1,Thn(D))
            elif IsKabisat(D) == False:
                return Makedate(28,Bln(D)-1,Thn(D))
        elif Bln(D) == 4 or Bln(D) == 6 or Bln(D) == 9 or Bln(D) == 11:
            return Makedate(31,Bln(D)-1,Thn(D))
        elif Bln(D) == 1:
            return Makedate(31,12,Thn(D)-1)
    else:
        return Makedate(Hr(D)-1,Bln(D),Thn(D))
        
def IsEqD(D1,D2):
    return Hr(D1)==Hr(D2) and Bln(D1)==Bln(D2) and Thn(D1)==Thn(D2)

def IsBefore(D1,D2):
    if Thn(D1)<Thn(D2):
        return True
    elif Thn(D1) == Thn(D2):
        if Bln(D1)<Bln(D2):
            return True
        elif Bln(D1)==Bln(D2):
            if Hr(D1)<Hr(D2):
                return True
    return False
    
def IsAfter(D1,D2):
    if Thn(D1)>Thn(D2):
        return True
    elif Thn(D1)==Thn(D2):
        if Bln(D1)>Bln(D2):
            return True
        elif Bln(D1)==Bln(D2):
            if Hr(D1)>Hr(D2):
                return True
    return False

D1 = Makedate(20,10,2023)
D2 = Makedate(19,10,2023)
print(NextDay(D1))
print(Yesterday(D2))
