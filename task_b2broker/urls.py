from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path('api/', include('core.urls'))
]

urlpatterns += staticfiles_urlpatterns()
