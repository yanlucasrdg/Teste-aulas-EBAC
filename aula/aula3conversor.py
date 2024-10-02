medida = float(input("Digite um numero para converter em medidas:  "))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
dam = medida / 10
print("A media de {} metros corresponde a {} centímetros e {} milímetros , {} kilômetros , {} decâmetros ".format(medida, cm , mm, km, dam))