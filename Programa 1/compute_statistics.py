"""
compute_statistics.py

Este programa ejecuta cálculos estadísticos sobre una lista de números
contenidos en un archivo, generando el resultado en otro archivo.

Instrucciones de uso:
python compute_statistics.py fileWithData.txt
"""
import sys
import time

def leer_archivo(ruta_archivo):
    """Recibe un archivo y filtra los datos devolviendo una lista de valores numéricos.

    Parámetro(s):
        ruta_archivo (str): La ruta del archivo a leer.

    Salida(s):
        Una lista de valores numéricos o None si detecta algún error.
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            # Creamos una lista para filtrar solo valores numéricos
            valores_numericos = []
            # Creamos otra lista para capturar los datos no válidos y mostrarlos posteriormente
            valores_errados = []
            # Creamos otra lista para capturar los datos no válidos que fueron corregidos
            valores_ajustados = []

            # Llenamos las listas
            for valor in file:
                for value in valor.split():
                    try:
                        valores_numericos.append(float(value))
                    except ValueError:
                        parte_numerica = ''.join(char for char in value if char.isdigit())
                        if parte_numerica:
                            valores_ajustados.append(value)
                            valores_numericos.append(float(parte_numerica))
                        else:
                            valores_errados.append(value)

            if valores_errados:
                print("Estos valores no son numéricos y no serán procesados:\n", valores_errados)

            if valores_ajustados:
                print("Estos valores no numéricos se ajustaron para procesar:\n", valores_ajustados)

            datos = valores_numericos

        return datos
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ruta_archivo}' indicado.")
        return None
    except PermissionError:
        print("No posee permiso para abrir el archivo.")
        return None
    except UnicodeDecodeError:
        print("No se puede abrir el archivo, revise la codificación.")
        return None

def realizar_calculos(datos):
    """Ejecuta cálculos estadísticos para la lista de datos numéricos recibida.

    Parámetro(s):
        datos (lista_numeros): Lista con valores numéricos reales.

    Salida(s):
        Resultados de cálculos realizados adicionando el número de elementos
        y el tiempo empleado para la ejecución de los cálculos.
    """
    if datos is None:
        return None

    conteo = len(datos)

    hora_inicio = time.time()

    mean = sum(datos) / len(datos)
    sorted_data = sorted(datos)
    n = len(sorted_data)

    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    # Moda
    counts = {}
    for value in datos:
        counts[value] = counts.get(value, 0) + 1

    max_count = max(counts.values())
    mode = [key for key, value in counts.items() if value == max_count][0]

    variance = sum((x - mean) ** 2 for x in datos) / (len(datos) - 1)
    std_deviation = variance ** 0.5

    tiempo_transcurrido = time.time() - hora_inicio

    return conteo, mean, median, mode, std_deviation, variance, tiempo_transcurrido

def crear_archivo_resultados(resultados):
    """Crea un archivo con los resultados generados a partir del cálculo

    Parámetro(s):
        resultados (lista_numeros): Resultados numéricos del cálculo.

    Salida(s):
        Archivo de texto llamado StatisticsResults mostrando resultados.
    """
    with open("StatisticsResults.txt", 'w', encoding='utf-8') as file:
        file.write("Descriptive Statistics:\n")
        file.write(f"Count: {resultados[0]}\n")
        file.write(f"Mean: {resultados[1]}\n")
        file.write(f"Median: {resultados[2]}\n")
        file.write(f"Mode: {resultados[3]}\n")
        file.write(f"Standard Deviation: {resultados[4]}\n")
        file.write(f"Variance: {resultados[5]}\n")
        file.write(f"Tiempo transcurrido: {resultados[6]} segundos")

def main():
    """Función principal que integrará la lógica y se ejecutará al correr el programa"""
    if len(sys.argv) != 2:
        print("Utilice el comando de ejecución: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    data = leer_archivo(file_path)

    if data is not None:
        resultados = realizar_calculos(data)

        if resultados is not None:
            print("\nA continuación los valores calculados para el archivo:\n")
            print("Descriptive Statistics:")
            print(f"Count: {resultados[0]}")
            print(f"Mean: {resultados[1]}")
            print(f"Median: {resultados[2]}")
            print(f"Mode: {resultados[3]}")
            print(f"Standard Deviation: {resultados[4]}")
            print(f"Variance: {resultados[5]}")
            print(f"Tiempo transcurrido: {resultados[6]} segundos")

            crear_archivo_resultados(resultados)

if __name__ == "__main__":
    main()
