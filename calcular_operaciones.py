import pandas as pd

def realizar_operacion(row):
    """Realiza la operación matemática especificada en la fila.

    Args:
        row: Una serie de pandas que representa una fila del DataFrame.

    Returns:
        El resultado de la operación o un mensaje de error si la operación no es válida.
    """

    operacion = row['operation']
    operando1 = row['operand_1']
    operando2 = row['operand_2']

    try:
        if operacion == 'SUMA':
            return operando1 + operando2
        elif operacion == 'RESTA':
            return operando1 - operando2
        elif operacion == 'MULTIPLICACION':
            return operando1 * operando2
        elif operacion == 'DIVISION':
            if operando2 == 0:
                return "División por cero"
            else:
                return operando1 / operando2
        elif operacion == 'POTENCIA':
            return operando1 ** operando2
        else:
            return "Operación no válida"
    except TypeError:
        return "Error de tipo de dato"

# Cargar el archivo CSV
df = pd.read_csv("operaciones.csv")

# Aplicar la función a cada fila y crear una nueva columna
df['resultado'] = df.apply(realizar_operacion, axis=1)

# Verificar los resultados (si existe la columna correct_result)
if 'correct_result' in df.columns:
    df['correcto'] = df['resultado'] == df['correct_result']

# Guardar los cambios en el archivo CSV
df.to_csv("resultados.csv", index=False)

print("Archivo CSV actualizado correctamente.")
