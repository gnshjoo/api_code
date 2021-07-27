from flask import Flask, Blueprint
from flask_restplus import Api
from app.api.login import api as login_api
from app.api.singup import api as signup_api

app = Flask(__name__)
api_prefix = '/api/v1/'
api = Api(app, version="1.0", title="ABLY CodingTest")

api.add_namespace(login_api, path="/users")
api.add_namespace(signup_api, path="/signup")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
