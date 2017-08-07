# Freestyle
#PURPOSE
  # to calculate the amount of stock that will expire

#EXPECTATIONS BEFORE RUNNING
  #STEP 1:  DO NOT ADJUST THE IMPORTED CSV FILE UNLESS TRAINED
  #STPE 2: TYPE IN AN INTEGER (PREFERABLY BETWEEN 7-9 WEEKS) TO DETERMINE THE MINIMUM NUMBER OF WEEKS THE PRODUCT REQUIRES TO SHIP FROM THE PLANT

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
