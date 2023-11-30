from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('evolution/',views.evolution, name = 'evolution'),
    path('graphiques/', views.graphiques, name='graphiques'),
    path('navforgraph/', views.navforgraph, name='navforgraph'),
    path('notebook/', views.notebook, name='notebook'),
    path('startnow/',views.startnow, name='startnow'),
    path('2022/',views.deuxmille, name='deuxmille'),
    path('2022/cartes/',views.cartes, name='cartes'),
    path('2022/cartes/france',views.cartesfrance, name='cartesfrance'),
    path('2022/cartes/iledefrance',views.cartesiledefrance, name='cartesiledefrance'),
    path('2022/cartes/paris92',views.cartesparis, name='cartesparis'),

    path('2022/cartes/france1',views.cartefrance1, name='cartefrance1'),
    path('2022/cartes/france2',views.cartefrance2, name='cartefrance2'),
    path('2022/cartes/france3',views.carteilefrance1, name = 'cartefrance3'),
    path('2022/cartes/france4',views.carteilefrance2, name = 'cartefrance4'),
    path('2022/cartes/paris1',views.carteparis1, name = 'carteparis1'),
    path('2022/cartes/paris2',views.carteparis2, name = 'carteparis2'),
    path('2022/cartes/paris3',views.carteparis3, name = 'carteparis3'),

    path('2022/graphiques',views.graphiques, name = 'graphiques'),
    path('2022/graphiques/graphique1',views.graphique1, name = 'graphique1'),
    path('2022/graphiques/graphique2',views.graphique2, name = 'graphique2'),
    path('2022/graphiques/graphique3',views.graphique3, name = 'graphique3'),
    path('2022/graphiques/graphique4',views.graphique4, name = 'graphique4'),

    path('evolution/graphique5',views.graphique5, name = 'graphique5'),
    path('evolution/graphique6',views.graphique6, name = 'graphique6'),
    path('evolution/graphique7',views.graphique7, name = 'graphique7'),
    path('evolution/graphique8',views.graphique8, name = 'graphique8'),


]