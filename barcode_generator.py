from barcode import EAN13
from barcode.writer import ImageWriter
import random

def generadorDeCodigo():
    global numero_random
    numero_random = random.randint(10**11, (10**12)-1)
    return str(numero_random)
from barcode import EAN13
from barcode.writer import ImageWriter

def BarcodeGenerator(codigo_de_barras, nombre_cod):
    nombre_codigo = nombre_cod
    carpeta_destino = "fotos_codigos" 
    codigo = EAN13(codigo_de_barras, writer=ImageWriter())
    ruta_completa = f"{carpeta_destino}/{nombre_codigo}"
    return codigo.save(ruta_completa)



