from user_database import UserDatabase
from user import User

db = UserDatabase()

def login(user: User) -> '???':
    for i in range(len(UserDatabase.users())):
        if UserDatabase.users()[i] == user:
            return user
    # user doesnt exists
        return 'errormsg'

def sign_up(some_dict):
    new_user = User(**some_dict)
    if new_user in db.users():
        return 'errormsg'
    else:
        db.add_user(new_user)


"""
Convert json to dict() flask.Request()


convert dict to json() "jsonify()"


from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
    
"""