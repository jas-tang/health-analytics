import pandas as pd
import numpy as np

number_variable = 10
string_variable = "string"
list_variable = ["a",10,"c"]

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

def gratuity(people, bill):
    if people >= 4:
        percentage = 20
        total_cost = (people * percentage + bill)
        return total_cost
    else:
        percentage = 1
        total_cost = (people * percentage + bill)
        return total_cost

