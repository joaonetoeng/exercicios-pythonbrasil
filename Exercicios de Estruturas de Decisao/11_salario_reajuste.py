print('')
print('--- Reajuste de salario de colaboradores ---')

salario = float(input('Digite o valor do salario que deve ser reajustado ='))

print(f'Salário atual = R$ {salario} reais')

if salario <= 280:
    print(f'Percentual de aumento = 20% ')
    aumento = salario * 0.2
    print(f'Valor de aumento = R$ {aumento} reais ')
    salario += aumento
    print(f'Salario reajustado = R$ {salario} reais')
elif 280 < salario < 700:
    print(f'Percentual de aumento = 15% ')
    aumento = salario * 0.15
    print(f'Valor de aumento = R$ {aumento} reais ')
    salario += aumento
    print(f'Salario reajustado = R$ {salario} reais')
elif 700 < salario <= 1500:
    print(f'Percentual de aumento = 10% ')
    aumento = salario * 0.1
    print(f'Valor de aumento = R$ {aumento} reais ')
    salario += aumento
    print(f'Salario reajustado = R$ {salario} reais')
elif salario > 1500:
    print(f'Percentual de aumento = 5% ')
    aumento = salario * 0.05
    print(f'Valor de aumento = R$ {aumento} reais ')
    salario += aumento
    print(f'Salario reajustado = R$ {salario} reais')
