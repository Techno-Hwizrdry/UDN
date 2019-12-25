from django.urls import path
from .           import views

app_name = 'participant_info'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_participant/', views.add_participant, name='add_participant'),
    path('all/', views.all_participants, name='all'),
]
