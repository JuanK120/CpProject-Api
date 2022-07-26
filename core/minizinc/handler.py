from ast import Mod
from importlib.abc import SourceLoader
from importlib.resources import path
from statistics import mode
from unittest import result
import pymzn
import asyncio
from pymzn.aio import minizinc

def RunTestCase(num):

    solucion = pymzn.minizinc('./core/minizinc/models/testCase.mzn', 
                                data={
                                    'i' : num
                                    })
    ret = [solucion[0],solucion.status]
    return ret

def cronogramaEnsayoWithForm(args):
    print("1")

    aux = pymzn.dzn2dict(args[0])
    
    if (args[9]=="Simple"):
        print(args[9])
        solucion = pymzn.minizinc('./core/minizinc/models/cronogramaEnsayos.mzn', data={
                                      'ACTORES' : aux["Actores"],
                                      'Escenas' : args[3],
                                      'Duracion' : args[4]
                                    }
        )
        if solucion.status is pymzn.Status.COMPLETE :
            ret = [solucion[0],"Complete"]
        if solucion.status is pymzn.Status.UNSATISFIABLE :
            ret = [[],"Unsatisfiable"]
        return ret

    print("2")

    if (args[9]=="Complex"):
        print(args[9])
        solucion = pymzn.minizinc('./core/minizinc/models/cronogramaEnsayos_extendido.mzn', data={
                                        'ACTORES' : aux['Actores'],
                                        'Escenas' : args[3],
                                        'Duracion' : args[4],
                                        'Disponibilidad' : args[6],
                                        'Evitar': args[8],
                                        }
        )
        print('3')
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

    