import csv
from menu import limpiar_consola
from tabulate import tabulate

def ordenar_stock():
    limpiar_consola()

    with open('./stock/inventario.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        hearders = csv_reader.fieldnames  # obtengo los nombres de las columnas del archivo original

        sorted_rows = sorted(csv_reader, key=lambda row: int(row['cantidad'])) #se utiliza una función lambda para definir una clave de ordenamiento. La función toma una fila (row) como entrada y devuelve el valor entero de la columna 'cantidad' de esa fila.
        #se utiliza sorted que toma un iterable y devuelve la lista con los elementos ordenados de manera ascendente. a diferencia del sort, el sorted crea una lista nueva.
    # abre un nuevo archivo CSV en modo escritura
    with open('./stock/inventario_ordenado.csv', 'w', newline='') as new_csv_file:
        csv_writer = csv.DictWriter(new_csv_file, hearders)

        # escribe los encabezados
        csv_writer.writeheader()

        # edcribe las filas ordenadas en el nuevo csv ordenado
        csv_writer.writerows(sorted_rows)

def imprimir_stock_ordenado():
    with open("./stock/inventario_ordenado.csv", "r", newline="") as ordfile:
        reader = csv.reader(ordfile)
        headers = next(reader)  # con esta variable la primer fila pasa a ser el encabezado
        data = [row for row in reader]  # las demás filas pasan a formar parte de los datos del encabezado

        if not data:
            print("El archivo de inventario está vacío.")
            input("Presiona Enter para continuar")
            return

        print(tabulate(data, headers, tablefmt='fancy_grid'))

        input("*** Se ha generado el stock ordenado, presiona Enter para continuar ***")
        limpiar_consola()
