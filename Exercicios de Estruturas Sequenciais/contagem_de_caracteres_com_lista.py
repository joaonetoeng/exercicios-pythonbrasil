def contar_carateres(s):
    """ Funcao que conta os caracteres de uma string
    Ex.:
    >>> contar_carateres('joao')
    o: 2
    a: 1
    j: 1

    >>> contar_carateres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada
    """

    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior} : {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior} : {contagem}')


if __name__ == '__main__':
    contar_carateres('joao')
    print('')
    contar_carateres('banana')