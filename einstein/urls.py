from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_code, name="get_code"),
    path('donate', views.donate, name="donate"),
    path('about', views.about, name="about"),
    path('createEmail', views.createEmail, name="createEmail"),
    path('thankyou', views.thankyou, name="thankyou"),
    path('jsnotes', views.jsnotes, name="jsnotes"),
    path('donatethankyou', views.donatethankyou, name="donatethankyou"),
]
