#solicitando o peso e a altura do usuario 
altura = float(input("digite seu altura: "))
peso = float(input("digite sua peso: "))

#calculando o imc
imc = peso / (altura ** 2)

#mostrando o imc
if imc >= 30.0:
    print("cuidado com a saude")
else:
    print("tudo ok")

#classificando os pesos
if imc <= 18.5:
    print("Abaixo do peso")
elif imc <= 25:
    print("peso normal ")
elif imc <= 30:
    print("sobrepeso ")
elif imc <= 35:
    print("obesidade Grau | ")
elif imc <= 40:
    print("obesidade Grau || ")
else:
    print("obesidade grau ||| ")
