#!/usr/bin/env python
import unittest
import sys
sys.path.append('../')
from Calculator2 import Calculator2


class TestCalculator(unittest.TestCase):

    def testsuma_2_mas_2(self):
        cal = Calculator2()
        self.assertEqual(4, cal.suma(2, 2))

    def testsuma_598_mas_4380(self):
        cal = Calculator2()
        self.assertEqual(4978, cal.suma(598, 4380))

    def testresta_100_menos_99(self):
        cal = Calculator2()
        self.assertEqual(1, cal.resta(100, 99))

    def testresta_8_menos_9(self):
        cal = Calculator2()
        self.assertEqual(-1, cal.resta(8, 9))

    def testmult_11_por_8(self):
        cal = Calculator2()
        self.assertEqual(88, cal.mult(11, 8))

    def testdiv_36_entre9(self):
        cal = Calculator2()
        self.assertEqual(4, cal.div(36, 9))

    def testdiv_5_entre_2(self):
        cal = Calculator2()
        self.assertEqual(2.5, cal.div(5.0, 2.0))

if __name__ == "__main__":
    unittest.main()
