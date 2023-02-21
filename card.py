# Name: Richard Cali

class Card:
    def __init__(self, x, y):
        self.x= x
        self.y= y
    def __repr__(self):
        return f"Card{self.x, self.y}"
    def __str__(self):
        return f"{self.x} of {self.y}"
    def __eq__(self, other):
        if Card((self.x + other.x), (self.y + other.y)):
            return True

        
    



    
