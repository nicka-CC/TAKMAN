from django.shortcuts import render
from .models import Cottage



def home(request):
    cottages = Cottage.objects.all()  # Получаем все коттеджи
    return render(request, 'pages/home.html', {'cottages': cottages})