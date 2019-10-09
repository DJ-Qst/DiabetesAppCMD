import json
import calculations

try:
    with open('data.json') as file:
        data = file.readlines()

except FileNotFoundError:
    data = calculations.intro()
meal = ''
while meal != 'b' and meal != 'l' and meal != 'd' and meal != 's':
    meal = (input("Hello, are you treating for (B)reakfast, (L)unch, (D)inner, or are you trying to change your"
                  "(S)ettings? ").strip()).lower()

if meal != 's':
    carb = calculations.getcarbs()
    number = calculations.getnum()
