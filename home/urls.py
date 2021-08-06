from django.urls import path
from django.conf.urls import handler404, handler500
from .views import HomeView, Error404View, Error500View

app_name="home"


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    
    ]

handler404 = Error404View.as_view()
handler500 = Error500View.as_error_view()
