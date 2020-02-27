from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error.append('Enter a search term.')
        elif len(q) > 20:
            error.append('please ent.POSTrequest er at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)  #https://blog.csdn.net/qq_39208536/article/details/79426939
            return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'error': error})

'''
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject')
        if not request.POST.get('message',''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'r2010shadow@163.com'),
                ['r2010shadow@163.com'],
            )
            return HttpResponseRedirect('contact_success.html')
    return render(request, 'contact_success.html',{
        'errors': errors,
        'subject:': request.POST.get('subject',''),
        'message:': request.POST.get('message',''),
        'email:': request.POST.get('email',''),
    })

'''
