#Estruturas de Repetição
#While:Enquanto a expressão for verdadeira,o bloco será repetido

numero_repeticoes=15# faz o controle da estrutura de repetição
while numero_repeticoes>0:
    print(numero_repeticoes,'Meu nome é Gabriela Lira')
    numero_repeticoes=numero_repeticoes-1 #Vai contando e tirando uma repetição até chegar em 15
print('Fim do programa')

n=15 
soma=0
contador=0

while contador<=n:
    soma=soma+contador
    contador=contador+1

print(f'A soma dos primeiros numeros{n} inteiros é a{soma} ')

num=16
soma1=0
while num>=0:
    soma1=soma1+num
    num=num-1
print(f'A soma  dos numeros inteiros é{soma1}')


#for_in: O for ele percorre uma sequencia e executa todos os códigos
numero='4589'
soma3=0
for c in numero:
    print(c)
    soma3=soma3+int(c)
print(f'O resultado é {soma3}')

g='Meu casamento está chegando'
contadorg_A=0
contadorg_B=0

for letra in g:
    if letra=='a':
        contadorg_A=contadorg_A+1
    if letra=='e':
        contadorg_B=contadorg_B+1
print(f'A frase {g} possui  {contadorg_A} letras"a" e {contadorg_B} letras "b"')

#Função range( inicio,fim,incremento)
s=15
som=0

for nume in range(s+1):
    som=som+nume
print(f'A soma dos primeiros {s} inteiros é {som}')

#Interrupcao da estrutura de repeticao

#Realiza a busca da faixa divisivel por 21 de 250 a 300

for numero6 in range(250,301):
    #verifica se o numero é divisivel por 21
    if numero6%21==0:
        print('Numero encontrado:',numero6)
        #se for divisivel por 21,interrompa a busca, se não colocar o break ele continua buscando po proximo numero
        break