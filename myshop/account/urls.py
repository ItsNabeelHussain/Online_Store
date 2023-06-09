from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views
 
urlpatterns = [
     # path('login/', LoginView.as_view(), name='login'),

     path('', include('django.contrib.auth.urls')),

    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
#      # login / logout urls
#         path('logout/', auth_views.LogoutView.as_view(), name='logout'),

#         # change password urls
#         path('password-change/',
#              views.CustomPasswordChangeView.as_view(
#                  template_name='registration/password_change_form.html'),
#              name='password_change'),
#         path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
#              name='password_change_done'),


#         # reset password urls
#         path('password-reset/', auth_views.PasswordResetView.as_view(),
#              name='password_reset'),
#         path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
#              name='password_reset_done'),
#         path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
#              name='password_reset_confirm'),
#         path('password-reset/complete/',
#              auth_views.PasswordResetCompleteView.as_view(),
#              name='password_reset_complete'),


]
