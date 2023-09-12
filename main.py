import pandas as pd
import csv

def Menu():
    print("*****MENÚ DEL CONTROL DE STOCK*****")
    print("1. Ver todo el stock ---------------------- 2. Añadir producto")
    print("3. Modificar producto --------------------- 4. Eliminar producto")
    print("5. Buscar producto por código ------------- 6. Buscar producto por nombre")
    print("7. Salir")
    opcion = str(input("Ingrese la opción que desea acceder: "))
    return opcion
    
def ExisteCodigo(codigo):
    with open("./stock/inventario.csv") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if (codigo == row["codigo"]):
                return row
    return "No existe"
            
def VerStock():
    df = pd.read_csv("./stock/inventario.csv", engine="python")
    print(df)

def NuevoProducto():
    codigo = input("Ingrese el código de producto nuevo: ")
    if ExisteCodigo(codigo) == "No existe":
        producto = input("Ingrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        precio = input("Ingrese el precio del producto: ")
        with open ("./stock/inventario.csv", "a") as File:
            File.write("\n"+codigo+","+producto+","+marca+","+precio)
    else:
        print("****El código ya existe****")
        

def ModificarProducto():
    codigo = input("Ingrese el código del producto que desea modificar: ")
    if ExisteCodigo(codigo) == "No existe":
        print("****El codigo que desea modificar no existe****")
    else:
        producto = input("Ingrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        precio = input("Ingrese el precio del producto: ")
        FuncionModificar(codigo, producto, marca, precio)
        
        
def FuncionModificar(codigo, producto, marca, precio):
    result = []
    with open('./stock/inventario.csv', newline="") as File:
        reader = csv.DictReader(File)
        rows = list(reader)
        for row in rows:
            if row["codigo"] == codigo:
                row["producto"] = producto
                row["marca"] = marca
                row["precio"] = precio
            result.append(row)
    
    with open("./stock/inventario.csv", "w") as File:
        fieldnames = ["codigo", "producto", "marca", "precio"]
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
        fieldnames = ["codigo", "producto", "marca", "precio"]
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
                print(""+ str(row["codigo"])+ "\t" + str(row["producto"]) + "\t" + str(row["marca"]) + "\t" + str(row["precio"]))


import pandas as pd

def BuscarProductoPorNombre():
    df = pd.read_csv("./stock/inventario.csv")
    palabra = input("Ingrese el nombre del producto que desea buscar: ")
    resultado = df[df["producto"].apply(lambda x: palabra in x)]
    print(resultado)

def main():
    while True:
        opcion = Menu()
        if opcion == "1":
            VerStock()
        elif opcion == "2":
            NuevoProducto()
        elif opcion == "3":
            ModificarProducto()
        elif opcion == "4":
            EliminarProducto()
        elif opcion == "5":
            BuscarProductoPorCodigo()
        elif opcion == "6":
            BuscarProductoPorNombre()
        elif opcion == "7":
            break
    return
    
    

main()