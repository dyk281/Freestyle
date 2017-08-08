# Freestyle
#PURPOSE
  The purpose of this application is to calculate the amount of stock that will expire at a single location provided inventory/stock, a weekly forecast, and code dates (dates the product will expire).  

  This program works for a SINGLE site/location and SINGLE item/material but CAN be expanded to multiple locations and products IN THE FUTURE.
  This program PRESUMES that the weekly sales will all happen on the Monday of the week.  Further expansion is needed to deal with products that will expire mid-week.

  The primary program is named "freeapp.py" in the "APP" folder.

#EXPECTATIONS BEFORE RUNNING
  +ADJUSTMENT TO THE IMPORTED CSV FILES CAN BE DONE BUT IT IS ADVISED TO CONSULT WITH DAVID KWAK IF ERRORS ARISES
  +THE ONLY PROMPT IS TO DETERMINE THE MINIMUM NUMBER OF WEEKS THE PRODUCT REQUIRES TO SHIP FROM THE PLANT. TYPE IN AN INTEGER PREFERABLY BETWEEN 7 & 9 TO REPRESENT 7, 8, OR 9 WEEKS OF CODE LEFT ON THE PRODUCT SHIPPING TO STORES.
  +THE MATERIAL NUMBER MAY NEED TO BE ADJUSTED VIA TEXT-TO-COLUMNS OR USE A SINGLE QUOTE IN FRONT (WITH THE LATTER BEING THE PREFERRED METHOD)

#PYTEST
TO RUN PYTEST, ONE MUST COMMENT ROWS 41-68 AND UNCOMMENT ROW 71.  

#OTHER NOTES
  #import modules were not grouped as when doing so, the program failed.

#DEFINITION FOR KEYS IN DICTIONARIES
  FORECAST DICTIONARIES:
    +material       =   material number for the product
    +description    =   description of the material/product
    +plant          =   4 digit code representing a location
    +date           =   date of Monday of the week's sale
    +fct            =   the forecasted quantity for the given week
    +id             =   unique identifier for the application only

  THRIFT DICTIONARIES:
    +material       =   material number for the product
    +description    =   description of the material/product
    +exp            =   expiration date printed on the product (last day consumers will eat)
    +qty            =   quantity of product being thrifted
    +thrift         =   the last day/date that the product can be sold to stores ( dictated number of weeks prior to "exp")
    +date thrifting =   the date the product was identified to be thrifted

  STOCK DICTIONARIES:
    +material       =   material number for the product
    +description    =   description of the material/product
    +exp            =   expiration date printed on the product (last day consumers will eat)
    +qty            =   quantity of product being thrifted
    +thrift         =   the last day/date that the product can be sold to stores ( dictated number of weeks prior to "exp")
