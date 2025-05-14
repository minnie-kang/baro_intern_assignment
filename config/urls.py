from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView)


api_urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),  
]


swagger_urlpatterns = [
    path('swagger.json/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = api_urlpatterns + swagger_urlpatterns
