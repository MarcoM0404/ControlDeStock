from existencias_codigos import existe_codigo
import csv
from menu import limpiar_consola
import os

def eliminar_producto():
    limpiar_consola()
    codigo = input("Ingrese el código del producto que desea eliminar: ")
    if existe_codigo(codigo) == "No existe":
        print("****El código que desea eliminar no existe****")
    else:
        foto_filename = f"{codigo}.png"
        eleccion = input("¿Desea eliminar el producto? [S/n]: ").lower()
        if eleccion == "s" or eleccion == "":
            funcion_eliminar(codigo, foto_filename)
            print("Producto eliminado con éxito.")
            input("Presiona Enter para continuar")
            limpiar_consola()

def funcion_eliminar(codigo, foto_filename):
    result = []

    with open("./stock/inventario.csv", newline="") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if row["codigo"] != codigo:
                result.append(row) #Se evalúa si el código de la fila actual coincide con el código que se desea eliminar (codigo). Si no coinciden, la fila se agrega a la lista result, lo que significa que la fila no se eliminará.
            else:  
                if foto_filename:
                    # Elimina la foto si existe
                    foto_path = os.path.join("fotos_codigos", foto_filename)
                    if os.path.exists(foto_path):
                        os.remove(foto_path)

    with open("./stock/inventario.csv", "w", newline="") as File:
        fieldnames = ["codigo", "producto", "marca", "precio", "cantidad", "codigo_barra", "veces_modificado"]
        writer = csv.DictWriter(File, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(result) # Luego, se escribe la fila de encabezado y se escriben las filas restantes (las que no se eliminaron) en el nuevo archivo CSV.
