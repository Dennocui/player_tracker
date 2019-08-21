from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name = 'signin'),
    path('players/', include('players.urls', namespace='players')),
    path('medical/', include('medical.urls', namespace='medical')),
    path('conditioning/', include('conditioning.urls', namespace='conditioning')),
    path('accounts/', include('accounts.urls', namespace='accounts'))
    
] 
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

