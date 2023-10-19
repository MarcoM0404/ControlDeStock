import pandas as pd
import os
import csv
import random
from barcode_generator import BarcodeGenerator
from lector_camara_barcode import buscar_producto, leer_codigo_desde_camara
from lector_barcode import buscar_producto, cargar_inventario, leer_codigo_desde_imagen

def Menu():
    print("*****MENÚ DEL CONTROL DE STOCK*****")
    print("1. Ver todo el stock ---------------------- 2. Añadir producto")
    print("3. Modificar producto --------------------- 4. Eliminar producto")
    print("5. Buscar producto por código ------------- 6. Buscar producto por nombre")
    print("7. Modificar cantidad del producto -------- 8. Leer código de barra con ruta de imagen")
    print("9. Leer código de barra con imagen -------- 10. Salir")
    opcion = str(input("Ingrese la opción que desea acceder: "))
    return opcion
    
    

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def ExisteCodigo(codigo):
    with open("./stock/inventario.csv") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if (codigo == row["codigo"]):
                return row
    return "No existe"

def ExisteCodigoDeBarras(codigo_barra):
    with open("./stock/inventario.csv") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if codigo_barra == row["codigo_barra"]:
                return row
    return None  # Devuelve None para indicar que el código de barras no existe




def VerStock():
    df = pd.read_csv("./stock/inventario.csv", engine="python")
    print(df)

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
        

def EliminarProducto():
    codigo = input("Ingrese el código del producto que desea eliminar: ")
    if ExisteCodigo(codigo) == "No existe":
        print("****El código que desea eliminar no existe****")
    else:
        eleccion = input("¿Está seguro? (Sí=S, No=N): ")
        eleccion = eleccion.upper()
        if eleccion == "S":
            FuncionEliminar(codigo)
            print("Producto eliminado con éxito.")

def FuncionEliminar(codigo):
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


def BuscarProductoPorCodigo():
    codigo = input("Ingrese el código del producto que desea buscar: ")
    if ExisteCodigo(codigo) == "No existe":
        print("****El código que desea buscar no existe****")
    else:
        FuncionBuscarCodigo(codigo)
        
def FuncionBuscarCodigo(codigo):
    with open('./stock/inventario.csv', 'r') as File:
        reader = csv.DictReader(File)
        for row in reader:
            if row["codigo"] == codigo:
                print(""+ str(row["codigo"])+ "\t" + str(row["producto"]) + "\t" + str(row["marca"]) + "\t" + str(row["precio"])+ "\t" + str(row["codigo_barra"]))



def BuscarProductoPorNombre():
    df = pd.read_csv("./stock/inventario.csv")
    palabra = input("Ingrese el nombre del producto que desea buscar: ")
    resultado = df[df["producto"].apply(lambda x: palabra in x)]
    if not resultado.empty:
        print(resultado)
    else:
        print("****Ese producto no se encuentra en el stock****")
        

def generadorDeCodigo():
    numero = random.randint(10**11, (10**12)-1)
    return str(numero)




               
def main():
    while True:
        opcion = Menu()
        if opcion == "1":
            limpiar_consola()
            VerStock()
        elif opcion == "2":
            limpiar_consola()
            NuevoProducto()
        elif opcion == "3":
            limpiar_consola()
            ModificarProducto()
        elif opcion == "4":
            limpiar_consola()
            EliminarProducto()
        elif opcion == "5":
            limpiar_consola()
            BuscarProductoPorCodigo()
        elif opcion == "6":
            limpiar_consola()
            BuscarProductoPorNombre()
        elif opcion == "7":
            limpiar_consola()
            ModificarCantidadProducto()
        elif opcion == "8":
            limpiar_consola()
            ruta_imagen = str(input("Ingrese la ruta del código de barra: "))
            leer_codigo_desde_imagen(ruta_imagen)
        elif opcion == "9":
            limpiar_consola()
            leer_codigo_desde_camara()
        elif opcion == "10":
            break
    return
    
    


main()
