def triangles(n):
    for i in range(1, n +1):
        for j in range(i):
            print("T", end="")
        print()

    for i in range(1,n):
        for j in range(n-i):
            print("T", end="")
        print()

n=int(input("Give me the size of the triangle"))
z=triangles(n)
print(z)                    
