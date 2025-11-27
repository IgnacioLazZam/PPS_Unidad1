def esBinario(strbinario):
    """
    Verifica si una cadena representa un número binario válido.
    
    Parámetros:
    strbinario (str): La cadena a verificar.
    
    Retorna:
    bool: True si la cadena es un número binario válido, False en caso contrario.
    """
    for char in strbinario:
        if char not in ('0', '1'):
            return False
    return True

def programa_binario():
    """
    Programa principal que solicita al usuario una cadena y verifica si es un número binario.
    """
    cadena_usuario = input("Introduce una cadena para verificar si es un número binario: ")
    
    if esBinario(cadena_usuario):
        # Convierte de binario a decimal
        numero_decimal = int(cadena_usuario, 2)
        print(f"El número binario {cadena_usuario} en decimal es: {numero_decimal}")
    else:
        print("Error: La cadena introducida no es un número binario válido.")

if __name__ == "__main__":
    programa_binario()