from django.urls import path
from .views import home, profile, RegisterView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]

urlpatterns += staticfiles_urlpatterns()