from user import User

class Petr:
    def __init__(self, name):
        self.name = name
        self._wants = []
        self._haves = []

    def add_to_want(self, user: User) -> None:
        self._wants.append(user)
        
    def add_to_haves(self, user: User) -> None:
        self._haves.append(user)

    def del_to_want(self, user: User) -> None:
        self._wants.remove(user)

    def del_to_haves(self, user: User) -> None:
        self._haves.remove(user)

    def haves(self) -> list:
        return self._haves

    def wants(self) -> list:
        return self._wants


    def set_name(self, change):
        self.name = change

    def get_name(self):
        return self.name
