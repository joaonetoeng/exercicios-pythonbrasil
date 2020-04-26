print('-----  Calculando área de um circulo -----')

raio = float(input('Digite o raio (cm): '))
import math
PI = 3.1416
area = round(PI * raio ** 2, 3)

if __name__ == '__main__':
    print(f'Área do circulo: ', area, 'cm quadrados')