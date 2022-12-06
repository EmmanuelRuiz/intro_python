
#este import nos da el path en dond se ejecuta el archivo.
import sys
print(sys.path)

#este import nos trae expresiones regulares.
import re
text = 'mi número de teléfono es 999 2 2 2 222 111 y tengo 26 años y  el código de pais es 57'
result = re.findall('[0-9]+', text)
print(result)

import time 
timestamp = time.localtime()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)


#retorna un diccionario con la cantidad de veces que se repite un número
import collections
numbers = [1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,2,1]