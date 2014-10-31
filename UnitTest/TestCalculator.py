#!/usr/bin/env python
import unittest
import sys
sys.path.append('../')
from Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def testsuma_2_mas_2(self):
        parametros= ["Suma", 2, 2]
        cal = Calculator(parametros)
        self.assertEqual(4, cal.getResult())

    def testsuma_598_mas_4380(self):
        parametros= ["Suma", 598, 4380]
        cal = Calculator(parametros)
        self.assertEqual(4978, cal.getResult())

    def testresta_100_menos_99(self):
        parametros= ["Resta", 100, 99]
        cal = Calculator(parametros)
        self.assertEqual(1, cal.getResult())

    def testresta_8_menos_9(self):
        parametros= ["Resta", 8, 9]
        cal = Calculator(parametros)
        self.assertEqual(-1, cal.getResult())

    def testmult_11_por_8(self):
        parametros= ["Multiplicacion", 11, 8]
        cal = Calculator(parametros)
        self.assertEqual(88, cal.getResult())

    def testdiv_36_entre9(self):
        parametros= ["Division", 36, 9]
        cal = Calculator(parametros)
        self.assertEqual(4, cal.getResult())

    def testdiv_5_entre_2(self):
        parametros= ["Division", 5.0, 2.0]
        cal = Calculator(parametros)
        self.assertEqual(2.5, cal.getResult())

if __name__ == "__main__":
    unittest.main()
