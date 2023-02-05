from user import User

class UserDatabase:
    def __init__(self):
        self._users: list[User] = []

    def add_user(self, new_user: User) -> None:
        self._users.append(new_user)

    def users(self) -> list[User]:
        return self._users

    def search_uid(self, select_uid: str)-> User:
        for a_user in self._users:
            if a_user.get_uid() == select_uid:
                print(a_user)
                return a_user
    def search_username(self, username: str) -> User:
        for user in self._users:
            if user.get_username() == username:
                return user