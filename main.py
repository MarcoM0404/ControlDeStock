from lector_camara_barcode import leer_codigo_desde_camara
from lector_barcode import leer_codigo_desde_imagen
from agregar_producto import NuevoProducto
from modificar_productos import ModificarProducto, ModificarCantidadProducto
from eliminar_producto import EliminarProducto
from buscar_productos import BuscarProductoPorCodigo, BuscarProductoPorNombre
from menu import Menu, limpiar_consola, VerStock

               
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
            ruta_imagen = input("Ingrese la ruta del código de barra: ")
            leer_codigo_desde_imagen(ruta_imagen)
        elif opcion == "9":
            limpiar_consola()
            leer_codigo_desde_camara()
        elif opcion == "10":
            limpiar_consola()
            break
    return
    
    


main()
