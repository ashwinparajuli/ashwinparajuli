from django.http import HttpResponse


from django.shortcuts import render


def homePage(request):
     return render(request,"index.html")

    


  # data={
  #    'title':'Home Page',
  #    'body':'Hello World!',
  #    'list':['Ashwin', 'Azy', 'Azywin'],
  #    'numbers':[10,20,30,40,50,60],
  #    'details':[
  #        {'Name':'Azy win','Phone':'061588945'},
  #        {'Name':'Ashwin Parajuli','Phone':'9864374144'}
  #]
  # }
   
    


def aboutUs(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")