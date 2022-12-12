import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    #obtener variables de la librería
    #fig es la figura y ax las cordenadas de graficacion

    fig, ax = plt.subplots()
    #grafica de barras
    ax.bar(labels, values)
    plt.show()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 100, 180]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)