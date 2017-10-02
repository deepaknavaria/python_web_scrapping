import csv

#opening csv file
f = open('products.csv')

#reading it and passing it to an object
csv_f = csv.reader(f)

#printing all columns using for interation
for col in csv_f:
    print(col)

#closing the file
f.close()
