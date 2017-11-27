class Apple():
    def __init__(self, name):
        self._name = name
    def display(self):
        if (self._name == "adam"):
            self._display_adam()
        elif (self._name == "isaac"):
            self._display_issac()
        elif (self._name == "steve"):
            self.display_steve()
    def display_adam(self):
        self.simple_apple(1)
    def display_issac(self):
        self.simple_apple(1.5)
    def display_steve(self):
        self.simple_apple(2)
    def simple_apple(self,scale_):
        pushMatrix()
        translate(displayWidth/2-30*factor,displayHeight/2)
        rotate(-PI/15)
        ellipse(0,0,150*factor,200*factor)
        popMatrix()
        pushMatrix()
        translate(displayWidth/2+30*factor,displayHeight/2)
        rotate(PI/15)
        ellipse(0,0,150*factor,200*factor)
        popMatrix()