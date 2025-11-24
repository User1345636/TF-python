def AND(a,b):
    if a and b == 1:
        return 1
    else:
        return 0

def OR(a,b):
    if a or b == 1:
        return 1
    else:
        return 0

def XOR(a,b):
    if a == 1 and b == 0 or a == 0 and b == 1:
        return 1
    else:
        return 0

def NOT(a):
    if a == 1:
        return 0
    else:
        return 1

def Full_Adder(a,b,cin):
    r0 = XOR(a,b)
    r1 = AND(a,b)
    r2 = XOR(r0,cin)
    r3 = AND(r0,cin)
    r4 = OR(r1,r3)
    return r2, r4
