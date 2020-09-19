

from django.urls    import path
from .views import gospel_music



urlpatterns = [
   
    path('', gospel_music , name='gospel_music' ),
    ]