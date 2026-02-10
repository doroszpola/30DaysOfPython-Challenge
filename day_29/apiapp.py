from flask import Flask, Response, request  
import json
import pymongo
import os
from bson import json_util, ObjectId  

app = Flask(__name__)

MONGODB_URI = 'mongodb+srv://doroszpola_db_user:<moje_haslo>@myfirstcluster.yp2t40y.mongodb.net/?appName=MyFirstCluster' 
client = pymongo.MongoClient(MONGODB_URI)
db = client['my_first_database']

# --- GET: Pobieranie wszystkich ---
@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
    students_collection = db['students']
    students_list = list(students_collection.find())
    return Response(json_util.dumps(students_list), mimetype='application/json')

# --- POST: Tworzenie nowego ---
@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    # Pobieramy dane z formularza
    name = request.form.get('name')
    surname = request.form.get('surname') # Poprawiona literówka
    age = request.form.get('age')

    student = {
        'name': name,
        'surname': surname,
        'age': age
    }
    
    db.students.insert_one(student)
    return Response(json_util.dumps({"result": "Student created"}), status=201, mimetype='application/json')

# --- PUT: Aktualizacja ---
@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    query = {"_id": ObjectId(id)} # ObjectId jest teraz dostępne
    
    # Pobieramy nowe dane
    updated_data = {
        'name': request.form.get('name'),
        'surname': request.form.get('surname'),
        'age': request.form.get('age')
    }
    
    # Używamy $set, aby zaktualizować pola
    db.students.update_one(query, {"$set": updated_data})
    
    return Response(json_util.dumps({"result": "Student updated"}), mimetype='application/json')

# --- DELETE: Usuwanie ---
@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    db.students.delete_one({"_id": ObjectId(id)})
    return Response(json_util.dumps({"result": "Student deleted"}), mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)