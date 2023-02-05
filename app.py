from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS
from search import login, sign_up, market



app = Flask(__name__)
CORS(app)
# Access this endpoint through: http://localhost:5000/

"""@app.route('/login-page')
def login_option():
    name = request.args.get('l')
    username = request.args.get('username')
    password = request.args.get('password')
    return login()
    if request.args.get('f') == '1':
        return render_template('LoginPage.html')
    elif req_data['l'] is True:
        return redirect(url_for('login_page'))
    else:
        return redirect(url_for('sign_up_page'))"""
    #unique user id

@app.route('/login')
def login_page():
    username = request.args.get('username')
    password = request.args.get('password')
    return jsonify(login(username, password))
    
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up_page():
    username = request.args.get('username')
    password = request.args.get('password')
    socials = request.args.get('socials')
    return sign_up(username, password, socials)


@app.route('/trade')
def trade() -> 'json':
    name = request.args.get('sticker')
    if name is not None:
        return jsonify(market(name))
    return jsonify({'message': 'enter User in Database'})

@app.route('/')
def index():
    return jsonify({'message': 'Hey, everything works!!'})