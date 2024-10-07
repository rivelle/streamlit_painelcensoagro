def formatar_numeros(value, sufix=''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{value} {unit} {sufix}'
        value /= 1000
    return f'{value} milhões {sufix}'   

