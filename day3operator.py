#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
       print(round(meal_cost+(meal_cost*tip_percent/100)+(meal_cost*tax_percent/100)))
if '_name_'== '_main_':
    meal_cost = float(input('meal cost').strip())

    tip_percent = int(input('tip').strip())

    tax_percent = int(input('tax').strip())

    solve(meal_cost, tip_percent, tax_percent)