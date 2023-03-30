from django.urls import path
from .views import index, shortened

app_name = 'home'
urlpatterns = [
    path('', index, name='index'),
    path('<str:shorted_url>/',shortened)
]