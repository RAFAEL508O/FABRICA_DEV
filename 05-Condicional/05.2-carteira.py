nome = input("qual é o seu nome? ")
idade = int(input("qual a sua idade? "))
possui_carteira = int(input("possui carteira de motorista? \n (1-sim / 2-nao)"))

if idade >= 18:
    possui_carteira = int(input("possui carteira de motorista? \n (1-sim / 2-não) "))

if possui_carteira == 1:
    print("pode dirigir")
else:
    print("nao pode dirigir")