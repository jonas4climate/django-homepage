from django.urls import path
from . import views

urlpatterns = [
   path('', views.post_cv_view, name='post_cv_view'),
   path('edit/', views.post_cv_edit_overview, name='post_cv_edit_overview'),
   path('edit/<str:sub>/<int:pk>', views.post_cv_edit, name='post_cv_edit'),
   path('add/<str:sub>', views.post_cv_add, name='post_cv_add'),
]