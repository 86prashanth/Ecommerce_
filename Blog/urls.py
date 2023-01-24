from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('collection/',collection,name='collection'),
    path('collectionview/<str:slug>',collectionview,name='collectionview'),
]
