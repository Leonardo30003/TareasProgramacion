"""Define una función que permita imprimir un mensaje en base a los valores
tomados de una lista para comprobar si todos los de la lista son mayores o
menores de edad."""

def mayorMenorEdad(lista):
    for i in lista:
        if i > 18:
            print ("Es mayor de edad")
        else:
            print ("Es menor de edad")
mayorMenorEdad([18,21,8,19,5,4,3,8,2,3])