from django.urls import path
from .views import index, shortened

app_name = 'home'
urlpatterns = [
    path('', index, name='index'),
    path('s/<int:pk>/', shortened, name='shortened'),
]