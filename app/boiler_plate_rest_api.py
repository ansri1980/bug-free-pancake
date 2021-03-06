""" Boiler plate API using flask"""

from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
import logging
import yaml
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
api = Api(app)
app.config['TEST'] = False

class HelloWorld(Resource):
    def get(self):
        app.logger.info("Serving request for /")
        return 'Hello World'

class Status(Resource):
    def get(self):
        app.logger.info("Service request for /status")
        shacommit = self.get_sha_commit()
        data = {"myapplication": 
                   [{
                    "version": self.version,
                    "description": self.description,
                    "lastcommitsha": shacommit
                    }]}
          
        resp = jsonify(data)
        resp.status_code = 200
        return resp


    def get_sha_commit(self):
        """ The version information is available from file lastshacommit created when building docker image. Read and return this information """
        self.get_meta()
        filename = 'lastshacommit'
        # For unittest read from localfile
        if app.config['TEST']:
            filename = 'lastshacommittest'
            app.logger.debug("App config set to TEST. Reading shacommit from file " +  filename)

        try:
            handle = open(filename, "r")
        except Exception as e:
            app.logger.error("Error occurred when opening file " + filename)
            app.logger.error(e)
            raise
        l_shacommit = handle.read().rstrip()
        handle.close()
        return l_shacommit

    def get_meta(self):
        meta_file = "meta.yml"
        try:
            with open(meta_file,"r") as stream:
                data = yaml.load(stream)
        except Exception as e:
            app.logger.error("Error occurred when reading yaml file " + meta_file)
            app.logger.error(e)

        self.version = data['version']
        self.description = data['description']

api.add_resource(HelloWorld, '/')
api.add_resource(Status,'/status')

# Support for both importing and standalone
if __name__ == '__main__':
    handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=1)
    # CAUTION: Loglevel should be set to INFO when going production
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0')

