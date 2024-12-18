from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView

from . import views
from django.urls import path, re_path

from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('skiing/', views.skiing, name='skiing'),
    path('not-found', views.notFound, name='not_found'),
    path('accommodation/', views.accomodation_list, name='accommodation'),
    path('accommodation/<int:id>/', views.accomodation_detail, name='accommodation_detail'),
    path('services/', views.services, name='services'),
    path('services/reservate-instructor/', views.reservateInstructor, name='reservate-instructor'),
    path('services/reservate-instrument/', views.reservateInstrument, name='reservate_instrument'),
    path('buy-sertificate/', views.sertificateBuy, name='buy-sertificate'),
    path('tour/', views.toursPage, name='tour'),
    path('inforamation/', views.informationPage, name='information'),
    path('summer/', views.summerPage, name='summer'),
    path('prices/', views.pricesPage, name='prices')
]

# Добавьте этот код перед редиректом
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Теперь редирект
urlpatterns += [
    re_path(r'^.*$', RedirectView.as_view(url='/not-found', permanent=False)),
]