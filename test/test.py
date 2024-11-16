import unittest
import math

import circle
import rectangle
import square
import triangle

class TestCircle(unittest.TestCase):
    # Circle tests
    def test_circle_area_positive(self):
        self.assertEqual(circle.area(10), 10 * math.pi * 10)
        self.assertEqual(circle.area(0), 0)

    def test_circle_area_negative(self):
        self.assertRaises(ValueError, circle.area, -1)

    def test_circle_area_string(self):
        self.assertRaises(TypeError, circle.area, "10")

    def test_circle_perimeter_positive(self):
        self.assertEqual(circle.perimeter(10), 2 * math.pi * 10)
        self.assertEqual(circle.perimeter(0), 0)

    def test_circle_perimeter_negative(self):
        self.assertRaises(ValueError, circle.perimeter, -1)

    def test_circle_perimeter_string(self):
        self.assertRaises(TypeError, circle.perimeter, "10")

class TestRectangle(unittest.TestCase):
    # Rectangle Tests
    def test_rectangle_area_positive(self):
        self.assertEqual(rectangle.area(2, 5), 10)
        self.assertEqual(rectangle.area(5, 0), 0)

    def test_rectangle_area_negative(self):
        self.assertRaises(ValueError, rectangle.area, -1, 1)
        self.assertRaises(ValueError, rectangle.area, 1, -1)

    def test_rectangle_area_string(self):
        self.assertRaises(TypeError, rectangle.area, "2", 5)
        self.assertRaises(TypeError, rectangle.area, 2, "5")

    def test_rectangle_perimeter_positive(self):
        self.assertEqual(rectangle.perimeter(2, 5), 14)

    def test_rectangle_perimeter_negative(self):
        self.assertRaises(ValueError, rectangle.perimeter, -1, 1)
        self.assertRaises(ValueError, rectangle.perimeter, 1, -1)
        self.assertRaises(Exception, rectangle.perimeter, 0, 1)
        self.assertRaises(Exception, rectangle.perimeter, 1, 0)

    def test_rectangle_perimeter_string(self):
        self.assertRaises(TypeError, rectangle.perimeter, "2", 5)
        self.assertRaises(TypeError, rectangle.perimeter, 2, "5")

class TestSquare(unittest.TestCase):
    # Square tests
    def test_square_area_positive(self):
        self.assertEqual(square.area(10), 100)
        self.assertEqual(square.area(0), 0)

    def test_square_area_negative(self):
        self.assertRaises(ValueError, square.area, -1)

    def test_square_area_string(self):
        self.assertRaises(TypeError, square.area, "10")

    def test_square_perimeter_positive(self):
        self.assertEqual(square.perimeter(10), 40)
        self.assertEqual(square.perimeter(0), 0)

    def test_square_perimeter_negative(self):
        self.assertRaises(ValueError, square.perimeter, -1)

    def test_square_perimeter_string(self):
        self.assertRaises(TypeError, square.perimeter, "10")

class TestTriangle(unittest.TestCase):
    # Triangle tests
    def test_triangle_area_positive(self):
        self.assertEqual(triangle.area(10, 5), 25)
        self.assertEqual(triangle.area(5, 0), 0)

    def test_triangle_area_negative(self):
        self.assertRaises(ValueError, triangle.area, -1, 1)
        self.assertRaises(ValueError, triangle.area, 1, -1)

    def test_triangle_area_invalid(self):
        self.assertRaises(Exception, triangle.area, 1, 2)

    def test_triangle_area_string(self):
        self.assertRaises(TypeError, triangle.area, "10", 5)
        self.assertRaises(TypeError, triangle.area, 10, "5")

    def test_triangle_perimeter_invalid(self):
        invalid_triangles = [
            (2, 2, 4), (4, 2, 2), (2, 4, 2),
            (1, 2, 4), (1, 4, 2), (4, 2, 1),
            (2, 4, 1), (2, 1, 4), (4, 1, 2)
        ]
        for sides in invalid_triangles:
            self.assertRaises(Exception, triangle.perimeter, *sides)

    def test_triangle_perimeter_negative(self):
        self.assertRaises(ValueError, triangle.perimeter, -1, 6, 4)
        self.assertRaises(ValueError, triangle.perimeter, 6, -1, 4)
        self.assertRaises(ValueError, triangle.perimeter, 6, 4, -1)

    def test_triangle_perimeter_zero(self):
        self.assertRaises(Exception, triangle.perimeter, 0, 0, 0)

    def test_triangle_perimeter_string(self):
        self.assertRaises(TypeError, triangle.perimeter, "2", 3, 4)
        self.assertRaises(TypeError, triangle.perimeter, 2, "3", 4)
        self.assertRaises(TypeError, triangle.perimeter, 2, 3, "4")

    def test_triangle_perimeter_positive(self):
        self.assertEqual(triangle.perimeter(2, 3, 4), 9)

if "__main__" == __name__:
    unittest.main()
