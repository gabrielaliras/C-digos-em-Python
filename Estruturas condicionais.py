#Estruturas condicionais 

#Condicional If:Se for verdadeiro executa o comando,mas se não for termina o código
idade=32
if idade>=18:
    print('Idade suficiente para a CNH')
else:
    print('Idade insuficiente para CNH')
#
idade2=15
if idade2>=18:
    print("Idade2 Suficiente para a CNH")
else:
    print('idade insuficiente para a CNH')
#
idade3=64
tempo_contribuicao=34
if idade>= 65 or tempo_contribuicao >=35:
    print('Habilidado para solicitar aposentadoria')
else:
    print('Inapto para aposentadoria')
#
idade4=65
tempo_contribuicao1=35
if idade4>= 65 and tempo_contribuicao1 >=35:
    print('Habilidado para solicitar aposentadoria')
else:
    print('Inapto para aposentadoria')

#
idade5=64
tempo_contribuicao2=30
if idade5>=65:
    print("Aposentadoria por idade")
else:
    if tempo_contribuicao2>=35:
        print('Aposentadoria por tempo de contribuicao')
    else:
        print('Inapto para aposentadoria')


#elif

idade6 =22
if idade6<12:
    faixa_etaria='Criança'
elif idade6<18:
    faixa_etaria='Adolecente'
elif idade6<60:
    faixa_etaria='Adulto'
else:
    faixa_etaria='Idoso'
print('A faixa Etaria é',faixa_etaria)

#Capitulo 5 Estrutura de dados

#Cria as variaveis com idade
p1=27
p2=49
p3=2
#verifica qual a maior idade
if p1>=p2:
    if p1>=p3:
        print('Maior idade é:',p1)
elif p2>=p3:
    print('A maior idade é:',p2)
else:
    print('A maior idade é:',p3)

