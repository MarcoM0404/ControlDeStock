import cv2
from pyzbar.pyzbar import decode
from menu import limpiar_consola
from tabulate import tabulate

def buscar_producto(codigo_barras):
    # Carga el inventario desde el archivo CSV
    inventario = cargar_inventario()

    # Busca el producto en el inventario
    for producto in inventario:
        if codigo_barras.startswith(producto['codigo_barra'][:12]):
            return producto

    return None

def cargar_inventario():
    # Carga el inventario desde el archivo CSV
    inventario = []
    with open("./stock/inventario.csv", 'r') as archivo:
        for linea in archivo:
            campos = linea.strip().split(',')
            
            # Verifica que haya suficientes campos antes de intentar acceder a ellos
            if len(campos) >= 7:
                codigo = campos[0].strip()
                producto = campos[1].strip()
                marca = campos[2].strip()
                precio = campos[3].strip()
                cantidad = campos[4].strip()
                codigo_barra = campos[5].strip()
                veces_modificado = campos[6].strip()
                inventario.append({
                    'codigo': codigo,
                    'producto': producto,
                    'marca': marca,
                    'precio': precio,
                    'cantidad': cantidad,
                    'codigo_barra': codigo_barra,
                    "veces_modificado": veces_modificado
                })

    return inventario



def leer_codigo_desde_imagen():
    limpiar_consola()
    ruta_imagen = input("Ingrese la ruta del código de barra: ")  # Solicitar la ruta de la imagen
    imagen = cv2.imread(ruta_imagen)

    codigos = decode(imagen)

    if codigos:
        productos_encontrados = []

        for codigo in codigos:
            codigo_barras = codigo.data.decode('utf-8')
            producto = buscar_producto(codigo_barras)

            if producto:
                producto_info = [producto["codigo"], producto["producto"], producto["marca"], producto["precio"], producto["cantidad"], producto["codigo_barra"], producto["veces_modificado"]]
                productos_encontrados.append(producto_info)
        
        if productos_encontrados:
            headers = ["Código", "Producto", "Marca", "Precio", "Cantidad", "Código de Barras", "Veces Modificado"]
            print(tabulate(productos_encontrados, headers, tablefmt="fancy_grid"))
        else:
            print('Productos no encontrados en la imagen')
    else:
        print('No se encontraron códigos de barras en la imagen')

    input("*** Presiona Enter para continuar ***")

