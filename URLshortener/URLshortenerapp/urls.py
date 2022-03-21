from django.urls import path
from .views import homeView, createUrl, routeToURL
urlpatterns=[
    path('home', homeView, name='home'),
    path('', createUrl),
    path('slug:key>', routeToURL)
]