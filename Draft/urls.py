from django.conf    import settings # for debug toolbar 
from django.contrib import admin
from django.urls    import path, include
#import debug_toolbar



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',   include ('draft_app.urls')),
       
    ]


if settings.DEBUG:

    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]+urlpatterns # very important