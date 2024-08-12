from django.urls import path, include

from . import views as v

urlpatterns=[
    path('register/', v.UserCreateListView.as_view()),
    path('user_detail/<int:id>/', v.UserDetailView.as_view()),
    path('category/', v.CategoryCreateListView.as_view()),
    path('CDV/<int:id>/',v.CategoryDeteilView.as_view()),
    path('product/', v.ProductCreateListView.as_view()),
    path('product_detail/<int:id>/',v.ProductDetailView.as_view()),
]