from django.urls import path, include

from . import views as v

urlpatterns=[
    path('create/', v.UserCreateListView.as_view()),
    path('detail/<int:id>/', v.UserDetailView.as_view()),
]