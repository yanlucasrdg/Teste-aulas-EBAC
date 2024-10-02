velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    print("VOCÊ FOI MULTADO ! EXCEDEU O LIMITE DE VELOCIDADE")
    multa = (velocidade-80) * 7
    
    print("VOCÊ DEVE PAGAR UMA MULTA DE {} REAIS".format(multa))
print("TENHA UM BOM DIA E DIRIJA COM SEGURANÇA")