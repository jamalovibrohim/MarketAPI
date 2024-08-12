from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .ser import U_SER,User_Get, Category_Ser, Product_Ser
from .models import User, Category, Product

class UserCreateListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = U_SER

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = U_SER
    lookup_field = 'id'
# ---------------------------------------------------------------------------------------

class CategoryCreateListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_Ser

class CategoryDeteilView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_Ser
    lookup_field = 'id'

    def delete(self, request, id):
        Category.objects.get(id=id).delete()
        return Response("o'chirildi")
    
#----------------------------------------------------------------------------------------

class ProductCreateListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_Ser

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_Ser
    lookup_field = 'id'

    def delete(self, request, id):
        Product.objects.get(id=id).delete()
        return Response("o'chirildi")
