from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
# Create your views here.
# RTURN STRING BY USING fbv
def fbv_string(request):
    return HttpResponse('<h1>This FBV string</h1>')

# returning string by using CBV
from app.forms import *
class Cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>CBV string</h1>')

# rendering html and sending context by FBV

def FBV_html(request):
    d={'name':"harshad"}
    return render(request,'FBV_html.html',d)
# rendering html and sending context by CBV

class CBV_html(View):
    def get(self,request):
        d={'name':'ASHU'}
        return render(request,'CBV_html.html',d)

#DEaling with django form by FBV

def FBV_djform(request):
    form=NameForm()
    d={'form':form}
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'FBV_djform.html',d)

#Dealing with Django form by using CBV
class CBV_djform(View):
    def get(self,request):
        NF=NameForm()
        d={'form':NF}
        return render(request,'CBV_djform.html',d)

    def post(self,request):
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))

#Dealing with Model forms by FBV

def FBV_Mdform(request):
    SF=StudentForm()
    d={'form':SF}
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Inserted Data')
    return render(request,'FBV_Mdform.html',d)

# Dealing with Model forms by CBV
class CBV_Mdform(View):
    def get(self,request):
        SF=StudentForm()
        d={'form':SF}
        return render(request,'CBV_Mdform.html',d)

    def post(self,request):
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Inserted Data')


class CBV_TVhtml(TemplateView):
    template_name='CBV_html.html'





















































