def get_population():
    keys = ['col', 'mx']
    population = [300,400]
    return keys, population

#A = "hola"



def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country,data ))
    return result
    