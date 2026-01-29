
from mymodule import generate_full_name as fullname
print(fullname('Pola','Dorosz'))

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

from math import *
print(pi)           # 3.141592653589793, pi constant
print(sqrt(2))      # 1.4142135623730951, square root
print(pow(2, 3))    # 8.0, exponential function
print(floor(9.81))  # 9, rounding to the lowest
print(ceil(9.81))   # 10, rounding to the highest
print(log10(100))   # 2, logarithm with 10 as base

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

import random
print(random.random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(random.randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

def random_user_id():
    name = ''
    characters = string.ascii_letters + string.digits
    for i in range(6):
        name += random.choice(characters)
    return name

print(random_user_id())


def generate_hex_color():
    color = '#'
    characters = 'abcdef' + string.digits
    for i in range(6):
        color += random.choice(characters)
    return color

print(generate_hex_color())  #maybe I could write a website with random color palette generation... :D



def seven_unique_numbers():
    return random.sample(range(10), 7) #sample picks unique

print(seven_unique_numbers())


def shuffle_list(lst):
    shuffled = lst.copy()          # make a copy
    random.shuffle(shuffled)     # shuffle in place
    return shuffled

print(shuffle_list([1,2,3,4,5]))