import csv

examplearquivo = open('example.csv')
exampleReader = csv.reader(examplearquivo)
exampleData = list(exampleReader)
exampleData


