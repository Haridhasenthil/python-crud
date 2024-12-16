from django.shortcuts import render
from .models import person_collection
from django.http import HttpResponse
# Create your views here.
from pymongo.errors import PyMongoError 
from bson import ObjectId

def index(request):
    return HttpResponse("App is running.")

def add_person(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    record = {
        "first_name":first_name,
        "last_name":last_name
        
    }
    print(record)
    person_collection.insert_one(record)
    return HttpResponse("new person is added")

def get_all_person(request):
    persons = person_collection.find({},{'_id':0})
    return HttpResponse(persons) 

def deletePerson(request):
    first_name = request.GET.get('first_name')
    persons = person_collection.delete_one({'name': first_name})   
    return HttpResponse("deleted ")

def updatePerson(request):
    first_name = request.GET.get('first_name')
    print(first_name)
    last_name = request.GET.get('last_name')
    print(last_name)
    id = request.GET.get('id')
    print(id)
    person = person_collection.find_one({'_id':ObjectId(id)})
    updatePerson ={}
    if(person):
        updatePerson['first_name']=first_name
        updatePerson['last_name']=last_name
        person_collection.update_one({'_id':ObjectId(id)},{"$set":updatePerson})
        return HttpResponse("update sucessfully")
    else:
        return  HttpResponse("not found")