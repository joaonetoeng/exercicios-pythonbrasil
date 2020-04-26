print('----- Programa que converte metros para centimetros -----')

valor_em_metro = float(input('Digite o valor em metros: '))
conversao = valor_em_metro * 100

if __name__ == '__main__':
    print(f'Valor convertido para centímetros: ', conversao, 'cm')