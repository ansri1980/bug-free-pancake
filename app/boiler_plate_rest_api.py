""" Boiler plate API using flask"""

from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return 'Hello World'

class Status(Resource):
    def get(self):
        data = {"myapplication": 
                   [{
                    "version": "1.0",
                    "description": "pre-interview technical test",
                    "lastcommitsha": "abc57858585"
                    }]}
          
        resp = jsonify(data)
        resp.status_code = 200
        return resp
 
# Expose root to call HelloWorld Resource
api.add_resource(HelloWorld, '/')
api.add_resource(Status,'/status')

# Support for both importing and standalone
if __name__ == '__main__':
    app.run(host='0.0.0.0')

