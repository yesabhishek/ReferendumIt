from django.contrib import admin
from django.urls import path,include
from Users import views as user_views
from polls import views as polls_views
from django.contrib.auth import views as auth_views             # importing Auth Views so that we can create an authentication system
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    
    path('',include('polls.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('update/', user_views.profile, name='update'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
]

    




