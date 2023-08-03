from __future__ import annotations
from math import sqrt, acos


class Vector:
    def __init__(self, args):
        if isinstance(args, int):
            self._v = [0 for i in range(args[0])]
        else:
            self._v = args

    @classmethod
    def _from(cls, array):
        return Vector(array)

    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, value):
        self._v[index] = value

    def __len__(self) -> int:
        return len(self._v)

    def __iter__(self):
        return iter(self._v)

    def __add__(self, other: Vector) -> Vector:
        if len(self) != len(other):
            raise TypeError("Adding vectors of different dimensions")
        return type(self)._from([self[i] + other[i] for i in range(len(self))])

    def __sub__(self, other: Vector) -> Vector:
        if len(self) != len(other):
            raise TypeError("Adding vectors of different dimensions")
        return type(self)._from([self[i] + other[i] for i in range(len(self))])

    def __neg__(self) -> Vector:
        return type(self)._from([-self[i] for i in range(len(self))])

    def __pos__(self) -> Vector:
        return type(self)._from([-self[i] for i in range(len(self))])

    def absolute(self) -> Vector:
        return type(self)._from([abs(self[i]) for i in range(len(self))])

    def __abs__(self):
        return sqrt(sum(map(lambda x: x**2, self)))

    def squaredabs(self):
        return sum(map(lambda x: x**2, self))

    def __div__(self, other):
        if not hasattr(other, "__iter__"):
            return type(self)._from([self[i] / other for i in range(len(self))])
        else:
            if len(self) != len(other):
                raise TypeError("Multiplying vectors of different dimensions")
            return sum([self[i] / other[i] for i in range(len(self))])

    def __floordiv__(self, other):
        if not hasattr(other, "__iter__"):
            return type(self)._from([self[i] // other for i in range(len(self))])
        else:
            if len(self) != len(other):
                raise TypeError("Multiplying vectors of different dimensions")
            return type(self)._from([self[i] // other[i] for i in range(len(self))])

    def __mod__(self, other):
        if not hasattr(other, "__iter__"):
            return type(self)._from([self[i] % other for i in range(len(self))])
        else:
            if len(self) != len(other):
                raise TypeError("Operation with vectors of different dimensions")
            return type(self)._from([self[i] % other[i] for i in range(len(self))])

    def __mul__(self, other):
        if not hasattr(other, "__iter__"):
            return type(self)._from([self[i] * other for i in range(len(self))])
        else:
            if len(self) != len(other):
                raise TypeError("Multiplying vectors of different dimensions")
            return sum([self[i] * other[i] for i in range(len(self))])

    def __rmul__(other, self):
        if not hasattr(other, "__iter__"):
            return type(self)._from([self[i] * other for i in range(len(self))])
        else:
            self.__mul__(other)

    def __eq__(self, other):
        return self._v == other._v

    def dot(self, other: Vector):
        return self.__mul__(other)

    def clamp(self, min_value=-float("inf"), max_value=float("inf")):
        if min_value <= max_value:
            array = []
            for i in self:
                if i < min_value:
                    i = min_value
                if i > max_value:
                    i = max_value
                array.append(i)
            return type(self)._from(array)
        else:
            raise ValueError("Invalid interval")

    def angle(self, other: Vector):
        return acos((self * other) / sqrt(self.squaredabs() * other.squaredabs()))

    def normalize(self):
        return self / abs(self)

    def __repr__(self):
        return type(self).__name__ + "{" + str(list(self._v))[1:-1] + "}"


class Vector2D(Vector):
    def __init__(self, x, y):
        super().__init__([x, y])

    @classmethod
    def _from(cls, array):
        if len(array) == 2:
            return Vector2D(*array)
        else:
            raise TypeError("Invalid vector length of Vector2D")

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value


class Vector3D(Vector):
    def __init__(self, x, y, z):
        super().__init__([x, y, z])

    @classmethod
    def _from(cls, array):
        if len(array) == 3:
            return Vector3D(*array)
        else:
            raise TypeError("Invalid vector length of Vector2D")

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

    @property
    def z(self):
        return self[2]

    @z.setter
    def z(self, value):
        self[2] = value

    def __matmul__(self, other: Vector3D):
        return self.cross(other)

    def cross(self, other: Vector3D) -> Vector3D:
        x = self.y * other.z - self.z * other.y
        y = other.x * self.z - other.z * self.x
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)


class Point2D:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __sub__(self, other) -> Vector2D:
        return Vector2D(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Point2D(-self.x, -self.y)

    def __pos__(self):
        return Point2D(+self.x, +self.y)

    def __abs__(self, other):
        return Point2D(abs(self.x), abs(self.y))

    def __mul__(self, other):
        return Point2D(self.x * other, self.y * other)

    def __rmul__(other, self):
        return Point2D(self.x * other, self.y * other)

    def __div__(self, other):
        return Point2D(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return Point2D(self.x // other, self.y // other)

    def distance(self, other: Point2D):
        return sqrt(self.squared_distance())

    def manhattan_distance(self, other: Point2D):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def squared_distance(self, other: Point2D):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2


class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    def __sub__(self, other) -> Vector2D:
        return Vector3D(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z)

    def __add__(self, other):
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z)

    def __neg__(self):
        return Point3D(-self.x, -self.y, -self.z)

    def __pos__(self):
        return Point3D(+self.x, +self.y, +self.z)

    def __abs__(self, other):
        return Point2D(abs(self.x), abs(self.y), abs(self.z))

    def __mul__(self, other):
        return Point2D(self.x * other, self.y * other, self.z * other)

    def __rmul__(other, self):
        return Point2D(self.x * other, self.y * other, self.z * other)

    def __div__(self, other):
        return Point2D(self.x / other, self.y / other, self.z / other)

    def __floordiv__(self, other):
        return Point2D(self.x // other, self.y // other, self.z // other)

    def distance(self, other: Point2D):
        return sqrt(self.squared_distance())

    def manhattan_distance(self, other: Point2D):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def squared_distance(self, other: Point2D):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2