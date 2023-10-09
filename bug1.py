class Base:
    
    def __init__(self, x, y, size, shape):
        self.x = x
        self.y = y
        self.size = size
        self.shp = shape

    def shape(self):
        return self.shp
        
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



    def shape(self):
        return super().shape()
