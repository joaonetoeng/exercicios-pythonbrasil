print('')
print('--- Verificar o formato de data dd/mm/aaaa  ---')

data = input('Digite uma data (dd/mm/aaaa) = ')
print('')

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

print(f'Data = {dia}/{mes}/{ano}')
print('')

if mes in (1, 3, 5, 7, 8, 10, 12):
    if (dia >= 1) and (dia <= 31):
        print('Data válida! ')
        if mes in (4, 6, 9, 11):
            if (dia >= 1) and (dia <= 30):
                print('Data válida! ')
    else:
        print('Data Inválida !')
else:
    print('Data Inválida !')
