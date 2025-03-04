#redirect to desired currency

from usdconvert import usdconvert
from eurconvert import eurconvert
from jpyconvert import jpyconvert
from gbpconvert import gbpconvert
from ngnconvert import ngnconvert
import variables

def currpicker():
    if variables.currencyFrom == 1:
        usdconvert()
    elif variables.currencyFrom == 2:
         eurconvert()
    elif variables.currencyFrom == 3:
        jpyconvert()
    elif variables.currencyFrom == 4:
        gbpconvert()
    elif variables.currencyFrom == 5:
        ngnconvert()
    else:
        print("Please enter a valid input")
        currpicker()