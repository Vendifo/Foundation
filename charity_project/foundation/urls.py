from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event/<slug:slug>/', views.event_detail, name='event_detail'),  # Добавьте этот маршрут
    path('donation/', views.donation, name='donation'),
    path('initiative/', views.initiative, name='initiative'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
]
