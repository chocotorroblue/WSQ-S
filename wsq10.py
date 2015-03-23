#Omar Chavez

import statistics

def tsum (s):
    tot = 0
    # add total each value in m
    for indice in range(len(s)):
        tot = tot + s[indice]
    return tot
def average (s):
    av = mitotal / 10.0
    return av

def standevi (s):
    sd = statistics.stdev(l)
    return sd

l=[]
x = 0

while (x < 10):
    x = x + 1
    n = float(input("Give me a number: "))
    l.append(n)
    mitotal = tsum(l)
    promedio = average(l)
devi = standevi(l)

print("No more values")
print("Total sum: ", mitotal)
print("Average: ", promedio)
print("Standar deviation: ", devi)
