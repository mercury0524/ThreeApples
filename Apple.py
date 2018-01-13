class Apple(object):
    def __init__(self):
        self.x = displayWidth/2
        self.y = displayHeight/2
        
    def display(self):
        raise NotImplementedError
        
    def _basic_apple(self,scale_):
        x_cen = width/2
        y_cen = height/2 + scale_*10
        stroke_scale = scale_/2+0.5
        fill(255,8,0)
        #noStroke()
        stroke(120,0,0)
        strokeWeight(0.2*stroke_scale)
        #noStroke()
        ellipse(x_cen,y_cen,400*scale_,400*scale_)
        stroke(0)
        strokeWeight(6*stroke_scale)
        noFill()
        curve(x_cen,y_cen-240*scale_,x_cen-30*scale_,y_cen-150*scale_,x_cen+30*scale_,y_cen-150*scale_,x_cen,y_cen-240*scale_)
        stroke(120,0,0)
        strokeWeight(8*stroke_scale)
        line(x_cen+20*scale_,y_cen-225*scale_,x_cen,y_cen-155*scale_)
        
    def _shadow(self,scale_):
        x_cen = width/2
        y_cen = height/2 + scale_*10
        fill(0)
        noStroke()
        stroke_scale = scale_/2+0.5
        #ellipse(width/2+5*scale_,height/2+20*scale_,400*scale_,400*scale_)
        ellipse(width/2+4*scale_,y_cen+15*scale_,410*scale_,420*scale_)
        stroke(0)
        strokeWeight(8*stroke_scale)
        line(width/2+20*scale_+20,y_cen-220*scale_,width/2+20,y_cen-150*scale_)
        