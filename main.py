import json
import calculations

# Attempting to open json file to get dict, otherwise running setup
try:
    with open('data.json') as file:
        data = json.load(file)

except FileNotFoundError:
    data = calculations.intro()

# Getting which meal to use
meal = ''
while meal != 'b' and meal != 'l' and meal != 'd' and meal != 's':
    meal = (input("Hello, are you treating for (B)reakfast, (L)unch, (D)inner, or are you trying to change your"
                  "(S)ettings? ").strip()).lower()

# Different options based on meal, or doing settings
if meal != 's':
    carb = calculations.getcarbs()
    number = calculations.getnum()

if meal == 'b':
    calculations.numunits(carb, data["Breakfast"], number, data["startScale"], data["rnge"])
elif meal == 'l':
    calculations.numunits(carb, data["Lunch"], number, data["startScale"], data["rnge"])
elif meal == 'd':
    calculations.numunits(carb, data["Dinner"], number, data["startScale"], data["rnge"])
elif meal == 's':
    data = calculations.intro()
    input("Thank you, press enter when finished . . . ")

# Dumping data to json file
with open('data.json', 'w') as file:
    json.dump(data, file)
