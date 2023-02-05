from uuid import uuid4
class User:
    def __init__(self, username: str, password: str, socials: str):
        self._uid = str(uuid4())
        self._username = username
        self._password = password
        self._socials = socials
        self._wants = []
        self._haves = []
        
    def change_username(self, new_username: str) -> None:
        self._username = new_username
        
    def change_password(self, new_password: str) -> None:
        self._password = new_password
    
    def update_socials(self, new_socials: str) -> None:
        self._socials = new_socials
    def change_uuid(self):
        self._uid = uuid4()

    def get_username(self) -> str:
        return self._username
    
    def get_password(self) -> str:
        return self._password
    
    def get_socials(self) -> str:
        return self._socials

    def get_uuid(self):
        return self._uid

    def check_login(self, user, password):
        if (self.get_username() == user) and (self.get_password() == password):
            return True
        else:
            return False
