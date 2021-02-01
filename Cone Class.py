import math
class Cone():
    def __init__(self,r,h):
        self.r = r
        self.h = h
    def volume(self):
        vol = 3.14*math.pow(self.r,2)*(self.h/3)
        print('volume of the cone is : ', vol)
    def Surfacearea(self):
        area = 3.14*self.r*(self.r+math.sqrt(math.pow(self.r,2) + math.pow(self.h,2)))
        print('Surface area of the cone is : ',area)

Radius = int(input('Enter Radius of the cone : '))
Height = int(input('Enter Height of the cone : '))
print()
cone = Cone(Radius,Height)
cone.volume()
cone.Surfacearea()
