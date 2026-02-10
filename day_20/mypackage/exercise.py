import requests

def transform_data(data):
    parts = data.replace(" ", "").split("-")

    nums = [int(p) for p in parts]

    return nums



url = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(url)

print(response)

cats = response.json()

# filtered_cats = [
#     {
#         "name": c.get("name"),
#         "weight": c.get("weight", {}).get('metric'),
#         "lifespan": c.get("life_span")
#     }
#     for c in cats
# ]

# print(filtered_cats[:3])




max_weight = [
    max(transform_data(c.get("weight", {}).get('metric')))
    for c in cats
]

print(f"Najcięższy kot waży {max(max_weight)} kilo")

min_weight = [
    min(transform_data(c.get("weight", {}).get('metric')))
    for c in cats
]

print(f"Najlżejszy kot waży {min(min_weight)} kilo")

weight_list = [
    num
    for c in cats
    for num in transform_data(c.get("weight", {}).get('metric'))  
]

# weight_list = []

# for c in cats:
#     nums = transform_data(c.get("weight", {}).get('metric', ''))
#     for num in nums:
#         weight_list.append(num)

import numpy

mean = numpy.mean(weight_list)
median = numpy.median(weight_list)

print(f"Średnia waga kotów to {mean}, a ich mediana to {median}.")

std_dev = numpy.std(weight_list)

print(f"Odchylenie standardowe to {std_dev}")


# how many countries are in the countries API?

url = "https://restcountries.com/v3.1/all"
params = {"fields": "name"}

response = requests.get(url, params=params)
countries = response.json()

print(countries)


count_countries = 0
for c in countries:
    count_countries+=1

print(count_countries)

print(len(countries))






