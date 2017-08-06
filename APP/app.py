
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
# import time

import os
from datetime import datetime, timedelta

for i in stock:
    i['exp'] = datetime.strptime(i['exp'],"%m/%d/%y")
for i in stock:
    i['qty'] = int(i['qty'])
for i in forecast:
    i['date'] = datetime.strptime(i['date'],"%m/%d/%y")
for i in forecast:
    i['fct'] = int(i['fct'])
#TEST CHANGE DATATYPE
# type_check = forecast[1]["date"]
# print(type(type_check))

#CALC THE THIFT DATE
min_code_wks = input("Enter minimum weeks of code to ship:  ")
min_code_days = int(min_code_wks) * 7

import datetime

for i in stock:
    date_exp = i['exp']
    i['thrift'] = date_exp - datetime.timedelta(days=min_code_days)


#SORT LIST
from operator import itemgetter

new_stock = sorted(stock, key=itemgetter('thrift'))
#TEST SORT LIST
print(stock)
print(new_stock)
























#
