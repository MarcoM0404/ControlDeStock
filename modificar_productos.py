import csv
from existencias_codigos import ExisteCodigo
from menu import limpiar_consola

def funcion_modificar(codigo, producto, marca, precio, cantidad):
    # Encuentra el producto existente en el archivo CSV
    result = []
    with open('./stock/inventario.csv', newline="") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if row["codigo"] == codigo:
                # agarramos el valor actual de veces_modificado y aumenta 1
                veces_modificado = int(row["veces_modificado"]) + 1
                row["producto"] = producto
                row["marca"] = marca
                row["precio"] = precio
                row["cantidad"] = cantidad
                row["veces_modificado"] = veces_modificado
            result.append(row)

    # escribe los cambios en el archivo CSV sin caracteres de nueva línea
    with open("./stock/inventario.csv", "w", newline="") as File:
        fieldnames = ["codigo", "producto", "marca", "precio", "cantidad", "codigo_barra", "veces_modificado"]
        writer = csv.DictWriter(File, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(result)


def funcion_modificar_cantidad_producto(codigo, cantidad, veces_modificado):
    result = []
    with open('./stock/inventario.csv', newline="") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if row["codigo"] == codigo:
                row["cantidad"] = cantidad
                row["veces_modificado"] = veces_modificado
            result.append(row)
    
    # Escribe los cambios en el archivo CSV sin caracteres de nueva línea
    with open("./stock/inventario.csv", "w", newline="") as File:
        fieldnames = ["codigo", "producto", "marca", "precio", "cantidad", "codigo_barra", "veces_modificado"]
        writer = csv.DictWriter(File, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(result)
    actualizar_registro_modificacion(codigo)

def actualizar_registro_modificacion(codigo):
    with open("./stock/inventario.csv", mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row[0] == codigo:
            # Encuentra el producto por su código
            veces_modificado = int(row[6])
            veces_modificado += 1
            row[6] = str(veces_modificado)
            break

    with open("./stock/inventario.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def modifica_productos():
    limpiar_consola()
    codigo = input("Ingrese el código del producto que desea modificar: ")
    if ExisteCodigo(codigo) == "No existe":
        print("****El código que desea modificar no existe****")
    else:
        producto = input("Ingrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        veces_modificado = 0  # Inicializa en 0
        funcion_modificar(codigo, producto, marca, precio, cantidad, veces_modificado)

def modificar_cantidad_producto():
    limpiar_consola()
    codigo = input("Ingrese el código del producto que desea modificar: ")
    if ExisteCodigo(codigo) == "No existe":
        print("****El código que desea modificar no existe****")
    else:
        cantidad = input("Ingrese la cantidad del producto: ")
        veces_modificado = obtener_veces_modificado(codigo)  # Obtener el valor de veces_modificado
        funcion_modificar_cantidad_producto(codigo, cantidad, veces_modificado)

def obtener_veces_modificado(codigo):
    with open("./stock/inventario.csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == codigo:
                # Encuentra el producto por su código
                veces_modificado = int(row[6])
                return veces_modificado
    return 0  # Si no se encuentra, inicializa en 0