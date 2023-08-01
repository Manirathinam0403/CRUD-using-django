from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import  Member
from django.template import loader
# Create your views here.
def main(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def details(request):
    myMember = Member.objects.all().values()
    template = loader.get_template('info.html')
    context = {
        'myMember' : myMember,
    }
    return HttpResponse(template.render(context,request))
def moreInfo(request,id):
    myMember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myMember' : myMember,
    }
    return HttpResponse(template.render(context,request))

def deleteIt(request,id):
    myMember = Member.objects.get(id=id)
    myMember.delete()
    return HttpResponseRedirect(reverse('details'))

def add(request):
    template = loader.get_template('addrecord.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    a = request.POST['id']
    b = request.POST['name']
    c = request.POST['age']
    d = request.POST['course']
    e = request.POST['cgpa']
    m = Member(registerId = a,name = b,age=c,course = d,CGPA =e)
    m.save()
    return HttpResponseRedirect(reverse('details'))

def update(request,id):
    myMember = Member.objects.get(id=id)
    template = loader.get_template('updaterecord.html')
    context = {
        'myMember' : myMember,
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    m = Member.objects.get(id=id)
    m.registerID = request.POST['id']
    m.name = request.POST['name']
    m.age = request.POST['age']
    m.course = request.POST['course']
    m.CGPA = request.POST['cgpa']
    m.save()
    return HttpResponseRedirect(reverse('details'))
