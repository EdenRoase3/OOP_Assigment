#-00-Importing Required Classes and/or Modules
from TShapes import Shape3D
from TShapes import Octahedron
from TShapes import Hexagonal

#-01---------Start-up Option Legend-----------
print('----------------------Option Menu--------------------' + '\n')
print('Legend of acessor/mutator methods in derived classes: \n\n 1.Get/set method for type and colour(RBG) \n 2.ASCII \
drawing method (.draw())\n 3.Get/set edge of Octahedron(set_edge or get_edge()) \n 4.Print coordinates(.get_coordinates())'
      '\n 5.Set specific coordinate points of Octahedron (e.g set_A2()) \n 6.Volume and SurfaceArea (volume() \
and surface_area())\n\n')


#-02-Testing Some Instantiation,Fields and Methods--
obj1 = Shape3D('sphere', (3, 4, 5))
obj1.set_type('butterfly')
obj1.set_colour((4, 5, 5))
print(obj1.get_type())

obj1 = Octahedron('diamond', 4, (2, 3, 4))
obj1.set_A2((1, 2, 3))  # Put the tuple inside parentheses to set it as a 1 Element/Value

obj1.get_coordinates()
print(obj1.get_colour())

obj2 = Hexagonal('ddddd',4,5,(3,4,5))
obj2.get_coordinates()
obj2.set_type('circle')
print(obj2.get_type())
print(obj2.surface_area())
print(obj2.volume())


print(obj1.surface_area())
obj1.draw()
obj2.draw()