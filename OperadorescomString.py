#Operadores com String
palavra='Luiz Felipe'
#Indices positivos
print('Primeiro caractere', palavra[0])
print('Segundo caractere', palavra[1])
#Indices negativos
print('Ultimo caractere', palavra[-1])
print('Penultimo caractere', palavra[-2])
#Acesso de mais de uma letra dentro do caractere
print(palavra[5:7])
#operadores de filiação(pertencimento): se uma palavra está dentro de outra
s1='Luiz Felipe'
s2='Felipe'
print(s1 in s2)
print(s2 in s1)
print('Luc'in s1)
print('Luc' not in s2)

#ver o tamanho da palavra: Funcao len
print(len(s1))

#Metodos: Funcoes embutidas no tipo:
print(s1.upper())#todas maiusculas
print(s1.lower())#todas minusculas
print(s1.title())#primeira letra de cada palavra maiuscula
print(s1.replace('Felipe','Aoki'))# Substitui a palavra
print(s1.startswith('Amor'))#verifica se a string comeca com amor
print(s1.endswith('Amor'))#verifica se a string termina com amor
print(s1.find('Amor'))#retorna o indice da primeira ocorrencia da palavra amor
print(s1.split())#particiona a string em outras , que sao separadas por espaco
print(s1.split(','))#particiona a string em outras ,separadas por ','
s3='Gabriela'
print(s3.strip())#remove espacos extras no inicio e fim da string
