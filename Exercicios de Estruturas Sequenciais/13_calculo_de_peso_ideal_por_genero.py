print('')
print('--- Algoritmo que calcula o peso ideal de uma pessoa por genero ---')

altura = float(input('Qual a sua altura (m) = '))
peso_ideal_m = round((72.7 * altura) - 58, 3)
peso_ideal_f = round((62.1 * altura) - 44.7, 3)


if __name__ == '__main__':
    print(f'Se voce é mulher, seu peso ideal é ', peso_ideal_f, 'Kg. Agora se você é homem, seu peso ideal é ', peso_ideal_m, 'Kg')
