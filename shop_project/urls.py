
"""
URL configuration for Afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from products import views
urlpatterns = [

     path('api/v1/products/', views.DirectorListAPIView.as_view()),
     path('api/v1/directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
     path('api/v1/products/', views.MovieListAPIView.as_view()),
     path('api/v1/products/<int:id>/', views.MovieDetailAPIView.as_view()),
     path('api/v1/reviews/', views.ReviewsListAPIView.as_view()),
     path('api/v1/reviews/<int:id>/', views.ReviewsDetailAPIView.as_view()),
     path('api/v1/users/', include('users.urls')),
]