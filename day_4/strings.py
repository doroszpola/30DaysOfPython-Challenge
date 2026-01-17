radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)


challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

challenge = 'thirty days of python' #find(): Returns the index of the first occurrence of a substring, if not found returns -1
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

challenge = 'thirty days of python'  #rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'


sentence = "You cannot end a sentence with because because because is a conjunction"
result = sentence.replace("because because because", "")
print(result.strip()) #remove additional spaces


web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

