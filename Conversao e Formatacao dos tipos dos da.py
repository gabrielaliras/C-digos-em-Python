#Conversao e Formatacao dos tipos dos dados


#Convercao
nascimento=1991
ano_atual=2024
idade=ano_atual-nascimento
saida='Eu tenho'  + str(idade)+  'anos de idade'# o srt esta convertendo de inteiro para string
print(saida)

#Tipos de conversao de interiro(int) para:
print(float(10))
print(bool(-1))
print(bool(0))
print(str(999))

#Tipos de conversao de Float(float) para:
print(int(9.999))
print(bool(-0.99))
print(str(0.99))

#Tipos de conversao de Booleano(bool) para:
print(int(True))
print(str(False))
print(float(True))

#Tipos de conversao de String(str) para:
print(bool('palavra'))
print(bool(''))
print(int('-99'))
print(float('0.01'))

#Formatação ultilizando f-strings
nascimento2=1992
ano_nas=2024
idade2=ano_nas-nascimento2
print(f'Eu tenho  { idade2} anos')

#Formatacao com 
palavra2='chocolate'
print(f'A palavra {palavra2.upper()} tem {len(palavra2)} letras')

