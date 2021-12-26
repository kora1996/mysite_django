from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.is_true = True
    feature1.name = 'fast'
    feature1.details = 'it works really fast'

    feature2 = Feature()
    feature2.id = 2
    feature2.is_true = False
    feature2.name = 'fart'
    feature2.details = 'it stiks lol'

    feature3 = Feature()
    feature3.id = 3
    feature3.name = 'fist'
    feature3.details = 'it hart'

    feature4 = Feature()
    feature4.id = 4
    feature4.name = 'fait'
    feature4.details = 'it is destiny'

    feature5 = Feature()
    feature5.id = 5
    feature5.name = 'past'
    feature5.details = 'it is a past'



    features = [feature1, feature2, feature3, feature4, feature5]


    context = {
            'name': 'Wojak',
            'age': 24,
            'job': 'jobless',
            'nationality': 'USA'
            }
    return render(request, 'index.html', {'features': features}) 

# Create your views here.
def oi(request):
    return render(request, 'oi.html')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
