from django.shortcuts import render


def ready(request):
    return render(request, 'ready/ready.html')

