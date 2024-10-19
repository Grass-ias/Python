def StateAir(x):
    if x <= 0:
        return "Keras euy"
    elif x > 0 and x < 100:
        return "Cair bosku"
    elif x >= 100:
        return "Asep euy"
    
print(StateAir(20))
print(StateAir(0))
print(StateAir(100))