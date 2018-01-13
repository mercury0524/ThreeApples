from Apple import Apple
class Adam(Apple):
    def __init__(self):
        self.scale_ = 0.4
        Apple().__init__()
        
        
    def display(self):
        Apple()._shadow(self.scale_)
        Apple()._basic_apple(self.scale_)
    
        