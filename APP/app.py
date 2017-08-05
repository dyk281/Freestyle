import csv

stock = [] #1. create empty list called product

csv_file_path = "data/products.csv"

# READ PRODUCTS CSV

#we will loop through each product
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) #3. using csv.DictReader function, each row will be dictionary like
    for row in reader: #2. when reading the file, iterating through each "row"
    #each row corresponds to a product
        products.append(row) #4 append each "row" to "products"
