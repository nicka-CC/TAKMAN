from django.shortcuts import render, redirect
from .models import Cottage, OurServices, Poster, Roads, PeopleReservationCottage
from .forms import DateForm, ReplenishmentForm, BuySkiPassForm, PeopleReservationForm, CottageReservationForm


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


def skiing(request):
    roads = Roads.objects.all()

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

    return render(request, 'pages/skiing.html', {
        'roads': roads,
        'replenishment_form': replenishment_form,
        'buy_ski_pass_form': buy_ski_pass_form,
    })
def notFound(request):
    return render(request, 'pages/notFound.html')

def accomodation_list(request):
    cottages = Cottage.objects.all()
    people_form = None
    if request.method == 'POST':
        form = CottageReservationForm(request.POST)
        full_names = request.POST.getlist('fullName')
        if form.is_valid():
            cottage_reservation = form.save()
            for name in full_names:
                if name:
                    PeopleReservationCottage.objects.create(fullName=name, cottage=cottage_reservation)
            return redirect('accommodation')
    else:
        form = CottageReservationForm()
        people_form = PeopleReservationForm()
    return render(request, 'pages/accomodation_list.html', {'cottages': cottages, 'form': form, 'people_form': people_form})

def accomodation_detail(request, id):
    cottage = Cottage.objects.get(id=id)
    people_form = None
    if request.method == 'POST':
        form = CottageReservationForm(request.POST)
        full_names = request.POST.getlist('fullName')
        if form.is_valid():
            cottage_reservation = form.save()
            for name in full_names:
                if name:
                    PeopleReservationCottage.objects.create(fullName=name, cottage=cottage_reservation)
            return redirect('accommodation')
    else:
        form = CottageReservationForm()
        people_form = PeopleReservationForm()
    return render(request, 'pages/accommodation.html', {'cottage': cottage,'form': form, 'people_form': people_form})
