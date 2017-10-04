# -*- coding: utf-8 -*-
from lettuce import step, world
from edad import Edad

@step(u'Dado que la edad del individuo es "([^"]*)"')
def dado_que_la_edad_del_individuo_es_group1(step, edad):
    world.edad = Edad()
    world.edad.evaluar_edad(int(edad))

@step(u'entonces obtengo que el individuo "([^"]*)"')
def entonces_obtengo_que_el_individuo_group1(step, res):
    assert world.edad.obtener_evaluacion() == res, 'Esperado: ' + res + ", obtenido: " + str(world.edad.obtener_evaluacion())
