
class Cloud(object):
    
    def __init__(self):
        self.square = createShape(RECT,0,0,1280,100)
        self.square.setFill(color(173,216,230))
        self.square.setStroke(False)
        
    def draw(self):
        shape(self.square,0,0)
        

        
