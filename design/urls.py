from django.urls import path
from design import views

urlpatterns = [
    path('', views.index, name='homepage')
]
