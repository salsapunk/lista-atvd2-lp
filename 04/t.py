from datetime import date
data_atual = date.today()

dia_nascimento, mes_nascimento, ano_nascimento = map(int, input('Digite sua data de nascimento separado por espaços: ').split())

dia_atual = data_atual.day
mes_atual = data_atual.month
ano_atual = data_atual.year

ano_dias = 365
mes_dias = 30
ano_meses = 12

diferenca_anos = ano_atual - ano_nascimento

if mes_atual < mes_nascimento:
    diferenca_anos = diferenca_anos - 1

diferenca_meses = abs(mes_atual - mes_nascimento)
meses_vividos = (diferenca_anos*ano_meses) 

if mes_atual > mes_nascimento:
    meses_vividos = meses_vividos + abs(mes_nascimento - mes_atual)

dias_vividos = (diferenca_anos*ano_dias)+(diferenca_meses*mes_dias)

print(diferenca_anos, meses_vividos, dias_vividos)

#18 219 