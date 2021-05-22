from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register',views.register , name='register'),
    path('login',views.login , name='login'),
    path('logout',views.logout , name='logout'),
    path('web_page',views.web_page , name='web_page'),
    path('create_article',views.create_article, name='create_article')


]
