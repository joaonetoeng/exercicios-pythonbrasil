print('')
print('--- Folha de pagamento de uma empresa --- ')

ganho_por_hora = float(input('Quanto você ganha por hora (R$) ? = '))
horas_trabalhadas = int(input('Quantas horas você trabalhou este mês ? = '))
salario = ganho_por_hora * horas_trabalhadas
inss = 0.1
fgts = 0.11
sindicato = salario * 0.03

print(' ------------------------------------- ')
print(f'Salário Bruto = R$ {salario} reais')
print(' ------------------------------------- ')
if salario < 900:
    inss *= salario
    fgts *= salario
    descontos = inss
    salario_liquido = salario - descontos

elif 900 < salario < 1500:
    inss *= salario
    fgts *= salario
    ir = 0.05 * salario
    descontos = inss + ir + sindicato
    salario_liquido = salario - descontos
    print(f'Imposto de Renda = R$ {ir} reais')

elif 1500 < salario < 2500:
    inss *= salario
    fgts *= salario
    ir = 0.1 * salario
    descontos = inss + ir + sindicato
    salario_liquido = salario - descontos
    print(f'Imposto de Renda = R$ {ir} reais')

else:
    inss *= salario
    fgts *= salario
    ir = 0.2 * salario
    descontos = inss + ir + sindicato
    salario_liquido = salario - descontos
    print(f'Imposto de Renda = R$ {ir} reais')


print(f'INSS = R$ {inss} reais')
print(f'FGTS = R$ {fgts} reais')
print(f'Descontos = R$ {descontos} reais')
print(f'Salário Liguido = R$ {salario_liquido} reais')


'''
# Solicita os dados
valorPorHora = float(raw_input('Informe o valor da hora trabalhada: '))
quantidadeHoras =\
    float(raw_input('Informe a quantidade de horas trabalhadas no mes:'))

# Calcula o salario bruto
salarioBruto = valorPorHora * quantidadeHoras

# Calcula o imposto de renda
if (salarioBruto > 2500):
    aliquotaIR = 20
elif (salarioBruto > 1500):
    aliquotaIR = 10
elif (salarioBruto > 900):
    aliquotaIR = 5
else:
    aliquotaIR = 0

valorIR = salarioBruto * (aliquotaIR / 100.0)

# Calcula o valor para o sindicato
valorSindicato = salarioBruto * (3 / 100.0)

# Calcula o total de descontos
totalDescontos = valorIR + valorSindicato

# Calcula o valor do FGTS
valorFGTS = salarioBruto * (11 / 100.0)

# Calcula o salario liquido
salarioLiquido = salarioBruto - totalDescontos

# Imprime o resultado
print 'Salario Bruto: (', valorPorHora, '*', quantidadeHoras, '): R$',\
    salarioBruto
print '(-) IR (', aliquotaIR, '%): R$', valorIR
print '(-) Sindicato ( 3 %): R$', valorSindicato
print 'FGTS ( 11 %): R$', valorFGTS
print 'Total de Descontos: R$', totalDescontos
print 'Salario Liquido: R$', salarioLiquido
'''