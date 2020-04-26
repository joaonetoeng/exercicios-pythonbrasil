from math import sqrt


print('')
print('--- Programa para calcular equação do segundo grau  ---')
print('')
print('--- Equação tem a seguinte forma: Ax**2 + Bx + C  ---')
print('')
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
print('')

if a == 0:
    print('A equação não é de segundo grau!')
else:
    delta = b ** 2 - 4 * a * c
    print(f'Delta = {delta}')
    if delta < 0:
        print('A equação não possui raízes reais !')
    elif delta == 0:
        x1 = (-b + sqrt(delta) / (2*a))
        print(f'A equação possui apenas 1 raíz = x = {x1}')
    elif delta > 0:
        x1 = (-(b) + sqrt(delta)) / (2*a)
        x2 = (-(b) - sqrt(delta)) / (2*a)
        print(f'A equação possui apenas 2 raízes = {x1,x2}')
    else:
        print('Dados inválidos !')





