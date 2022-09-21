def buscar_repetidos(list):
    diccionario = {}
    for i in list:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    return diccionario
