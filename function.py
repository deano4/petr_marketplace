from user_database import UserDatabase
from user import User
def login(user: User) -> '???':
    for i in range(len(UserDatabase.users())):
        if UserDatabase.users()[i] == user:
            return user
    # user doesnt exists
        return 'errormsg'

def sign_up(new_user: User) -> '???':
    if new_user in UserDatabase.users():
        return 'errormsg'
    else:
        UserDatabase.add_user(new_user)



Convert json to dict()


convert dict to json() "jsonify()"
