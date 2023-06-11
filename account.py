class Account:
    def __init__(self, id: str, name: str, type: str, offbudget: bool, closed: bool):
        self.id = id
        self.name = name
        self.type = type
        self.offbudget = offbudget
        self.closed = closed