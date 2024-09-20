from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop_all/', views.shop_all, name='shop_all'),
    path('ingredients/', views.ingredients, name='ingredients'),

    # footer components 
    path('pages/shipping_policy/', views.shipping_policy, name='shipping_policy'),
    path('pages/terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('pages/website_terms_and_conditions/', views.website_terms_and_conditions, name='website_terms_and_conditions'),
    path('pages/privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('pages/acceptable_use_policy/', views.acceptable_use_policy, name='acceptable_use_policy'),
]
