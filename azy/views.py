from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':'Home Page',
        'body':'Hello World!',
        'list':['Ashwin', 'Azy', 'Azywin'],
        'numbers':[10,20,30,40,50,60],
        'details':[
            {'Name':'Ashwin Parajuli','Phone':'9864374144'},
            {'Name':'Azy win','Phone':'061588945'},

        ]
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Welcome Azy")

def courseDetails(request,courseid):
    return HttpResponse(courseid)