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
def run():
    country = input("ingresa el país=> ").title()
    result = utils.population_by_country(data, country)
    print(result)

#si es ejecutado desde la terminal que ejecute el metodo run(), pero si es ejecutado
#desde otro archivo no va a ejecutar el código.
if __name__ == '__main__':
    run()