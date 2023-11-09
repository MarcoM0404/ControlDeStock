from lector_camara_barcode import leer_codigo_desde_camara
from lector_barcode import leer_codigo_desde_imagen
from agregar_producto import nuevo_producto
from modificar_productos import modifica_productos, modificar_cantidad_producto
from eliminar_producto import eliminar_producto
from buscar_productos import buscar_producto_por_nombre, buscar_productos_por_codigo
from menu import menu_opciones, limpiar_consola, ver_stock
from csv_ordenado import ordenar_stock, imprimir_stock_ordenado
               
def main():
    while True:
        opcion = menu_opciones()
        if opcion == "1":  
            ver_stock()
        elif opcion == "2":
            nuevo_producto()
        elif opcion == "3":
            modifica_productos()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_productos_por_codigo()
        elif opcion == "6":
            buscar_producto_por_nombre()
        elif opcion == "7":
            modificar_cantidad_producto()
        elif opcion == "8":
            leer_codigo_desde_imagen()
        elif opcion == "9":
            leer_codigo_desde_camara()
        elif opcion == "10":
            limpiar_consola()
            ordenar_stock()
            imprimir_stock_ordenado()
        elif opcion == "11":
            limpiar_consola()
            break
    return
    
    


main()
