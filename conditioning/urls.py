from django.urls import path

from . import views

app_name = 'conditioning'

urlpatterns = [
	path('', views.home, name= 'home'),
    path('players/', views.PlayersView.as_view(), name='players'),
    path('details/<int:id>', views.PlayerDetails, name= 'details'),
    
    path('new/', views.NewReport, name='new'),
    path('edit/<int:id>', views.EditReport, name= 'edit'),  
    path('reharb', views.reharb, name='reharb'),  
]