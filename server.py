
# from flask import Flask
# from flask_session import Session
# from flask_cors import CORS

# from Routes.userRoutes import userApp

# app = Flask(__name__)
# CORS(app, supports_credentials=True)
# app.config['SESSION_TYPE'] = 'filesystem' 
# Session(app)

# app.register_blueprint(blueprint=userApp)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_session import Session
from Routes.userRoutes import UserResource, UserListResource

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

api = Api(app)

# Add resources
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)