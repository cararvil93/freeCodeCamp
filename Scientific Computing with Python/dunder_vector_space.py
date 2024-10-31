class R2Vector:
    def __init__(self, *, x, y):
        # Initialize a 2D vector with x and y components#+
        self.x = x
        self.y = y

    def norm(self):
        # Calculate and return the Euclidean norm (magnitude) of the vector#+
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        # Return a string representation of the vector as a tuple#+
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        # Return a detailed string representation of the vector for debugging#+
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        # Define vector addition#+
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        # Define vector subtraction#+
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        # Define scalar multiplication or dot product#+
        if type(other) in (int, float):
            # Scalar multiplication#+
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            # Dot product#+
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented

    def __eq__(self, other):
        # Define equality comparison#+
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))

    def __ne__(self, other):
        # Define inequality comparison#+
        return not self == other

    def __lt__(self, other):
        # Define less-than comparison based on vector norm#+
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        # Define greater-than comparison based on vector norm#+
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        # Define less-than-or-equal comparison#+
        return not self > other

    def __ge__(self, other):
        # Define greater-than-or-equal comparison#+
        return not self < other

class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        # Initialize a 3D vector with x, y, and z components#+
        super().__init__(x=x, y=y)
        self.z = z

    def cross(self, other):
        # Calculate and return the cross product of two 3D vectors#+
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }

        return self.__class__(**kwargs)
#+
# Example usage of the R3Vector class#+
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * v2
print(f'v1 * v2 = {v5}')
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')
