from flask import Flask, jsonify, request
from flask_cors import CORS
from function import login, sign_up


app = Flask(__name__)
CORS(app)

# Access this endpoint through: http://localhost:5000/
@app.route('/')
def index():
    return jsonify({'message': 'Hey, everything works!!'})

"""
Access this endpoint through: http://localhost:5000/adding-test?x=1&y=2
"""

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        return jsonify({'message': 'show login page'})
        # return login()
    else:
        return jsonify({'message': 'enter User in Database'})
        # return sign_up()

