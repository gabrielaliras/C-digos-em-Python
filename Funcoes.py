#Funções-Reutilização de códigos.Ex: print()- exibição;range()-gera sequencia de inteiros;len()-retorna o 
#tamanho de uma sequencia

#Criando funções- sintaxe: a palavra def define o inicio da declaração da funcao
#def nome_da_funcao(argumento1,argumento2):
#	<bloco de codigo a ser executado>
#	return resultado

#criando uma lista para somar
l1=[1,2,3,4,5]
l2=[3,1,5,9,0,8,2,3,4]
l3=[12,43,23,12,789]

#criando a função
def soma_lista(lista):
	soma=0
	for item in lista:
		soma=soma+item
	return soma

#chama a função na lista
soma_l1=soma_lista(l1)
print(soma_l1)
soma_l2=soma_lista(l2)
print(soma_l2)
soma_l3=soma_lista(l3)
print(soma_l3)

#Exibe a mensagem de boas vindas a uma pessoa
def boas_vindas(nome):
	print(f' Olá {nome}. Seja Bem vinda!' )

#Chamando a função
boas_vindas('Luiz Felipe')


#Calcula a área de um quadrado:1x1
def area_quadrado(lado):
	return lado*lado

#Chamando a função
print(area_quadrado(4))
print(area_quadrado(10))


#Calcula a área de um triangulo:(bxh)/2
def area_triangulo(base,altura):
	return(base*altura)/2

#Chamando a função
print(area_triangulo(5,2))
print(area_triangulo(4,5))

#realiza uma divisão.Se o divisor é zero,retorna uma mensagem de erro
def div(dividendo,divisor):
	if divisor==0:
		print('Erro :Divisor igual a zero!')
		return
	return dividendo/divisor

#Função similar a função div,mas que retorna o dividendo e o resto da divisão
def div_qr(dividendo,divisor):
	if divisor==0:
		print('Erro:Divisor igual a zero')
		return
	quociente=dividendo//divisor
	resto=dividendo%divisor
	return(quociente,resto)

print('div(10,4)==>',div(10,4))# dividendo=10 e divisor=4

print('div_qr(10,4)==>',div_qr(10,4)) #Dividendo=10 e divisor=4


#Verifica se é um divisor inválido(divisor==0)
def divisor_invalido(divisor):
	if divisor==0:
		print('erro:divisor é zero!')
		return True
	return False


#Retorna o resultado da divisão
def div(dividendo,divisor):
	if divisor_invalido(divisor):
		return
	return dividendo/divisor


#Retorna o quociente e o resto de uma divisão
def div_qr(dividendo,divisor):
	if divisor_invalido (divisor):
		return
	quociente=dividendo//divisor
	resto=dividendo % divisor
	return(quociente,resto)

div(10,0)
div(10,4)
div_qr(10,0)
div_qr(10,4)


#Argumentos das funções #

#calcula a area de um triangulo(bxh)/2

def area_triangulo(base,altura):
	return(base*altura)/2

print(area_triangulo(5,10))
print(area_triangulo(altura=10,base=5))
#print(area_triangulo(8)) #da um erro porque nao passou altura e base

#Argumentos padrao (default)

def exibe_pessoa(nome,idade=30):
	print(f'Meu nome é {nome} e tenho  {idade} anos.')

exibe_pessoa('Antonio')
exibe_pessoa('Antonio',36)