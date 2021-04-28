print('Olá mundo!')
nome = str(input('Qual o seu nome?'))
print(f'É um prazer te conhecer,{nome}!')
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
print(f'A soma de {n1} e {n2} é igual à {n1 + n2}')
a = input('Digite algo:')
print('O time primitivo é', type(a))
print(f'Está em maiúsculo?', a.isupper())
print(f'É um número?', a.isalnum())
num = int(input('Digite um número:'))
print(f'O número digitado tem como antecessor {num - 1} e como sucessor {num + 1}')
from math import sqrt
n = int(input('Digite um número:'))
print(f"O dobro desse número é {n * 2} o triplo é {n * 3} e a raiz quadrada {sqrt(n)}")
not1 = float(input('Digite a primeira nota:'))
not2 = float(input('Digite a segunda nota:'))
m = (not1 + not2) / 2
print(f'O aluno tirou {not1} e {not2} e sua média foi {m}.')
if m > 7:
    print('Parabéns, você está aprovado!')
elif m >= 5:
    print('Você está na final, estude para as provas!')
else:
    print('Você não alcançou a média mínima e foi ligeiramente reprovado!')
m = int(input('Digite uma distância em metros:'))
print(f'{m} equivalem à:\n'
      f'{m / 1000} quilômetros.\n'
      f'{m / 100} hectômetros.\n'
      f'{m / 10} decâmetros.\n'
      f'{m * 10} decímetros.\n'
      f'{m * 100} centímetros.\n'
      f'{m * 1000} milímetros!\n')
tab = int(input('Digite um número para saber sua tabuada:'))
print(f'A tabuada do {tab} é\n 1x{tab} = {tab * 1}\n 2x{tab} = {tab * 2}\n '
      f'3x{tab} = {tab * 3}\n 4x{tab} = {tab * 4}\n 5x{tab} = {tab * 5}\n '
      f'6x{tab} = {tab * 6}\n 7x{tab} = {tab * 7}\n 8x{tab} = {tab * 8}\n '
      f'9x{tab} = {tab * 9}\n 10x{tab} = {tab * 10}')
real = int(input('Quantos reais você tem? R$:'))
print(f'Convertendo R${real:.2f}, você terá U${real / 5.45:.2f}.')
ação = str(input('Deseja prosseguir? ')[0]).upper()
if ação == 'S':
    print('Fazendo a conversão, um instante..')
    from time import sleep
    sleep(4)
    print('Conversão concluída, não retire o cartão!')
    sleep(4)
    print('Pode retirar o cartão!')
    sleep(1)
else:
    print('Ok, qualquer coisa estaremos aqui!')
print('Desejamos um ótimo dia!')
from time import sleep

lar = float(input('Largura da parede em m:'))
alt = float(input('Altura da parede em m:'))
a = lar * alt
p = a / 2
print(f'As dimensões de sua parede é {lar}x{alt}, e sua área é {a:.2f}/m²')
sleep(1)
print('Calculando a quantidade de tinta a ser usada na pintura...')
sleep(3)
print(f'Para pintar sua parede, serão necessários {p:.2f} litros de tinta.')
