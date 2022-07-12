from django.urls import path
# the '.' represent that we are on the same file line, like a sibling file
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('travels/', views.travels_index, name='index'),
    path('travels/<int:travel_id>/', views.travels_detail, name='detail'),
]