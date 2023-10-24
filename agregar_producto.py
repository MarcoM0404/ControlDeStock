from existencias_codigos import ExisteCodigo, ExisteCodigoDeBarras
from barcode_generator import generadorDeCodigo, BarcodeGenerator

codigo_barra = None
def NuevoProducto():
    global codigo_barra
    codigo = input("Ingrese el código de producto nuevo: ")
    if ExisteCodigo(codigo) == "No existe":
        producto = input("Ingrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        
        # Genera el código de barras único para el producto
        
        codigo_barra = generadorDeCodigo()
        
        nombre_cod = input("Ingrese el nombre del código: ")
        while ExisteCodigoDeBarras(codigo_barra) is not None:
            codigo_barra = generadorDeCodigo()
        
        # Llama a BarcodeGenerator con el código de barras único
        BarcodeGenerator(codigo_barra, nombre_cod)
        
        # Luego, escribe los detalles del producto en el archivo CSV
        with open("./stock/inventario.csv", "a") as File:
            File.write("\n"+codigo+","+producto+","+marca+","+precio+","+cantidad+","+codigo_barra)
    else:
        print("****El código ya existe****")
