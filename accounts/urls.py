from django.urls import path

from .views import SignUpView
from . import views
from .views import mal_Requirements
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('', views.malRequirements(), name='user_page')
    path('mal/', views.mal_Requirements, name='jobs')
]