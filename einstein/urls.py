from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_code, name="get_code"),
    path('actionUrl', views.importData),
    path('donate', views.donate, name="donate"),
<<<<<<< HEAD
    path('contact', views.contact, name="contact")
=======
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about")
>>>>>>> 2d134f0 (07102021-1)
]
