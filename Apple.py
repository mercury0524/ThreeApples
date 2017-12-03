class Apple(object):
    def __init__(self):
        self.x = displayWidth/2
        self.y = displayHeight/2
        
    def display(self):
        # if (self._name == "adam"):
        #     self._display_adam()
        # elif (self._name == "isaac"):
        #     self._display_issac()
        # elif (self._name == "steve"):
        #     self._display_steve()
        
        pass
            
    def _display_adam(self):
        self._simple_apple(1)
        
    def _display_issac(self):
        self._branch_and_leaf()
        self._simple_apple(1.5)
        
        
        
    def _display_steve(self):
        self._simple_apple(2)
        self._bite()
        
        
    def _simple_apple(self,scale_):
        fill(255,0,0)
        noStroke()
        pushMatrix()
        translate(self.x-30*scale_,self.y)
        rotate(-PI/15)
        ellipse(0,0,150*scale_,200*scale_)
        popMatrix()
        pushMatrix()
        translate(self.x+30*scale_,self.y)
        rotate(PI/15)
        ellipse(0,0,150*scale_,200*scale_)
        popMatrix()
        
    #for isaac's apple
    def _branch_and_leaf(self):
        fill(100,30,30)
        rect(self.x,self.y-165,20,75)
    
    def _bite(self):
        pass