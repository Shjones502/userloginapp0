from mongodb import *
from classes import *
users = {}
status = ""

def displayMenu():
    status = input("Are you a registered user? y/n?")
    if status == "y":
        oldUser()
    elif status =="n":
        newUser(username,password)

def secMenu():
    print("What will you like to do?")
    print("[1]Update Password")
    print("[2]Delete User")

secMenu()
option = input("Please make a choice ")

if option == "1":
    print("Update is happening")
elif option == "2":
    print("Delete is happening")
def newUser(username,password):
    username = input("Create a username:")
    password = input("Create a password:")
    users = {
        "usern": f"{username}",
        "passw": f"{password}"
    }


    if password != password:
        print("Passwords do not match")
        displayMenu()
    else:
        if len(password)<=6:
            print("Password too short")
            displayMenu()

        elif username in datalist:
            return data
            print("Username exist")
            displayMenu()
        else:
            dbResponse = db.mydb.newUser.insert_one("newUser")
            print(dbResponse.inserted_id)
            print("Registered")

def oldUser():
    login = input("Enter username: ")
    passw = input("Enter password: ")

    if login in users and users[login] == passw:
        print("\nLogin Successful!\n")
    else:
        print("\nUser doesnt exist or input is incorrect!\n")

displayMenu()


def login(oldUser):
    if(success):
        print("Login Successful!")
    else:
        print("Wrong name or password")




def access(name,password):  #if (option=="login"):
    oldUser = {
        "name": f"{name}",
        "password": f"{password}"
    }
    access(name,password)

    print("Enter your name and password to register")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    register(name,password)




def newUser():
    createLogin = input("Create login name: ")

    if createLogin in users:
        print("\nLogin name already exist!\n")
        users[createLogin] = createPassw
        print("\nUser created\n")

def oldUser():
    olduser = [x for x in user.find({'Name':name})]
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    if login in user and user[login] ==passw:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or invalid input")

