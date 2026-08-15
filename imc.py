# pedindo dados

nome = (input("digite seu nome: "))
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

#calculando imc
imc = peso / (altura ** 2)

print("------------------------------")
print(nome)
print("------------------------------")
print("seu imc é:", imc)
print("------------------------------")

#mostrando o imc

if imc >= 30.0:
    print("cuidado com a saude")
else:
    print("tudo ok")
    print("------------------------------")

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
    
print("|---------------------|------------------------------|")
print("|     Faixa de IMC    |         Classificação        |")
print("|---------------------|------------------------------|")
print("| < 18.5              | Abaixo do peso               |")
print("| 18.5 – 24.9         | Peso normal                  |")
print("| 25.0 – 29.9         | Sobrepeso                    |")
print("| 30.0 – 34.9         | Obesidade Grau I             |")
print("| 35.0 – 39.9         | Obesidade Grau II            |")
print("| ≥ 40.0              | Obesidade Grau III (mórbida) |")
print("|---------------------|------------------------------|")