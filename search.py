from user_database import UserDatabase
from user import User
from petr_database import PetrDatabase
from petr import Petr

user_db = UserDatabase()
petr_db = PetrDatabase()

def login(user: User) -> '???':
    for i in range(len(UserDatabase.users())):
        if UserDatabase.users()[i] == user:
            return user
    # user doesnt exists
        return 'errormsg'

def sign_up(some_dict):
    new_user = User(**some_dict)
    if new_user in user_db.users():
        return 'errormsg'
    else:
        user_db.add_user(new_user)

def market(name: str) -> 'str':
    a_petr = petr_db[name]
    wants = a_petr.wants() 
    haves = a_petr.haves()
    usrs_want = ""
    for index, user in enumerate(wants):
        usrs_want += f'{user.get_username()}: {user.get_socials}'
        if index != len(wants) - 1:
            usrs_want += ', '
    usrs_have =  ""
    for index, user in enumerate(haves):
        usrs_have += f'{user.get_username()}: {user.get_socials}'
        if index != len(wants) - 1:
            usrs_have += ', '
    return '{' + f"users_have: {usrs_have}, users_want: {usrs_want}" + '}'
    
"""
Convert json to dict() flask.Request()


convert dict to json() "jsonify()"


from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
    
"""