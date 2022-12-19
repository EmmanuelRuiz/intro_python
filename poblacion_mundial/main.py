import read_csv
import charts

def run():
    data = read_csv.read_csv('./data.csv')
    countries = list(map(lambda x : x['Country/Territory'], data))
    percentajes = list(map(lambda x : x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentajes)

if __name__ == '__main__':
    run()