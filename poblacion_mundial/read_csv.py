import csv

#función leer csv
def read_csv(path):
    #el delimitador en esta ocación es "," 
    #r es el permiso para leer
    with open(path, 'r') as csvfile:
        #este es el lector
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

       
#ejecutar como script desde la terminal
if __name__ == '__main__':
    data = read_csv('./data.csv')
    print(data[1])