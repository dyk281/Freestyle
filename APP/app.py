#IMPORTING THE INFO
import csv

stock = [] #1. create empty list called product
csv_file_path = "data/stock.csv"
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

#CHANGE DATATYPE
import os
from datetime import datetime, timedelta

for i in stock:
    i['exp'] = datetime.strptime(i['exp'],"%m/%d/%y")
for i in stock:
    i['qty'] = int(i['qty'])
for i in stock:
    i['material'] = str(i['material'])
for i in forecast:
    i['date'] = datetime.strptime(i['date'],"%m/%d/%y")
for i in forecast:
    i['fct'] = int(i['fct'])
for i in forecast:
    i['material'] = str(i['material'])
#TEST CHANGE DATATYPE
# type_check = forecast[1]["date"]
# print(type(type_check))

#CALC THE THIFT DATE
min_code_wks = input("Enter the minimum weeks of code life allowed to ship (suggested values are 6, 7, 8, or 9):  ")
min_code_days = int(min_code_wks) * 7
import datetime
for i in stock:
    date_exp = i['exp']
    i['thrift'] = date_exp - datetime.timedelta(days=min_code_days)

#SORT LIST
from operator import itemgetter
new_stock1 = sorted(stock, key=itemgetter('thrift'))
new_forecast1 = sorted(forecast, key=itemgetter('date'))
#TEST SORT LIST
# print(forecast)
# print(new_forecast1)
# print(stock)
# print(new_stock1)

#INSERT ID/BATCH #
for i in new_stock1:
    i['id'] = new_stock1.index(i) + 1
for i in new_forecast1:
    i['id'] = new_forecast1.index(i) + 1
#TEST ADDING ID
# print(new_stock1)
# print(new_forecast1)

# CHECK IF THRIFT
thrift_table = []
if len(new_forecast1) == 0:
    print("No remaining forecast")
else:
    date_check = new_forecast1[0]['date']
    for i in new_stock1:
        i['date_thrifting'] = date_check
        if i['thrift'] < date_check:
            thrift_table.append(i)

for v in thrift_table:
    del_item = next((item for item in new_stock1 if item['id'] == v['id']), None)
    index_num = new_stock1.index(del_item)
    new_stock1.pop(index_num)
# thrift_id = int(thrift_table["id"])
# print(thrift_id)

# def lookup_product(stock_id, new_stock1):
#     matching_products = [p for p in new_stock1 if int(p["id"]) == int(product_id)]
#     return matching_products[0]
# def destroy_product(products):
#     product_id = user_inputs_product_id()
#     try:
#         product = lookup_product(product_id, products)
#         del products[products.index(product)]
#         print("DESTROYING A PRODUCT HERE!")
#         print(product)
#         return product
#     except IndexError as e:
#         handle_index_error()

#TEST THRIFT thrift_table

print("THESE ARE THE ITEMS THRIFTING:")
print(thrift_table)

print("THESE ARE THE ITEMS IN STOCK STILL:")
print(new_stock1)




















#
