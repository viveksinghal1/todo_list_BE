from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.

def apiOverview(request):
    return JsonResponse("API BASE ROUTE", safe=False)