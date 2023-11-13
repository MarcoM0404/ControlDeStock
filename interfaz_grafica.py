from lector_camara_barcode import leer_codigo_desde_camara
from lector_barcode import leer_codigo_desde_imagen
from agregar_producto import nuevo_producto
from modificar_productos import modifica_productos, modificar_cantidad_producto
from eliminar_producto import eliminar_producto
from buscar_productos import buscar_producto_por_nombre, buscar_productos_por_codigo
from menu import ver_stock
import tkinter as tk
from ttkthemes import ThemedTk

def open_gui():
    root = ThemedTk(theme="equilux")
    root.title("Control de Stock")
    root.config(bg="lightblue")
    root.config(width = 500, height = 150)
    label = tk.Label(root, text="**MENÚ DEL CONTROL DE STOCK**")
    label.pack()

    # Botones
    btn_ver_stock = tk.Button(root, text="Ver todo el stock", command=ver_stock)
    btn_ver_stock.pack()

    btn_nuevo_producto = tk.Button(root, text="Añadir producto", command=nuevo_producto)
    btn_nuevo_producto.pack()

    btn_modificar_producto = tk.Button(root, text="Modificar producto", command=modifica_productos)
    btn_modificar_producto.pack()

    btn_eliminar_producto = tk.Button(root, text="Eliminar producto", command=eliminar_producto)
    btn_eliminar_producto.pack()

    btn_buscar_codigo = tk.Button(root, text="Buscar producto por código", command=buscar_productos_por_codigo)
    btn_buscar_codigo.pack()

    btn_buscar_nombre = tk.Button(root, text="Buscar producto por nombre", command=buscar_producto_por_nombre)
    btn_buscar_nombre.pack()

    btn_modificar_cantidad = tk.Button(root, text="Modificar cantidad del producto", command=modificar_cantidad_producto)
    btn_modificar_cantidad.pack()
    
    btn_leer_codigo_barra_ruta = tk.Button(root, text="Leer código de barra con código", command=leer_codigo_desde_imagen)
    btn_leer_codigo_barra_ruta.pack()
    
    btn_leer_codigo_barra_camara = tk.Button(root, text="Leer código de barra con imagen", command=leer_codigo_desde_camara)
    btn_leer_codigo_barra_camara.pack()

    btn_salir = tk.Button(root, text="Salir", command=root.destroy)
    btn_salir.pack()
    

    root.mainloop()




open_gui()  # Abre la interfaz gráfica al ejecutar el script