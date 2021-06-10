import unittest
from clases import Circulo
from math import pi

class TestClases(unittest.TestCase):
    def testRadioValue(self):
        self.assertRaises(TypeError, Circulo, True) # Check invalid type -> Invalid
        self.assertRaises(TypeError, Circulo, '0') # Check invalid type -> Invalid
        self.assertRaises(ValueError, Circulo, 0) # Check invalid radio value -> Invalid
        self.assertRaises(ValueError, Circulo, -1) # Check invalid radio value -> Invalid
        self.assertEqual(Circulo, type(Circulo(1))) # Check valid type -> valid

    def testArea(self):
        self.assertAlmostEqual(Circulo(1).area(), pi) 

    def testPerimetro(self):
        self.assertAlmostEqual(Circulo(1).perimetro(), 2*pi)

if __name__ == '__main__':
    unittest.main()