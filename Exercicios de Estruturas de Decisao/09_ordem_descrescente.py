print('')
print('--- Tres numeros em ordem descrescente ---')

n1 = input('Qual é o valor do primeiro =')
n2 = input('Qual é o valor do segundo =')
n3 = input('Qual é o valor do terceiro =')
print('')
print(' Ordem Decrescente:')

if (n1 >= n2) and (n1 >= n3):
    print(n1)
    if (n2 >= n3):
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)

elif (n2 >= n3):
    print(n2)
    if (n1 >= n3):
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)

else:
    print(n3)
    if (n1 >= n2):
        print(n1)
        print(n2)
    else:
        print(n2)
        print(n1)

'''
if (num1 >= num2) and (num1 >= num3):
    print num1
    if (num2 >= num3):
        print num2
        print num3
    else:
        print num3
        print num2
elif (num2 >= num3):
    print num2
    if (num1 >= num3):
        print num1
        print num3
    else:
        print num3
        print num1
else:
    print num3
    if (num1 >= num2):
        print num1
        print num2
    else:
        print num2
        print num1
'''