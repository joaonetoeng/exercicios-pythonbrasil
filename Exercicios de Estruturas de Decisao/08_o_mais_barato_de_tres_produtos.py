print('')
print('--- O mais barato de tres produtos ---')

celular = input('Qual é o valor do celular que você quer comprar? =')
notebook = input('Qual é o valor do notebook que você quer comprar? =')
tablet = input('Qual é o valor do tablet que você quer comprar? =')

if (celular < notebook) and (celular < tablet):
    print(f'Você deve comprar o celular porque está mais barato! (valor: R$ {celular} reais)')
elif (notebook < tablet) and (notebook < celular):
    print(f'Você deve comprar o notebook porque está mais barato! (valor: R$ {notebook} reais)')
else:
    print(f'Você deve comprar o tablet porque está mais barato! (valor: R$ {tablet} reais)')