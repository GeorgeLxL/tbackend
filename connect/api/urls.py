from django.conf.urls import url
from django.urls import path
from connect.api.views import  UserLoginView, UserRegistrationView, CurrencyView, AdminLoginView, UploadView, Account, UserList, AccountUpdate,AvatarUpdate
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('signup', UserRegistrationView.as_view()),
    path('login', UserLoginView.as_view()),
    path('myadmin/login', AdminLoginView.as_view()),
    path('getProfile', Account.as_view()),
    path('updateProfile', AccountUpdate.as_view()),
    path('updateAvatar', AvatarUpdate.as_view()),
    path('getusers', UserList.as_view()),
    path('uploadcsv', UploadView.as_view())
]