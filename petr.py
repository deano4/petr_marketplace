from user import User

class Petr:
    def __init__(self):
        self._wants = []
        self._haves = []

    def add_to_want(self, user: User) -> None:
        self._wants.append(user)
        
    def add_to_haves(self, user: User) -> None:
        self._haves.append(user)

    def get_haves(self) -> list:
        return self._haves

    def get_wants(self) -> list:
        return self._wants
