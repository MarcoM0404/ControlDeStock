import cv2
from pyzbar.pyzbar import decode
import csv
from menu import limpiar_consola
from tabulate import tabulate
def buscar_producto(codigo_barra):
    # Abre el archivo CSV y busca el producto por código
    with open("./stock/inventario.csv") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if row["codigo_barra"] == codigo_barra:
                return row
    return None  # Devuelve None si el código no se encuentra

def leer_codigo_desde_camara():
    limpiar_consola()
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
                    producto_info = [producto["codigo"], producto["producto"], producto["marca"], producto["precio"], producto["cantidad"], producto["codigo_barra"], producto["veces_modificado"]]
    
    # Imprimir la tabla con el producto encontrado
                    headers = ["Código", "Producto", "Marca", "Precio", "Cantidad", "Código de Barras", "Veces Modificado"]
                    tabla_producto = [producto_info]
                    print(tabulate(tabla_producto, headers, tablefmt="fancy_grid"))
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
    input("*** Presiona Enter para continuar ***")
    limpiar_consola()

