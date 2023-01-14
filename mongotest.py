import pymongo
client = pymongo.MongoClient("mongodb+srv://gaanasuman:gaana123@cluster0.zjkpg6v.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"gaana",
    "mail":"gaanasuman22gmail.com",
     "surname":"suman"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
d = {
    "name":"gaana",
    "mail":"gaanasuman22gmail.com",
     "surname":"suman"
}
d = {
    "name":"gaana",
    "mail":"gaanasuman22gmail.com",
     "surname":"suman"
}
