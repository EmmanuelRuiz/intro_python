import utils
import read_csv
import charts

def run():
    data = read_csv. read_csv('./data.csv')
    country_choosen = input('Elige un país: ')
    result = utils.population_by_country(data, country_choosen)
    if len(result) > 0:
        #si encontramos el país lo guardamos en una var.
        print(f'result {result[0]}')
        country = result[0]
        #print(f"la var country tiene {country[0]} y la posición 0 es = {country}")
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)


if __name__ == '__main__':
    run()