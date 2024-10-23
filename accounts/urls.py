from django.urls import include, path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup, name="signup_page"),
    path('login/',views.login, name="login_page"),
]
