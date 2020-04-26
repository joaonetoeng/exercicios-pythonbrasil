print('')
print('--- Calcula e mostra o total do seu salário no referido mês --- ')

ganho_por_hora = float(input('Quanto você ganha por hora (R$) ? = '))
horas_trabalhadas = int(input('Quantas horas você trabalhou este mês ? = '))
salario = ganho_por_hora * horas_trabalhadas

if __name__ == '__main__':
    print(f'Salário =', salario, 'reais')
