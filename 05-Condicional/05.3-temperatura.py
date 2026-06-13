# criando a variavel
temperatura = float(input("digite a temperatura em celsilios: "))

#verificando a condição da temperatura
if temperatura < 10:
    print("esta muito frio")
elif temperatura < 20:
    print ("esta frio")
elif temperatura < 30:
    print("esta agradavel")
else:
    print("esta muito quente")