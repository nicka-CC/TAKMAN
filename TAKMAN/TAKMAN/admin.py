from django.contrib import admin
from .models import Roads, RoadsImage, ReplenishmentOfBalanceSkiPass, BuySkiPass, BuyCertificate, \
    CottageReservation, Cottage, CottageImage, Poster, PosterImage, OurServices, ServicesImage, \
    ReservationInstructor, PeopleReservationInstructor, ReservationInstrument, PeopleReservationInstrument, \
    PeopleReservationCottage  # Добавлено


class RoadImageInline(admin.TabularInline):
    model = RoadsImage
    extra = 1  # Количество пустых форм для добавления новых изображений

class RoadAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description', 'fullDescription')
    search_fields = ('name',)
    inlines = [RoadImageInline]  # Включаем инлайн-класс

class PeopleReservationCottageInline(admin.TabularInline):
    model = PeopleReservationCottage
    extra = 1

class CottageReservationAdmin(admin.ModelAdmin):
    list_display = ('cottage', 'dateTo', 'dateFrom')
    search_fields = ('cottage',)
    inlines = [PeopleReservationCottageInline]

class CottageInline(admin.TabularInline):
    model = CottageImage
    extra = 1

class CottageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)
    inlines = [CottageInline]

class PosterImageInline(admin.TabularInline):
    model = PosterImage
    extra = 1

class PosterImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'instagram', 'vk',)
    search_fields = ('name',)
    inlines = [PosterImageInline]

class ServicesImageInline(admin.TabularInline):
    model = ServicesImage
    extra = 1

class ServicesImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'long_description', 'url',)
    search_fields = ('name',)
    inlines = [ServicesImageInline]

class PeopleReservationInstructureInline(admin.TabularInline):
    model = PeopleReservationInstructor
    extra = 1

class ReservationInstructureAdmin(admin.ModelAdmin):
    list_display = ('date', 'instructor', 'time', 'price',)
    search_fields = ('instructor',)
    inlines = [PeopleReservationInstructureInline]

class PeopleReservationInstrumentInline(admin.TabularInline):
    model = PeopleReservationInstrument
    extra = 1

class ReservationInstrumentAdmin(admin.ModelAdmin):
    list_display = ('date', 'instrument', 'time', 'instructor', 'price')
    search_fields = ('instrument',)
    inlines = [PeopleReservationInstrumentInline]

admin.site.register(ReplenishmentOfBalanceSkiPass)
admin.site.register(BuyCertificate)  # Исправлено на BuyCertificate
admin.site.register(BuySkiPass)
admin.site.register(Roads, RoadAdmin)
admin.site.register(CottageReservation, CottageReservationAdmin)
admin.site.register(Cottage, CottageAdmin)
admin.site.register(Poster, PosterImageAdmin)
admin.site.register(OurServices, ServicesImageAdmin)




admin.site.register(ReservationInstructor, ReservationInstructureAdmin)
admin.site.register(ReservationInstrument, ReservationInstrumentAdmin)
