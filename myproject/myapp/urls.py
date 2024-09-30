from myapp import views
from django.urls import path
urlpatterns = [
    path('', views.index),
    path('form/', views.form, name='form'),  # form view
    path('about/', views.about, name='about'),  # about view
    path('delete/<Person_id>',views.delete),
    path('edit/<Person_id>',views.edit),
]