from django.shortcuts import render,redirect
from .river_api import river
import asyncio

#home

def home(request):
    responses=asyncio.run(river())
    if request.method=='POST':
        data=request.POST
        search=data.get('name')
    responses=responses[0:3]
    context={'title':'flood system','responses':responses}
    return render(request,'index.html',context)