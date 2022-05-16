import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

customerscollection = mydb["customers"]

# Adding another group stage after the previous ones to group on the derived fields from before

# Here we want to group on the birthdate that was available from before and we converted it to a date in previous steps

# Grouping by birthyear:
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
    }},
    # isoWeekYear retrieves the year out of the date
    {"group": {"_id": {"birthYear": {"$isoWeekYear": "$birthdate"}}, "numPersons": {"$sum": 1} }},

    # sorting the number of persons in decending order to get which year had the most birthrate
    {"$sort": {"numPersons": -1}}


]   )


# Group is for grouping multiple documents into one document grouped by one or more categories of your choice and any new fields, while project is a one to one relation (1 doc in and return 1 doc, it will just have changed). In project, we transform a single document, adding new fields for instance,...