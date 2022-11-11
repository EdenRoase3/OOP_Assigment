# Initiating Class in Python (3D) Shapes
import math
import ascii_magic


class Shape3D:

    def __init__(self, type, colour):
        self.type = type
        self.colour = colour

    def volume(self):
        return None

    def surface_area(self):
        return None

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def draw(self):
        return None


class Octahedron(Shape3D):
    def __init__(self, type, colour, edge, x, y, z):
        super().__init__(type, colour)
        self.edge = edge
        self.x = x
        self.y = y
        self.z = z

    def get_edge(self):
        return self.edge

    def set_edge(self, edge):
        self.edge = edge

    def volume(self):
        volume = ((self.edge ** 3) * (math.sqrt(2) / 3))
        return volume

    def surface_area(self):
        surface_area = 2 * math.sqrt(3) * self.edge ** 2
        return surface_area

    def draw(self):
        output = ascii_magic.from_image_file('octa1.png', columns=100, char='@', back=ascii_magic.Back.WHITE)
        ascii_magic.to_terminal(output)


class Octapoints:
    def __init__(self, A1=(0, 0, 1), A2=(0, 1, 0), A3=(1, 0, 0)):
        pass
