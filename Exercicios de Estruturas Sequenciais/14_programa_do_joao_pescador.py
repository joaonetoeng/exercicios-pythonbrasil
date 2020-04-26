print('')
print('--- Programa do Joao Pescador ---')

peso = float(input('João, quantos quilos você trouxe = '))
excesso  = peso - 50
multa = excesso * 4

if __name__ == '__main__':
    print(f'João, você trouxe ', peso, 'quilos, excedendo', excesso, 'quilos do limite regulamentado.')
    print(f'Você deve pagar uma multa de R$', multa, 'Reais')