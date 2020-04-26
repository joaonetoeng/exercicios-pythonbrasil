print('')
print('--- Calculo de notal final de um aluno e seu status ---')

nota1 = float(input('Digite a primeira nota do aluno = '))
nota2 = float(input('Digite a segunda nota do aluno = '))
media = (nota1 + nota2) / 2

print(f'Notal final = {media}')

if media == 10:
    print(f' Aprovado com Distinção !')
elif media > 7:
    print(f' Aprovado!')
else:
    print(f'Reprovado !')
