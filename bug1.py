class Base:
    
    def __init__(self, x, y, size, shape):
        self.x = x
        self.y = y
        self.size = size
        self.shape = shape

    def shape(self):
        return self.shape
        
    def draw(self, string):
        return string

class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, "This is a circle")

    def draw(self):
        return f"""({self.x}, {self.y})\n{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """



    def get_shape(self):
        return super().shape()

def main():
    c = Circle(1, 2, 3)
    print(c.get_shape())
    print(c.draw())

main()
