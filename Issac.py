from Apple import Apple
class Issac(Apple):
    def __init__(self):
        self.scale_ = 1.2
        Apple().__init__()
        
        
    def display(self):
        Apple()._shadow(self.scale_)
        Apple()._basic_apple(self.scale_)
    