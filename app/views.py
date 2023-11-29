from django.shortcuts import render
from myceleryproject.celery import add
# Create your views here.

def index(request):
     print("Results")
     result=add(10,90)
     print(result,"kjhgcfghj")
     return render(request,"index.html")
