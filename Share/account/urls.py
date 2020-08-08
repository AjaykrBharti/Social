from django.urls import path
from .views import index,user_login,dashboard,register,edit
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',index,name='home'),
    # path('login/',user_login,name='login'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('',dashboard, name='dashboard'),
    # change password urls
    path('password-change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$',
     auth_views.PasswordResetView.as_view(),
     name='password_reset'),
    url(r'^password-reset/done/$',
     auth_views.PasswordResetDoneView.as_view(),
     name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
     auth_views.PasswordResetConfirmView.as_view(),
     name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
     auth_views.PasswordResetCompleteView.as_view(),
     name='password_reset_complete'),


    path('register/', register, name='register'),

    path('edit/',edit, name='edit')
]