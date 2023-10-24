import pandas as pd
from lector_camara_barcode import leer_codigo_desde_camara
from lector_barcode import leer_codigo_desde_imagen
from agregar_producto import NuevoProducto
from modificar_productos import ModificarProducto, ModificarCantidadProducto
from eliminar_producto import EliminarProducto
from buscar_productos import BuscarProductoPorCodigo, BuscarProductoPorNombre
from menu import Menu, VerStock
from tkinter import messagebox
from barcode_generator import BarcodeGenerator
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


# En la función open_gui():
def open_gui():
    root = ThemedTk(theme="equilux")
  # Puedes elegir un tema diferente

    root.geometry("300x300")
    root.minsize(300, 300)
    root.title("Control de Stock")

    # Para configurar el fondo en un tema personalizado, puedes hacerlo así:
    root.config( background="blue")

    # Etiquetas
    label = tk.Label(root, text="**MENÚ DEL CONTROL DE STOCK**")
    label.pack()

    # Botones
    btn_ver_stock = tk.Button(root, text="Ver todo el stock", command=VerStock)
    btn_ver_stock.pack()

    btn_nuevo_producto = tk.Button(root, text="Añadir producto", command=NuevoProducto)
    btn_nuevo_producto.pack()

    btn_modificar_producto = tk.Button(root, text="Modificar producto", command=ModificarProducto)
    btn_modificar_producto.pack()

    btn_eliminar_producto = tk.Button(root, text="Eliminar producto", command=EliminarProducto)
    btn_eliminar_producto.pack()

    btn_buscar_codigo = tk.Button(root, text="Buscar producto por código", command=BuscarProductoPorCodigo)
    btn_buscar_codigo.pack()

    btn_buscar_nombre = tk.Button(root, text="Buscar producto por nombre", command=BuscarProductoPorNombre)
    btn_buscar_nombre.pack()

    btn_modificar_cantidad = tk.Button(root, text="Modificar cantidad del producto", command=ModificarCantidadProducto)
    btn_modificar_cantidad.pack()
    
    btn_leer_codigo_barra_ruta = tk.Button(root, text="Leer código de barra con ruta de imagen", command=leer_codigo_desde_imagen)
    btn_leer_codigo_barra_ruta.pack()
    
    btn_leer_codigo_barra_camara = tk.Button(root, text="Leer código de barra con imagen", command=leer_codigo_desde_camara)
    btn_leer_codigo_barra_camara.pack()

    btn_salir = tk.Button(root, text="Salir", command=root.destroy)
    btn_salir.pack()

    root.mainloop()




open_gui()  # Abre la interfaz gráfica al ejecutar el script