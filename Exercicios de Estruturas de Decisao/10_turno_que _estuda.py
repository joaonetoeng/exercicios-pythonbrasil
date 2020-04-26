print('')
print('--- Saudações de acordo com o turno que estuda ---')

print('')
print('Qual turno você estuda ? Digite M-matutino ou V-Vespertino ou N- Noturno')
turno = input(' Digite a letra correspondente = ')

if turno == 'M':
    print('Bom dia !!! ')
elif turno == 'V':
    print('Boa Tarde !!!')
elif turno == 'N':
    print('Boa Noite !!! ')
else:
    print('Tente novamente ! Digite uma letra válida para o Turno (M, V ou N). ')