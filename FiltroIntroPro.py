#Construya un programa que muestre los números divisibles de 3 y 7 entre 1 y 1000. 

print("Numeros Divisibles de 3 y 7 ")

for i in range (1,1001) :
    if i%3==0 and i%7==0 :
        print(i)

