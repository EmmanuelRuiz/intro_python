"""
Listas == Array
Puede guardar varios tipos de datos
Es mutable

"""
numbers = [1, 2, 3,4]
tareas = ["Lavar", "cocinar"]
types = [1, True, "hola"]

print(numbers[1])
tareas[1] = "jugar"
print(tareas)
print(numbers[:3])

#saber si haya un valor en el array
print("Lavar" in tareas)
print(True in types)

"""
TUPLA ==
una tupla es inmutable, 
a diferencia de las listas que son mutables.
"""
numbers = (1, 2, 3, 4, 5)
strings = ("nico", "emma", "david")
print(numbers)
print("posición 0 =>", numbers[0])
print("última posición =>", numbers[-1])
print(type(numbers))

#conocer la posición de un valor
print(strings.index("emma"))
#conocer cuantas veces hay un valor en la tupla
print(strings.count("emma"))

#convertir una tupla a lista
my_list = list(strings)
print(my_list)

my_list[1] = "juli"
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

#transformar una lista a un array
my_tuple2 = tuple(my_list)
print(my_tuple2)
#Esos valores puede ser 'desempaquetados' y asignados a variables individuales.



"""
SET/Conjunto 
No tiene elementos duplicados
No tiene un orden
Se puede modificar
Se puede conbinar con otros conjuntos
"""
set_countries = {"col", "mex", "bol"}

#los datos que se repitan se eliminan
set_numbers = {1, 2, 2, 3, 4, 5}
print(set_numbers)

#se pueden agregar varios tipos de datos
set_types = {1, "hola", False, 12.12}

set_from_string = set("hoola")
print(set_from_string)

set_from_tuples = set(("abc", "cbv" , "sas", "abc"))

#puedo convertir una lista de números en un conjunto
numbers = [1,2,3,4,5,5,6]
set_numbers = set(numbers)
print(set_numbers)
# ese conjunto de numeros lo podemos convertir a una lista.
unique_numbers = list(set_numbers)
print(unique_numbers)

set_countries = {"col", "mex", "bol"}

size = len(set_countries)
print(size)

print("col" in set_countries)
print("pe" in set_countries)

#agregar un registro al conjunto, si ya existe ese conjunto no lo agregará
set_countries.add("pe")
print(set_countries)

set_countries.update({"ar", "ecua", "pe"})
print(set_countries)

#con remove podemos eliminar un elemento del conjunto, pero si este no existe nos dará un error
set_countries.remove("col")
print(set_countries)

#con discard podemos eliminar un elemento del conjunto y este no marca error
set_countries.discard("ar")

#borrar todo el contenido del conjunto
set_countries.clear()
print(set_countries)


set_a = {"col", "mex", "bol"}
set_b = {"pe", "bol"}

#unir dos conjuntos
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#mostrar los elementos que tienen en comun, los que crean la intersección
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#hallar la diferencia entre el conjunto a y b, quitarle a a los elementos de b
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#diferencia simetrica, es hacer una unión excluyendo del resultado los elementos en común
set_c = set_a.symmetric_difference(set_b)
print(set_a ^ set_b)

