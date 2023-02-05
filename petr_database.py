from petr import Petr

class PetrDatabase:
    def __init__(self):
        self._petrs: dict[str: Petr] = {}

    def add_petr(self, name:str, new_petr: Petr) -> None:
        self._petrs[name] = new_petr

    def petrs(self) -> dict[str: Petr]:
        return self._petrs
    
    def petr_count(self) -> int:
        return len(self._petrs)

    
        