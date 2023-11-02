from existencias_codigos import ExisteCodigo
import csv
from menu import limpiar_consola
def eliminar_producto():
    limpiar_consola()
    codigo = input("Ingrese el código del producto que desea eliminar: ")
    if ExisteCodigo(codigo) == "No existe":
        print("****El código que desea eliminar no existe****")
    else:
        eleccion = input("¿Está seguro? (Sí=S, No=N): ")
        eleccion = eleccion.upper()
        if eleccion == "S":
            funcion_eliminar(codigo)
            print("Producto eliminado con éxito.")

def funcion_eliminar(codigo):
    result = []
    with open("./stock/inventario.csv", newline="") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if row["codigo"] != codigo:
                result.append(row)
    
    with open("./stock/inventario.csv", "w", newline="") as File:
        fieldnames = ["codigo", "producto", "marca", "precio", "cantidad", "codigo_barra"]
        writer = csv.DictWriter(File, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(result)

