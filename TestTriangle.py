# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

        # ---------- Invalid / Not a triangle ----------
    def testInvalidZero(self):
        self.assertEqual(classifyTriangle(0,4,5), 'InvalidInput', '0,4,5 should be invalid')

    def testInvalidTooLarge(self):
        self.assertEqual(classifyTriangle(201,4,5), 'InvalidInput', '201,4,5 should be invalid')

    def testInvalidNegative(self):
        self.assertEqual(classifyTriangle(-1,2,3), 'InvalidInput', '-1,2,3 should be invalid')

    def testInvalidNonInteger(self):
        self.assertEqual(classifyTriangle(1.5,2,3), 'InvalidInput', '1.5,2,3 should be invalid')

    def testNotATriangle_EqualEdge(self):
        # 1+2=3：not a triangle
        self.assertEqual(classifyTriangle(1,2,3), 'NotATriangle', '1,2,3 is not a triangle')

    def testNotATriangle_StrictLess(self):
        # 2+3<6：not a triangle
        self.assertEqual(classifyTriangle(2,3,6), 'NotATriangle', '2,3,6 is not a triangle')

    def testNotATriangle_TwoEqualTooShort(self):
        self.assertEqual(classifyTriangle(1,1,3), 'NotATriangle', '1,1,3 is not a triangle')

    def testNotATriangle_LargeEqualEdge(self):
        self.assertEqual(classifyTriangle(200,1,199), 'NotATriangle', '200,1,199 is not a triangle')

    # ---------- Equilateral / Isosceles / Scalene ----------
    def testEquilateral_Small(self):
        self.assertEqual(classifyTriangle(200,200,200), 'Equilateral', '200,200,200 should be Equilateral')

    def testIsosceles_Basic(self):
        self.assertEqual(classifyTriangle(9,9,3), 'Isosceles', '9,9,3 should be Isosceles')

    def testIsosceles_Boundary(self):
        self.assertEqual(classifyTriangle(2,2,3), 'Isosceles', '2,2,3 should be Isosceles')

    def testScalene_Basic(self):
        self.assertEqual(classifyTriangle(4,5,6), 'Scalene', '4,5,6 should be Scalene')

    def testScalene_Large(self):
        self.assertEqual(classifyTriangle(100,101,200), 'Scalene', '100,101,200 should be Scalene')

    # ---------- Right triangles ----------
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(200, 160, 120), 'Right', '200,160,120 is a Right triangle')

    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(10,6,8), 'Right', '10,6,8 is a Right triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

