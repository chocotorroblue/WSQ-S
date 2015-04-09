def find_e(x):
    e = 0
    w = 0
    r = 1
    for y in range(100000):
        w = e
        e = e + 1/ r
        print("Now e is",e,"for iteration",y)
        e1 = 1 + e
        r = r*(r+1)
        if accuracy(w,e,x):
            break
    return e

def accuracy(x,w,z):
    import math
    x1 = x*pow(10,z)
    x1 = math.trunc(x1)
    x1 = x1/ pow(10,z)
    w1 = w * pow(10,z)
    w1 = math.trunc(w1)
    w1 = w1 / pow(10,z)
    return(x1==w1)
x=float(input("Give me the accuracy: "))
b= find_e(x)
print(b)
