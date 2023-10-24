import cv2
from pyzbar.pyzbar import decode
import csv

def buscar_producto(codigo_barra):
    # Abre el archivo CSV y busca el producto por código
    with open("./stock/inventario.csv") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if row["codigo_barra"] == codigo_barra:
                return row
    return None  # Devuelve None si el código no se encuentra

def leer_codigo_desde_camara():
    cap = cv2.VideoCapture(0)  # Abre la cámara (puede ajustar el número según su configuración)
    
    codigo_leido = False  # Variable de control
    
    while not codigo_leido:  # Continúa buscando hasta que se lea un código
        success, img = cap.read()
        
        for barcode in decode(img):
            try:
                mydata = barcode.data.decode("utf-8")
                codigo_producto = mydata[:12]  # Obtiene los primeros 12 dígitos
                
                # Busca el producto en el inventario
                producto = buscar_producto(codigo_producto)
                
                if producto:
                    print(f'Código de barras leído: {mydata}')
                    print(f'Producto: {producto["producto"]}')
                    print(f'Código: {producto["codigo"]}')
                    print(f'Marca: {producto["marca"]}')
                    print(f'Precio: {producto["precio"]}')
                    print(f'Cantidad: {producto["cantidad"]}')
                    codigo_leido = True  # Marca que se ha leído un código válido
                else:
                    print(f'Código de barras leído: {mydata} (Producto no encontrado en el inventario)')
            except Exception as e:
                print(f"Error al decodificar el código de barras: {e}")
        
        cv2.imshow("Result", img)
        
        # Cierra la ventana si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera la cámara y cierra la ventana
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    leer_codigo_desde_camara()
