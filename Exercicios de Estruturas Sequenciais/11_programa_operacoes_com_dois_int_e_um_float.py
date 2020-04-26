print('')
print('--- Programa de operações com dois numeros inteiros e um real ---')

num1_inteiro = int(input('Digite um numero inteiro = '))
num2_inteiro = int(input('Digite outro numero inteiro = '))
num3_float = float(input('Agora digite um numero real = '))

operacao1 = (num1_inteiro * 2) * (num2_inteiro/2)
operacao2 = (num1_inteiro * 3) + num3_float
operacao3 = num3_float ** 3

if __name__ == '__main__':
    print('')
    print(f'Produto do dobro do primeiro com metade do segundo = ', operacao1)
    print(f'Soma do triplo do primeiro com o terceiro = ', operacao2)
    print(f'Terceiro elevado ao cubo. = ', operacao3)