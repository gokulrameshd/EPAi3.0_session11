from math import *
from objective1 import *


class polygons_sequence:
    """
    This class returns the returns an objects -> iterable & iterator.
    It also have properties such maximum efficient polygon.
    """
    def __init__(self,n,r):
        self.n = n
        if n < 3:
            raise ValueError("n must be greater then 3")
        self.r = r
        self._polygons = list([polygon((i), r )  for (i) in range(3,self.n+1)])
        self.maximum_efficient_polygon = self.max_efficiency_polygons()
#         self.iter_polygon = iter(self._polygons)
        self.index = 0
    def __repr__(self):
        return f'Polygon sequence of {len(self._polygons)} polygons'

    def __len__(self):
        return len(self._polygons)

    def __getitem__(self,s):
        return self._polygons[s] #next(self._polygons[s])
    def __iter__(self):
        return self
    def __next__(self):
#         return next(self.iter_polygon)
        try:
            result = self._polygons[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result
    def max_efficiency_polygons(self):
        seq = sorted(self._polygons,
                    key = lambda p:p.area/p.perimeter,
                    reverse = True)
        # print(seq)
        return seq[0]
    