from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def contact_succ(request):
    return HttpResponse("Email Send!")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'r2010shadow@163.com'),
                ['r2010shadow@163.com'],
            )
            return HttpResponseRedirect('/contact')
    else:
        form = ContactForm(
            initial={'subject': 'Let Django fly away!~~ '}
        )
    return render(request, 'contact_form.html',{'form': form})