a, b = map(int, input('Digite os números de A e B separados por espaço: ').split())
if a == b:
    c = a+b
    print(c)
else:
    c = a*b
    print(c)