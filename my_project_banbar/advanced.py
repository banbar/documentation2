import sys, os 
from shapely.geometry import Polygon, Point
import geopandas as gp

# When packaging & developing:
# from . import add_subtract as base_module

# When creating the documentation
import add_subtract as base_module


def multiply_two_numbers(num1, num2):
    """Multiplies two numbers.

    Extended description on multiplying two numbers.

    Args:
        num1 (int or float): Could be a float or an int 
        num22 (int): the second number to add 

    Returns:
        int: the added value of the two input values.

    """
    t = 0
    for i in range(num2): 
        t = t + base_module.add_two_numbers(num1, 0) 
    return t

def distance_between_point_polygon(point_a, polygon_b):
    geo_poly = gp.GeoSeries(polygon_b)
    dist = geo_poly.boundary.distance(gp.GeoSeries(Point(point_a)))
    return dist[0]

def super_f3(num1):
    return num1**3

def super_f4(num1):
    return num1**4

def super_f5(num1):
    return num1**5

def super_f6(num1):
    return num1**6

    
        