from ast import Mod
from importlib.abc import SourceLoader
from importlib.resources import path
from statistics import mode
from unittest import result
import pymzn
#testModel = Model("./models/test.mzn")

#cronogramaEnsayo = Model('./models/cronogramaEnsayos.mzn')

#gecode = Solver.lookup("gecode")



def testCase(num):
    solucion = pymzn.minizinc('./core/minizinc/models/testCase.mzn', data={"i":num})
    ret = solucion[0]
    return ret

def cronogramaEnsayoWithForm(args):
    solucion = pymzn.minizinc('./core/minizinc/models/testCase.mzn', 
                                data={'Actores' : args[0],
                                      'NumActores' : args[1],
                                      'NumEscenas' : args[2],
                                      'Escenas' : args[3],
                                      'Duracion' : args[4],
                                      'NumActoresConDisponibilidad' : args[5],
                                      'Disponibilidad' : args[6],
                                      'NumEvitaciones' : args[7],
                                      'Evitar': args[8],
                                    })
    ret = solucion[0]
    return ret

def cronogramaEnsayoWithForm(file):
    solucion = pymzn.minizinc('./core/minizinc/models/testCase.mzn',file)
    ret = solucion[0]
    return ret

    