"""
URL configuration for LITReview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
import authentication.views, reviews.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', reviews.views.home, name='home'),
#    path('', LoginView.as_view(
    path('', authentication.views.login_page, name='login'),
#        template_name='authentication/login.html',
#        redirect_authenticated_user=True), name='login'),
    path('pwd-change/', PasswordChangeView.as_view(
        template_name='authentication/pwd_change.html'), name='pwd-change'),
    path('pwd-change-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/pwd_change_done.html'), name='pwd-change-done'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', authentication.views.register_page, name='register'),
    path('flux/', reviews.views.flux, name='flux'),
    path('posts/', reviews.views.posts, name='posts'),
    path('subscribed/', reviews.views.subscribed, name='subscribed'),
]
