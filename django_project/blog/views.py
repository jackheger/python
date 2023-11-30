from django.shortcuts import render
from django.http import HttpResponse

def home(request) :
    return render(request,'blog/home.html')

def navforgraph(request) :
    return render(request,'blog/navforgraph.html')
def notebook(request) :
    return render(request,'blog/notebook.html')
def contact(request) :
    return render(request, 'blog/contact.html')


def startnow(request):
    return render(request, 'blog/startnow.html')

def evolution(request):
    return render(request, 'blog/evolution.html')



def deuxmille(request) : 
    return render(request, 'blog/deuxmille.html')


def cartes(request) : 
    return render(request, 'blog/cartes.html')

def cartesfrance(request) : 
    return render(request, 'blog/cartesfrance.html')
def cartesiledefrance(request):
    return render(request, 'blog/cartesiledefrance.html')
def cartesparis(request):
    return render(request, 'blog/cartesparis.html')

def cartefrance1(request):
    return render(request, 'graphiques/cartefrance1.html')
def cartefrance2(request):
    return render(request, 'graphiques/cartefrance2.html')
def carteilefrance1(request):
    return render(request, 'graphiques/carteilefrance1.html')
def carteilefrance2(request):
    return render(request, 'graphiques/carteilefrance2.html')
def carteparis1(request):
    return render(request, 'graphiques/carteparis1.html')
def carteparis2(request):
    return render(request, 'graphiques/carteparis2.html')
def carteparis3(request):
    return render(request, 'graphiques/carteparis3.html')





def graphiques(request):
    return render(request, 'blog/graphiques.html')

def graphique1(request):
    return render(request, 'graphiques/testFichier.html')

def graphique2(request):
    return render(request, 'graphiques/dataframe1.html')
def graphique3(request):
    return render(request, 'graphiques/graphique3.html')
def graphique4(request):
    return render(request, 'graphiques/graphique4.html')

def graphique5(request):
    return render(request, 'graphiques/graphique5.html')
def graphique6(request):
    return render(request, 'graphiques/graphique6.html')
def graphique7(request):
    return render(request, 'graphiques/graphique7.html')
def graphique8(request):
    return render(request, 'graphiques/graphique8.html')