from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displayCoso(request):
    return HttpResponse("<h1>Titulo</h1><nav><ul><li>elemento1</li></ul></nav><h4>coso</h4>")

def displayForm(request):
    return HttpResponse("<h2>Bienvenido</h2><div><form><input type='text' placeholder='Ingrese nombre'></input><a href=''>link</a></div></form>")