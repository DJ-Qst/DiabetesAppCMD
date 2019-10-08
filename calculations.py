def numunits(carbs, perunit, number, startscale, rnge, startunits=.5, ):
    units = round(carbs / perunit, 2)
    print("You should give " + str(units) + " for the food.")
    if number >= startscale:
        exunits = (number - (startscale - rnge)) / (rnge / startunits)
        print("You should give an extra " + str(exunits) + " units for the food.")
    else:
        print("Your number is great! You need to give no extra units!")
