import pymongo
client = pymongo.MongoClient("mongodb+srv://amadhdeshia1:12345@cluster0.spa6q.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name" : "thor",
    "email" : "thor@avengers.com",
    "surname" : "hammer"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

