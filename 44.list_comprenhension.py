days = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']

days_with_a = []
for i in days:
    if 'a' in i:
        days_with_a.append(i)

print(days_with_a)

#[element for element in iterable]
list_comprenhension = [day for day in days if 'a' in day]
print(list_comprenhension)

