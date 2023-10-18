import matplotlib.pyplot as plt
import pandas as pd

def filtro_de_departapento (departamento,data):
    resultado_de_filtro = list(filter(lambda x: x["n_departamento"] == departamento,data))
    return resultado_de_filtro

def get_industry(resultado_de_filtro):
    industrias_unicas = set(item["ntipo_negocio"] for item in resultado_de_filtro)
    return list(industrias_unicas)

def sumar_por_industrias(data, industria_De_santander):
    resultados = {}
    for industria in industria_De_santander:
        resultados[industria] = 0
    for diccionario in data:
        for clave, valor in diccionario.items():
            if clave == "ntipo_negocio" and valor in industria_De_santander:
                cantidad = float(diccionario["cantidad"])
                resultados[valor] += cantidad 
    return resultados

