from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('dashboard/', views.seller_dashboard, name='sellerd'),
    path("products/add/", views.product_create, name="add_product"),
    path("category/add/", views.category_create, name="add_category"), 
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
    path('product/add-image/', views.add_product_image, name='add_product_image'),
    
]