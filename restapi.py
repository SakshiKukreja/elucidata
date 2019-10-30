from flask import Flask
from flask import request,jsonify
import sqlite3
from sqlite3 import Error

app = Flask(__name__)


 
def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')
        #print(sqlite3.version)
    except Error as e:
        print(e)

        
 
 
@app.route("/")
def hello():
    return "Hello World!"


quiz=[
    {'id' : 0,
     'name' : 'Elucidata_Quiz',
     'description' : 'A quiz to test'} 
    ]
error=[{}]

e400=[
    {
        'status': 404,
        'reason': 'Not Found'}]

@app.route("/api/quiz/:quiz_id", methods=['GET'])
def fun():
    return jsonify(quiz)

@app.errorhandler(404)
def notFound():
    return error

@app.errorhandler(400)
def notFound():
    return e400

@app.route("/api/quiz/", methods=['POST'])
def fun():
    return jsonify(quiz)






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    create_connection()
