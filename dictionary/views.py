from django.shortcuts import render
from django.http import HttpResponse
from .models import Dictionary


# Create your views here.

def dictionary(request):
    soz = request.GET.get('q', '')
    if soz and soz != '':
        result = Dictionary.objects.filter(inglizcha__contains=soz).all()[:3]
    else:
        result = None
    return render(request, 'dictionary.html', {'q': soz, 'result': result})
