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
print(patientscollection.find())


# Updating the patients collection in the hospital database, where the first name is Wiam, changing the name, age and history to new values
# For now overwriting the old history list with a new list
updatedPatientsCollection = patientscollection.update_one({"first_name": "Wiam"}, {"$set": {"last_name":"Nasrr", "age": 31.3, "history": [{"disease": "headache", "treatment": 54}]}})

print(updatedPatientsCollection)


# Finding all patients older than 30:
olderthan30 = patientscollection.find({"age": {"$gt": 30}})

print(olderthan30)

# Deleting all the patients who have had a cold
patientswithcold = patientscollection.delete_many({"history.disease": "cold"})