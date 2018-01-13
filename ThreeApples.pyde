from Apple import Apple
from Adam import Adam
from Issac import Issac
from Steve import Steve

mode = 1
shift = 0

def setup():
  background(50)
  fullScreen()
  ellipseMode(CENTER)
  rectMode(CENTER)
  
def draw():
    global mode
    global shift
    background(50)
    Bible = Adam()
    Newton = Issac()
    Jobs = Steve()
    Apples = [Jobs,Newton,Bible]
    if (mode == 1):
        shift = 0
        fill(255)
        for apple_ in Apples:
            apple_.display()
    elif (mode == 2):
        translate(0,shift)
        Newton.display()
        shift = shift+0

def mouseClicked():
    global mode
    if (mode == 1):
        mode = 2
    if (mode == 2):
        mode = 1
    

        