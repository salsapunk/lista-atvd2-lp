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