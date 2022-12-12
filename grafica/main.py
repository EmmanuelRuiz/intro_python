import utils
import leer_csv
import charts

def run():
    data = leer_csv.read_csv('./data.csv')
    country = input('Selecciona un país ')

    result = utils.population_by_country(data, country)
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
    run()