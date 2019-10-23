from flask import Flask, jsonify, request
from flask_cors import CORS
from Mediciones import Medicion

app = Flask(__name__)
CORS(app)

@app.route('/mediciones',methods=['GET'])
def getAll():
    return (Medicion.list())

@app.route('/mediciones',methods=['POST'])
def postOne():
    body = request.json
    return (Medicion.create(body))
    
''' quitamos el app run para que la app corra en azure '''
''' app.run(port=5000,debug=True) '''