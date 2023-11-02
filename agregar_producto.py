from existencias_codigos import ExisteCodigo, ExisteCodigoDeBarras
from barcode_generator import generadorDeCodigo, BarcodeGenerator
from menu import limpiar_consola
nombres_codigos_barras = []  # Lista para almacenar los nombres de códigos de barras

def nuevo_producto():
    limpiar_consola()
    global codigo_barra
    codigo = input("Ingrese el código de producto nuevo: ")
    if ExisteCodigo(codigo) == "No existe":
        producto = input("Ingrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        veces_modificado = 0
        
        # Genera el código de barras único para el producto
        codigo_barra = generadorDeCodigo()
        
        nombre_cod = input("Ingrese el nombre del código: ")
        while ExisteCodigoDeBarras(codigo_barra) is not None:
            codigo_barra = generadorDeCodigo()
        
        # Agrega el nombre del código de barras a la lista
        nombres_codigos_barras.append(nombre_cod)
        
        # Llama a BarcodeGenerator con el código de barras único
        BarcodeGenerator(codigo_barra, nombre_cod)
        
        # Luego, verifica si el archivo CSV ya existe
        archivo_existe = False
        try:
            with open("./stock/inventario.csv", "r") as File:
                archivo_existe = True
        except FileNotFoundError:
            pass
        
        # Abre el archivo en modo "a" o "w" según si el archivo ya existe o no
        with open("./stock/inventario.csv", "a" if archivo_existe else "w", newline="") as File:
            if not archivo_existe:
                # Escribe el encabezado si el archivo no existía
                File.write("codigo,producto,marca,precio,cantidad,codigo_barra,veces_modificado\n")
            
            # Escribe los detalles del producto en el archivo CSV sin caracteres de nueva línea
            File.write(f"{codigo},{producto},{marca},{precio},{cantidad},{codigo_barra},{veces_modificado}\n")
    else:
        print("****El código ya existe****")

