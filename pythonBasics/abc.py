# Ref:: https://www.geeksforgeeks.org/abstract-classes-in-python/
# https://docs.python.org/3/library/abc.html

from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def sidesnumber(self):
        pass

class Triangle(Polygon):
    # overrideing the abstract method
    def sidesnumber(self):
        print("Triangle has 3 sides")

class Pentagon(Polygon):
    # overriding abstract method
    def sidesnumber(self):
        print("Pentagon have 5 sides")


tri= Triangle()
tri.sidesnumber()

pent= Pentagon()
pent.sidesnumber()
