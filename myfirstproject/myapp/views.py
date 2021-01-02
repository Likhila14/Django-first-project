from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def myfirfun(request):
    return HttpResponse("Hello World")

def myfirfunadd(request,a,b):
    return HttpResponse(a+b)

def myfirjson(request,name,age):
    mydict = {
        "Name" : name,
        "Age"  : age
    }
    return JsonResponse(mydict)