print('')
print('--- Conversor de temperatura: Celsius para Farenheit ---')

temperatura_em_celcius = int(input('Digite a temperatura em Celsius = '))
temperatura_em_farenheit = round(((temperatura_em_celcius * 9/5) + 32), 2)


if __name__ == '__main__':
    print(f'Temperatura em Farenheit = ', temperatura_em_farenheit, '°F')
