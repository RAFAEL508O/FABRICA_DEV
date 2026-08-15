#solicitando os dados do usuario 
nome = input("digite o seu nome: ")
email = input("digite seu emali: ")

#ascxessando o arquivo e gravando os dados do usuario 

arquivo = open("09.1-pessoas.txt","a",encoding="utf-8")
arquivo.write(nome + " | " + email + "\n")
arquivo.close()

