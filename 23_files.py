file = open('./text.txt')
#leer el doc
print(file.read())

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

#es mejor iterar el archivo con un for para usar menos memoria
for line in file:
    print(line)

#es necesario cerrar el archivo para liberar memoria
file.close()



#otra manera de leer el archivo y la forma correta es esta:
with open('./text.txt') as archivo:
    for linea in archivo:
        print(linea)




