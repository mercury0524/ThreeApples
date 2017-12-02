from Apple import Apple
def setup():
  background(0)
  fullScreen()
  ellipseMode(CENTER)
  rectMode(CENTER)
  
def draw():
    fill(255)
    #rect(width/2,height/2,width/3,height/3)
    Bible = Apple("adam")
    Newton = Apple("isaac")
    Jobs = Apple("steve")
    Apples = [Jobs,Newton,Bible]
    for apple_ in Apples:
        #apple_.display()
        pass
    Newton.display()
        