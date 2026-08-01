#lista inicial
nomes = ["joaquim","maria","ana"]
print("lista inicial: ",nomes)

#adicionando elementos
nomes.append("carlos")#adicional ao final da lista
print("após append ", nomes)

nomes.insert(1,"fernanda") #insere fernanda no indice 1
print("apos insert ",nomes)

#modificando elementos 
nomes[2] = "paulo" # modificada o elemento no indice 2
print("apos modificação ", nomes)

#removendo elementos
del nomes [3]# remove o elemento de indice 3
print("apos del ", nomes)

nomes.remove("paulo") #remove a primeira a primeira incidencia de maria
print("apos remove ", nomes)

removido = nomes.pop(2) #removido e retorna o elemento do indice 2
print(f"apos pop (removido {removido})", nomes)

nomes.clear()# esvazia a lista
print("Após clear ", nomes)
