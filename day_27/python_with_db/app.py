from flask import Flask, render_template
import os 
import pymongo 

MONGODB_URI = 'mongodb+srv://doroszpola_db_user:<my-password>@myfirstcluster.yp2t40y.mongodb.net/?appName=MyFirstCluster' 
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())


########################
# STEP 1 - creating and inserting
########################


#db = client.my_first_database
#db.students.insert_one({'name': 'Pola', 'surname' : 'Dorosz', 'age': 21})
# print(client.list_database_names())


########################
# STEP 2 - inserting multiples
########################


# students = [
#     {'name': 'Lala', 'surname' : 'Kicia', 'age': 2},
#     {'name': 'Yuki', 'surname' : 'Kicior', 'age': 2},
#     {'name': 'Poter', 'surname' : 'Pluszak', 'age': 200}
# ]

# for student in students:
#     db.students.insert_one(student) # we can alsu use insert_many() instead of a for loop


########################
# STEP 3 - findning
########################

try:
    db = client['my_first_database']
    student = db.students.find_one()
    print(student)
except:
    print("nie udało się znaleźć")

print('###################')

students = db.students.find()
for student in students:
    print(student)

print('###################')

students = db.students.find({}, {'_id':0, 'name' : 1, 'surname': 1}) # 0 means not include and 1 means include

for student in students:
    print(student)

print('###################')


########################
# STEP 4 - querying
########################


query = {"age":{"$gt":100}}

students = db.students.find(query)

for student in students:
    print(student)

print('###################')


########################
# STEP 5 - limiting
########################


students = db.students.find().limit(2)

for student in students:
    print(student)
print('###################')


########################
# STEP 6 - sort
########################


students = db.students.find().sort('name')
for student in students:
    print(student)
print('###################')


students = db.students.find().sort('name', -1)
for student in students:
    print(student)
print('###################')


########################
# STEP 6 - updates
########################


query = {'age' : 200}
new_value = {'$set':{'age': 5}}

db.students.update_one(query, new_value)

for student in db.students.find():
    print(student)
print('###################')


########################
# STEP 7 - deletion
########################

print('BEFORE DELETION:')
db.students.insert_one({'name': 'AAA', 'surname' : 'BBB', 'age': 999})
for student in db.students.find():
    print(student)

query = {"age":{"$gt":100}}
db.students.delete_one(query)

print('AFTER DELETION:')
for student in db.students.find():
    print(student)
 

 # using delete_many({}) we can delete everything by not passing an argument


########################
# STEP 7 - dropping 
########################

# db.students.drop()

app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
