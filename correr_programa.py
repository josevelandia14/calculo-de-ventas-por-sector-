    
import leer_Archivo
import convirtiendo_en_dic

def correr():
    colunmas, data_leido = leer_Archivo.leer("INTERMEDIO DE PYTHON//proyecto_de_ecenarios//data_ventas_2020_2022_with_dates (1).csv")
    dic_de_data = convirtiendo_en_dic.dic_data(colunmas, data_leido)
    print(dic_de_data)

if __name__ == "__main__":
    correr()
