from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.addDeveloper, name='add'),
    path('edit/<int:id>/', views.editDeveloper, name='edit'),
    path('delete/<int:id>/', views.deleteDeveloper, name='delete'),
]
