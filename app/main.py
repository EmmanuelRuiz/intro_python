import utils 

keys, values = utils.get_population()
print(keys, values)

#print(utils.A)

data = [
    {
        'Country': 'Colombia',
        'Population': 100
    },
    {
        'Country': 'Peru',
        'Population': 300
    }

]
country = input("ingresa el país=> ").title()
result = utils.population_by_country(data, country)
print(result)