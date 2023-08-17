#importing pandas and numpy
import pandas as pd
import numpy as np

#Creating variables and assigning values
number_variable = 10
string_variable = "string"
list_variable = ["a",10,"c"]

#Creating a dictionary that has at least one list and one nested dictionary
dictionary = {
    "name": "Jane Doe",
    "age": 25,
    "family_members": ["mother", "father","sister"],
    "health": {
        "weight": 126,
        "height": "64 inches",
        "bp": "120/80mmHg"
    }
}


#Creating an if/else function that takes two inputs
def gratuity(people, bill):
    if people >= 4:
        percentage = 0.20
        total_cost = bill + (bill * percentage)
        return total_cost
    else:
        percentage = 0
        total_cost = bill + (bill * percentage)
        return total_cost

people = 4
bill = 100
total_cost = gratuity(people, bill)
print("Total Cost:", total_cost)

cost_of_meal = gratuity(2,50)
print("Meal #2: ",cost_of_meal)