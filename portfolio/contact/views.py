from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            form = ContactForm()
            messages.success(request, 'Thanks, Your message have sent.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form':form})