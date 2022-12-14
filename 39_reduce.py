"""
La función reduce()

reduce() es una función incorporada de Python 2, que toma como argumento un conjunto de valores (una lista, una tupla, o cualquier objeto iterable) y lo “reduce” a un único valor. Cómo se obtiene ese único valor a partir de la colección pasada como argumento dependerá de la función aplicada.

Por ejemplo, el siguiente código reduce la lista [1, 2, 3, 4] al número 10 aplicando la función accum(counter, item), que retorna la suma de sus argumentos.
"""

import functools

numbers = [1,2,3,4,5]

reduce = functools.reduce(lambda counter, item: counter + item, numbers)
print(reduce)