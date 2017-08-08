#IMPORTING THE INFO
import csv
import pytest

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

#CHECKING DATATYPE
# type_check = forecast[1]["date"]
# print(type(type_check))

#MESSAGE AND TO DETERMINE THRIFT DATE (COMMENT 41-68 FOR PYTEST)
intro = """
-----------------------------------------------
THRIFT/STOCK CALCULATION APPLICATION OVERVIEW
-----------------------------------------------
This database calculates the (1) balance of inventory (stock), (2) forecast/sales balance,
and (3) the thrift (amount of product that will not sell due to code life) given the inputs.

The application will stop after either (a) all of the stock is gone or (b) the forecast is covered.

Below is the high level desciption of the application:

Part                            | DESCRIPTION
---------------------------     | ------------------
'Part1: Inputs                  | Inputs are the forecast and inventory/stock in CSV files in the 'DATA' folder
'Part2: Input(prompted below)   | Enter in the minimum number of weeks of code life required to sell/send to the stores.
'Part3: Output a display        | The output will display (1) stock balance, (2) forecast balance, and (3) projected thrift.
'Part4" Output CSV              | The output from Part3 will be written into CSV files in the EXPORT folder.

IMPORTANT NOTE:
***Read the "README" file for header definitions and other information (i.e. pytest)***

-----------------------------------
    INPUT INSTRUCTIONS
-----------------------------------
Enter the minimum weeks of code life on a product allowed to ship to the customer.
Type an integer value (suggested values are 7', '8', or '9'):
"""
min_code_wks = input(intro)

# UNCOMMENT FOR PYTEST AND COMMENT FOR RUN
# min_code_wks = 7

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

## FUNCTIONS
#CREATE THRIFT TABLE AND CHECKING FOR THRIFT
thrift_table = []

def adj_thrift():
    if len(new_forecast1) == 0:
        print("No remaining forecast")
    else:
        date_check = new_forecast1[0]['date']
        for i in new_stock1:
            i['date_thrifting'] = date_check
            if i['thrift'] < date_check:
                thrift_short_term = []
                thrift_table.append(i)
                thrift_short_term.append(i)
                for v in thrift_short_term:
                    del_item = next((item for item in new_stock1 if item['id'] == v['id']), None)
                    index_num = new_stock1.index(del_item)
                    new_stock1.pop(index_num)
            else:
                pass
#CALC DECISION
def calc():
    balance = new_stock1[0]['qty'] - new_forecast1[0]['fct']
    if balance == 0:
        del new_forecast1[0]
        del new_stock1[0]
    elif balance > 0:
        del new_forecast1[0]
        new_stock1[0]['qty'] = balance
    else:
        new_forecast1[0]['fct'] = balance * -1
        del new_stock1[0]

#FOR PRINTING THRIFT
def check_if_thrift():
    if len(thrift_table) == 0:
        print("-----------------------------------------------")
        print("THRIFT: NO THRIFT OCCURRED!  NO THRIFT INFORMATION TO SHARE!")
    else:
        print("-----------------------------------------------")
        print("THRIFT")
        print("     Projected thrifted product is:")
        for p in thrift_table:
            print("  +", dict(p))

#CALCULATE
while len(new_stock1) != 0 and len(new_forecast1) != 0:
    adj_thrift()
    calc()

#RESULTS
if len(new_stock1) == 0:
    print("-----------------------------------------------")
    print("STOCK: STOCK WAS DEPLETED! NO STOCK INFO TO SHARE!")
    print("-----------------------------------------------")
    print("FORECAST:")
    print("     Remaining forecasted sales are/is:")
    for p in new_forecast1:
        print("  +", dict(p))
        # print("  +" + " material: " + p['material'] + " description: " + p['description'] + " plant: " + p['plant'] + " date: " + p['date'] + " forecast qty: " + p['qty'])
    check_if_thrift()
elif len(new_forecast1) == 0:
    print("-----------------------------------------------")
    print("FORECAST: FORECAST WAS COVERED!  NO FORECAST TO SHARE!")
    print("-----------------------------------------------")
    print("STOCK")
    print("     Projected Stock Balance is:")
    for p in new_stock1:
        print("  +", dict(p))
        # exp_format = str(p['exp'])
        # print("  +" + " material: " + p['material'] + " description: " + p['description'] + " plant: " + p['plant'] + " Expiration date: " + exp_format + " Stock qty: " + p['qty'] + " Thrift date: " + p['thrift'])
    check_if_thrift()
else:
    print("-----------------------------------------------")
    print("FORECAST: Remaining forecasted sales are/is:")
    for p in new_forecast1:
        print("  +", dict(p))
    print("-----------------------------------------------")
    print("STOCK: Projected Stock Balance is:")
    for p in new_stock1:
        print("  +", dict(p))
    check_if_thrift()


# TEST CALCULATE
# adj_thrift()
# calc()
# adj_thrift()
# calc()

# print("new_forecast1")
# print(new_forecast1)
# print("new_stock1")
# print(new_stock1)
# print("thrift")
# print(thrift_table)

#EXPORT CSV FILE
csv_output_path = "EXPORT/THRIFT.csv"
dict_list = thrift_table

with open(csv_output_path, 'w') as f:
    fieldnames = ['material', 'description', 'plant', 'exp', 'qty', 'thrift', 'id', 'date_thrifting']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for p in dict_list: #to loop through each statement
        writer.writerow(p)

csv_output_path = "EXPORT/FORECAST_BALANCE.csv"
dict_list = new_forecast1

with open(csv_output_path, 'w') as f:
    fieldnames = ['material', 'description', 'plant', 'date', 'fct', 'id']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for p in dict_list: #to loop through each statement
        writer.writerow(p)

csv_output_path = "EXPORT/STOCK_BALANCE.csv"
dict_list = new_stock1

with open(csv_output_path, 'w') as f:
    fieldnames = ['material', 'description', 'plant', 'exp', 'qty', 'thrift', 'id']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for p in dict_list: #to loop through each statement
        writer.writerow(p)

print("-----------------------------------------------------------------------------------------")
print("THRIFT.CSV, STOCK_BALANCE.CSV, AND FORECAST_BALANCE.CSV ARE UPDATED IN THE 'EXPORT' FOLDER.")
print("-----------------------------------------------------------------------------------------")

#FOR PYTEST ONLY
def fct_result():
    return new_forecast1[0]["fct"]

def test_fct_result():
    result = fct_result()
    assert result == 50
# t_variable = fct_result()
# print (t_variable)

# if __name__ == "__main__": # "if this script is run from the command-line"
#     fct_result()
















#
