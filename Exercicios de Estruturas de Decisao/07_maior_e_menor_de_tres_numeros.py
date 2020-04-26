print('')
print('--- Maior de tres numeros ---')

num1 = float(input('Digite um numero ='))
num2 = float(input('Digite o segundo numero ='))
num3 = float(input('Digite o terceiro número ='))

if (num1 > num2) and (num1 > num3):
    print(f'O numero maior é : ', num1)
elif (num2 > num3) and (num2 > num1):
    print(f'O numero maior é : ', num2)
else:
    print(f'O numero maior é :', num3)

if (num1 < num2) and (num1 < num3):
    print(f'O numero menor é : ', num1)
elif (num2 < num3) and (num2 < num1):
    print(f'O numero menor é : ', num2)
else:
    print(f'O numero menor é :', num3)
