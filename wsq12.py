#lol
def gcd(a,b):
    if(a == b):
        answer = a
    elif(a > b):
        answer = gcd((a-b), b)
    else:
        answer = gcd(a, (b-a))
    return answer
#lel
print("Here is the GCD of two integer numbers")
x = int(input("Give me the first number: "))
y = int(input("Give me the second number "))
rgcd = gcd(x, y)
print("The GCD of", x , "and", y, "is", rgcd)
