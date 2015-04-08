def sqrt(W):
    if W == 0:
        return W
    elif W < 0:
        return ("Error: You cant calculate the sqrt of a negative number")
    else:
        X = 0
        U = 0
        while X < W:
            X = U**2
            U = U+1

        if X == W:
            return (U - 1)

        else:
            N = (U-1)
            E= ((W / N) + N)/2
            while (E != N):
                N = E
                E = ((W / N) + N) /2
            return E
D = float(input("Enter the number that you want to calculate the sqrt of"))

print (sqrt(D))
