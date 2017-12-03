from Apple import Apple
class Adam(Apple):
    def __init__(self):
        Apple().__init__
        
    def display(self):
        Apple().display()
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
    
        