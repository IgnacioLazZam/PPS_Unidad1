import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.functions.binario import esBinario
from src.functions.lista import estaEnLista, estaEnRango

class TestFunciones(unittest.TestCase):
    
    # Pruebas para la función estaEnRango

    def test_estaEnRango(self):
        """Pruebas para la función estaEnRango."""
        self.assertTrue(estaEnRango(1, 1, 20))
        self.assertTrue(estaEnRango(10, 1, 20))
        self.assertFalse(estaEnRango(0, 1, 20))
        self.assertFalse(estaEnRango(21, 1, 20))

    def test_estaEnRango_caso_especiales(self):
        """Pruebas para casos especiales de la función estaEnRango."""
        self.assertTrue(estaEnRango(1, 1, 1))
        self.assertFalse(estaEnRango(0, 1, 1))
        self.assertFalse(estaEnRango(2, 1, 1))

    def test_estaEnRango_caracteres(self):
        """Pruebas para caracteres en la función estaEnRango."""
        self.assertRaises(TypeError, estaEnRango, 'a', 1, 10)
        self.assertRaises(TypeError, estaEnRango, 5, 'b', 10)
        self.assertRaises(TypeError, estaEnRango, 5, 1, 'c')

    def test_estaEnRango_numeros_negativos(self):
        """Pruebas para números negativos en la función estaEnRango."""
        self.assertTrue(estaEnRango(-5, -10, 0))
        self.assertTrue(estaEnRango(-10, -10, -5))
        self.assertFalse(estaEnRango(-11, -10, -5))
        self.assertFalse(estaEnRango(0, -10, -1))

    def test_estaEnRango_flotantes(self):
        """Pruebas para números flotantes en la función estaEnRango."""
        self.assertTrue(estaEnRango(5.5, 1.0, 10.0))
        self.assertTrue(estaEnRango(1.0, 1.0, 10.0))
        self.assertFalse(estaEnRango(10.1, 1.0, 10.0))
        self.assertFalse(estaEnRango(0.9, 1.0, 10.0))

    def test_estaEnRango_rango_invertido(self):
        """Pruebas para rangos invertidos en la función estaEnRango."""
        self.assertFalse(estaEnRango(5, 10, 1))
        self.assertFalse(estaEnRango(10, 10, 1))
        self.assertFalse(estaEnRango(1, 10, 1))

    # Pruebas para la función estaEnLista

    def test_estaEnLista(self):
        """Pruebas para la función estaEnLista."""
        lista = [6, 14, 11, 3, 2, 1, 15, 19]
        self.assertTrue(estaEnLista(6, lista))
        self.assertTrue(estaEnLista(19, lista))
        self.assertFalse(estaEnLista(5, lista))
        self.assertFalse(estaEnLista(20, lista))

    def test_estaEnLista_caso_vacio(self):
        """Pruebas para lista vacía en la función estaEnLista."""
        lista = []
        self.assertFalse(estaEnLista(1, lista))
        self.assertFalse(estaEnLista(0, lista))
    
    def test_estaEnLista_caso_un_elemento(self):
        """Pruebas para lista con un solo elemento en la función estaEnLista."""
        lista = [5]
        self.assertTrue(estaEnLista(5, lista))
        self.assertFalse(estaEnLista(3, lista))

    def test_estaEnLista_numeros_negativos(self):
        """Pruebas para números negativos en la función estaEnLista."""
        lista = [-5, -10, 0, 5, 10]
        self.assertTrue(estaEnLista(-5, lista))
        self.assertTrue(estaEnLista(-10, lista))
        self.assertFalse(estaEnLista(-3, lista))

    def test_estaEnLista_duplicados(self):
        """Pruebas para lista con elementos duplicados en la función estaEnLista."""
        lista = [1, 2, 2, 3, 3, 3, 4]
        self.assertTrue(estaEnLista(2, lista))
        self.assertTrue(estaEnLista(3, lista))

    def test_estaEnLista_tipo_string(self):
        """Pruebas para lista con diferentes tipos de datos en la función estaEnLista."""
        lista_strings = ["a", "b", "c"]
        self.assertTrue(estaEnLista("a", lista_strings))
        self.assertFalse(estaEnLista("d", lista_strings))
    
    def test_estaEnLista_tipo_float(self):
        """Pruebas para lista con números flotantes en la función estaEnLista."""
        lista_flotantes = [1.5, 2.5, 3.5]
        self.assertTrue(estaEnLista(2.5, lista_flotantes))
        self.assertFalse(estaEnLista(2.0, lista_flotantes))

    def test_estaEnLista_con_none(self):
        """Pruebas para lista que contiene None en la función estaEnLista."""
        lista = [1, None, 3]
        self.assertTrue(estaEnLista(None, lista))
        
        lista_sin_none = [1, 2, 3]
        self.assertFalse(estaEnLista(None, lista_sin_none))

    def test_estaEnLista_lista_grande(self):
        """Pruebas para lista grande en la función estaEnLista."""
        lista_grande = list(range(1000))
        self.assertTrue(estaEnLista(500, lista_grande))
        self.assertFalse(estaEnLista(1001, lista_grande))

    # Pruebas para la función esBinario

    def test_esBinario(self):
        """Pruebas para la función esBinario."""
        self.assertTrue(esBinario("110011"))
        self.assertTrue(esBinario("1111"))
        self.assertFalse(esBinario("12301"))
        self.assertFalse(esBinario("xyz12"))

    def test_esBinario_caso_vacio(self):
        """Pruebas para cadena vacía en la función esBinario."""
        self.assertTrue(esBinario(""))
    
    def test_esBinario_caso_un_caracter(self):
        """Pruebas para cadena de un solo carácter en la función esBinario."""
        self.assertTrue(esBinario("1"))
        self.assertTrue(esBinario("0"))
        self.assertFalse(esBinario("3"))

    def test_esBinario_caso_espacios(self):
        """Pruebas para cadena con espacios en la función esBinario."""
        self.assertFalse(esBinario("11 01"))
        self.assertFalse(esBinario(" 1100"))
        self.assertFalse(esBinario("0011 "))

    def test_esBinario_caso_caracteres_especiales(self):
        """Pruebas para cadena con caracteres especiales en la función esBinario."""
        self.assertFalse(esBinario("11@01"))
        self.assertFalse(esBinario("01#11"))

    def test_esBinario_numeros_largos(self):
        """Pruebas para cadenas largas en la función esBinario."""
        self.assertTrue(esBinario("0" * 100))
        self.assertTrue(esBinario("01" * 50))
        self.assertFalse(esBinario("0" * 50 + "5"))

    def test_esBinario_tipo_none(self):
        """Pruebas para tipos None en la función esBinario."""
        self.assertRaises(TypeError, esBinario, None)

    def test_esBinario_tipo_float(self):
        """Pruebas para tipos float en la función esBinario."""
        self.assertRaises(TypeError, esBinario, 3.14)

    def test_esBinario_tipo_int(self):
        """Pruebas para tipos int en la función esBinario."""
        self.assertRaises(TypeError, esBinario, 1010)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
