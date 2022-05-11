import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

customerscollection = mydb["customers"]

# The aggregation pipeline
customerscollection.aggregate([
    # Match Stage e.g: finding all the customers whos gender matched female -> returns a cursor
    { "$match": {"gender": "female"}},

    # Group Stage allows us to group the data by certain field or multiple fields
    { "$group": {"_id": {"state": "$location.state"}, totalPersons: { "$sum": 1 }}},

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

