from django.urls import path
from users.api.views import RegisterView, UserView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register', RegisterView.as_view()),
    path('auth/me', UserView.as_view()),
]