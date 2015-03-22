from flask import Flask, jsonify
from flask.ext import restful
from corr import *

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
	

app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
	def get(self):
		return {'hello': 'world'}

class corra(restful.Resource):
	def get(self, s1,s2):
		#x = jsonify(getCor(s1,s2))
		return (getCor(s1,s2))


api.add_resource(HelloWorld,'/')
api.add_resource(corra, '/corr/api/v1/<string:s1>/<string:s2>')

