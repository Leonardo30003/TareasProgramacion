"""Define una función que permita multiplicar los números de una lista y sumar
sus resultados."""

def multip (lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    print (multiplicacion)
multip([2,4,5,21,1,2,])
