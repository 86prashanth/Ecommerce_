from django.urls import path
from  Blog.controller import authviews
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('collection/',collection,name='collection'),
    path('collectionview/<str:slug>',collectionview,name='collectionview'),
    path('productview/<str:cat_slug>/<str:prod_slug>',productview,name='productview'),
    path('product-list',product_list,name='product_list'),
    path('profile/',authviews.profile,name='profile'),
    path('register/',authviews.register,name='register'),
    path('login/',authviews.loginpage,name='login'),
    path('logout/',authviews.logoutpage,name='logout'),
    # path('password_reset/',authviews.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset/done/',authviews.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uuidb64>/<token>/',authviews.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/',authviews.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
