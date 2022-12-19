#{key:value for var in iterable}

dict = {}
for i in range(1,5):
    dict[i] = i * 2
    
print(dict)

dict2 = { i : i * 2 for i in range(1,5)}
print(dict2)