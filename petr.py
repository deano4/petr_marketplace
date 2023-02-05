from user import User

class Petr:
    def __init__(self, name):
        self.name = name
        self._wants = {}
        self._haves = {}

    def add_to_want(self, user: User) -> None:
        self._wants[user.get_username()] = user.get_socials()
        
    def add_to_haves(self, user: User) -> None:
        self._haves[user.get_username()] = user.get_socials()

    def del_to_want(self, user: User) -> None:
        del self._wants[user.get_username()]

    def del_to_haves(self, user: User) -> None:
        del self._haves[user.get_username()]

    def haves(self) -> dict:
        return self._haves

    def wants(self) -> dict:
        return self._wants

    def set_name(self, change):
        self.name = change

    def get_name(self):
        return self.name
