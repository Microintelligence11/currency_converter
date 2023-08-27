
from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    return render(request, 'index.html')


def usd(request):
    mytext = request.POST.get('text', 'default')
    us = request.POST.get('usd', 'off')
    dr= request.POST.get('dir','off')
    riya=request.POST.get('riyal','off')

    if us == "on" and mytext != "":
        khan=float(mytext) * float(0.014)
        params = {'parpose': 'monye converter', 'convert': khan}
        return render(request,'usd.html',params)

    elif(dr == "on" and mytext != ""):
        khan1=float(mytext)*float(0.052)
        params={'parpose':'dirham','convert':khan1}
        return  render(request,'dir.html',params)

    elif(riya == "on" and mytext != ""):
        khan3=float(mytext)*float(595.74)
        params={'parpose':'riyal','convert':khan3}
        return  render(request,'riyal.html',params)

    else:
        return HttpResponse("error")






















