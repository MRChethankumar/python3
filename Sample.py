class Area:
   def area1(self, length, breadth):
       return length * breadth

class Area2:
   def __init__(self, length ,breadth, height):
       self.length = length
       self.breadth = breadth
       self.height = height

   def area1(self):
       return 0.5*self.length * self.breadth
  
   def volume(self):
       return self.length*self.breadth*self.height

area2 = Area2(4,5,6)

tri_area = area2.area1()

vol = area2.volume()

print(tri_area)
print(vol)

