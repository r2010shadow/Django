from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render

def debug():
    pass

def current_datetime(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
    #return render(request,'current_datetime.html',{'current_date':now})
    current_date = datetime.datetime.now()   # current_date in c*_d*.html
    return render(request,'current_datetime.html',locals())


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>In %s hours(s), it will be %s..</body></html>" % (offset, dt)
    return HttpResponse(html)


def hello(request):
    return HttpResponse("Hello world , Good Luck")
