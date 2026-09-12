class Student:
    def __init__(
            self,
            id:str,
            name:str,
            age:int,
            score:float,):
        self.sid = id
        self.name=name
        self.age=age
        self.score=score
    def to_dict(self) -> dict:
        return {
            "id": self.sid,
            "name": self.name,
            "age": self.age,
            "score": self.score
        }