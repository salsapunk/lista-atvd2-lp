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