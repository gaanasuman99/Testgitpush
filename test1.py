import pymongo
client = pymongo.MongoClient("mongodb+srv://gaanasuman:gaana123@cluster0.zjkpg6v.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"gaana",
    "mail":"gaanasuman22gmail.com",
     "surname":"suman"
}