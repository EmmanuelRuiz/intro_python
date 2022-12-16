age = input('¿Cuál es tu edad? ')
print('age es tipo: ', type(age)) #string
print('Mi edad es ', str(age))

age = int(age)
age = age + 10
print(f'tu edad en 10 años es {age}')

original = [1,2,3,4,5] 
new = list(map(lambda x : x * 2, original))
print(new

)
a = {1,2}
b = {2,3}
print(a | b)