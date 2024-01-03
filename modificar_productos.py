import csv
from existencias_codigos import existe_codigo
from menu import limpiar_consola

def funcion_modificar(codigo, producto, marca, precio, cantidad):
    
    result = []
    with open('./stock/inventario.csv', newline="") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if row["codigo"] == codigo:
                
                veces_modificado = int(row["veces_modificado"]) + 1
                row["producto"] = producto
                row["marca"] = marca
                row["precio"] = precio
                row["cantidad"] = cantidad
                row["veces_modificado"] = veces_modificado
            result.append(row)

    
    with open("./stock/inventario.csv", "w", newline="") as File:
        headers = ["codigo", "producto", "marca", "precio", "cantidad", "codigo_barra", "veces_modificado"]
        writer = csv.DictWriter(File, headers, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(result)
        
def modifica_productos():
    limpiar_consola()
    codigo = input("Ingrese el código del producto que desea modificar: ")
    if existe_codigo(codigo) == "No existe":
        print("****El código que desea modificar no existe****")
    else:
        producto = input("Ingrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        funcion_modificar(codigo, producto, marca, precio, cantidad)


def funcion_modificar_cantidad_producto(codigo, cantidad):
    result = []
    with open('./stock/inventario.csv', newline="") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if row["codigo"] == codigo:
                veces_modificado = int(row["veces_modificado"]) + 1
                row["cantidad"] = cantidad
                row["veces_modificado"] = veces_modificado
            result.append(row)
    
    
    with open("./stock/inventario.csv", "w", newline="") as File:
        headers = ["codigo", "producto", "marca", "precio", "cantidad", "codigo_barra", "veces_modificado"]
        writer = csv.DictWriter(File, headers, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(result)


def modificar_cantidad_producto():
    limpiar_consola()
    codigo = input("Ingrese el código del producto que desea modificar: ")
    if existe_codigo(codigo) == "No existe":
        print("****El código que desea modificar no existe****")
    else:
        cantidad = input("Ingrese la cantidad del producto: ")
        funcion_modificar_cantidad_producto(codigo, cantidad)
