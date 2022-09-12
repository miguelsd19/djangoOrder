from django.urls import path
from season.api.views import seasonView


urlpatterns = [
    path('Season', seasonView.as_view(), name='seasonView'),

]