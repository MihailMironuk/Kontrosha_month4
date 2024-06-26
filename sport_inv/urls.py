from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('', views.about_us_view, name='about_us_view'),
    path('', views.contact_us_view, name='contact_us_view'),

]
