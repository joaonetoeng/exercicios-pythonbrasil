print('')
print('--- Calculo da velocidade de um download --- ')

tamanho_arquivo = float(input('Qual é o tamanho do arquivo que precisa baixar? (MB)= '))
velocidade_da_internet = float(input('Qual a veloidade da internet em Mbps = '))

tempo_do_download_m = round((tamanho_arquivo / velocidade_da_internet) / 60)

if __name__ == '__main__':
    print(f'Tempo do download = ', tempo_do_download_m, 'minutos e alguns segundos (kkk)')

