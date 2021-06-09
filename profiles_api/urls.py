from django.urls import path, include
from django.urls.resolvers import URLPattern
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewset,basename='hello-viewset')
router.register('profile',views.UserProfileViewset)

urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view(),name= 'helloapiview'),
    path('',include(router.urls)),
    
]