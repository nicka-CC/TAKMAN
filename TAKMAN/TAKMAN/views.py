from django.shortcuts import render

from .forms import DateForm
from .models import Cottage



def home(request):
    cottages = Cottage.objects.all()  # Получаем все коттеджи
    date_form = DateForm()  # Создаем экземпляр формы даты
    return render(request, 'pages/home.html', {'cottages': cottages, 'date_form': date_form})