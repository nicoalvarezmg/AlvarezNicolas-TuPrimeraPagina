from home.views import home
from django.urls import path
urlpatterns = [
    path('pipes-home/', home, name='pipes_home')
]