print('Essa é a questão 1: \n')
print('Algoritmo que lê os valores A, B e C e imprime na tela a soma de A e B e mostra se a soma é maior que C. \n')
a, b, c = map(int, input('Digite A, B e C separados por espaço: ').split())
print(a+b)
if a+b > c:
    print('A soma de A e B é maior que C')
else:   
    print('A soma de A e B não é menor que C')


print()


print('Essa é a questão 2: \n')
print('Algoritmo que recebe um número qualquer e verifica se ele é impar ou par e positivo ou negativo. \n')
n = int(input('Digite um número que gostaria de analisar: '))
if n > 0:
    print(f'{n} é um número positivo!')
else:
    print(f'{n} é um número negativo!')
print('e')
if n%2 == 0:
    print(f'{n} é par!')
else:
    print(f'{n} é ímpar!')


print()

print('Essa é a questão 3: \n')
print('Algoritmo que lê dois valores inteiros, se os valores de A e B forem iguais, soma os valores, caso contrário ele os multiplica. \n')
a, b = map(int, input('Digite os números de A e B separados por espaço: ').split())
if a == b:
    c = a+b
    print(c)
else:
    c = a*b
    print(c)


print()


print('Essa é a questão 4: \n')
print('Algoritmo que recebe um número inteiro e imprime o seu antecessor e sucessor. \n')
n = int(input('Digite o número: '))
print(f'O antecessor de {n} é {n-1}')
print(f'O sucessor de {n} é {n+1}')


print()

print('Essa é a questão 5: \n')
print('Algoritmo queu lê o valor do salário mínimo e o salário de um usuário e calcula quantos salários mínimos o usuário ganha. \n')
s = int(input('Digite seu salário: '))
m = 1518
r = int(s/m)
print(f'Você ganha, aproximadamente, {r} salários mínimos!')


print()


print('Essa é a questão 6: \n')
print('Algoritmo que lê um valor e imprime um reajuste de 5%. \n')
v = int(input('Digite o valor que será reajustado: '))
print(f'O valor reajustado é: {v*1.05}')


print()


print('Essa é a questão 7: \n')
print('Verifica os valores lógicos de duas condições com base em 1 e 0. \n')
0 == False
1 == True
print('Digite 1, para Verdadeiro, e 0 para Falso.')
a = int(input('> '))
b = int(input('> '))
if  a == True and b == True:
    print('Ambas as condições são verdadeiras!')
elif a == False and b == False:
    print('Ambas as condições são falsas!')
else:
    print('As condições possuem valores lógicos diferentes!')


print()


print('Essa é a questão 8: \n')
print('Algoritmo que lê três valores inteiros diferentes e imprime os valores em ordem decrescente. \n')
x, y, z = map(int, input('Digite, separados por espaço, os três números que deseja ordenar: ').split())
lista = [x, y, z]
lista.sort(reverse=True)
print(lista)


print()


print('Essa é a questão 9: \n')
print('Algoritmo que calcula o IMC de uma pessoa. \n')
peso = float(input('Digite seu peso em quilos: '))
altura = float(input('Digite sua altura em centímetros: '))/100
imc = peso/(altura*altura)
imc = round(imc, 2)
if imc <= 18.5:
    print(f'Você está abaixo do peso! Seu IMC é {imc}')
elif 18.6 <= imc <=24.9:
    print(f'Você está no peso ideal! Seu IMC é {imc}')
elif 25 <= imc <= 29.9:
    print(f'Você está levemente acima do peso! Seu IMC é {imc}')
elif 30 <= imc < 34.9:
    print(f'Você está com Obesidade grau 1! Seu IMC é {imc}')
elif 35 <= imc <= 39.9:
    print(f'Você está com Obesidade grau 2 (severa)! Seu IMC é {imc}')
else:
    print(f'Você está com Obesidade grau 3 (mórbida) Seu IMC é {imc}')


print()


print('Essa é a questão 10: \n')
print('Algoritmo que lê três notas obtidas pelo aluno e retorna sua média. \n')
n1, n2, n3 = map(int, input('Digite as três notas separadas por espaço: ').split())
media = (n1+n2+n3)/3
print(f'A média é: {round(media, 2)}')


print()


print('Essa é a questão 11: /n')
print('Algoritmo que lê quatro notas obtidas por um aluno, calcula a média das notas e diz se o aluno foi aprovado ou não. \n')
nome = input('Digite o nome do aluno: ')
n1, n2, n3, n4 = map(int, input('Digite as quatro notas separadas por espaço: ').split())
media = (n1+n2+n3+n4)/4
if media >= 7:
    print(f'O aluno {nome} foi aprovado!')
else: 
    print(f'O aluno {nome} foi reprovado!')


print()


print('Essa é a questão 12: \n')
print('Algoritmo que lê o valor de um produto e determina o valor que deve ser pago, conforme a escolha da forma de pagamento pelo comprador e imprime na tela o valor final do produto a ser pago. \n')
valor = int(input('Digite o valor do produto a ser comprado: '))
pagamento = int(input('Escolha o método de pagamento com base nos descontos: \n' \
'1. À Vista em Dinheiro ou Pix, receba 15% de desconto. \n' \
'2. À Vista em Cartão de Crédito, receba 10% de desconto. \n' \
'3. Parcelando no cartão em duas vezes, preço normal sem juros. \n' \
'4. Parcelando no cartão três vezes ou mais, preço normal do produto mais juros de 10%. \n'
'> '))
match pagamento:
    case 1:
        valor_final = valor - (valor*0.15)
        print(f'O valor final é {valor_final}')
    case 2:
        valor_final = valor - (valor*0.1)
        print(f'O valor final é {valor_final}')
    case 3:
        print(f'O valor final é {valor}')
    case 4:
        valor_final = round(valor*1.1)
        print(f'O valor final é {valor_final}')


print()


print('Essa é a questão 13: \n')
print('Algoritmo que verifica se uma pessoa é maior ou menor de idade. \n')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if idade < 18:
    print(f'{nome}, você é menor de idade!')
else:
    print(f'{nome}, você é maior de idade!')


print()


print('Essa é a questão 14: \n')
print('Algoritmo que recebe valor A e B e troca A por B e o valor de B por A. \n')
A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
A, B = B, A
print(f'O novo valor de A é {A} e o novo valor de B é {B}')


print()


print('Essa é a questão 15: \n')
print('Algoritmo que lê o ano em que uma pessoa nasceu e imprime na tela quantos anos, meses e dias essa pessoa já viveu (Ano = 365d, Mês = 30). \n')
print('Não consegui fazer')                                                                                                                           


print()

print('Essa é a questão 16: \n')
print('Algoritmo que lê três valores que representam os três lados de um triângulo e verifica se são válidos, determinando se o triângulo é equilátero, isósceles ou escaleno.')
a, b, c = map(int, input('Digite, separado por espaços, o valor dos lados de um triângulo: ').split())
if a + b > c and a + c > b and b + c > a:
    print('o triângulo é válido')
    if a == b != c or a == c != b or b == c != a:
        print('O triângulo é isósceles!')
    elif a == b == c:
        print('O triângulo é equilátero!')
    elif a != b != c:
        print('O triângulo é escaleno!')
    elif a + b == c or a + c == b or b + c == a:
        print('O triângulo é inválido')
else:
    print('O triângulo não é válido!')


print()


print('Essa é a questão 17: \n')
print('Algoritmo que lê uma temperatura em Fahrenheit e calcula a temperatura correspondente em Celsius.')
F = int(input('Digite a temperatura em Fahreinheit que deseja converter: '))
C = (5*(F-32)/9)
print(f'A temperatura em graus Celsius é {C}')


print()


print('Essa é a questão 18: \n')
print('Algoritmo que calcula quantos anos serão necessários para Sara ser maior que Francisco.')
altura_francisco = 1.50
print(f'A altura de Francisco é {altura_francisco}')
f_cresce = 0.02
altura_sara = 1.10
print(f'A altura de Sara é {altura_sara}')
s_cresce = 0.03
ano = 0
while altura_sara < altura_francisco:
    ano = ano + 1
    altura_sara = round(altura_sara + s_cresce, 2)
    altura_francisco = round(altura_francisco + f_cresce, 2)
print(f'Em {ano} anos, Sara será mais alta que Francisco!')


print()


print('Essa é a questão 19: \n')
print('Algoritmo que imprime a tabuada de 1 a 10.')
i = 1
y = 1
while i < 11:
    print(f'Tabuada de {i}')
    print(f'{i}* 1 = {i*1}')
    print(f'{i}* 2 = {i*2}')
    print(f'{i}* 3 = {i*3}')
    print(f'{i}* 4 = {i*4}')
    print(f'{i}* 5 = {i*5}')
    print(f'{i}* 6 = {i*6}')
    print(f'{i}* 7 = {i*7}')
    print(f'{i}* 8 = {i*8}')
    print(f'{i}* 9 = {i*9}')
    print(f'{i}* 10 = {i*10}')
    print()
    i = i + 1


print()


print('Essa é a questão 20: \n')
print('Algoritmo que recebe um valor inteiro e imprime na tela a sua tabuada.')
n = int(input('Digite um número para receber sua tabuada: '))
print(f'Tabuada de {n}')
print(f'{n}* 1 = {n*1}')
print(f'{n}* 2 = {n*2}')
print(f'{n}* 3 = {n*3}')
print(f'{n}* 4 = {n*4}')
print(f'{n}* 5 = {n*5}')
print(f'{n}* 6 = {n*6}')
print(f'{n}* 7 = {n*7}')
print(f'{n}* 8 = {n*8}')
print(f'{n}* 9 = {n*9}')
print(f'{n}* 10 = {n*10}')