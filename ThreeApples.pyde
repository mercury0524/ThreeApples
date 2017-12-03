from Apple import Apple
from Adam import Adam
from Issac import Issac
from Steve import Steve
def setup():
  background(0)
  fullScreen()
  ellipseMode(CENTER)
  rectMode(CENTER)
  x_cen = width/2
  y_cen = height/2
  
def draw():
    fill(255)
    #rect(width/2,height/2,width/3,height/3)
    #Bible = Apple("adam")
    #Newton = Apple("isaac")
    #Jobs = Apple("steve")
    Bible = Adam()
    #Apples = [Jobs,Newton,Bible]
    #for apple_ in Apples:
        #apple_.display()
        #pass
    Bible.display()


def minimal():
    x_cen = width/2
    y_cen = height/2
    fill(255,0,0)
    #noStroke()
    stroke(120,0,0)
    strokeWeight(6)
    ellipse(x_cen,y_cen,400,400)
    stroke(0)
    strokeWeight(6)
    noFill()
    curve(x_cen,300,x_cen-30,y_cen-150,x_cen+30,y_cen-150,x_cen,300)
    stroke(120,0,0)
    strokeWeight(8)
    line(x_cen+20,y_cen-225,x_cen,y_cen-155)
    