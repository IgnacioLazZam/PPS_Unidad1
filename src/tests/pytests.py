import pytest  # type: ignore
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.functions.binario import esBinario
from src.functions.lista import estaEnLista, estaEnRango


# Pruebas para la función estaEnRango

def test_estaEnRango():
    """Pruebas para la función estaEnRango."""
    assert estaEnRango(1, 1, 20) == True
    assert estaEnRango(10, 1, 20) == True
    assert estaEnRango(0, 1, 20) == False
    assert estaEnRango(21, 1, 20) == False


def test_estaEnRango_caso_especiales():
    """Pruebas para casos especiales de la función estaEnRango."""
    assert estaEnRango(1, 1, 1) == True
    assert estaEnRango(0, 1, 1) == False
    assert estaEnRango(2, 1, 1) == False


def test_estaEnRango_caracteres():
    """Pruebas para caracteres en la función estaEnRango."""
    with pytest.raises(TypeError):
        estaEnRango('a', 1, 10)
    with pytest.raises(TypeError):
        estaEnRango(5, 'b', 10)
    with pytest.raises(TypeError):
        estaEnRango(5, 1, 'c')


def test_estaEnRango_numeros_negativos():
    """Pruebas para números negativos en la función estaEnRango."""
    assert estaEnRango(-5, -10, 0) == True
    assert estaEnRango(-10, -10, -5) == True
    assert estaEnRango(-11, -10, -5) == False
    assert estaEnRango(0, -10, -1) == False


def test_estaEnRango_flotantes():
    """Pruebas para números flotantes en la función estaEnRango."""
    assert estaEnRango(5.5, 1.0, 10.0) == True
    assert estaEnRango(1.0, 1.0, 10.0) == True
    assert estaEnRango(10.1, 1.0, 10.0) == False
    assert estaEnRango(0.9, 1.0, 10.0) == False


def test_estaEnRango_rango_invertido():
    """Pruebas para rangos invertidos en la función estaEnRango."""
    assert estaEnRango(5, 10, 1) == False
    assert estaEnRango(10, 10, 1) == False
    assert estaEnRango(1, 10, 1) == False


# Pruebas para la función estaEnLista

def test_estaEnLista():
    """Pruebas para la función estaEnLista."""
    lista = [6, 14, 11, 3, 2, 1, 15, 19]
    assert estaEnLista(6, lista) == True
    assert estaEnLista(19, lista) == True
    assert estaEnLista(5, lista) == False
    assert estaEnLista(20, lista) == False


def test_estaEnLista_caso_vacio():
    """Pruebas para lista vacía en la función estaEnLista."""
    lista = []
    assert estaEnLista(1, lista) == False
    assert estaEnLista(0, lista) == False


def test_estaEnLista_caso_un_elemento():
    """Pruebas para lista con un solo elemento en la función estaEnLista."""
    lista = [5]
    assert estaEnLista(5, lista) == True
    assert estaEnLista(3, lista) == False


def test_estaEnLista_numeros_negativos():
    """Pruebas para números negativos en la función estaEnLista."""
    lista = [-5, -10, 0, 5, 10]
    assert estaEnLista(-5, lista) == True
    assert estaEnLista(-10, lista) == True
    assert estaEnLista(-3, lista) == False


def test_estaEnLista_duplicados():
    """Pruebas para lista con elementos duplicados en la función estaEnLista."""
    lista = [1, 2, 2, 3, 3, 3, 4]
    assert estaEnLista(2, lista) == True
    assert estaEnLista(3, lista) == True


def test_estaEnLista_tipo_string():
    """Pruebas para lista con diferentes tipos de datos en la función estaEnLista."""
    lista_strings = ["a", "b", "c"]
    assert estaEnLista("a", lista_strings) == True
    assert estaEnLista("d", lista_strings) == False


def test_estaEnLista_tipo_float():
    """Pruebas para lista con números flotantes en la función estaEnLista."""
    lista_flotantes = [1.5, 2.5, 3.5]
    assert estaEnLista(2.5, lista_flotantes) == True
    assert estaEnLista(2.0, lista_flotantes) == False


def test_estaEnLista_con_none():
    """Pruebas para lista que contiene None en la función estaEnLista."""
    lista = [1, None, 3]
    assert estaEnLista(None, lista) == True
    
    lista_sin_none = [1, 2, 3]
    assert estaEnLista(None, lista_sin_none) == False


def test_estaEnLista_lista_grande():
    """Pruebas para lista grande en la función estaEnLista."""
    lista_grande = list(range(1000))
    assert estaEnLista(500, lista_grande) == True
    assert estaEnLista(1001, lista_grande) == False


# Pruebas para la función esBinario

def test_esBinario():
    """Pruebas para la función esBinario."""
    assert esBinario("110011") == True
    assert esBinario("1111") == True
    assert esBinario("12301") == False
    assert esBinario("xyz12") == False


def test_esBinario_caso_vacio():
    """Pruebas para cadena vacía en la función esBinario."""
    assert esBinario("") == True


def test_esBinario_caso_un_caracter():
    """Pruebas para cadena de un solo carácter en la función esBinario."""
    assert esBinario("1") == True
    assert esBinario("0") == True
    assert esBinario("3") == False


def test_esBinario_caso_espacios():
    """Pruebas para cadena con espacios en la función esBinario."""
    assert esBinario("11 01") == False
    assert esBinario(" 1100") == False
    assert esBinario("0011 ") == False


def test_esBinario_caso_caracteres_especiales():
    """Pruebas para cadena con caracteres especiales en la función esBinario."""
    assert esBinario("11@01") == False
    assert esBinario("01#11") == False


def test_esBinario_numeros_largos():
    """Pruebas para cadenas largas en la función esBinario."""
    assert esBinario("0" * 100) == True
    assert esBinario("01" * 50) == True
    assert esBinario("0" * 50 + "5") == False


def test_esBinario_tipo_none():
    """Pruebas para tipos None en la función esBinario."""
    with pytest.raises(TypeError):
        esBinario(None)


def test_esBinario_tipo_float():
    """Pruebas para tipos float en la función esBinario."""
    with pytest.raises(TypeError):
        esBinario(3.14)


def test_esBinario_tipo_int():
    """Pruebas para tipos int en la función esBinario."""
    with pytest.raises(TypeError):
        esBinario(1010)