print('')
print('--- Calcula o salário liquido no mês --- ')

ganho_por_hora = float(input('Quanto você ganha por hora (R$) ? = '))
horas_trabalhadas = int(input('Quantas horas você trabalhou este mês ? = '))
salario_bruto = ganho_por_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

if __name__ == '__main__':
    print('')
    print(f'=> Salário Bruto = R$', salario_bruto,'reais')
    print(f'=> Imposto de Renda (11%) = R$', ir,'reais')
    print(f'=> INSS (8%) = R$', inss,'reais')
    print(f'=> Sindicato (5%) = R$', sindicato,'reais')
    print(f'=> Salário Líquido = R$', salario_liquido,'reais')