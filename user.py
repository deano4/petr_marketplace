


class User:
    def __init__(self, username: str, password: str, socials: str):
        self._username = username
        self._password = password
        self._socials = socials
        
    def change_username(self, new_username: str) -> None:
        self._username = new_username
        
    def change_password(self, new_password: str) -> None:
        self._password = new_password
    
    def update_socials(self, new_socials: str) -> None:
        self._socials = new_socials
        
    def get_username(self) -> str:
        return self._username
    
    def get_password(self) -> str:
        return self._password
    
    def get_socials(self) -> str:
        return self._socials