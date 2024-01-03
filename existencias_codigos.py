import csv

def existe_codigo(codigo):
    with open("./stock/inventario.csv") as File:
        reader = csv.DictReader(File)  # cada fila del archivo CSV se representa como un diccionario donde las claves son los encabezados de las columnas y los valores son los datos correspondientes en esa fila.
        for row in reader:
            if (codigo == row["codigo"]):
                return row
    return "No existe"

def existe_codigo_de_barras(codigo_barra):
    with open("./stock/inventario.csv") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if codigo_barra == row["codigo_barra"]:
                return row
    return None  

