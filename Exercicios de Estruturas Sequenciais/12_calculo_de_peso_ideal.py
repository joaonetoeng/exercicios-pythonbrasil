print('')
print('--- Algoritmo que calcula o peso ideal de uma pessoa ---')

altura = float(input('Qual a sua altura (m) = '))
peso_ideal = (72.7 * altura) - 58

if __name__ == '__main__':
    print(f'Seu peso ideal é : ', peso_ideal, 'Kg')
