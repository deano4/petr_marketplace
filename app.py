from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Access this endpoint through: http://localhost:5000/
@app.route('/')
def index():
    return jsonify({'message': 'Hey, everything works!!'})

"""
Access this endpoint through: http://localhost:5000/adding-test?x=1&y=2

Takes two numbers, adds them together, and returns the value. 
Not a very good case for setting up and hosting an entire backend
server but this example shows a proof of concept of how it works.

For a simple example like this, you're better of just writing this 
in javascript.
"""
@app.route('/adding-test')
def add():
    sum_result = int(request.args.get('x')) + int(request.args.get('y'))

    return jsonify({
        "answer": sum_result
    })

