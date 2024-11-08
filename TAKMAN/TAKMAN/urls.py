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
]

# Добавьте этот код перед редиректом
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Теперь редирект
urlpatterns += [
    re_path(r'^.*$', RedirectView.as_view(url='/not-found', permanent=False)),
]