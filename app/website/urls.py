from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),

    path('form.html', views.form, name="form"),

    path('appreciation.html', views.appreciation, name="appreciation"),

    path('review.html', views.review, name="review"), 
]