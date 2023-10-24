from existencias_codigos import ExisteCodigo
import pandas as pd
import csv

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
        
