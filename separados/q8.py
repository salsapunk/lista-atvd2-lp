x, y, z = map(int, input('Digite, separados por espaço, os três números que deseja ordenar: ').split())
lista = [x, y, z]
lista.sort(reverse=True)
print(lista)