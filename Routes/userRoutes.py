
from Database.userDB import db
from flask import request,jsonify,Blueprint

userApp = Blueprint('user',__name__)


@userApp.route('/users',methods=['POST'])
def createUser():
    data = request.json
    name = data.get('name')
    password = data.get('password')
    email = data.get('email')

    if not name or not password or not email:
        return jsonify({"error": "Missing required fields"}), 400
    
    newUserID = db.addUser(data['name'],data['email'],data['password'])


    if isinstance(newUserID, str):
        # User was successfully created
        return jsonify({"message": "User created successfully", "user_id": newUserID}), 201
    else:
        # User already exists
        return jsonify({"error": "User with this email or name already exists"}), 400

@userApp.route('/users',methods=['GET'])
def getUsers():
    users = db.allUsers()
    for user in users:
        user['_id'] = str(user['_id'])
        del user['password'] 
    return jsonify(users)


@userApp.route('/users/<userID>',methods=['GET'])
def getUser(userID):
    user = db.findUser(userID)
    if user:
        
        user['_id'] = str(user['_id'])
        user['password'] = str(user['password'])
        print(user)
        return jsonify(user)
    return jsonify({'Error':'No user found with this ID'}),404

@userApp.route('/users/<userID>',methods=['PUT'])
def updateUser(userID):
    data = request.json
    if db.updateUser(userID,data):
        return jsonify({'Success':'User Data Update'})

    return jsonify({'error': 'User not found'}), 404

@userApp.route('/users/<userID>', methods=['DELETE'])
def delete_user(userID):
    if db.delUser(userID):
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'error': 'User not found'}), 404