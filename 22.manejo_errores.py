try: 
    #esta operación genera error, por lo que detendría la ejecución
    #con try hacemos que no se detenga y con except podemos detectar el error
    print(0 / 0)
except ZeroDivisionError as error:
    print(error)

try:
#assert tiene la funcionalidad de que si falla el error podemos imprimir un mensaje
#pero assert genera un error de tipo assertion  
    assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores')
except Exception as error:
    print(error)

#lo mismo pero más corto
try:
    print(0 / 0)
    assert 1 != 1, 'uno no es diferente de uno'
    age = 10
    if age < 19:
        raise Exception('no se permiten menores')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)
    