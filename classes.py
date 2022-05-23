import json
from bson.objectid import ObjectId

class Users:

    def register(self):

        user = {
            "_id": "",
            "username": "",
            "password": ""
        }

        dbResponse = db.mydb.user.insert_one(newUser)
        #print(dbResponse.inserted_id)
        #print("Registered")
        for attr in dir(dbResponse):
                print(attr)

        return Response(
            response= json.dumps(
                {"message":"user created",
                "id": f"{dbResponse.inserted_id}"
                 }),
                mimetype="application/json"
        )

        user.insert_one({'Name':name, 'Password':password})

def getUser():
    try:
        data = db.users.find()
        return data

    except Exeption as ex:
        print(ex)
        return Response(
            response= json.dumps(
                {"message":"cannot read user", "id": f"{dbResponse.inserted_id}"}),mimetype="application/json")

def updateUser(id):
    try:
        dbResponse = db.users.update_one(
            {"_id":ObjectId("")},
        {"$set":{"name":request.form["name"]}}
        )
        for attr in dir(dbReponse):
            print(f"{attr}")
        dbResponse.modified_count == 1
        return Response(
         response= json.dumps(
            {"message":"User is updated", "id": f"{dbResponse.inserted_id}"}),mimetype="application/json")

        return Response(
            response= json.dumps(
                {"message":"Nothing to update", "id": f"{dbResponse.inserted_id}"}),mimetype="application/json")
    finally:
        print("")


def deleteUser(id):
    try:
        dbResponse = db.user.delete_one({"_id":ObjectId(id)})
        for attr in dir(dbResponse):
            print(f"***{attr}***")
        return Response(
            response= json.dumps(
                {"message":"User deleted", "id": f"{id}"}),mimetype="application/json")

    except Exception as ex:
        print("")
        print("ex")
        print("")
        return Response(
            response= json.dumps(
                {"message":"Sorry, unable to delete the user", "id": f"{dbResponse.inserted_id}"}),mimetype="application/json")




    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps(
                {"message":"unable to update","id": f"{dbResponse.inserted_id}"
                 }),
            mimetype="application/json"
        )
    return id

def create_user(name,password):
    split_names = name.split()
    split_password = name.split()[0]

    user = [x['_id']for x in user.find({'Name':name, 'Password':password})]

    if len(user)==0:
        User(name,password)
        print(Success)

    else:
        response = str(input('A user by the name "%s" already exist'))






