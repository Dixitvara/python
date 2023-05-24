import csv
with open('python/excel.csv') as csvfile:
    file = csv.reader(csvfile, delimiter=' ')
    for row in file:
        print(', '.join(row))