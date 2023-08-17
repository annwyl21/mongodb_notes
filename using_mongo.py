from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['school']
collection = db['students']

# 1. Find all the students
all_students = collection.find()
for student in all_students:
    print(student)

# 2. insert a new student
new_student = {'name': 'Mr Krabs', 'age': 125, 'fullTime': False}
collection.insert_one(new_student)
