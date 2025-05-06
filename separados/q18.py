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