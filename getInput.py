#collect inputs from user

import variables

def getInput():
    from currpicker import currpicker

    # input source currency
    variables.currencyFrom = int(input("What currency are you converting from? "))

    # test inputs are between 1 & 5
    if 1 <= variables.currencyFrom <= 5:

        #input destination currency
        variables.currencyTo = int(input("What currency are you converting to? "))

        #tests inputs are between 1 & 5
        if 1 <= variables.currencyTo <= 5:

            #input amount to be converted
            variables.amount = int(input("Enter the Amount to be Converted: "))

            #logice to track source and destination currency
            variables.engine = [variables.currencyFrom, variables.currencyTo]
            currpicker()
        else:
            print("Please Enter an option between 1 and 5")
            getInput()
    else:
        print("Please Enter an option between 1 and 5")
        getInput()

