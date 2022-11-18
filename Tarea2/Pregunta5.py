"""Define una función que nos devuelva True, pero al darle una vocal mayúscula nos
devuelva False, mientras que si es minúscula sea True."""


def true():
    vocal = input("Ingrese una vocal minuscula: ")
    print(vocal.islower())
true()




"""Para saber si son minuscula se utiliza .islower
pero para saber si es mayuscula se utiliza .isupper"""
