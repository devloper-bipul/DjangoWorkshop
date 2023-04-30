from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .utils import Form

# Create your views here.
form=Form()

def get_random_uuid():
    return "my_simple_uuid"

def home(request):
    return render(request,"home.html")

def create(request): 
    pk=form.create()
    return HttpResponseRedirect(reverse_lazy('update_form',args=[pk]))

def update_form(request,pk):
    try:
        form_data=form.find(pk)
        return render(request,'update_form.html',{
            'pk':pk,
            'form':form_data
        })
    except:
        # return 404
        pass