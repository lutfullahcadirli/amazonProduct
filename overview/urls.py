from django.urls import include, path
from overview import views



urlpatterns = [
    path('',views.home_page, name="home_page"),
]
