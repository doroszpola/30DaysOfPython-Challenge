# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)   


# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32


################################
# exercise
################################

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_numbers = [i for i in numbers if i>=0]
print(positive_numbers)


list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [number for sublist1 in list_of_lists for sublist2 in sublist1 for number in sublist2]


flattened = []
for sublist1 in list_of_lists:
    for sublist2 in sublist1:
        for number in sublist2:
            flattened.append(number)  # <- equivalent to the "item" at the front

print(flattened)
print(flattened_list)

list_of_tuples = [(i, *[i**k for k in range(6)]) for i in range(11)]  # *[i**k for k in range(6)]  -> * used as the unpacking operator

# i, i^0, i^1, i^2 ... i^10

print(list_of_tuples)




# for i in range(11):
#     powers = []
#     for k in range(6):
#         powers.append(i**k)
#     tuple_for_i = (i, *powers)   # unpack the powers list into the tuple
#     list_of_tuples.append(tuple_for_i)

# print(list_of_tuples)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

countries2 = [ [country.upper(), country[:3].upper(), capital.upper()] 
  for sublist in countries 
  for country, capital in sublist ]

print(countries2)


lst = [('Finland', 'Helsinki'), ('a','b')]
for country, capital in lst:
    print(country, capital)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

countries3 = [{'country': country.upper(), 'city': city.upper()}
              for sublist in countries
              for country, city in sublist]

print(countries3)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

names2 = [first_name +' ' + second_name
          for sublist in names
          for first_name, second_name in sublist]

print(names2)


