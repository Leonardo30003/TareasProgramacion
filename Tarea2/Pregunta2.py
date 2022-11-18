"""Define una función llamada num_max() que nos devuelva en pantalla el número
mayor entre 4 diferentes enteros. No definas ningún valor a imprimir en caso
de que ambos números sean iguales."""

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese otro numero: "))
numero4 = int(input("Ingrese otro numero: "))


def num_max():
    if numero1 > numero2 and numero1 > numero3 and numero1 > numero4:
        print("El numero mayor es: ", numero1)
    elif numero2 > numero1 and numero2 > numero3 and numero1 > numero4:
        print("El mayor es: ", numero2)
    elif numero3 > numero1 and numero3 > numero2 and numero3 > numero4:
        print("El mayor es: ", numero3)
    elif numero4 > numero1 and numero4 > numero2 and numero4 > numero3:
        print("El mayor es: ", numero4)
    else:
        print()


num_max()
