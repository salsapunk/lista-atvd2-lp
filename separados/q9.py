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