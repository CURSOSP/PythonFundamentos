

INICIO_VISA = ['4']
INICIO_MASTERCARD = ['51','52','53','54','55']
INICIO_AMEX = ['34','37']


def algoritmo_luhn(tarjeta :str):
    # paso1
    tarjeta_invertida =  tarjeta[::-1]
    lista_impares = []
    lista_pares = []
    for i, n in enumerate(tarjeta_invertida):
        if i % 2==1:
            lista_impares.append(int(n) * 2)
            continue
        lista_pares.append(int(n))
    
    # paso2:
    suma_d = 0
    for e in lista_impares:
        if e // 10 == 0:
            suma_d += e
        else:
            suma_d += e // 10
            suma_d += e % 10
    suma_d += sum(lista_pares)
    # Paso3 : Validar que último digito de suma sea '0'
    if suma_d % 10==0:
        return True
    else:
        return False


# 1. Solicitar numero de tarjeta
tarjeta = input('Introduce tu numero de tarjeta: ')

# 2. Validar tarjeta
tarjeta_es_valida = algoritmo_luhn(tarjeta)
# 3. Categorizar la tarjeta

if tarjeta_es_valida:
    longitud = len(tarjeta)
    
    # criterios para verificar tarjeta
    if longitud == 15 and tarjeta[:2] in INICIO_AMEX:
        print('AMEX')
    elif longitud == 16 and tarjeta[:2] in INICIO_MASTERCARD:
        print('MASTERCARD')
    elif longitud in [*range(13,17)] and tarjeta[0] in INICIO_VISA:
        print('VISA')
    else:
        print('INVALID')
else:
    print('INVALID')
    
