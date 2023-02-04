from user import User

class UserDatabase:
    def __init__(self):
        self._users: list[User] = []

    def add_user(self, new_user: User) -> None:
        self._users.append(new_user)

    def users(self) -> list[User]:
        return self._users