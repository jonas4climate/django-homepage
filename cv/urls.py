from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_view, name='cv_view'),
    path('edit/', views.cv_edit, name='cv_edit')
]