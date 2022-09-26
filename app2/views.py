from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def displayBtn (request):
    return HttpResponse("<div><a class='btn' href=''></a><button class='btn' type='submit'>Coso</button></div>")

def displayBtn2 (request):
    return HttpResponse("<nav><ul><li>Elemento1</li></ul><button type='submit'>a</button></nav>")
    