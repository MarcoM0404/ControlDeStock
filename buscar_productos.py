from existencias_codigos import ExisteCodigo
import csv
from menu import limpiar_consola
from tabulate import tabulate
def buscar_productos_por_codigo():
    limpiar_consola()
    codigo = input("Ingrese el código del producto que desea buscar: ")
    if ExisteCodigo(codigo) == "No existe":
        print("****El código que desea buscar no existe****")
    else:
        funcion_buscar_codigo(codigo)

def funcion_buscar_codigo(codigo):
    with open('./stock/inventario.csv', 'r') as File:
        reader = csv.DictReader(File)
        productos = [row for row in reader if row["codigo"] == codigo]

    if not productos:
        print("No se encontró un producto con el código especificado.")
        input("*** Presiona Enter para continuar ***")
        return

    # Mostrar los resultados en una tabla utilizando tabulate
    headers = ["Código", "Producto", "Marca", "Precio", "Cantidad", "Código de Barras", "Veces Modificado"]
    tabla_productos = [[producto["codigo"], producto["producto"], producto["marca"], producto["precio"], producto["cantidad"], producto["codigo_barra"], producto["veces_modificado"]] for producto in productos]
    print(tabulate(tabla_productos, headers, tablefmt="fancy_grid"))
    input("*** Presiona Enter para continuar ***")

def buscar_producto_por_nombre():
    limpiar_consola()
    palabra = input("Ingrese el nombre del producto que desea buscar: ")

    # Leer el archivo CSV e inicializar una lista para almacenar los resultados
    resultados = []

    with open("./stock/inventario.csv", mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Leer la primera fila del archivo (encabezados)
        for row in reader:
            codigo, producto, marca, precio, cantidad, codigo_barra, veces_modificado = row
            if palabra in producto:
                resultados.append([codigo, producto, marca, precio, cantidad, codigo_barra, veces_modificado])

    if resultados:
        # Mostrar los resultados en una tabla
        table_headers = ["Código", "Producto", "Marca", "Precio", "Cantidad", "Código de Barras", "Veces Modificado"]
        print(tabulate(resultados, headers=table_headers, tablefmt="fancy_grid"))
    else:
        print("****Ese producto no se encuentra en el stock****")

    input("*** Presiona Enter para continuar ***")

# Llamar a la función para buscar productos por nombre