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