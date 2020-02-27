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
    image_data = open('/Users/RedShadow/PycharmProjects/iDjango/templates/boy-wind.png','rb').read()
    return HttpResponse(image_data,content_type = "image/png")


import csv
UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203]

def unruly_passengers_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=unruly.csv'

    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])
    return response


from reportlab.pdfgen import canvas
def hello_pdf(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    p = canvas.Canvas(response)
    p.drawString(100, 100, 'Hello world.')
    p.showPage()
    p.save()
    return response


from io import BytesIO
def hello_pdf_io(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    temp = BytesIO()

    p = canvas.Canvas(temp)
    p.drawString(100, 100, 'Hello world Again.')
    p.showPage()
    p.save()
    response.write(temp.getvalue())
    return response


