# Freestyle
#PURPOSE
  The purpose of this application is to calculate the amount of stock that will expire at a single location provided inventory/stock, a weekly forecast, and code dates (dates the product will expire).  

  This program is setup for expansion is dealing with multiple locations and products IN THE FUTURE but CURRENTLY only works for a single site and single item.
  This program PRESUMES that the weekly sales will all happen on the Monday of the week.  Further expansion is needed to deal with products that will expire mid-week.

  The program is (poorly) named "app.py" in the "APP" folder.

#EXPECTATIONS BEFORE RUNNING
  +ADJUSTMENT TO THE IMPORTED CSV FILES CAN BE DONE BUT IT IS ADVISED TO CONSULT WITH DAVID KWAK IF ERRORS ARISES
  +TYPE IN AN INTEGER (PREFERABLY BETWEEN 7-9 WEEKS) TO DETERMINE THE MINIMUM NUMBER OF WEEKS THE PRODUCT REQUIRES TO SHIP FROM THE PLANT
  +THE MATERIAL NUMBER MAY NEED TO BE ADJUSTED VIA TEXT-TO-COLUMNS OR USE A SINGLE QUOTE IN FRONT (WITH THE LATTER BEING THE PREFERRED METHOD)

#NOTES
  #import functions were not grouped at the top as when doing so, the program failed

#DEFINITION FOR TABLES/DICTIONARIES
  FORECAST:
    +material       =   material number for the product
    +description    =   description of the material/product
    +plant          =   4 digit code representing a location
    +date           =   date of Monday of the week's sale
    +fct            =   the forecasted quantity for the given week
    +id             =   unique identifier for the application only

  THRIFT:
    +material       =   material number for the product
    +description    =   description of the material/product
    +exp            =   expiration date printed on the product (last day consumers will eat)
    +qty            =   quantity of product being thrifted
    +thrift         =   the last day/date that the product can be sold to stores ( dictated number of weeks prior to "exp")
    +date thrifting =   the date the product was identified to be thrifted

  STOCK:
    +material       =   material number for the product
    +description    =   description of the material/product
    +exp            =   expiration date printed on the product (last day consumers will eat)
    +qty            =   quantity of product being thrifted
    +thrift         =   the last day/date that the product can be sold to stores ( dictated number of weeks prior to "exp")
    +date thrifting =   the date the product was identified to be thrifted
