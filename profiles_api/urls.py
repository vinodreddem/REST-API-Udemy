from django.urls import path
from django.urls.resolvers import URLPattern

from profiles_api import views

urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view(),name= 'helloapiview'),
]