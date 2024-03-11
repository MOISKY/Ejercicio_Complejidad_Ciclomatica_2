#Diseñe un algoritmo que solicite al usuario un monto en pesos e indique el número de
#monedas de $10, $5, $2, $1 en las que se puede dividir la cantidad.
cantidad = int(input("Ingresar monto: "))
cantidad10,residuo10 = cantidad // 10,cantidad % 10
cantidad5,residuo5 = residuo10 // 5,residuo10 % 5
cantidad2,residuo2 = residuo5 // 2,residuo5 % 2
cantidad1,residuo1 = residuo2 // 1,residuo2 % 1
print("numero de monedas de 10: ",cantidad10,"\n numero de monedas de 5",cantidad5,"\n numero de monedas de 2",cantidad2,"\n numero de monedas de 1",cantidad1)