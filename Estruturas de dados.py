#Estruturas de dados

#Lista:Pode ter elementos de varios tipos e é Ordenada e multavel - []

lista1=[1,'a',3,4,"Luiz Felipe"]
lista2=[2,'b',[4,5],'Gabriela Lira']#pode ter uma lista dentro de uma lista
lista3=[1,'a',3,4,"Luiz Felipe"]
#Lista 1 é igual a lista 2
print(lista1==lista2)
#Acesso por indices
print(lista1[4])
print(lista2[2])
#Acesso por slices(intervalos)
print(lista1[1:4])
print(lista2[-2:])
#Adiciona um novo elemento a lista -Adiciona um valor no final
lista1.append(999)
print(lista1)
#Altera o valor do quarto e do ultimo elemento
lista1[3]='a'
lista1[-1]=lista1[-1]+1
print(lista1)
#Remove a primeira ocorrencia do elemento 'a'
lista1.remove('a')
print(lista1)
#Funções,Operadores e Metodos

#Operadores de concatenação(+),repetição(*) e filiação (in)

l1=[30,10,20]
l2=[2,'a',5.44,True]

print(l1+l2)#Juntar todas as listas
print(l1*3) #Repete a lista 3 vezes
print(10 in l1) #O valor 10 está em l1

#Funções úteis

print(len(l2))# len retorna a quantidade de elementos na lista
print(sum(l1))# sum retorna a soma dos elementos de uma lista
print(max(l1))# max retorna o maior elemento da lista l1

#Metodos que alteram os valores internos da lista

l2.reverse() #reverse inverte a ordem dos elementos
print(l2)

l1.extend([10,20,30,40,10])#extend adiciona elementos de outra sequencia
print(l1)

l1.sort()#sort ordena os valores da lista
print(l1)

l2.insert(2,'novo valor') #insert:Adiciona um elemento no indice específico
print(l2)

l2.pop()#pop remove o ultimo elemento da lista
print(l2)

l2.clear()#clear limpa a lista e remove todos os elementos

#Metodos que retornam valores e não alteram a lista

print(l1.index(40))#index retorna o indice da primeira ocorrencia do elemento(primeira vez que aparece na lista)
print(l1.count(10))# count conta as ocorrencias do elemento

#l4=[2,'a',5.44,True]  -  Da um erro porque tem varios tipos juntos.
#print(max(l4))

idades=[27,49,12,67,21,32,18,45,84,53,22,56,80,35,18]
print('Maior idade é:',max (idades))

#Tupla:Ordenada e imutavel.Tem as mesmas operações que as listas, porem nada que altere 
#Tuplas:São semelhantes as listas,porem são imultaveis.

#Criando uma tupla homogênea
tupla=(0,1,2,3,4)
print(tupla)

#Tupla Heterogênea
tupla2=(2,'a',5.44,True,None)
print(tupla2)

#Tupla vazia
tupla3=()
print(tupla3)

#Acesso por indices
print(tupla[0])
print(tupla2[3])
print(tupla[-1])



#Conjunto:Nao ordenada e valores unicos

#Conjuntos

#União : Pega tudo que tem no conjunto A e no Conjunto B e junta tudo criando um novo conjunto.Caso tenha algum
#valor repetido, só ficará um

#Interseção:Pega apenas os valores que são comuns entre os dois conjuntos.

#Diferença: Só vão pegar os valores que estão em A mas nao estão no B e visse e versa

#Criação de conjunto Homogêneo (não existe elemento repetido no conjunto e eles sempre se ordenam automaticamente)
c1={3,0,1,4,3}
print(c1)

#Conjunto com ordenação diferente
c2={2,1,4,3,0}
print(c2)

#Conjunto Heterogênio
c3={2,'a',5.44,True,None}
print(c3)

#Criação dos conjuntos A e B
A={1,2,3,4,5}
B={4,5,6,7,8}
print('A:',A)
print('B:',B)


#Operação de União(A e B)
print('A | B =>',A|B) #Pode usar o simbulo  ou 
print('A.union(B)=>',A.union(B))# Usar a metodo union

#Operação de intersecção
print('A & B =>',A & B)#Pode usar o simbulo  ou 
print('A.intersection(B) =>',A.intersection(B))# Usar a metodo intersection


#Operação de diferença
print('A-B =>',A-B)#Pode usar o simbulo  ou 
print('A.difference(B) =>',A.difference(B))# Usar a metodo difference
print('B-A =>',B-A)#Pode usar o simbulo  ou 
print('A.difference(A) =>',A.difference(A)) # Usar a metodo difference

#Adicionando elemento no conjunto
A.add(6)
print(A)

#Adiciona os elementos no conjunto e exclui os que ja tem
A.update([2,4,6,8])
print(A)

#Descarta um elemento do conjunto(Diferente do set.remove(), o discard não gera erro se o elemento não existir
A.discard(8)
print(A)

#Verifica se os conjuntos são distintos, ou seja,se não possui nenhum elemento em comum
print(A.isdisjoint(A))
print(B.isdisjoint(B))

#Verifica se o conjunto é subconjunto de outro
print(A.issubset(A))
print(B.issubset(B))

#Verifica se o conjunto contem outro conjunto(superset)
print(A.issuperset(A))
print(B.issuperset(B))

#Exemplos práticos dos conjuntos 

#Criação das listas de alunos das turmas com listas

ing={'Gabriel','Caio','Maria','Ana','Juliano','Flavia','Rubens','Bruna'}
esp={'Caio','Arthur','Beatriz','Carolina','Maria','Juliano','Bruna','Rui'}
fran={'Pedro','Bruna','Paula','Tiago','Maria','Flavia','Rui','Carolina'}

todos= ing|esp|fran
print(todos)

alunos_desconto= (ing&esp)|(ing&fran)|(esp&fran) #intersecção entre os pares e depois calcula a união das intersecções
print('Relação dos alunos com desconto')
print(alunos_desconto)


# Dicionario:Mapeamento(Key,value),não-ordenado e mutavel
#Tipo dicionario(dict): Fica: {chave:valor1,chave:valor2}

#Dicionario onde as chaves são do tipo string
d1={'nome':'Gabriela Lira','idade':32,'sexo':'Feminino'}
print(d1)

#Dicionario misto
d3={2:'a',5.44:'True','key':None,}
print(d3)

#Acesso aos elementos
print(d3[2]) # Vai trazer o elemento dois e não a posição
print(d1['nome'])

print(f' Meu nome é{d1["nome"]},tenho {d1["idade"]} anos de idade e sou do sexo {d1["sexo"]}')

#Alterar uma um valor dentro da chave
d1['nome']='Luiz Felipe'
print(d1)

#Adicionar uma nova chave
d1['endereco']='Rua Achiles Beline'
print (d1)

#Encontrar a maior e a menor chave
print('Maior e menor chave são',max(d1),min(d1)) # é a menor chave e não o menor valor dentro da chave.

#Adiciona elementos de um outro dicionario
d1.update({'cinco':5,'seis':6})
print(d1)


#Verifica se o dicionario possui as seguintes chaves
print('A chave"dois" está no dicionario?','dois' in d1)
print('A chave"cinco" está no dicionario?','cinco' in d1
)
#remove o elemento
d1.pop('seis')
print(d1)

#Interação sobre os dicionarios

d1={'zero':0,'um':1,'dois':2,'tres':3,'quatro':4}

#intera sobre as chaves
for key in d1:		#Pode usar assim ou 
	if key=='tres':
	  print('Chave Tres encontrada!')

for key in d1.keys():	#Pode usar assim
	if key=='dez':
	  print('Chave dez encontrada!')

#intera sobre os valores
soma=0
for value in d1.values():
	soma=soma+value
print('soma dos valores do dicionario',soma)

#intera dobre os itens
for key,value in d1.items():
	print(key,value)


