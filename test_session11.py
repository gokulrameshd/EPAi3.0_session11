
#import necessary modules
from math import *
from objective1 import *
from objective2 import *
import pytest


def test_1():
    polygon1 = polygon(n =5 , r =10)
    assert polygon1.edges == 5 , "Wrong number of edges!!"

def test_2():
    polygon1 = polygon(n =5 , r =10)
    assert polygon1.vertices == 5 , "Wrong number of vertices!!"

def test_3():
    polygon1 = polygon(n =5 , r =10)
    assert polygon1.edge_length == 11.755705045849464 , "edge_length is calculation is wrong!!"

def test_4():
    polygon1 = polygon(n =5 , r =10)
    assert polygon1.interior_angle == 108 , "interior_angle is calculation is wrong!!"

def test_5():
    polygon1 = polygon(n =5 , r =10)
    assert polygon1.apothem == 8.090169943749475 , "apothem is calculation is wrong!!"

def test_6():
    polygon1 = polygon(n =5 , r =10)
    assert polygon1.perimeter ==  58.77852522924732 , "perimeter is calculation is wrong!!"

def test_7():
    polygon1 = polygon(n =5 , r =10)
    assert polygon1.area ==  237.76412907378844 , "area is calculation is wrong!!"

def test_8():
    polygon1 = polygon(n =5 , r =10)
    assert polygon1.__repr__() == "No of sides :5 , Radius : 10" , "__repr__ is not working !!"

def test_9():
    polygon1 = polygon(n =5 , r =10) # the initializer takes in  
    polygon2 = polygon(n =5 , r =10)
    assert polygon1 == polygon2 , " __eq__ is not working !!"

def test_10():
    polygon1 = polygon(n =5 , r =10) # the initializer takes in  
    polygon2 = polygon(n =4 , r =10)
    assert polygon1 > polygon2 , " __gt__ is not working !!"

def test_11():
    poly_seq = polygons_sequence(n = 25 , r =100)
    assert len(poly_seq) == 23 , " __len__ is not working !!"

def test_12():
    poly_seq = polygons_sequence(n = 25 , r =100)
    assert str(next(poly_seq)) == "No of sides :3 , Radius : 100" , "__next__ is not working!!"

def test_13():
    poly_seq = polygons_sequence(n = 25 , r =100)
    poly_seq.__iter__() == "Polygon sequence of 23 polygons" , "__iter__ is not working!!"