"""Define una función llamada menorque() que nos devuelva en pantalla el número
menor entre dos enteros. Define una salida de texto en caso de que."""
a=int(input("Ingrese un numero: "))
b=int((input("Ingrese un segundo numero: ")))

def menorque():
    if a>b:
        print(b,"Es menor que ",a)
    else:
        print(a,"Es menor que ",b)
menorque()