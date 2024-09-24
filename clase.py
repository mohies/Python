
#1
print("Hola mundo")
#2
num1=int(input("Introduce un numero "))
num2=int(input("Introduce un numero2 "))

suma=num1+num2
print("la suma es "+str(suma))

#3
base=float(input("Introduce la base "))
altura = float(input("Introduce la altura "))

area=float((base*altura)/2)

print("La base es "+str(area))

#4

grados=float(input("Introduce los grados "))
conversion=float((grados*(9/5)+32))

print("Esta es la conversion en farenheit "+str(conversion))

#5

n=int(input("Introduce numero "))
cuenta=1
for i in range(n,0,-1):
        cuenta=cuenta*i

print(f"El factorial de {n} es: {cuenta}")


#6

n=int(input("Introduce numero "))

if n % 2 ==0:
    print("Es par")
else:
    print("Es impar")


 
#7
n=int(input("Introduce numero "))
n2=int(input("Introduce numero "))

for i in range(n,0,-1):
    if n % i == 0:
        for j in range(n2,0,-1):
            if n2 % j == 0 :
                if i==j:
                    print("El maximo comun divisor es "+str(i)+" "+str(j))
    break       
    
#8  
for i in range(1,11):
    print(i)        
            
        
#9 
suma=0
for i in range(1,101):
    suma=suma+i 
    
print("La suma total seria"+str(suma))
 

#10
lista=[1,2,3,4,5,6,7,8]
contador=0
suma=0
for i in lista:
    suma=suma+i
    contador+=1

cuenta=suma/contador

print("EL promedio es "+cuenta)


    

