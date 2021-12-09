from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='fresh_start-home'),
    path('about/', views.about, name='fresh_start-about'),
    path('', views.add_resources, name='add_resources.html'),
    path('', views.comments, name='comments.html'),
    #path('', views.index , name='index'),
    #url(r'^$', 'index', name='index'),
]