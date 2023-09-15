import cv2
from pyzbar.pyzbar import decode

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
            if len(campos) >= 6:
                codigo = campos[0].strip()
                producto = campos[1].strip()
                marca = campos[2].strip()
                precio = campos[3].strip()
                cantidad = campos[4].strip()
                codigo_barra = campos[5].strip()
                inventario.append({
                    'codigo': codigo,
                    'producto': producto,
                    'marca': marca,
                    'precio': precio,
                    'cantidad': cantidad,
                    'codigo_barra': codigo_barra
                })

    return inventario



import cv2
from pyzbar.pyzbar import decode

def leer_codigo_desde_imagen(ruta_imagen):
    # Carga la imagen desde la ruta especificada
    imagen = cv2.imread(ruta_imagen)

    # Decodifica el código de barras desde la imagen
    codigos = decode(imagen)
    
    if codigos:
        for codigo in codigos:
            codigo_barras = codigo.data.decode('utf-8')
            producto = buscar_producto(codigo_barras)

            if producto:
                print(f'Código: {codigo_barras}')
                print(f'Producto: {producto["producto"]}')
                print(f'Marca: {producto["marca"]}')
                print(f'Precio: {producto["precio"]}')
                print(f'Código de barras: {producto["codigo_barra"]}')
            else:
                print('Producto no encontrado')
    else:
        print('No se encontraron códigos de barras en la imagen')

if __name__ == "__main__":
    # Ruta de la imagen que contiene el código de barras
    ruta_imagen = "./fotos_codigos/mouse_logitech_1.png"

    leer_codigo_desde_imagen(ruta_imagen)



if __name__ == "__main__":
    # Ruta de la imagen que contiene el código de barras
    ruta_imagen = "./fotos_codigos/mouse_logitech_1.png"

    leer_codigo_desde_imagen(ruta_imagen)

