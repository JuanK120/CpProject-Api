from ast import Mod
from importlib.abc import SourceLoader
from importlib.resources import path
from statistics import mode
from unittest import result
import pymzn
import asyncio
from pymzn.aio import minizinc
import config 
#testModel = Model("./models/test.mzn")

#cronogramaEnsayo = Model('./models/cronogramaEnsayos.mzn')

#gecode = Solver.lookup("gecode")



def RunTestCase(num):

    solucion = pymzn.minizinc('./core/minizinc/models/testCase.mzn', 
                                data={
                                    'i' : num
                                    })
    ret = [solucion[0],solucion.status]
    return ret

def cronogramaEnsayoWithForm(args):
    
    solucion = pymzn.minizinc('./core/minizinc/models/cronogramaEnsayos.mzn', data={
                                      'NumActores' : args[1],
                                      'Actores' : args[0],
                                      'NumEscenas' : args[2],
                                      'Escenas' : args[3],
                                      'Duracion' : args[4],
                                      'NumActoresConDisponibilidad' : args[5],
                                      'Disponibilidad' : args[6],
                                      'NumEvitaciones' : args[7],
                                      'Evitar': args[8],
                                    }
    )
    if solucion.status is pymzn.Status.COMPLETE :
        ret = [solucion[0],"Complete"]
    if solucion.status is pymzn.Status.UNSATISFIABLE :
        ret = [[],"Unsatisfiable"]

    return ret

def cronogramaEnsayoWithFile(file):
    solucion = pymzn.minizinc('./core/minizinc/models/testCase.mzn',file)
    if solucion.status is pymzn.Status.COMPLETE :
        ret = [solucion[0],"Complete"]
    if solucion.status is pymzn.Status.UNSATISFIABLE :
        ret = [[],"Unsatisfiable"]
    return ret

    