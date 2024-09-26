
'''
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

#11
class Persona:
    
    
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def decirnombre(self):
        return self.nombre
    

p1=Persona("Juan",18)

print("El nombre es "+str(p1.nombre)+" y la edad "+str(p1.edad))
print(p1.decirnombre())

#12
    
class Rectangulo():
    
    def __init__(self,ancho,altura):
        self.ancho=ancho
        self.altura=altura
    
    def area(self):
        ar=float(self.ancho*self.altura)
        return ar
    
    def perimetro(self):
        per=float(2*(self.ancho+self.altura))
        return per
    

n1=float(input("Introduce el ancho del cuadrado "))
n2=float(input("Introduce la altura del cuadrado "))

r1=Rectangulo(n1,n2)

print("El area es "+str(r1.area()))
print("El perimetro es "+str(r1.perimetro()))

#13
class Estudiante():
    def __init__(self,nombre,edad,curso):
        self.nombre=nombre
        self.edad=edad
        self.curso=curso
    
    def __str__(self):
         return self.nombre + " " + str(self.edad) + " " + self.curso 
    

e1=Estudiante("Alvaro",24,"2DAW")
e2=Estudiante("Lolo",27,"2DAW")
e3=Estudiante("Mohcen",23,"2DAW")

lista=[]

lista.append(e1)
lista.append(e2)
lista.append(e3)

for i in range(0,len(lista)):
    print(lista[i])
    


#14
class CuentaBancaria():
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
        
    def depositar(self):
        dinero=float(input("introduce el dinero que quieres depositar "))
        self.saldo=self.saldo+dinero
        return "Tienes tal saldo " , self.saldo
    
    def retirar(self):
        dinero=float(input("introduce el dinero que quieres sacar "))
        if(self.saldo>=dinero):
            self.saldo=self.saldo-dinero
            return "Tienes tal saldo ",self.saldo
        else:
            return "No tienes dinero suficiente"
   
         
c1=CuentaBancaria("Felipe",3000)

cadena=input("Introduce si quieres retirar o depositar ").lower()

if(cadena=="depositar"):
    print(c1.depositar())
elif(cadena=="retirar"):
    print(c1.retirar())
else:
    print("No disponible dicha operacion")

    



#15
class Coche():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def __str__(self):
        return f"El coche es la marca {self.marca} y el modelo es {self.modelo} "

c1=Coche("Volkswagen","Golf")
print(c1)


#16
class animal():
    def __init__(self,nombre):
        self.nombre=nombre
        
    def decirnombre(self):
        return "El nombre es",self.nombre

class perro(animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def hablar(self):
        return "Guau soy un "+self.nombre
        

class gato(animal):
    def __init__(self, nombre):
        self.nombre=nombre
    def hablar(self):
        return "Miau soy un "+self.nombre

a1=gato("gato")
a2=perro("perro")
print(a1.hablar())
print(a2.hablar())

#17
class FiguraGeometrica():
    def __init__(self,ancho,altura):
        self.ancho=ancho
        self.altura=altura
        
    def area(self):
            return "Suscribir el metodo"        

class Rectangulo(FiguraGeometrica):
    def area(self):
         return super().area()
      
      
class Triangulo(FiguraGeometrica):
    def area(self):
        return (self.ancho * self.altura) / 2



f1 = Rectangulo(30, 20)
f2 = Triangulo(10, 10)



print(f1.area())
print(f2.area())

'''
#18 
class vehiculo():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def imprimir(self):
        return f"La marca es {self.marca} y el modelo es {self.modelo}"
    
class Coche(vehiculo):
    def __init__(self, marca, modelo,velocidad,ruedas):
        super().__init__(marca, modelo)
        self.velocidad=velocidad
        self.ruedas=ruedas
    
    def ruedas(self):
        return "El coche tiene ",self.ruedas
    
            
    
    


            
    
    
    


     

