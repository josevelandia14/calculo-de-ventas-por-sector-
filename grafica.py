import matplotlib.pyplot as plt


def generate_bar_chart():
    labels = input("Escribe los labels de la gráfica separados por coma: ").split(',')
    values = [float(val.strip()) for val in input("Escribe los valores de la gráfica separados por coma: ").split(',')]
    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.xlabel('Industrias')
    plt.ylabel('Cantidad')
    plt.title('Gráfico de Barras')
    plt.show()

generate_bar_chart()
