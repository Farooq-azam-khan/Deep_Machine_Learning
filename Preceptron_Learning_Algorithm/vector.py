import random
from typing import List 
import unittest

Vec = List[float]

class Vector():

    def __init__(self, dim: int):
        self.dim = dim # num of dimensions
        self.data: Vec = [0 for _ in range(dim)]
        # self.initalize()

    def initalize(self):
        for _ in range(self.dim):
            self.data.append(0)

    def randomize(self):
        self.data = [random.uniform(-1, 1) for _ in range(self.dim)]
        # for indx, _ in enumerate(self.data):
        #     self.data[indx] = random.uniform(-1, 1)

    @staticmethod
    def scalar_mul(vec, num: float):
        ret = Vector(vec.dim)
        ret.data = [num * val for val in vec.data]
        return ret

    def append(self, val):
        self.data.append(val)
    def set_dim(self, dim):
        self.dim = dim

    @staticmethod
    def to_vector(arr):
        ret = Vector(0)
        for val in arr:
            ret.append(val)
        ret.set_dim(len(arr))
        return ret

        return ret

    def __mul__(self, other):
        if (self.dim == other.dim):
            ret = Vector(0)
            for val_self, val_other in zip(self.data, other.data):
                ret.append(val_self * val_other)
            ret.dim = self.dim
            return ret
        else:
            print("must be same dim")
            return None
    @staticmethod
    def dot(vec1, vec2):
        if vec1.dim == vec2.dim:
            sum = 0
            for val1, val2 in zip(vec1.data, vec2.data):
                sum += (val1 * val2)
            return sum
        else:
            print("need to be same dimension", vec1.dim, vec2.dim)
            return None

    def to_array(self):
        return self.data

    def map(self, func):
        for indx, val in enumerate(self.data):
            self.data[indx] = func(val)

    @staticmethod
    def static_map(vec, func):
        ret = Vector(0)
        for val in vec.data:
            ret.append(func(val))
        ret.dim = len(vec.data)
        return ret

    def scalar_add(self, num):
        for indx, val in enumerate(self.data):
            self.data[indx] += num

    @staticmethod
    def scalar_add(v, num: float):
        vec = Vector(v.dim)
        vec.data = [val + num for val in v.data]
        return vec 

    def __add__(self, other):
        if self.dim == other.dim:
            result = Vector(self.dim)
            for indx, data_self in enumerate(self.data):
                result.data[indx] = data_self + other.data[indx]
            return result
        else:
            print("must have same dimensions")
            return None

    def __sub__(self, other):
        if self.dim == other.dim:
            result = Vector(self.dim)
            for indx, data_self in enumerate(self.data):
                result.data[indx] = data_self - other.data[indx]
            return result
        else:
            print("must have same dimensions")
            return None

    def __repr__(self):
        ret = "["
        for indx, val in enumerate(self.data):
            if indx == len(self.data)-1:
                ret += "{:.2f}".format(val)
            else:
                ret += "{:.2f}, ".format(val)
        return ret + "]"


class TestVector(unittest.TestCase):
    def test_init(self):
        v1 = Vector(10)

        self.assertTrue(v1.dim == 10)
        self.assertTrue(len(v1.data) == 10)
    
    def test_scalar(self):
        v = Vector(2)
        v.data[0] = 1
        v.data[1] = 2
        vs = Vector.scalar_mul(v, 2)
        self.assertTrue(vs.data[0] == 2)
        self.assertTrue(vs.data[1] == 4)

        v = Vector(2)
        vs = Vector.scalar_add(v, 2)
        self.assertTrue(vs.data[0] == 2)
        self.assertTrue(vs.data[1] == 2)
        


if __name__=="__main__":
    unittest.main()
