"""Define una función llamada num_min() que nos devuelva en pantalla el número
menor entre 3 diferentes enteros. En caso de que todos sean iguales imprime en
pantalla un mensaje indicándolo."""

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese otro numero: "))


def num_min():
    if numero1 < numero2 and numero1 < numero3:
        print("El numero menor es: ", numero1)
    elif numero2 < numero1 and numero2 < numero3:
        print("El menor es: ", numero2)
    elif numero3 < numero1 and numero3 < numero2:
        print("El menor es: ", numero3)

    else:
        print("Error numeros repetidos")

num_min()
