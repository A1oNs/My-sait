from django.shortcuts import render, redirect
from .forms import newForm
import time


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def service(request):
    return render(request, 'main/service.html')


def contact(request):
    return render(request, 'main/contact.html')

def record(request):
    error = ''
    if request.method == 'POST':
        form = newForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complete')
        else:
            error = 'Запись не выполнена'

    form = newForm()

    date = {
        'form': form,
        'error': error
    }

    return render(request, 'main/record.html', date)

def complete(request):
    return render(request, 'main/complete.html')