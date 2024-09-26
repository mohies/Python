prueba=5
prueba="Hola clase de daw"
print(prueba)

numero=25
#Else if aqui es elif
if numero>=18:
    print("es mayor")
    if numero>30:
        print("Esta la cosa buena")
    else:
        print("Esta la cosa mala")
        
for i in range(6,22):
    print(i)
print("fin")

for i in range(0,10):
    for j in range(0,10):
        print(str(i)+" "+str(j)) #para concatenar hay que concatenar con strings por eso hay que poner str
        
lista = [1,7,8,9]

for x in lista:
    print(x)
    
a=5
b=5.0
if a is b: #esto pasa porque uno es de un tipo y el otro es otro si ponemos == es para ver si el numero es igual
    print("Es igual")
else:
    print("No es igual")