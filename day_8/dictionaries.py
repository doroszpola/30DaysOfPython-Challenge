person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)


dog = {
    'name' : 'Poter',
    'color' : 'Beige',
    'legs' : '30',
    'age' : 'eternal'

}

student = {
    'first_name' : 'Pola',
    'last_name' : 'Dorosz',
    'gender' : 'Female',
    'age' : '21',
    'marital_status' : 'not_married',
    'skills' : ['dancing, singing, drawing'],
    'country' : 'Poland',
    'city' : 'Łódź',
    'address' : 'none of your business :D'
}

print(len(student))

print(type(student['skills']))

print(student.keys())
print(student.values())

del student['address']

print(student)

del student