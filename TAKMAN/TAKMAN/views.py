from django.shortcuts import render, redirect
from .models import Cottage, OurServices, Poster
from .forms import DateForm, ReplenishmentForm, BuySkiPassForm

def home(request):
    cottages = Cottage.objects.all()
    services = OurServices.objects.all()
    posters = Poster.objects.all()

    replenishment_form = ReplenishmentForm()  # Создаем экземпляр формы пополнения
    buy_ski_pass_form = BuySkiPassForm()  # Создаем экземпляр формы покупки ски-пасса

    if request.method == 'POST':
        if 'replenish' in request.POST:  # Проверяем, была ли отправлена форма пополнения
            replenishment_form = ReplenishmentForm(request.POST)
            if replenishment_form.is_valid():
                replenishment_form.save()
                return redirect('home')  # Укажите вашу страницу успешного завершения
        elif 'buy' in request.POST:  # Проверяем, была ли отправлена форма покупки
            buy_ski_pass_form = BuySkiPassForm(request.POST)
            if buy_ski_pass_form.is_valid():
                buy_ski_pass_form.save()
                return redirect('home')  # Укажите вашу страницу успешного завершения

    return render(request, 'pages/home.html', {
        'cottages': cottages,
        'services': services,
        'posters': posters,
        'replenishment_form': replenishment_form,
        'buy_ski_pass_form': buy_ski_pass_form,
    })
