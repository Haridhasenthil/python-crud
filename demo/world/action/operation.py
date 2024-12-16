from django.http import HttpResponse, JsonResponse
from bson import ObjectId
from world.models import Person
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):
    return HttpResponse("App is running.")

@csrf_exempt
def add_person(request):
        json_data = json.loads(request.body)  
        first_name = json_data.get("first_name")
        last_name = json_data.get("last_name")        
        print(first_name, last_name)
        person1 = Person(first_name=first_name, last_name=last_name)
        person1.save()
        return JsonResponse({"message": "New person added successfully"})

# @csrf_exempt
# def get_all_person(request):
#     persons = Person.objects.all()
#     print(persons)
#     return JsonResponse(persons,safe=False)
# def deletePerson(request):
#     first_name = request.GET.get('first_name')
#     persons = person_collection.delete_one({'name': first_name})   
#     return HttpResponse("deleted ")

# def updatePerson(request):
#     json_data =json.loads(request.body)
#     first_name = json_data.get("first_name")
#     first_name = request.GET.get('first_name')
#     print(first_name)
#     last_name = request.GET.get('last_name')
#     print(last_name)
#     id = request.GET.get('id')
#     print(id)
#     person = person_collection.find_one({'_id':ObjectId(id)})
#     updatePerson ={}
#     if(person):
#         updatePerson['first_name']=first_name
#         updatePerson['last_name']=last_name
#         person_collection.update_one({'_id':ObjectId(id)},{"$set":updatePerson})
#         return HttpResponse("update sucessfully")
#     else:
#         return  HttpResponse("not found")