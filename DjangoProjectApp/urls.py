from django.urls import path

from DjangoProjectApp import views
urlpatterns = [
    path('', views.home, name='My_index'),

    path('about/', views.about, name='My_about'),

    path('blog/', views.blog, name='blog'),

    path('contact/', views.contact, name='My_contact'),

    path('service/', views.services, name='My_service'),

    path('jobs/', views.jobs, name='My_jobs'),

    path('news/', views.news, name='My_news'),


]