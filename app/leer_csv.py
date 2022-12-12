import csv

#función leer csv
def read_scv(path):
    #el delimitador en esta ocación es "," 
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
    data = read_scv('./data.csv')
    print(data[0])