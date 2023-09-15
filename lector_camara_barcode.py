import cv2
from pyzbar.pyzbar import decode

"""cap = cv2.VideoCapture(2)
cap.set(3, 640)
cap.set(4, 480)

# Cargar los datos del inventario desde el archivo CSV
inventario = []
with open("./stock/inventario.csv", 'r') as archivo:
    for linea in archivo:
        campos = linea.strip().split(',')
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

while True:
    success, img = cap.read()

    for barcode in decode(img):
        mydata = barcode.data.decode("utf-8")
        
        # Buscar el producto en el inventario por el código de barras
        producto_encontrado = None
        for producto in inventario:
            if producto['codigo_barra'] == mydata:
                producto_encontrado = producto
                break
        
        if producto_encontrado:
            print(f'Código: {mydata}')
            print(f'Producto: {producto_encontrado["producto"]}')
            print(f'Marca: {producto_encontrado["marca"]}')
            print(f'Precio: {producto_encontrado["precio"]}')
        else:
            print(f'Código: {mydata} (Producto no encontrado en el inventario)')

    cv2.imshow("Result", img)
    
    # Cerrar la ventana si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
"""