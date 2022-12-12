#cuando usamos open viene por defecto el permiso de lectura (r)
#con r+ podemos escribir y leer un archivo
#con w+ podemos escribir y leer una archivo pero el contenido se eliminará
with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('esta es una nueva linea\n')
    file.write('esta es una nueva linea\n')
    file.write('esta es una nueva linea\n')


