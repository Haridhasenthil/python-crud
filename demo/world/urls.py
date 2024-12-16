from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_person, name='add_person'),
    path('show/', views.get_all_person, name='get_all_person'),
    path('delete/',views.deletePerson,name='deletePrson'),
    path('update/',views.updatePerson,name='updatePerson')
]
