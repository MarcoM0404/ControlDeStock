import cv2
from pyzbar.pyzbar import decode
from menu import limpiar_consola
from tabulate import tabulate
import csv

def buscar_producto(codigo_barras, inventario):
    # Busca el producto en el inventario
    for producto in inventario:
        if codigo_barras.startswith(producto['codigo_barra'][:12]):
            return producto
    return None

def cargar_inventario():
    inventario = []
    with open("./stock/inventario.csv", 'r') as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            inventario.append(row)
    return inventario

def leer_codigo_desde_imagen():
    limpiar_consola()
    
    while True:
        ruta_imagen = input("Ingrese la ruta del código de barras: ")
        
        try:
            imagen = cv2.imread(ruta_imagen)
            if imagen is None:
                raise Exception("No se pudo abrir la imagen. Ingrese una dirección que sea válida.")
            
            codigos = decode(imagen)
            break  # Salir del bucle si la lectura de la imagen fue exitosa
        except Exception as e:
            print(f'Error: {e}')
    
    if not codigos:
        print('No se encontraron códigos de barras en la imagen')
        return

    inventario = cargar_inventario()
    productos_encontrados = []

    for codigo in codigos:
        codigo_barras = codigo.data.decode('utf-8')
        producto = buscar_producto(codigo_barras, inventario)

        if producto:
            producto_info = [producto["codigo"], producto["producto"], producto["marca"], producto["precio"], producto["cantidad"], producto["codigo_barra"], producto["veces_modificado"]]
            productos_encontrados.append(producto_info)

    if productos_encontrados:
        headers = ["Código", "Producto", "Marca", "Precio", "Cantidad", "Código de Barras", "Veces Modificado"]
        print(tabulate(productos_encontrados, headers, tablefmt="fancy_grid"))
    else:
        print('Productos no encontrados en la imagen')

    input("*** Presiona Enter para continuar ***")
    limpiar_consola()

