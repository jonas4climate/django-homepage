from django.urls import path
from . import views

urlpatterns = [
   path('', views.cv_view, name='cv_view'),
   path('edit/', views.cv_edit_overview, name='cv_edit_overview'),
   path('edit/<str:sub>/<int:pk>', views.cv_edit, name='cv_edit'),
   path('add/<str:sub>', views.cv_add, name='cv_add'),
]