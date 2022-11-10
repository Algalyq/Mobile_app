
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Swagger",
        default_version='v1',
        description="test swag",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@swaggerBlog.local"),
        license=openapi.License(name="test licence")
    ),
    public=True,
)
urlpatterns = [   
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
    path('admin/', admin.site.urls),
    path('api/', include('Auth.urls')),
    path('rent/', include('Rent_app.urls'))
]
