from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # /admin/
    path('admin/', admin.site.urls),

    # /api-auth/
    path('api-auth/', include('rest_framework.urls')),

    # /core/
    path('core/', include('core.urls')),

    # /auth/token/
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # /auth/token/refresh/
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
