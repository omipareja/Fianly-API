from django.contrib import admin
from django.urls import path,include,re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Fianly Backend  API",
      default_version='v1',
      description="Backend Prueba",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="juanmanuel.sanchez@utp.edu.co"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('',include('applications.home.urls')),
    path('admin/', admin.site.urls),
    path('',include('applications.users.urls')),
    path('',include('applications.users.api.routers')),
    #Swaguer Routes
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
