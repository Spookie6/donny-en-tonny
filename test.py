class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def centered(w=0, h=0):
        return Pos(1280 / 2 - w / 2, 720 / 2 - h / 2)
    
    def getPosTuple(self):
        return (self.x, self.y)
    
print(Pos.centered(100, 100).getPosTuple())