#Modulos:Uma serie de declarações de variaveis e funções . Conjunto com funções úteis que ficam seradas.Podem ser modulos feitos por você 
#ou de uma biblioteca publica. É UM ARQUIVO

#Criação de bodulos( arquivo com nome de areas.py):

#defina o valor de PI

PI=3.141592

from datetime import areas

#Calcula a área do quadrado
def quadrado(l2):
	return 1**2

#Calcula a área do triangulo
def triangulo(b,h):
	return(b*h)/2

#Calcula a area do circulo
def circulo(r):
	return PI*(r**2)

#Calcula a area do elipse
def elipse(a,b):
	return PI*a*b

#calcula a area de um trapezio
def trapezio(B,b,h):
	return(B+b)*h/2

#Importar modulo feito

import areas # aqui importa o modulo todo

areas.triangulo(5,8) 

#

from areas import triangulo # aqui só importa uma função do modulo

triangulo(5,8)

#
from areas import * #importa tudo, porem pode dar confusão quando tiver importando  mais de um modulo
quadrado(6)

#
import areas as ar # para deixar o nome menor na hora de puxar o código 
ar.triangulo(5,10).


#Importar modulos de bibliotecas nativas do python. Oferecem mais de 150 modulos prontos

#collectons:Estruturas de dados com diferentes funcionalidades

#csv:Manipulação de arquivos csv

#datetime:Manipulação de datas e timestamps
from datetime import datetime,timedelta
print('Datetime atuals:',datetime.now())

#json:Manipulação de arquivos json

#math:Funções matemáticas
import math
print('Função cosseno:',math.cons(100))

#intertools - serve para criar sequuencias elaboradas
import intertools
print(list(intertools.combinations('ABCD,3'))) #Quantas combinações da letra existem
print(list(intertools.permutations(['a','b','c'],2)))

#multiprocessing: possibilida o processamento paralelo

#os: Funções de interação com o sistema operacional
import os
os.mkdir('Abacaxi') # Criar uma pasta no sistema

#randon:Geração de dados aleatórios
import random
print('numero aleatorio entre 0 e 1:'random.random())
print('Inteiro aleatorio entre 50 e 100:',random.randint(50,100))

#sys:Funções e parametros específicos do sistema

#Como instalar e importar modulos disponiveis pela comunidade
#pypi é o repositório oficial Python. 

!pip install coloroma

from colorama import Fore,Back,Style
print('Texto normal')
print(Fore.BLUE + ' Texto em azul')
print(Black.BLUE + Fore.WHITE+'Texto em branco com o fundo azul')
print(Style.RESET_ALL+'Texto normal novamente')