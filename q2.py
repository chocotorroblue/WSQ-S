def find_threes(l):
    x = 0
    for e in l:
        if(e % 3 == 0):
            x = x + e
        return x

n = [0,4,2,6,9,8,3,12]
print(find_threes(n))
