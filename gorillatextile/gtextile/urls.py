from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('dashboard/', views.seller_dashboard, name='sellerd'),
    path("products/add/", views.product_create, name="add_product"),
    path("category/add/", views.category_create, name="add_category"), 
    
]