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