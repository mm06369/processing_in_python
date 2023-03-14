# from gui import GUI
from screen import Screen
from cloud import Cloud
from car import Car
from gui import GUI
from particleEmitter import particleEmitter

hud = None
def setup():
    global hud, ps
    size(1280,800)
    hud = GUI()
    img = loadImage("images/texture_3.png")
    initial = 0
    ps = particleEmitter(initial, img, PVector(500, height/2))

    
def draw():
    screen = Screen()
    screen.draw()
    cloud = Cloud()
    cloud.draw()
    car = Car()
    car.draw(500,600)
    # car.update()
    hud.draw()
    ps.update()
    ps.add_particle(400,680)
        # background(0)
    # image(bg,80,100)
    # screen = Screen()
    # screen.draw()
