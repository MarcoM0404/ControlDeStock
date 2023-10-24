from existencias_codigos import ExisteCodigo
import csv
def ModificarProducto():
    global codigo_barra
    codigo = input("Ingrese el código del producto que desea modificar: ")
    if ExisteCodigo(codigo) == "No existe":
        print("****El codigo que desea modificar no existe****")
    else:
        producto = input("Ingrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        FuncionModificar(codigo, producto, marca, precio, cantidad)
        
        
def FuncionModificar(codigo, producto, marca, precio, cantidad):
    global codigo_barra  # Indicamos que vamos a utilizar la variable global
    
    # Encuentra el producto existente en el archivo CSV
    result = []
    with open('./stock/inventario.csv', newline="") as File:
        reader = csv.DictReader(File)
        rows = list(reader)
        for row in rows:
            if row["codigo"] == codigo:
                # Preserva el código de barras existente
                codigo_barra = row["codigo_barra"]
                row["producto"] = producto
                row["marca"] = marca
                row["precio"] = precio
                row["cantidad"] = cantidad
            result.append(row)
    
    # Escribe los cambios en el archivo CSV
    with open("./stock/inventario.csv", "w") as File:
        fieldnames = ["codigo", "producto", "marca", "precio", "cantidad", "codigo_barra"]
        writer = csv.DictWriter(File, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(result)


def ModificarCantidadProducto():
    codigo = input("Ingrese el código del producto que desea modificar: ")
    if ExisteCodigo(codigo) == "No existe":
        print("****El codigo que desea modificar no existe****")
    else:
        cantidad = input("Ingrese la cantidad del producto: ")
        FuncionModificarCantidadProducto(codigo, cantidad)
        
        
def FuncionModificarCantidadProducto(codigo, cantidad):
    result = []
    with open('./stock/inventario.csv', newline="") as File:
        reader = csv.DictReader(File)
        rows = list(reader)
        for row in rows:
            if row["codigo"] == codigo:
                row["cantidad"] = cantidad
            result.append(row)
    
    with open("./stock/inventario.csv", "w") as File:
        fieldnames = ["codigo", "producto", "marca", "precio", "cantidad", "codigo_barra"]
        writer = csv.DictWriter(File,fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(result)
        