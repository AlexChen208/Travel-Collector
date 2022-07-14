from django.urls import path
# the '.' represent that we are on the same file line, like a sibling file
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('travels/', views.travels_index, name='index'),
    path('travels/<int:travel_id>/', views.travels_detail, name='detail'),
    path('travels/create/', views.TravelCreate.as_view(), name='travels_create'),
    path('travels/<int:pk>/update/', views.TravelUpdate.as_view(), name='travels_update'),
    path('travels/<int:pk>/delete/', views.TravelDelete.as_view(), name='travels_delete'),
    path('travels/<int:travel_id>/add_review/', views.add_review, name='add_review'),
    path('tags/', views.tags_index, name='tags_index'),
    path('tags/<int:tag_id>/', views.tags_detail, name='tags_detail'),
    path('tags/create/', views.TagCreate.as_view(), name='tags_create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tags_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tags_delete'),
]