print('')
print('--- Programa Loja de Tintas --- ')


metros_por_litro = 3
litros_por_lata = 18
rendimento_por_lata = metros_por_litro * litros_por_lata
preco_da_lata = 80

area_a_ser_pintada = int(input('Quantos metros a ser pintado = '))

import math
total_de_latas = math.ceil(area_a_ser_pintada / rendimento_por_lata)
total_a_pagar = total_de_latas * preco_da_lata

if __name__ == '__main__':
    print(f'Total de latas = ', total_de_latas)
    print(f'Total a pagar = R$ ', total_a_pagar, 'reais' )