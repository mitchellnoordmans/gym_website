
from django.contrib import admin
from django.urls import path
from core.views import (
    home, contact ,personal_trainer, 
    group_lessons, membership_plans, about, 
    roster, blog, about_location, services_sauna, services_fysiotherapy,
    services_sportmassage
    )
from django.conf import settings
from django.conf.urls.static import static


app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('personal_training/', personal_trainer, name='personal_training'),
    path('membership_plans/', membership_plans, name='membership_plans'),
    path('contact/', contact, name='contact'),
    path('group_lessons/', group_lessons, name='group_lessons'),
    path('roster/', roster, name='roster'),
    path('blog/', blog, name='blog'),
    path('about/location/', about_location, name='about_location'),
    path('services/sauna', services_sauna, name='services_sauna'),
    path('services/fysiotherapie', services_fysiotherapy, name='services_fysiotherapy'),
    path('services/sportmassage', services_sportmassage, name='services_sportmassage')
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
