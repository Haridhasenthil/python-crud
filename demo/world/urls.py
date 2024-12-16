from django.urls import path
from world.action.operation import index, add_person

urlpatterns = [
    path('', index, name='index'),
    path('add/',add_person, name='add_person'),
    # path('show/', get_all_person, name='get_all_person'),
    # path('delete/',views.deletePerson,name='deletePrson'),
    # path('update/',views.updatePerson,name='updatePerson')
]
