from django.shortcuts import render, redirect
from .models import Cottage, OurServices, Poster, Roads, PeopleReservationCottage, PeopleReservationInstrument, \
    PeopleReservationInstructor
from .forms import ReplenishmentForm, BuySkiPassForm, PeopleReservationForm, CottageReservationForm, \
    InstrumentReservationForm, PeopleReservationInstrumrntForm, InstructorReservationForm, \
    PeopleReservationInstructorForm, BuySertificateForm


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

    replenishment_form = ReplenishmentForm()
    buy_ski_pass_form = BuySkiPassForm()

    if request.method == 'POST':
        if 'replenish' in request.POST:
            replenishment_form = ReplenishmentForm(request.POST)
            if replenishment_form.is_valid():
                replenishment_form.save()
                return redirect('home')
        elif 'buy' in request.POST:
            buy_ski_pass_form = BuySkiPassForm(request.POST)
            if buy_ski_pass_form.is_valid():
                buy_ski_pass_form.save()
                return redirect('home')

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

def services(request):
    services = OurServices.objects.all()
    replenishment_form = ReplenishmentForm()
    buy_ski_pass_form = BuySkiPassForm()
    if request.method == 'POST':
        if 'replenish' in request.POST:
            replenishment_form = ReplenishmentForm(request.POST)
            if replenishment_form.is_valid():
                replenishment_form.save()
                return redirect('home')
        elif 'buy' in request.POST:
            buy_ski_pass_form = BuySkiPassForm(request.POST)
            if buy_ski_pass_form.is_valid():
                buy_ski_pass_form.save()
                return redirect('home')
    return render(request, 'pages/services.html',
                  {
                   'services': services,
                    'replenishment_form': replenishment_form,
                    'buy_ski_pass_form': buy_ski_pass_form,
                })

def reservateInstructor(request):
    people_form = None
    if request.method == 'POST':
        form = InstructorReservationForm(request.POST)
        full_names = request.POST.getlist('fullName')
        if form.is_valid():
            instructor_reservation = form.save()
            for name in full_names:
                if name:
                    PeopleReservationInstructor.objects.create(fullName=name, instructor=instructor_reservation)
            return redirect('services')
    else:
        form = InstructorReservationForm()
        people_form = PeopleReservationInstructorForm()
    return render(request, 'pages/reservateInstructor.html',{'form': form, 'people_form': people_form})

def reservateInstrument(request):
    people_form = None
    if request.method == 'POST':
        form = InstrumentReservationForm(request.POST)
        full_names = request.POST.getlist('fullName')
        if form.is_valid():
            instrument_reservation = form.save()
            for name in full_names:
                if name:
                    PeopleReservationInstrument.objects.create(fullName=name, instrument=instrument_reservation)
            return redirect('services')
    else:
        form = InstrumentReservationForm()
        people_form = PeopleReservationInstrumrntForm()
    return render(request, 'pages/reservateInstrument.html',{'form': form, 'people_form': people_form})


def sertificateBuy(request):
    replenishment_form = ReplenishmentForm()
    buy_ski_pass_form = BuySkiPassForm()
    buy_certificate_form = BuySertificateForm()
    if request.method == 'POST':
        if 'replenish' in request.POST:
            replenishment_form = ReplenishmentForm(request.POST)
            if replenishment_form.is_valid():
                replenishment_form.save()
                return redirect('buy-sertificate')
        elif 'buy' in request.POST:
            buy_ski_pass_form = BuySkiPassForm(request.POST)
            if buy_ski_pass_form.is_valid():
                buy_ski_pass_form.save()
                return redirect('buy-sertificate')
        elif 'buy_certificate' in request.POST:
            buy_certificate_form = BuySertificateForm(request.POST)
            if buy_certificate_form.is_valid():
                buy_certificate_form.save()
                return redirect('buy-sertificate')
    return render(request, 'pages/sertificate.html', {
        'replenishment_form': replenishment_form,
        'buy_ski_pass_form': buy_ski_pass_form,
        'buy_certificate_form': buy_certificate_form,})

def toursPage(request):
    return render(request, 'pages/tour.html')

def informationPage(request):
    people_form = None
    if request.method == 'POST':
        form = InstrumentReservationForm(request.POST)
        full_names = request.POST.getlist('fullName')
        if form.is_valid():
            instrument_reservation = form.save()
            for name in full_names:
                if name:
                    PeopleReservationInstrument.objects.create(fullName=name, instrument=instrument_reservation)
            return redirect('services')
    else:
        form = InstrumentReservationForm()
        people_form = PeopleReservationInstrumrntForm()
    return render(request, 'pages/information.html',{'form': form, 'people_form': people_form})

def summerPage(request):
    return render(request, 'pages/summer.html')