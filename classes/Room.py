
class Room:
    def __init__(self, number: int, passage_path: str) -> None:
        self.number: int = number
        self.passage_path: str = passage_path

    def __str__(self) -> str:
        return str(self.number)

     

    