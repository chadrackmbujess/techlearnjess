from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('a-propos/', views.about, name='about'),
    path('tableau-de-bord/', views.dashboard, name='dashboard'),
    path('faq/', views.faq_list, name='faq'),
]