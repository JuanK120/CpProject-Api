import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.minizinc.handler import RunTestCase, cronogramaEnsayoWithForm, cronogramaEnsayoWithFile
import asyncio
import config

# Create your views here.

@csrf_exempt
def test(request):
    req=json.load(request)
    i = req["i"]
    ret = RunTestCase(i)
    config.Solution=ret
    return JsonResponse(ret,safe=False)

@csrf_exempt
def getTest(request):
    
    return JsonResponse(config.Solution,safe=False)

@csrf_exempt
def runWithForm(request):
    req=json.load(request)
    args = []
    args.append(req['Actores'])
    args.append(req['NumActores'])
    args.append(req['NumEscenas'])
    args.append(req['Escenas'])
    args.append(req['Duracion'])
    args.append(req['NumActoresConDisponibilidad'])
    args.append(req['Disponibilidad'])
    args.append(req['NumEvitaciones'])
    args.append(req['Evitar'])
    ret = cronogramaEnsayoWithForm(args)
    return JsonResponse(ret,safe=False)

@csrf_exempt
def runWithFile(request):
    req=json.load(request)
    ret = cronogramaEnsayoWithFile(req['file'])
    return JsonResponse(ret,safe=False)

@csrf_exempt
def getSolution(request):
    return JsonResponse(config.Solution,safe=False)