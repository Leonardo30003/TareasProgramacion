"""Crea un código que solicite ingresar el nombre de un archivo con su extensión y
devuelva la extensión de la misma. Por ejemplo: La extensión de programando-
aprenderpython.py es “.py”."""

nombrearchivo = input("Ingrese el nombre del archivo: ")
na_extns = nombrearchivo.split(".")
print ("La extensión del archivo es : " + repr(na_extns[-1]))