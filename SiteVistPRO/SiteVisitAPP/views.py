from django.shortcuts import render
from .models import site_visit_collection
from django.http import HttpResponse


def Index(request):
    return HttpResponse("<h1>App is Running</h1>")


def add_person(request):
    records={
        "F_name":"Sarath",
        "L_name":"S Nair"
    }
    site_visit_collection.insert_one(records)
    return HttpResponse("New Record Inserted")

def get_all_records(request):
    records=site_visit_collection.find()
    return HttpResponse(records)
