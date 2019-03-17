from db import food_collection
from bson import ObjectId
def add(name, price):
    new_food = {
        "name" : name,
        "price": price
    }
    food_collection.insert_one(new_food)

def get(query): #filter, limit, skip
    food_list = food_collection.find(query) #many
    return food_list

def get_by_id(id):
    f = food_collection.find_one({ "_id": ObjectId(id) })
    return f 

def delete_by_id(id):
    d = food_collection.delete_one({ "_id": ObjectId(id) })
    return d 

def update_by_id(id, name, price):
    query = { "_id": ObjectId(id) }
    updater = { 
        "$set": { "price": price },
        "$set": { "name"  : name },
        }
    food_collection.find_one_and_update(query, updater)

#def find_by_username(username)

if __name__ == "__main__":
    query = { "_id": ObjectId("5c8124fc552d4d1164eac22e") }
    updater = { "$set": { "price": 23000 } } # $inc : tang, $dec : giam, #set , $unset
    food_collection.find_one_and_update(query, updater)
    print(*get({}), sep="\n")
    # food_collection.delete_one({ "_id": ObjectId("5c81232b552d4d2d50f7cda3") })
    # f = get_by_id("5c81232b552d4d2d50f7cda3")
    # #for food in get({ "_id": ObjectId("5c81232b552d4d2d50f7cda3") }):
    # if f != None: #found
    #     print(f["name"])
    # else:
    #     print("Not found")
     