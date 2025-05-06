nome = input('Digite o nome do aluno: ')
n1, n2, n3, n4 = map(int, input('Digite as quatro notas separadas por espaço: ').split())
media = (n1+n2+n3+n4)/4
if media >= 7:
    print(f'O aluno {nome} foi aprovado!')
else: 
    print(f'O aluno {nome} foi reprovado!')