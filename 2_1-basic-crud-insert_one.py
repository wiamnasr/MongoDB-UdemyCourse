# SOURCE: https://www.w3schools.com/python/python_mongodb_insert.asp

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

customerscollection = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37"}

x = customerscollection.insert_one(mydict)



# Another Example using insert_many

hospitaldatabase = myclient["hospital"]

patientscollection = hospitaldatabase["patients"]

mylist = [{"first_name": "Wiam", "last_name": "Nasr", "age": 31, "history": [{"disease": "cold", "treatment": 1}]}, {"first_name": "Jake", "last_name": "smith", "age": 25, "history": [{"disease": "cough", "treatment": 4}]}]

y = patientscollection.insert_many(mylist)

# print(mydb)
print(y)