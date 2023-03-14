

class Car(object):

    def __init__(self):
        self.img = loadImage('images/car.png')
        self.x = 500
        
    def draw(self, cx, cy):
        self.img.resize(200,100)
        image(self.img, cx,cy)
        
    
    def update(self):
        self.x += 10
        # cy = cy
        # cxx = 100
        # while(cxx < 1100):
        #     cxx += 1
        # image(self.img,cxx,600)
