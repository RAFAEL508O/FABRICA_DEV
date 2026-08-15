#solicitando os dados do usuario 
nome = input("digite o seu nome: ")
email = input("digite seu emali: ")

#ascxessando o arquivo e gravando os dados do usuario 

with open("09.2-pessoas.txt","a",encoding="utf-8") as arquivo:
    arquivo.write(nome + "| " + email + "\n")
    