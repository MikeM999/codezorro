from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_code, name="get_code"),
    path('actionUrl', views.importData),
    path('donate', views.donate, name="donate"),
    path('contact', views.contact, name="contact")
]
