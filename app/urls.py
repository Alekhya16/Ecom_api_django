from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProductCreateAPIView, ProductListAPIView, CustomerCreateAPIView, CustomerListAPIView, OrderCreateAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('product/list/', ProductListAPIView.as_view(), name='product-list'),
    path('customer/create/', CustomerCreateAPIView.as_view(), name='customer-create'),
    path('customer/list/', CustomerListAPIView.as_view(), name='customer-list'),
    path('order/create/', OrderCreateAPIView.as_view(), name='order-create'),
]




