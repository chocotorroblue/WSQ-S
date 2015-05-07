x=open("93cars.dat.txt","r")
mpgc=0
mpgh=0
mp=0
cars=0
f=1
for line in x:
    if f%2==1:
        mpgc=mpgc+float(line[52:54])
        mpgh=mpgh+float(line[55:57])
        mp=mp+float(line[43:46])
        cars=cars+1
    f=f+1
y=round(mpgc/cars,6)
w=round(mpgh/cars,6)
z=round(mp/cars,6)

print("City MPG: ", y)
print("Highway MPG: ", w)
print("Avarage midrange price of vehicles: ",z)        
