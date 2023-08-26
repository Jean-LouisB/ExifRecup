class autoId():
    def __init__(self):
        self.id = 0
    def nextId(self):
        id= self.id
        self.id+=1
        return id

