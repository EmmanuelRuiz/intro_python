"""
1. importar matplotlib
"""
import matplotlib.pyplot as plt
#generar gráfica de barras
def generate_bar_chart(labels, values):
    #estas dos vars me las da matplotlib
    figure, coordenate =  plt.subplots()
    #indicar que quiero una gráfica de barras
    coordenate.bar(labels, values)
    plt.show()
#generar gráfica de pay
def generate_pie_chart(labels, values):
    figure, coordenate = plt.subplots()
    #en el caso de pie chart, el label se envía así
    coordenate.pie(values, labels = labels)
    #indicar que organice la gráfica en el centro y que sea en forma de circulo
    coordenate.axis('equal')
    plt.show()



if __name__ == '__main__':
    #datos para la gráfica
    labels = ['a', 'b', 'c']
    values = [100, 200, 300]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)