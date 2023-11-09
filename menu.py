import os
import csv
from tabulate import tabulate
def menu_opciones():
    print("╔═════════════════════════════════════════════╗")
    print("║     MENÚ DEL CONTROL DE STOCK               ║")
    print("╠═════════════════════════════════════════════╣")
    print("║ 1. Ver todo el stock                        ║")
    print("║ 2. Añadir producto                          ║")
    print("║ 3. Modificar producto                       ║")
    print("║ 4. Eliminar producto                        ║")
    print("║ 5. Buscar producto por código               ║")
    print("║ 6. Buscar producto por nombre               ║")
    print("║ 7. Modificar cantidad del producto          ║")
    print("║ 8. Leer código de barra con ruta de imagen  ║")
    print("║ 9. Leer código de barra con imagen          ║")
    print("║ 10. Ordenar stock por cantidades            ║")
    print("║ 11. Salir                                   ║")
    print("╚═════════════════════════════════════════════╝")

    opcion = input("Ingrese la opción que desea acceder: ")
    limpiar_consola()
    return opcion

    
    

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')



def ver_stock():
    limpiar_consola()
    
    with open("./stock/inventario.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # con esta variable la primer fila pasa a ser el encabezado
        data = [row for row in reader] #las demas filas pasan a formar parte de los datos del encabezado

    if not data:
        print("El archivo de inventario está vacío.")
        input("Presiona Enter para continuar")
        return

    print(tabulate(data, headers=headers, tablefmt='fancy_grid'))# uso "tabulate" para que lo haga en forma de tabla y el tablefmt es el formato, el "pretty" esta bueno tambien

    input("*** Presiona Enter para continuar ***")
    limpiar_consola()
