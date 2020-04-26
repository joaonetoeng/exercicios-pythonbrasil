print('')
print('--- Conversor de temperatura: Farenheit para Celsius ---')

temperatura_em_farenheit = int(input('Digite a temperatura em Farenheit = '))
temperatura_em_celcius = round((5 * (temperatura_em_farenheit-32) / 9), 2)

if __name__ == '__main__':
    print(f'Temperatura em Celsius = ', temperatura_em_celcius, '°C')
