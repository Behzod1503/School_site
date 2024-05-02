from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from dj_rest_auth.views import PasswordResetConfirmView

schema_view = get_schema_view(
    openapi.Info(
        title='School site',
        description='Project for school № 13',
        default_version='v1',
        terms_of_service='https://sarvarazim.uz/',
        contact=openapi.Contact(email='princeasia013@gmail.com', name='Prince Asia', url='https://tilshunos.com'),
        license=openapi.License(name='Hech qanaqa litsenziya'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # docExpansion = 'none',
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('users.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/pages/', include('app_pages.urls')),
    path('api/v1/piar/', include('app_piar.urls')),
    path('api/v1/school/', include('app_school.urls')),
    path('api/v1/search/', include('app_search.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0, ), name='schema-swagger-ui'),
    path('', schema_view.with_ui('swagger', cache_timeout=0, ), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
#
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
