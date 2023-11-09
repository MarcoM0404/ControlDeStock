import csv

def existe_codigo(codigo):
    with open("./stock/inventario.csv") as File:
        reader = csv.DictReader(File)
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
    return None  # Devuelve None para indicar que el código de barras no existe

