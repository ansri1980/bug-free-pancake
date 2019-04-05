""" Boiler plate API using flask"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return 'Hello World'

# Expose root to call HelloWorld Resource
api.add_resource(HelloWorld, '/')

# Support for both importing and standalone
if __name__ == '__main__':
    app.run(host='0.0.0.0')

