#solicitando informaçoes de acesso ao usuário
email = input("digite o e-mail de acesso: ")
senha = input("digite a senha de acesso: ")

if email == "teste@teste.com.br":
    print("email correto")
else:
    print("usuario não cadastrado")
    
    
# verificando se a senha está correta e liberando acesso ao sistema
if senha == "123456":
    print("bemn vindo ao sistema da fabrica")
else:
    print("senha incorreta")


