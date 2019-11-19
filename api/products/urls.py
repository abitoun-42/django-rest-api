from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views
from products import views
from django.conf.urls import include

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('products/<int:pk>/highlight/', views.ProductHighlight.as_view(), name='product-highlight'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail')
])

urlpatterns += [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]