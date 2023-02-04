from petr import Petr

class PetrDatabase:
    def __init__(self):
        self._petrs: list[Petr] = []

    def add_petr(self, new_petr: Petr) -> None:
        self._petrs.append(new_petr)

    def petrs(self) -> list[Petr]:
        return self._petrs
    
    def petr_count(self) -> int:
        return len(self._petrs)