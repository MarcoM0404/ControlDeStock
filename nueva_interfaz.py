import tkinter as tk
from existencias_codigos import ExisteCodigo, ExisteCodigoDeBarras
from barcode_generator import generadorDeCodigo, BarcodeGenerator
from menu import limpiar_consola

nombres_codigos_barras = []  # Lista para almacenar los nombres de códigos de barras

def nuevo_producto():
    codigo = codigo_entry.get()
    if ExisteCodigo(codigo) == "No existe":
        producto = producto_entry.get()
        marca = marca_entry.get()
        precio = precio_entry.get()
        cantidad = cantidad_entry.get()

        # Genera el código de barras único para el producto
        codigo_barra = generadorDeCodigo()
        
        nombre_cod = nombre_cod_entry.get()
        while ExisteCodigoDeBarras(codigo_barra) is not None:
            codigo_barra = generadorDeCodigo()

        # Agrega el nombre del código de barras a la lista
        nombres_codigos_barras.append(nombre_cod)

        # Llama a BarcodeGenerator con el código de barras único
        BarcodeGenerator(codigo_barra, nombre_cod)

        # Luego, escribe los detalles del producto en el archivo CSV sin caracteres de nueva línea
        with open("./stock/inventario.csv", "a") as File:
            File.write(f"{codigo},{producto},{marca},{precio},{cantidad},{codigo_barra}\n")
    else:
        print("****El código ya existe****")

root = tk.Tk()
root.title("Sistema de Gestión de Productos")

codigo_label = tk.Label(root, text="Código del producto:")
codigo_label.pack()
codigo_entry = tk.Entry(root)
codigo_entry.pack()

producto_label = tk.Label(root, text="Nombre del producto:")
producto_label.pack()
producto_entry = tk.Entry(root)
producto_entry.pack()

marca_label = tk.Label(root, text="Marca del producto:")
marca_label.pack()
marca_entry = tk.Entry(root)
marca_entry.pack()

precio_label = tk.Label(root, text="Precio del producto:")
precio_label.pack()
precio_entry = tk.Entry(root)
precio_entry.pack()

cantidad_label = tk.Label(root, text="Cantidad del producto:")
cantidad_label.pack()
cantidad_entry = tk.Entry(root)
cantidad_entry.pack()

nombre_cod_label = tk.Label(root, text="Nombre del código de barras:")
nombre_cod_label.pack()
nombre_cod_entry = tk.Entry(root)
nombre_cod_entry.pack()

btn_nuevo_producto = tk.Button(root, text="Añadir producto", command=nuevo_producto)
btn_nuevo_producto.pack()

root.mainloop()
