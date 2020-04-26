def contar_carateres(s):
    """ Funcao que conta os caracteres de uma string
    Ex.:
    >>> contar_carateres('joao')
    { 'o': 2, 'a': 1, 'j': 1 }

    >>> contar_carateres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada
    """

    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado


if __name__ == '__main__':
    print(contar_carateres('joao'))
    print('')
    print(contar_carateres('banana'))