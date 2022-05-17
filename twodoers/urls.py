from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include


urlpatterns = [ 
    path('', include('landing.urls')),
    path('ws/', include('reports.urls')) ,
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()

