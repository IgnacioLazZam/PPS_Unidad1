# PPS_Unidad1 - Prácticas de Evaluación

## 📋 Descripción

Proyecto que implementa funciones para validación de números binarios, verificación de rangos y búsqueda en listas. Incluye suites completas de tests con unittest y pytest, cubriendo casos normales, límite y excepcionales.

## 👤 Autor

**Ignacio Lázaro Zambrano**  
IES Campanillas - Curso de Especialista en Ciberseguridad 21-22

## 🚀 Características

- ✅ **esBinario**: Validación de cadenas binarias
  - Verifica que solo contenga 0s y 1s
  - Manejo de cadenas vacías
  - Detección de caracteres inválidos

- ✅ **estaEnRango**: Verificación de valores en rangos
  - Soporte para enteros y flotantes
  - Números negativos
  - Validación de tipos de datos

- ✅ **estaEnLista**: Búsqueda de elementos en listas
  - Listas de cualquier tamaño
  - Múltiples tipos de datos (int, float, string, None)
  - Listas vacías y con duplicados

- ✅ **Suite completa de tests**:
  - 24 tests con unittest
  - 24 tests con pytest
  - Cobertura exhaustiva de casos límite

## 🔧 Requisitos

- Python 3.6 o superior
- unittest (incluido en la biblioteca estándar)
- pytest (para tests con pytest)
```bash
python -m pip install pytest
```

## 💻 Uso

### Programa Binario (binario.py)

Convierte números binarios a decimales:
```bash
python src/functions/binario.py
```

**Ejemplo de ejecución:**
```
Introduce un número binario: 1010
El número binario 1010 en decimal es: 10

Introduce un número binario: Hola
Error: La cadena introducida no es un número binario válido.
```

### Programa Lista (lista.py)

Verifica si un número del 1-20 está en una lista predefinida:
```bash
python src/functions/lista.py
```

**Ejemplo de ejecución:**
```
Introduce un número del 1 al 20: 6
El número 6 está en la lista.

Introduce un número del 1 al 20: 5
El número 5 no está en la lista.
```

## 🧪 Ejecución de Tests

### Con unittest
```bash
python -m unittest src/tests/test_funciones.py
```

### Con pytest
```bash
python -m pytest src/tests/test_funciones_pytest.py -v
```

## 📚 Tests Incluidos

### Para esBinario
- Cadenas binarias válidas
- Cadenas con caracteres inválidos
- Casos especiales (vacía, un carácter, espacios)
- Cadenas largas
- Validación de tipos (None, int, float)

### Para estaEnRango
- Valores dentro y fuera de rango
- Números negativos y flotantes
- Rangos invertidos
- Validación de tipos de datos

### Para estaEnLista
- Búsqueda en listas normales
- Listas vacías y de un elemento
- Números negativos y duplicados
- Diferentes tipos de datos (string, float, None)
- Listas grandes (1000+ elementos)
