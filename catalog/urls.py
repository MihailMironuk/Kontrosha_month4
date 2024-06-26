from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('add_review/<int:id>/', views.AddReviewView.as_view(), name='add_review'),
    path('edit_product/<int:id>/', views.EditProductView.as_view(), name='edit_product'),
    path('delete_product/<int:id>/', views.ProductDeleteView.as_view(), name='delete_product'),
]
