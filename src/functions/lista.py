def estaEnRango(valor, minimo, maximo):
    """
    Verifica si un valor está dentro de un rango específico [minimo, maximo].

    Parámetros:
    valor: El valor a verificar.
    minimo: El límite inferior del rango.
    maximo: El límite superior del rango.

    Retorna:
    bool: True si el valor está dentro del rango, False en caso contrario.
    """
    return minimo <= valor <= maximo

def estaEnLista(valor, lista):
    """
    Verifica si un elemento está presente en una lista.

    Parámetros:
    valor: El elemento a buscar en la lista.
    lista: La lista en la que se buscará el elemento.

    Retorna:
    bool: True si el valor está en la lista, False en caso contrario.
    """
    return valor in lista


def programa_lista():
    """
    Programa principal que solicita al usuario un número entre 1 y 20,
    """
    lista_numeros = [6, 14, 11, 3, 2, 1, 15, 19]
    
    try:
        numero_usuario = int(input("Introduce un número del 1 al 20: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        return

    if not estaEnRango(numero_usuario, 1, 20):
        print("El número no está en el rango de 1 a 20.")
        return

    if estaEnLista(numero_usuario, lista_numeros):
        print(f"El número {numero_usuario} está en la lista.")
    else:
        print(f"El número {numero_usuario} no está en la lista.")

if __name__ == "__main__":
    programa_lista()

