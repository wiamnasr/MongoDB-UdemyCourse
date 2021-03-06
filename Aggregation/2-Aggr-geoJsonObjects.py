# In the previous file, we included gender and transformed name
# After that, below turning the location into a geoJSON object so we can later on work with it
# This geoJSON object type will be a point (2 coordinates (longitude and latitude))
# the coordinates in the below example is an array  of 2 numbers instead of an object of long and lat which are strings not numbers
# We are converting the data using the convert operator

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

customerscollection = mydb["customers"]


customerscollection.aggregate([
    # Adding an extra project stage before the one from before
    # note that excluding the _id here in the first project stage will make it unavailable in the next stage (following project)
    {"$project": {"_id": 0, "name": 1, "email": 1, "birthdate": {"$convert": {"input": "$dob.date", "to": "date"}}, "age": "$dob.age" ,"location": {"type": "point", "coordinates": [{"$convert": {"input": '$location.coordinates.longitude', "to": 'double', "onError": 0.0, "onNull": 0.0}}, {"$convert": {"input": '$location.coordinates.latitude', "to": 'double', "onError": 0.0, "onNull": 0.0}}]}}},
    { "$project": { "gender": 1, "email": 1, "location": 1, "birthdate":1, "age": 1 ,"fullName": {"$concat": [
        { "$toUpper": {"$substrCP": ['$name.first', 0, 1]}},
        {"$substCP": ['$name.first', 1, {"$subtract": [{"$strLenCP": "$name.first"}, 1]}]},
        ' ',
         { "$toUpper": {"$substrCP": ['$name.last', 0, 1]}},
        {"$substCP": ['$name.last', 1, {"$subtract": [{"$strLenCP": "$name.last"}, 1]}]},
        ]
        }
    }}


]   )



# We can also use shortcuts for our transformations, especially if we are plannin on doin a simple conversion where we dont specify on error or on null as above:

# There are special operators in MOngoDb (checkout documentation for more on this, under aggregation pipeline operators), below we are using toDate() shortcut to do this specific transformation
 
customerscollection.aggregate([
    # Adding an extra project stage before the one from before
    # note that excluding the _id here in the first project stage will make it unavailable in the next stage (following project)
    {"$project": {"_id": 0, "name": 1, "email": 1, "birthdate": {"$toDate": "$dob.date"}, "age": "$dob.age" ,"location": {"type": "point", "coordinates": [{"$convert": {"input": '$location.coordinates.longitude', "to": 'double', "onError": 0.0, "onNull": 0.0}}, {"$convert": {"input": '$location.coordinates.latitude', "to": 'double', "onError": 0.0, "onNull": 0.0}}]}}},
    { "$project": { "gender": 1, "email": 1, "location": 1, "birthdate":1, "age": 1 ,"fullName": {"$concat": [
        { "$toUpper": {"$substrCP": ['$name.first', 0, 1]}},
        {"$substCP": ['$name.first', 1, {"$subtract": [{"$strLenCP": "$name.first"}, 1]}]},
        ' ',
         { "$toUpper": {"$substrCP": ['$name.last', 0, 1]}},
        {"$substCP": ['$name.last', 1, {"$subtract": [{"$strLenCP": "$name.last"}, 1]}]},
        ]
        }
    }}


]   )
