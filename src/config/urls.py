from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="subscription-system API",
        default_version='v1',
        description="This is for all client of subscription-system",
        terms_of_service="https://www.subscription-system.com/policies/terms/",
        contact=openapi.Contact(email="testemail@example.com"),
        license=openapi.License(name="subscription-system License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

docpatterns = []

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('config.auth.Users.urls.register_urls')),
    path('auth/', include('config.auth.Users.urls.login_urls')),
    path('auth/', include('config.auth.Users.urls.socialauth_urls')),
    path('profile/', include('config.auth.Profiles.urls.editprofile_urls')),
    path('profile/', include('config.auth.Profiles.urls.subscription_urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/api.json', schema_view.without_ui(cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
