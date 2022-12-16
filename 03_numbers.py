#prioridad de operadores
#https://j2logo.com/python/tutorial/operadores-en-python/#:~:text=Prioridad%20de%20los%20operadores%20en%20Python,-Al%20igual%20que&text=Este%20orden%20es%20el%20siguiente,prioridad%20que%20en%20las%20matem%C3%A1ticas).
print((8 / 2) + 4 * 8 )

lives = 5

lives = lives - 1 # 4
print(lives)
lives -= 2 #2
print(lives)
lives += 9 #11
print(lives)

ene = 100
feb = 140
mar = 29
prom = ene + feb + mar
print(prom)
res = prom / 3
print(f"el resultado es: {res}")

#FLOAT
y = 1.1 + 2.2
x = 3.3
#el resultado es 3.3000000000000003
print(y)
#Para recortarlo podemos usar la función format.
#esto no es lo correcto
y_str = format(y, ".2g")
#format es un string
print(type(y_str), f"el valor es {y_str}")
y_str = float(y_str)
print(type(y_str))

#la forma correcta de recortarlo es:

#forma matematica
#en este caso se usó una tolerancia
tolerance = 0.00001
#restamos x - y y cambiamos el valor apositivo con abs (sino el resultado sería negativo)
#abs obtiene el valor absoluto y lo combierte a positivo
print(abs(x - y))
#si el valor es menor a la tolerancia que le asignamos quiere decir que la resta es igual
#aquí lo que se tiene es un márgen de tolerancia
print(abs(x - y) < tolerance)

#otra forma con round

y = round(1.1 + 2.2, 1)
print(y == x)
