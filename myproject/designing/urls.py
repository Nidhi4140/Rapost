
from django.urls import path
from .import views
app_name = 'designing'
urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('feedback/', views.feedback, name='feedback'),
    path('hire/', views.hire, name='hire'),
    path('home/', views.home, name='home'),
]
