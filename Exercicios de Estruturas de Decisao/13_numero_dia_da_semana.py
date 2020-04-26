print('')
print('--- Indicar o dia da semana apartir de um numero  ---')

numero_do_dia = int(input('Digite um numero, para saber o dia correspondente da semana = '))

if numero_do_dia == 1:
    print('Domingo')
elif numero_do_dia == 2:
    print('Segunda')
elif numero_do_dia == 3:
    print('Terça')
elif numero_do_dia == 4:
    print('Quarta')
elif numero_do_dia == 5:
    print('Quinta')
elif numero_do_dia == 6:
    print('Sexta')
elif numero_do_dia == 7:
    print('Sábado')
else:
    print('Valor inválido. Digite um numero de 1 a 7! ')