import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.minizinc.handler import testCase, cronogramaEnsayoWithForm

# Create your views here.

@csrf_exempt
def test(request):
    req=json.load(request)
    i = req["i"]
    ret = testCase(i)
    return JsonResponse(ret,safe=False)

@csrf_exempt
def getResultWithForm(request):
    req=json.load(request)
    args = []
    args.append(req['Actores'])
    args.append(req['NumActores'])
    args.append(req['NumEscenas'])
    args.append(req['Duracion'])
    args.append(req['NumActoresConDisponibilidad'])
    args.append(req['Disponibilidad'])
    args.append(req['NumEvitaciones'])
    args.append(req['Evitar'])
    ret = cronogramaEnsayoWithForm(args)
    return JsonResponse(ret,safe=False)

@csrf_exempt
def uploadFileAndSolve(request):
    res = JsonResponse({})
    return res

@csrf_exempt
def getStoredFiles(request):
    res = JsonResponse({})
    return res

@csrf_exempt
def getResultWithUploadedFile(request):
    res = JsonResponse({})
    return res


