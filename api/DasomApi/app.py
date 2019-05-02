from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return "Hello, Flask!"

api.add_resource(Hello, '/')

if __name__ == "__main__":
    app.run(debug=False, port=5000, host='0.0.0.0')
