# # syntax
# # Declaring a function
# def function_name(*args):
#     codes
#     codes
# # Calling function
# function_name(param1, param2, param3)  # allows us to create a function with an arbitrary number of parameters

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

def remove_item(list, item):
    if item in list:
        list.remove(item)
    return list


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]


def all_uniq(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                return False
    return True


def all_uniq_2(list):
    return len(list) == len(set(list))
        

if all_uniq(food_staff):
    print("all unique")
else:
    print("found dupes")

if all_uniq_2(food_staff):
    print("all unique")
else:
    print("found dupes")
