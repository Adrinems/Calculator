# -*- coding: utf-8 -*-
<<<<<<< HEAD
from lettuce import step, world
=======
from lettuce import step,world
>>>>>>> 0c9b53e11fc87e6517e3ea9d086d890aa6e55a86
import sys
sys.path.append('../')
from Calculator import Calculator


@step(u'Given La operación es una "([^"]*)" y sus sumandos son "([^"]*)" y "([^"]*)"')
def given_la_operacion_es_una_suma_y_sus_sumandos_son_4_y_4(step, operacion, a, b):
    world.parametros = [operacion, int(a), int(b), 0]


@step(u'when realizo el cálculo')
def when_realizo_el_calculo(step):
    cal = Calculator(world.parametros)
    world.calculos = cal.getResult()


@step(u'then obtengo como resultado "([^"]*)"')
def then_obtengo_como_resultado_8(step, resultado):
    assert world.calculos == int(
        resultado), "resultado calculado {0}, resultado esperado {1}".format(world.calculos, resultado)
