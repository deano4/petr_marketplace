from user_database import UserDatabase
from user import User
from petr_database import PetrDatabase
from petr import Petr

user_db = UserDatabase()
petr_db = PetrDatabase()

# hard coding users in 
user1 = User('peter', 'anteater', '@petera')
user2 = User('user2', 'anteater', '@peter222')
user_db.add_user(user1)
user_db.add_user(user2)
petr1 = Petr()
petr2 = Petr()
petr_db.add_petr('antman', petr1)
petr_db.add_petr('aot', petr2)
petr1.add_to_want(user1)
petr2.add_to_haves(user1)


def login(user: User) -> '???':
    for i in range(len(user_db.users())):
        if user_db.users()[i] == user:
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