user_input_age = int(input("How old are you? "))

if user_input_age > 21:

    dif = user_input_age - 21
    text = "You are {} years older than me.".format(dif)
    print(text)

else:
    print("You are younger than me.")



dog = {
    'name' : 'Poter',
    'color' : 'Beige',
    'legs' : '30',
    'age' : 'eternal'
}

if 'name' in dog:
    print("Your dog's name is {}".format(dog['name']))


student = {
    'first_name' : 'Pola',
    'last_name' : 'Dorosz',
    'gender' : 'Female',
    'age' : '21',
    'marital_status' : 'not_married',
    'skills' : ['dancing', 'singing', 'drawing'],
    'country' : 'Poland',
    'city' : 'Łódź',
    'address' : 'none of your business :D'
}

if 'skills' in student:
    print("this student is skilled")
    if 'dancing' in student['skills']:
        print("this student is skilled in dancing")

