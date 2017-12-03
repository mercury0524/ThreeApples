from Apple import Apple
from Adam import Adam
from Issac import Issac
from Steve import Steve

def setup():
  background(50)
  fullScreen()
  ellipseMode(CENTER)
  rectMode(CENTER)
  x_cen = width/2
  y_cen = height/2
  
def draw():
    fill(255)
    Bible = Adam()
    Newton = Issac()
    Jobs = Steve()
    Apples = [Jobs,Newton,Bible]
    for apple_ in Apples:
        apple_.display()
    