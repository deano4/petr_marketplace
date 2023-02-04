from user_database import UserDatabase
from user import User
from petr_database import PetrDatabase
from petr import Petr
from random import randrange
user_db = UserDatabase()
petr_db = PetrDatabase()

# hard coding users in 
"""user1 = User('peter', 'anteater', '@petera')
user2 = User('user2', 'anteater', '@peter222')
user_db.add_user(user1)
user_db.add_user(user2)
petr1 = Petr()
petr2 = Petr()
petr_db.add_petr('antman', petr1)
petr_db.add_petr('aot', petr2)
petr1.add_to_want(user1)
petr2.add_to_haves(user1)"""
first_names=('John','Andy','Joe', "James", "Lucas", "Howard", "Steve", "Bad")
last_names=('Johnson','Smith','Williams', "Nguyen", "Lee", "Pham", "Stupid")
for fn in first_names:
    for ln in last_names:
        input_name = fn + " " + ln
        social = "@" + input_name
        x = User(input_name, input_name, social)
        user_db.add_user(x)


petr_names = ("antman", "aot", "bday", "bday", "christmas", "duck", "fire", "firefighter",
              "grad", "green", "hello_kitty", "hero", "horse", "jack", "mom", "nurse",
              "robber", "shrek", "thanos", "theWeeknd")
for petr_n in petr_names:
    x = Petr(petr_n)
    for i in range(0,randrange(0, 10)):
        num = randrange(0, len(user_db.users()))
        adding = user_db.users()[num]
        x.add_to_want(adding)
    for i in range(0,randrange(0, 10)):
        num = randrange(0, len(user_db.users()))
        adding = user_db.users()[num]
        x.add_to_haves(adding)
    petr_db.add_petr(x.get_name(), x)

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

def market(name: str) -> dict:
    a_petr = petr_db.petrs()[name]
    wants = a_petr.wants() 
    haves = a_petr.haves()
    usrs_want = {}
    for user in wants:
        usrs_want[user.get_username()] = user.get_socials()
    usrs_have =  {}
    for user in haves:
        usrs_have[user.get_username()] = user.get_socials()
    print(usrs_want)
    return {"users_want": usrs_want, "users_have": usrs_have}
    
"""
Convert json to dict() flask.Request()


convert dict to json() "jsonify()"


from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
    
"""