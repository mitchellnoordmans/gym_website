"""
URL configuration for gym_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, services, contact ,personal_trainer, group_lessons, membership_plans, about, roster, blog
from django.conf import settings
from django.conf.urls.static import static


app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('personal_training/', personal_trainer, name='personal_training'),
    path('membership_plans/', membership_plans, name='membership_plans'),
    path('contact/', contact, name='contact'),
    path('group_lessons/', group_lessons, name='group_lessons'),
    path('roster/', roster, name='roster'),
    path('blog/', blog, name='blog'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
