from django.urls import path, include
from rest_framework import routers

from . import views
from .views import UserViewSet

# User router
user_router = routers.SimpleRouter()
user_router.register(
    r'user',
    UserViewSet,
)

urlpatterns = [
    path('api/v1/', include(user_router.urls)),
    path('api/v1/user/<int:pk>/', views.UserDetail.as_view())
]
