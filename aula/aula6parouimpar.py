numero = int(input("ME FALE UM NÚMERO: "))
resultado = numero % 2
if resultado == 0:
    print("Então significa que {} é PAR".format(numero))
else:
    print("Então significa que {} é ÍMPAR".format(numero))