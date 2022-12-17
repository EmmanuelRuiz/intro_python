#recibimos el diccionario con el país elegido
def get_population(country_dict):
    print(f"country_dict contiene {country_dict}")
    population_dict = {
        '2022' : int(country_dict['2022 Population']),
        '2020' : int(country_dict['2020 Population']),
        '2015' : int(country_dict['2015 Population']),
        '2010' : int(country_dict['2010 Population']),
        '1990' : int(country_dict['1990 Population']),
        '1980' : int(country_dict['1980 Population']),
        '1970' : int(country_dict['1970 Population'])
    }
    #guardar el nombre de la columna
    labels = population_dict.keys()
    values = population_dict.values()
    print(f"labels {labels}, values {values}")
    return labels, values

def population_by_country(data, country_choosen):
    result = list(filter(lambda item: item['Country/Territory'] == country_choosen, data))
    return result