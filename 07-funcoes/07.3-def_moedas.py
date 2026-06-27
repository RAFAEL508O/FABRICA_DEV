#definindo as funções de conversão de moeda
def dolar_real(valor_dolar):
    taxa = 5.06 #
    valor_real = valor_dolar * taxa
    return valor_real

def real_dolar (valor_real):
    taxa = 5.06 #
    valor_dolar = valor_real / taxa
    return valor_dolar

#criando o menu interativo
def menu():
    while True:
        print("\n=== conversor de moedas ===")
        print("1 - dólar para real")
        print("2 - real para doólar")
        print("0 - sair ")
        
        opcao = int(input("escolha uma opção: ")) #lê a opção do usuario
        
        if opcao == 1:
            valor = float(input("digite o valor em dolar $ "))
            resultado = dolar_real(valor)
            print(f"$ {valor} = R${resultado:.2f}")
            
        elif opcao == 2:
            valor = float(input("digite o valor em real R$ "))
            resultado = real_dolar(valor)
            print(f"$ {valor} = R${resultado:.2f}")
            
        elif opcao == 0:
            print("obrigado por usar o conversor de moedas!")
            break
        
        else:
            print("opção inválida. tente novamente.")
                
#executa o programa
menu()
