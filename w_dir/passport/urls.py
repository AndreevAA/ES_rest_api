from django.urls import path, include
from rest_framework import routers

from . import views
from .views import PassportViewSet

# User router
user_router = routers.SimpleRouter()
user_router.register(
    r'passport',
    PassportViewSet,
)

urlpatterns = [
    path('api/v1/', include(user_router.urls)),
    path('api/v1/passport/<int:pk>/', views.PassportDetail.as_view())
]
