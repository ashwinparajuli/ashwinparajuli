from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import usersForm



def homePage(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"index.html",{'output':output})

    


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
    return render(request,"about-us.html")

#def contact(request):
    #return render(request,"contact.html")

def calculator(request):
    c=''
    data={} 
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=='+':
                c=n1+n2

            elif opr=='-':
                c=n1-n2

            elif opr=='*':
                c=n1*n2

            elif opr=='/':
                c=n1/n2
        
        data={
            'n1':n1,
            'n2':n2,
            'opr':opr,
            'c':c
        }
        
    except:
        c="...Invalid OPR..."
    print(c)
    return render(request,"calculator.html",data)
    


def userForm(request):
    finalans=0
    fn=usersForm()

    data={'form':fn}
    try:
        if request.method=="POST":
        
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            n3=int(request.POST.get('num3'))
            finalans=n1+n2+n3;
            data={
                'form':fn,
              
                'output':finalans
            }
            url="/?output={}".format(finalans)
            #return HttpResponseRedirect(url)
            return redirect(url)
    except:
        pass   
    return render(request,"userform.html",data)



def submitForm(request):
    fianlans=0
    data={}
    try:
        if request.method=="POST":
        
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            n3=int(request.POST.get('num3'))
            finalans=n1+n2+n3;
            data={
                'n1':n1,
                'n2':n2,
                'n3':n3,
                'output':finalans
            }
            
            return HttpResponse(finalans)
           
    except:
        pass   
    return render(request,"userform.html")