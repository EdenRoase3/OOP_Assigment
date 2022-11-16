##--0---Importing Required Packages--##
import math
import ascii_magic

##--1---Creating a 3D Shape Parent Class--##
class Shape3D:

    def __init__(self, type: str, colour: tuple =(255,255,255)):
        self.type = type
        self.colour = colour

    def volume(self):
        return None

    def surface_area(self):
        return None

    def get_type(self):
        return self.type

    def set_type(self, type: str):
        self.type = type

    def get_colour(self):
        return self.colour

    def set_colour(self, colour: str):
        self.colour = colour

    def draw(self):
        return None


class Octapoints:
    def __init__(self, A1=(0, 0, -1), A2=(-1, 0, 0), A3=(0, 0, 1), A4=(1, 0, 0), B1=(0, 1, 0), C1=(0, -1, 0)):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.B1 = B1
        self.C1 = C1

    def set_A1(self, new: float):
        self.A1 = new

    def set_A2(self, new: float):
        self.A2 = (new)

    def set_A3(self, new: float):
        self.A3 = (new)

    def set_A4(self, new: float):
        self.A4 = (new)

    def set_B1(self, new: float):
        self.B1 = (new)

    def set_C1(self, new: float):
        self.C1 = (new)

    def get_coordinates(self):
        print(
            f'Point 1: {self.A1}\nPoint 2: {self.A2}\nPoint 3: {self.A3}\nPoint 4: {self.A4}\nPoint 5: {self.B1}\nPoint 6: {self.C1}')


class Hexapoints:
    def __init__(self, O=(0, 8, 0), A=(-5, 0, 0), B=(-2.5, 0, 4.33), C=(2.5, 0, 4.33), D=(5, 0, 0), E=(2.5, 0, -4.33),
                 F=(-2.5, 0, -4.33)):
        self.O = O
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F

    def set_O(self, new: tuple):
        self.O = new

    def set_A(self, new: tuple):
        self.A = new

    def set_B(self, new: tuple):
        self.B = new

    def set_C(self, new: tuple):
        self.B = new

    def set_D(self, new: tuple):
        self.D = new

    def set_E(self, new: tuple):
        self.E = new

    def get_coordinates(self):
        print(
            f'Point 1: {self.A}\nPoint 2: {self.B}\nPoint 3: {self.C}\nPoint 4: {self.D}\nPoint 5: {self.E}\nPoint 6: {self.F}')


class Octahedron(Shape3D, Octapoints):
    def __init__(self, type, edge, colour):
        super().__init__(type, colour)
        super(Shape3D, self).__init__()
        self.edge = edge

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
        output = ascii_magic.from_image_file('octahedron.jpg', columns=70, char='@', back=ascii_magic.Back.WHITE)
        ascii_magic.to_terminal(output)


class Hexagonal(Shape3D, Hexapoints):
    def __init__(self, type, a, h, colour):
        super().__init__(type, colour)
        super(Shape3D, self).__init__()
        self.a = a
        self.h = h

    def surface_area(self):
        surface_area = ((3 * math.sqrt(3) / 2) * self.a ** 2) + 3 * self.a * (
            math.sqrt(self.h ** 2 + (3 * (self.a ** 2) / 4)))
        return surface_area

    def volume(self):
        volume = (math.sqrt(3) / 2) * (self.a ** 2) * self.h
        return volume

    def set_a(self, new):
        self.a = new

    def set_h(self, new):
        self.h = new

    def get_a(self):
        return self.a

    def get_h(self):
        return self.h

    def draw(self):
        output = ascii_magic.from_image_file('hex1.png', columns=70, char='@', back=ascii_magic.Back.WHITE)
        ascii_magic.to_terminal(output)
