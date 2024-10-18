
class Room:
    def __init__(self, number: int, passage_path: str) -> None:
        self.number: int = number               #Room Number
        self.passage_path: str = passage_path   #The Passage that Guest come from

    def __str__(self) -> str:
        return str(self.number)

     

    