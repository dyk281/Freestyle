import csv

stock = [] #1. create empty list called product
csv_file_path = "data/stock.csv"
# READ PRODUCTS CSV
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) #using csv.DictReader function, each row will be dictionary like
    for row in reader:
        stock.append(row) #append each "row" to "products"

forecast = [] #1. create empty list called product
csv_file_path = "data/forecast.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) #using csv.DictReader function, each row will be dictionary like
    for row in reader:
        forecast.append(row)

print (stock)
print (forecast)
