import csv
import funciones
import grafica


limite = 1000
contador = 0

def leer_csv(archivo):
    global contador
    data = []
    with open(archivo, "r", encoding="utf-8") as ventas:
        read = csv.reader(ventas, delimiter=";")
        nombre_de_columnas = next(read)
        for row in read:
            if contador >= limite:
                break
            iterable = zip(nombre_de_columnas, row)
            dic_de_data = {key: value for key, value in iterable}
            data.append(dic_de_data)
            contador+= 1
    return data

if __name__ == "__main__":
    data = leer_csv("INTERMEDIO DE PYTHON//proyecto_de_ecenarios//data_ventas_2020_2022_with_dates (1).csv")

departamento = input("digite depertamento en mayuscula=> ")

filtro_De_Departamento = funciones.filtro_de_departapento(departamento,data)


industria_De_santander = funciones.get_industry(filtro_De_Departamento)
print(industria_De_santander)

cantidad_de_ventas_por_industria= funciones.sumar_por_industrias(filtro_De_Departamento,industria_De_santander)
print(cantidad_de_ventas_por_industria)


grafica.generate_bar_chart()


