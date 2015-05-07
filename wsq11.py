def inverse(o):
    o =str(o)
    o = o[::-1]
    o =int(o)
    return o


num=[]
lyc=[]

B = int(input("Please enter the lower bound: "))
U = int(input("Please enter the upper bound: "))

print ("The range of numbers checked is: %s to %s" %(B,U))

for i in range(U-B+1):
    num.append(B)
    B = B+1
L=0
I=0
N=0
for i in num:
    B = inverse(i)
    if i== B:
        L = L+1
    else:
        E = i + B
        B = inverse(E)
        for q in range(30):
            if E == B:
                I = I+1
                break
            else:
                E = E + B
                B = inverse(E)
                if q == 29:
                    N = l+1
                    lyc.append(i)

print ('The number of natural palindromes is : %s' %(L))
print ('The number of Non-Lychrel numbers is: %s' %(I))
print ('The number of Lychrel number candidates is: %s' %(N))

if N!= 0:
    print ("The Lychrel number candidates is:")
    print (lyc)
