
import os

from flask import Flask
from flask_session import Session
from flask_cors import CORS

from Routes.userRoutes import userApp

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SECRET_KEY'] = '!nS72@wq$u%xY'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

app.register_blueprint(blueprint=userApp)

if __name__ == '__main__':
    app.run(debug=True)