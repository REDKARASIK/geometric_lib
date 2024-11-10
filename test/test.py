import unittest
import math

import circle
import rectangle
import square
import triangle

class TestCircle(unittest.TestCase):
    # Circle tests
    def test_circle_area(self):
        # Tests for standart math operation equals
        self.assertEqual(circle.area(10), 10 * math.pi * 10)
        self.assertEqual(circle.area(0), 0)
        # Test for checking positive numbers
        self.assertRaises(ValueError, circle.area, -1)
    def test_circle_perimeter(self):
        # Tests for standart math operation equals
        self.assertEqual(circle.perimeter(10), 2 * math.pi * 10)
        self.assertEqual(circle.perimeter(0), 0)
        # Test for checking positive numbers
        self.assertRaises(ValueError, circle.perimeter, -1)
    # Rectangle Tests
    def test_rectangle_area(self):
        # Tests for standard math operation equals
        self.assertEqual(rectangle.area(2, 5), 10)
        self.assertEqual(rectangle.area(5, 0), 0)
        # Tests for checking positive numbers
        self.assertRaises(ValueError, rectangle.area, -1, 1)
        self.assertRaises(ValueError, rectangle.area, 1, -1)
    def test_rectangle_perimeter(self):
        # Tests for standard math operation equals
        self.assertEqual(rectangle.perimeter(2, 5), 14)
        # Tests for checking positive numbers
        self.assertRaises(ValueError, rectangle.perimeter, -1, 1)
        self.assertRaises(ValueError, rectangle.perimeter, 1, -1)
        self.assertRaises(Exception, rectangle.perimeter, 0, 1)
        self.assertRaises(Exception, rectangle.perimeter, 1, 0)
    # Square tests
    def test_square_area(self):
        # Tests for standard math operation equals
        self.assertEqual(square.area(10), 100)
        self.assertEqual(square.area(0), 0)
        # Test for checking positive numbers
        self.assertRaises(ValueError, square.area, -1)
    def test_square_perimeter(self):
        # Tests for standard math operation equals
        self.assertEqual(square.perimeter(10), 40)
        self.assertEqual(square.perimeter(0), 0)
        # Test for checking positive numbers
        self.assertRaises(ValueError, square.perimeter, -1)
    # Triangle tests
    def test_triangle_area(self):
        # Tests for standard math operation equals
        self.assertEqual(triangle.area(10, 5), 25)
        self.assertEqual(triangle.area(5, 0), 0)
        # Tests for checking positive numbers
        self.assertRaises(ValueError, triangle.area, -1, 1)
        self.assertRaises(ValueError, triangle.area, 1, -1)
        # Tests that H more than Side
        self.assertRaises(Exception, triangle.area, 1, 2)
    def test_triangle_perimeter(self):
        # Tests for existing of triangle
        self.assertRaises(Exception, triangle.perimeter, 2, 2, 4)
        self.assertRaises(Exception, triangle.perimeter, 4, 2, 2)
        self.assertRaises(Exception, triangle.perimeter, 2, 4, 2)
        self.assertRaises(Exception, triangle.perimeter, 1, 2, 4)
        self.assertRaises(Exception, triangle.perimeter, 1, 4, 2)
        self.assertRaises(Exception, triangle.perimeter, 4, 2, 1)
        self.assertRaises(Exception, triangle.perimeter, 2, 4, 1)
        self.assertRaises(Exception, triangle.perimeter, 2, 1, 4)
        self.assertRaises(Exception, triangle.perimeter, 4, 1, 2)
        # Tests for checking positive numbers
        self.assertRaises(ValueError, triangle.perimeter, -1, 6, 4)
        self.assertRaises(ValueError, triangle.perimeter, 6, -1, 4)
        self.assertRaises(ValueError, triangle.perimeter, 6, 4, -1)
        self.assertRaises(Exception, triangle.perimeter, 0, 0, 0)
        # Test for standard math operation equals
        self.assertEqual(triangle.perimeter(2, 3, 4), 9)

if "__main__" == __name__:
    unittest.main()
