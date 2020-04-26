print('')
print('--- Programa Loja de Tintas 2 --- ')

# dados da tinta
metros_por_litro = 6

# opção por lata
litros_por_lata = 18
rendimento_por_lata = metros_por_litro * litros_por_lata
preco_da_lata = 80

#opção por galao
litros_por_galao = 3.6
rendimento_por_galao = metros_por_litro * litros_por_galao
preco_do_galao = 25

area_a_ser_pintada = int(input('Quantos metros a ser pintado = '))

import math
total_de_latas = math.ceil(area_a_ser_pintada / rendimento_por_lata)
total_de_galoes = math.ceil(area_a_ser_pintada / rendimento_por_galao)
total_a_pagar_latas = total_de_latas * preco_da_lata
total_a_pagar_galoes = total_de_galoes * preco_do_galao

#opção lata e galao
total_de_latas_inteiras = math.floor(area_a_ser_pintada / rendimento_por_lata)
sobra = area_a_ser_pintada - total_de_latas_inteiras * rendimento_por_lata
total_de_galoes_inteiros = math.ceil(sobra / rendimento_por_galao)
total_latas_e_galoes_juntos = (total_de_latas_inteiras * preco_da_lata + total_de_galoes_inteiros + preco_do_galao)


if __name__ == '__main__':
    print(f'Opção em Lata = Quantidade de latas:', total_de_latas, ', Custo de R$', total_a_pagar_latas, 'reais')
    print(f'Opção em Galão = Quantidade de galões:', total_de_galoes, ', Custo de R$', total_a_pagar_galoes, 'reais')
    print(f'Opção em Lata e Galão = ', total_de_latas_inteiras, ' latas e ',total_de_galoes_inteiros, ' galoes. Custo de R$', total_latas_e_galoes_juntos, 'reais')