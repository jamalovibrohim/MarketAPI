from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .ser import U_SER,User_Get
from .models import User

class UserCreateListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = U_SER

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = User_Get
    lookup_field = 'id'

# Create your views here.
