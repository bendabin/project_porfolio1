#Create a class called shape
class Shape():                  #Parent class
    def __init__(self):
        pass
    
    def what_am_i(self):
        print("I am a shape")
        
class Square(Shape):            #Child1 class
    pass

class Rectangle(Shape):         #Child2 class
    pass
  
#Create the objects    
square = Square()
rectangle = Rectangle()

#Call the methods
square.what_am_i()
rectangle.what_am_i()