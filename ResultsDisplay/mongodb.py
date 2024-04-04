import pymongo

def mongodb(data):
    #connect to mongodb local conncetion
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    #create the mongodb database
    mydb = client["ResultsDatabase"]
    #create a collection to database
    collection = mydb["grade"]
    #insert records to collection
    x = collection.insert_many(data)
    #printing the data in mongodb
    print(x)