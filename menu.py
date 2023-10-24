import os
import pandas as pd

def Menu():
    print("*****MENÚ DEL CONTROL DE STOCK*****")
    print("1. Ver todo el stock ---------------------- 2. Añadir producto")
    print("3. Modificar producto --------------------- 4. Eliminar producto")
    print("5. Buscar producto por código ------------- 6. Buscar producto por nombre")
    print("7. Modificar cantidad del producto -------- 8. Leer código de barra con ruta de imagen")
    print("9. Leer código de barra con imagen -------- 10. Salir")
    opcion = input("Ingrese la opción que desea acceder: ")
    limpiar_consola()
    return opcion
    
    

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def VerStock():
    df = pd.read_csv("./stock/inventario.csv", engine="python")
    print(df)