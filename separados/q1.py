a, b, c = map(int, input('Digite A, B e C separados por espaço: ').split())
print(a+b)
if a+b > c:
    print('A soma de A e B é maior que C')
else:   
    print('A soma de A e B não é menor que C')