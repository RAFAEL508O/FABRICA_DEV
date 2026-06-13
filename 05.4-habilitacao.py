# Entrada de dados nome

nome_aluno = input("Digite o nome do aluno: ") 
nota1 = float(input("Digite a primeira nota: ")) 
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média aritmética media
media = (nota1 + nota2 + nota3) / 3

# Verificação da situação do aluno
if media >= 6:
    situacao = "Aprovado"
elif media > 5:
    situacao = "Em Recuperação"
else:
    situacao = "Reprovado"

# Exibição do resultado
print("\nAluno:", nome_aluno)
print("média:", media)
print("situação:", situacao)