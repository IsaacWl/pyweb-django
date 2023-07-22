from django.urls import path
from . import views
# config urls
urlpatterns = [
    path('', views.members, name='members'),
    path('members/', views.members_list, name='members_list'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members/create', views.create_member, name='member_create'),
    path('testing/', views.testing, name='testing')
]
