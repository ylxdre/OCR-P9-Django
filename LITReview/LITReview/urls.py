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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
import authentication.views
import reviews.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', reviews.views.home, name='home'),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', authentication.views.register_page, name='register'),
    path('flux/', reviews.views.flux, name='flux'),
    path('posts/', reviews.views.posts, name='posts'),
    path('subscribed/', reviews.views.subscribed, name='subscribed'),
    path('ticket/add/', reviews.views.create_ticket, name='ticket-add'),
    path('review/add/', reviews.views.create_review, name='review-add'),
    path('ticket/<int:ticket_id>/',
         reviews.views.ticket, name='ticket-detail'),
    path('ticket/<int:ticket_id>/update/',
         reviews.views.update_ticket, name='ticket-update'),
    path('ticket/<int:ticket_id>/delete/',
         reviews.views.delete_ticket, name='ticket-delete'),
    path('ticket/<int:ticket_id>/review/',
         reviews.views.ticket_review, name='review-ticket'),
    path('review/<int:review_id>/',
         reviews.views.review, name='review-detail'),
    path('review/<int:review_id>/update/',
         reviews.views.update_review, name='review-update'),
    path('review/<int:review_id>/delete/',
         reviews.views.delete_review, name='review-delete'),
    path('unsubscribe/<int:followed_user_id>/',
         reviews.views.unsubscribe, name='unsubscribe'),
]

if settings.DEBUG:
    urlpatterns += static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
