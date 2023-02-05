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
petr1.add_to_wants(user1)
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
        x.add_to_wants(adding)
    for i in range(0,randrange(0, 10)):
        num = randrange(0, len(user_db.users()))
        adding = user_db.users()[num]
        x.add_to_haves(adding)
    petr_db.add_petr(x.get_name(), x)

def login(user, password) -> '???':
    output = {}
    for index in range(0, len(user_db.users())):
        existing_user = user_db.users()[index]
        if existing_user.check_login(user, password):
            output['uid'] = existing_user.get_uid()
            output['error'] = False
            return output
    # user doesnt exists
    output['error'] = True
    return output


# a testable user
test_user = User("test", "test", "@test")
user_db.add_user(test_user)
petr_db.petrs()["antman"].add_to_wants(test_user)
petr_db.petrs()["antman"].add_to_haves(test_user)


def sign_up(username, password, socials):
    output = {}
    new_user = User(username, password, socials)
    for a_user in user_db.users():
        if username == a_user.get_username():
            output['error'] = True
            return output
    user_db.add_user(new_user)
    output['uid'] = new_user.get_uid()
    output['error'] = False
    return output

def market(name: str, uid: str) -> dict:
    a_petr = petr_db.petrs()[name]
    wants = a_petr.wants() 
    haves = a_petr.haves()
    user_want = False
    user_have = False
    usrs_want = {}
    for username in wants.keys():
        user = user_db.search_username(username)
        usrs_want[user.get_username()] = user.get_socials()
        if uid == user.get_uid():
            user_want = True
    usrs_have =  {}
    for username in haves.keys():
        user = user_db.search_username(username)
        usrs_have[user.get_username()] = user.get_socials()
        if uid == user.get_uid():
            user_have = True
    output = {
        "list_want": usrs_want,
        "list_have": usrs_have,
        "user_want": user_want,
        "user_have": user_have
    }
    return output

def have_toggle(name: str, uid: str) -> dict:
    output = {}
    
    a_petr = petr_db.petrs()[name]
    have_list = a_petr.haves()
    for username in have_list.keys():
        user = user_db.search_username(username)
        if user.get_uid() == uid:
            a_petr.del_to_haves(user)
            output["list_have"] = a_petr.haves()
            output["user_have"] = False
            output['error'] = False
            return output
    the_user = user_db.search_uid(uid)
    a_petr.add_to_haves(the_user)
    output["list_have"] = a_petr.haves()
    output["user_have"] = True
    output['error'] = False
    return output
    #except:
    output['error'] = True
    return output

def want_toggle(name: str, uid: str):
    output = {}
    try:
        a_petr = petr_db.petrs()[name]
        want_list = a_petr.wants()
        for username in want_list.keys():
            user = user_db.search_username(username)
            if user.get_uid() == uid:
                a_petr.del_to_wants(user)
                output["list_want"] = a_petr.wants()
                output["user_want"] = False
                output['error'] = False
                return output
        the_user = user_db.search_uid(uid)
        a_petr.add_to_wants(the_user)
        output["list_want"] = a_petr.wants()
        output["user_want"] = True
        output['error'] = False
        return output
    except:
        output['error'] = True
        return output


"""
Convert json to dict() flask.Request()


convert dict to json() "jsonify()"


from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
    
"""