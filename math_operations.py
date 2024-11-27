import pandas as pd

def perform_operation(row):
    """Realiza la operación matemática especificada en la fila.

    Args:
        row: Una serie de pandas que representa una fila del DataFrame.

    Returns:
        El resultado de la operación o un mensaje de error si la operación no es válida.
    """

    operation = row['operation']
    operand1 = row['operand_1']
    operand2 = row['operand_2']

    if operation == 'SUM':
        return operand1 + operand2
    elif operation == 'MUL':
        return operand1 * operand2
    elif operation == 'DIV':
        if operand2 == 0:
            return "División por cero"
        else:
            return operand1 / operand2
    elif operation == 'POW':
        return operand1 ** operand2
    else:
        return "Operación no válida"

# Cargar el archivo CSV
df = pd.read_csv("math_operations.csv")

# Aplicar la función a cada fila y crear una nueva columna
df['result'] = df.apply(perform_operation, axis=1)

# Verificar los resultados (si existe la columna correct_result)
if 'correct_result' in df.columns:
    df['correct'] = df['result'] == df['correct_result']

# Guardar los cambios en el archivo CSV
df.to_csv("math_operations.csv", index=False)

print("Archivo CSV actualizado correctamente.")
