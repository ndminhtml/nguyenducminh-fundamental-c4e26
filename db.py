from pymongo import MongoClient

uri = "mongodb+srv://admin:admin1@tk-c4e-zz290.mongodb.net/test?retryWrites=true"
#1. Connect
client = MongoClient(uri)

#2. Get database
db = client.test

#3. Get collection
food_collection = db["food"]
user=db["user"]

# #4. Creat a new document
new_user ={
    "user": "ducminh",
    "password": "minh1998"
}
new_food = {
    "name" : "com rang",
    "price" : "30000"
} #document

#5. Insert new document into collection
food_collection.insert_one(new_food)
user.insert_one(new_user)
#6. Close connection
def close():
    client.close()