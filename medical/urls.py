from django.urls import path

from .import views

app_name = 'medical'

urlpatterns = [

    path('', views.home, name= 'home'),
    path('players/', views.players, name= 'players'),
    path('injured/', views.injured, name= 'injured'),
    path('new', views.NewMedicalReport, name='new'),
    #path('add', views.AddMedicalReport, name='add'),
    path('details/<int:id>', views.PlayerDetails, name= 'details'),
    path('edit/<int:id>', views.EditReport, name= 'edit'),

    path('data', views.get_data, name='data'),
    
]