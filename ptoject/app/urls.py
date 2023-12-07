from django.urls import path
from .views import index,appointmentForm

urlpatterns = [
    path('', index, name="index"),
    path('form',appointmentForm,name='form'),
    path('news',news,name='news'),
    # path('user', postuser, name='user'),
]