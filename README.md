# Calculadora de Operaciones Básicas

**Descripción**

Este proyecto Python realiza operaciones matemáticas básicas (suma, resta, multiplicación, división y potencia) sobre un conjunto de datos proporcionado en un archivo CSV. El script lee el archivo CSV, realiza los cálculos y actualiza el archivo con los resultados obtenidos.

**Estructura del Proyecto**

* **math_operations.csv:** Archivo CSV que contiene las operaciones a realizar y los operandos.
* **calcular_operaciones.py:** Script de Python que realiza los cálculos y actualiza el archivo CSV.
* **README.md:** Este archivo.

**Cómo usar**

1. **Requisitos:**
   * Python (versión 3.x)
   * Librerías: pandas, numpy (instalar con `pip install pandas numpy`)
2. **Ejecución:**
   * Coloca el archivo `math_operations.csv` y el script `calcular_operaciones.py` en la misma carpeta.
   * Ejecuta el script desde la línea de comandos:
     ```bash
     python calcular_operaciones.py
     ```
3. **Resultados:**
   * El archivo `math_operations.csv` será actualizado con una nueva columna "result" que contiene los resultados de las operaciones.

**Estructura del archivo CSV**

| Columna | Descripción |
|---|---|
| operation | Operación a realizar (SUM, MUL, DIV, POW) |
| operand_1 | Primer operando |
| operand_2 | Segundo operando |
| correct_result (opcional) | Resultado correcto (para verificación) |
| result | Resultado calculado por el script |

**Contribuciones**

¡Las contribuciones son bienvenidas! Si encuentras algún error o deseas agregar nuevas funcionalidades, por favor, crea un issue o un pull request.

**Licencia**

Este proyecto está bajo la licencia MIT.

**Autor**
[Wilson Quintero]
