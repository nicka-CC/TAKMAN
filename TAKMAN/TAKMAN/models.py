from django.db import models


# пополнение баланса ски-пасса
class ReplenishmentOfBalanceSkiPass(models.Model):
    date = models.DateField(auto_now_add=True)
    tarif = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)  # Изменено на CharField
    email = models.EmailField(max_length=254)  # Изменена максимальная длина
    numberCard = models.CharField(max_length=20)
    summ = models.IntegerField()

    def __str__(self):
        return self.numberCard


# покупка ски-пасса
class BuySkiPass(models.Model):
    type = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Изменено на DecimalField
    fullName = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)  # Изменено на CharField
    email = models.EmailField(max_length=254)  # Изменена максимальная длина

    def __str__(self):
        return self.fullName


# покупка сертификата
class BuyCertificate(models.Model):  # Исправлена опечатка здесь
    fullNameBuyer = models.CharField(max_length=30)
    fullNameUses = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)  # Изменено на CharField
    email = models.EmailField(max_length=254)  # Изменена максимальная длина
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Изменено на DecimalField

    def __str__(self):
        return self.fullNameBuyer


# дороги
class Roads(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    description = models.TextField()  # Удалена максимальная длина
    fullDescription = models.TextField()  # Удалена максимальная длина

    def __str__(self):
        return self.name


class RoadsImage(models.Model):
    roads = models.ForeignKey(Roads, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.roads.name


# бронирование коттеджа
class CottageReservation(models.Model):
    dateTo = models.DateField()
    dateFrom = models.DateField()
    cottage = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.dateFrom} - {self.dateTo}, {self.cottage}"


class PeopleReservationCottage(models.Model):
    fullName = models.CharField(max_length=30)
    cottage = models.ForeignKey(CottageReservation, related_name='reservations', on_delete=models.CASCADE)

    def __str__(self):
        return self.fullName


# коттедж
class Cottage(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Изменено на DecimalField
    description = models.TextField()

    def __str__(self):
        return self.name


class CottageImage(models.Model):
    cottage = models.ForeignKey(Cottage, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.cottage.name


# постер
class Poster(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    instagram = models.CharField(max_length=30)
    vk = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PosterImage(models.Model):
    poster = models.ForeignKey(Poster, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.poster.name


# наши услуги
class OurServices(models.Model):
    name = models.CharField(max_length=30)
    short_description = models.TextField()
    long_description = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ServicesImage(models.Model):
    service = models.ForeignKey(OurServices, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.service.name


# бронирование инструктора
class ReservationInstructor(models.Model):  # Исправлена опечатка здесь
    date = models.DateField()
    instructor = models.CharField(max_length=30)
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Изменено на DecimalField

    def __str__(self):
        return self.instructor


class PeopleReservationInstructor(models.Model):  # Исправлена опечатка здесь
    instructor = models.ForeignKey(ReservationInstructor, related_name='reservations_instructor', on_delete=models.CASCADE)
    fullName = models.CharField(max_length=30)

    def __str__(self):
        return self.fullName


# бронирование инструмента
class ReservationInstrument(models.Model):
    date = models.DateField()
    instrument = models.CharField(max_length=30)
    time = models.TimeField()
    instructor = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Изменено на DecimalField

    def __str__(self):
        return self.instrument


class PeopleReservationInstrument(models.Model):
    instrument = models.ForeignKey(ReservationInstrument, related_name='reservations_instrument', on_delete=models.CASCADE)
    fullName = models.CharField(max_length=30)

    def __str__(self):
        return self.fullName
