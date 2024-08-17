from pymongo import MongoClient
from bson import objectid
import bcrypt 
import uuid
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId

class User:

    def __init__(self,dbName,collName):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[dbName]
        self.collection = self.db[collName]
    
    def addUser(self,name,email,password):
        # salt = bcrypt.gensalt(rounds =14)
        passwordHash = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt(rounds=14))
        
        newUser = {
            "name":name,
            "password":passwordHash,
            "email":email
        }
    
        existing_user = self.collection.find_one({"$or": [{"email": email}, {"name": name}]})
    
        if existing_user:
            return "User with this email or name already exists", 400

        try:
            user = self.collection.insert_one(newUser)
            return str(user.inserted_id)
        except DuplicateKeyError:
            return "User already exists",401

    def findUser(self,userId):
        return self.collection.find_one({"_id":ObjectId(userId)})
    
    def updateUser(self,userID,newData):
        """
        either the neData can be password or email, if its password, first we need
        to hash the password and modify it, after that just replace the existing data
        with new data
        """

        if 'password' in newData:
            newData['password'] = bcrypt.hashpw(newData['password'].encode('utf-8'),bcrypt.gensalt(rounds=14))

        updatedUser = self.collection.update_one({"_id":ObjectId(userID)},{"$set":newData})

        return updatedUser.modified_count >0


    def delUser(self,userId):
        userDel = self.collection.delete_one({"_id":ObjectId(userId)})
         
        return userDel.deleted_count > 0
    
    def allUsers(self):
        userslist = list(self.collection.find())
        if len(userslist) ==0:
            return "No user present in database",404
        
        return userslist
    
db = User("UserDB","Users")