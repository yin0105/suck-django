from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('48fortySolutions/', views.fortySolutions, name='48fortySolutions'),
    path('4earthFarms/', views.earthFarms, name='4earthFarms'),
    path('organicFarms/', views.organicFarms, name='organicFarms'),
    path('coldStorage/', views.coldStorage, name='coldStorage'),
    path('thomasProduce/', views.thomasProduce, name='thomasProduce'),
    path('abbottCobb/', views.abbottCobb, name='abbottCobb'),
    path('abcResearchLabs/', views.abcResearchLabs, name='abcResearchLabs'),
    path('abl/', views.abl, name='abl'),
    path('amerifresh/', views.amerifresh, name='amerifresh'),
    path('amhpac/', views.amhpac, name='amhpac'),
    path('ampco/', views.ampco, name='ampco'),
    path('amrAgro/', views.amrAgro, name='amrAgro'),

    path('login', views.login_attempt, name='login'),
    path('social-auth', views.social_auth, name='social-auth'),
    path('register', views.register_attempt, name='register'),
    path('check-email/', views.check_email, name="check-email"),
    path('email-verify/', views.email_verify, name="email-verify"),
    path('logout', views.logout_attempt, name='logout'),

    path('admin/profile', views.admin_profile, name="admin-profile"),
    path('admin/profile/update', views.admin_profile_update, name="admin-profile-update"),

]
