from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (LoginView, logoutView, CreateUserView, DoneView,  PassworChangeView,
                    ResetPasswordView, PasswordResetDoneView1, PasswordResetConfirmView1, PasswordResetCompleteView1,
                    AccountView, UserDataUpdateView, DeleteUserView)

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', login_required(logoutView), name="logout"),
    path('register/', CreateUserView.as_view(), name="register"),
    path('done/', DoneView.as_view(), name="done"),
    path('password_change/', login_required(PassworChangeView.as_view()), name="change"),
    path('info/', AccountView.as_view(), name="account"), #Protegido desde view
    path('user_data/<int:pk>', UserDataUpdateView.as_view() , name="user_data_update"),
    path('eliminar/<int:pk>', DeleteUserView.as_view(), name="delete_user"),
    path('reset_password/', ResetPasswordView.as_view(), name="reset_password"),
    path('reset_password_sent/', PasswordResetDoneView1.as_view(), name="password_reset_done"), 
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView1.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', PasswordResetCompleteView1.as_view(), name="password_reset_complete"),
    
]



