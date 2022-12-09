for i in range(1,11):
    print(i)


#con next podemos ir iterando cada valor del rango.
#pero al llegar al límite del rango nos dará error
my_iter = iter(range(1,11))
print(my_iter)
print(next(my_iter))