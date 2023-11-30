from django.shortcuts import render
from myceleryproject.celery import add
from .tasks import sub
# Create your views here.


# Enque Task using delay()
# Return Task ID
"""
def index(request):
     print("Results")
     result=add.delay(10,90)
     print(result,"kjhgcfghj")
     result2=sub.delay(80,10)
     print(result2)
     return render(request,"index.html")
"""

# Enque Task using apply_async()
# Return Apply Async Object
def index(request):
     print("Results")
     result=add.apply_async(args=[10,10])
     print(result,"kjhgcfghj")
     result2=sub.apply_async(args=[10,20])
     print(result2)
     return render(request,"index.html")

