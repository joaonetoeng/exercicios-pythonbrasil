print('')
print('--- Media de aluno, com conceito de A à E  ---')


nota1 = float(input('Qual a primeira nota (0 à 10): '))
nota2 = float(input('Qual a segunda nota (0 à 10): '))
media = (nota1 + nota2)/2

print('')
print(f'Nota do Aluno = {media}')

if 9 <= media <= 10:
    status = True
    print('Conceito : A')
elif 7.5 <= media < 9:
    status = True
    print('Conceito : B')
elif 6 <= media < 7.5:
    status = True
    print('Conceito : C')
elif 4 <= media <6:
    status = False
    print('Conceito : D')
else:
    status = False
    print('Conceito : E')

if status:
    print('Aprovado !')
else:
    print('Reprovado !')