print('')
print('--- Ano Bissexto  ---')

ano = int(input('Digite um ano, vou verificar se ele é um ano bissexto = '))

condicao1 = ano / 4
condicao2 = ano / 400

if condicao1.is_integer():
    print(f'{ano} => Ano Bissexto !')
elif condicao2.is_integer():
    print(f'{ano} => Ano Bissexto !')
else:
    print(f'{ano} => Este Ano não é Bissexto !')