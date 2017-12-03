from Apple import Apple
class Steve(Apple):
    def __init__(self):
        self.scale_ = 2.4
        Apple().__init__()
        
        
    def display(self):
        Apple()._shadow(self.scale_)
        Apple()._basic_apple(self.scale_)