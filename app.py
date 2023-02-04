from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS
from function import login, sign_up, db



app = Flask(__name__)
CORS(app)
# Access this endpoint through: http://localhost:5000/
@app.route('/')
def index():
    return jsonify({'message': 'Hey, everything works!!'})

@app.route('/login-page')
def login_option():
    req_data = {'l': True} # replace with json
    username = request.form.get('username')
    print(username)
    if request.args.get('f') == '1':
        return render_template('LoginPage.html')
    elif req_data['l'] is True:
        return redirect(url_for('login_page'))
    else:
        return redirect(url_for('sign_up_page'))

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        return jsonify({'message': 'show login page'})
        pass
        # return login()
    else:
        return jsonify({'message': 'enter User in Database'})
        # return sign_up()
    
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up_page():
    if request.method == 'POST':
        user_data = request.form.to_dict()
        sign_up(user_data)
        return db.print()
    return render_template('LoginPage.html')
    return


@app.route('/trade')
def trade():
    if id is not None:
        return
    return render_template('TradePage.html')