from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = 'players'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.home, name= 'home'),
    path('current', views.players, name= 'players'),
    path('past', views.past_players, name= 'past_players'),

    #path('new', views.new_player, name='new'),
    path('new_player', views.new_player, name='new_player'),
    path('details/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('edit_player/<int:id>/', views.edit_player, name='edit_player'),
    path('delete/<int:id>/', views.delete, name='delete'),

    path('settings',views.Settings, name='settings'),
    path('new_club', views.new_club, name='new_club'),
    path('edit_club/<int:id>',views.edit_club, name='edit_club'),

    path('new_school', views.new_school, name='new_school'),
    path('edit_school/<int:id>',views.edit_school, name='edit_school'),
] 