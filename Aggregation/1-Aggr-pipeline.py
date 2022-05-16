import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

customerscollection = mydb["customers"]

# The aggregation pipeline (each stage below can exist multiple times)
customerscollection.aggregate([
    # Match Stage e.g: finding all the customers whos gender matched female -> returns a cursor
    { "$match": {"gender": "female"}},

    # Group Stage allows us to group the data by certain field or multiple fields
    { "$group": {"_id": {"state": "$location.state"}, "totalPersons": { "$sum": 1 }}},

    # Sort Stage comes after grouping, here sorting in decending order by specifying -1
    { "$sort": { "totalPersons": -1}}
])


# Another example
customerscollection.aggregate([
    {"$match": { "dob.age": {"$gt": 50}}},
    # The avg operator helps us calculate the average in a field
    {"$group": {"_id": {"gender": "$gender"}, "numPersons": {"$sum: 1"}, "avgAge": {"$avg": "$dob.age"}}},
    {"$sort": {"numPersons": -1}}


])


# Concatination stage that allows us to transform every document instead of grouping them together

# We know project from the find() method, using aggregate, its even more powerful
# In the below example, we do not want to do any filtering just to transform every document
# In its most simple form, project works in the same way as projection works in the find() method

# here we are saying we do not want the _id field, by setting it to 0
# We are reformating some of the other fields we want to include
# Gender for instance is included so we specify it as 1 not 0 like the _id field
# We can add new fields here as well for instance the full name field in the below example --> using concat  that allows us to concatenate 2 strings
# transforming the strings befor concatenating them is possible directly in the projection phase
# In the example we are transforming the first and last names to start with an upper case letter
# we are using substrCP to do another operation within the project concat operation in order to only upper case the first letter in each word
# we are using the subtract operator, that returns the difference of 2 numbers because we need to find our the length of the name then substract one from it so the rest are not uppercase and concatinated with the first letter that is uppercase

customerscollection.aggregate([
    { "$project": {"_id": 0, "gender": 1, "fullName": {"$concat": [
        { "$toUpper": {"$substrCP": ['$name.first', 0, 1]}},
        {"$substCP": ['$name.first', 1, {"$subtract": [{"$strLenCP": "$name.first"}, 1]}]},
        ' ',
         { "$toUpper": {"$substrCP": ['$name.last', 0, 1]}},
        {"$substCP": ['$name.last', 1, {"$subtract": [{"$strLenCP": "$name.last"}, 1]}]},
        ]
        }
    }}


])

