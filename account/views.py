from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .ser import U_SER,User_Get, Category_Ser, Product_Ser, ChangePasswordSer
from .models import User, Category, Product

class UserCreateListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = U_SER

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = User_Get
    lookup_field = 'id'

class ChangePasswordView(APIView):
    def post(self, request):
        ser = ChangePasswordSer(data=request.data)
        inform = request.data
        if ser.is_valid():
            old_password = request.data['old_password']
            if request.user.check_password(old_password):
                if inform['new_password'] == inform['confirm_password']:
                    request.user.set_password(inform['confirm_password'])
                    request.user.save()
                    return Response({'message':"Siz parolingizni o'zgartirdingiz!"})
            else:
                return Response({'message':"eski parolni to'gri kiriting :("})
        return Response(ser.errors)
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

class ProductList(APIView):
    def post(self, request):
        ser = Product_Ser(data=request.data, context = {'request':request})
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

# class ProductCreateListView(APIView):
#     def get(self, request):
#         books = Product.objects.all()
#         serializer = Product_Ser(books, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         data = request.data
#         serializer = Product_Ser(data=request.data)
#         if serializer.is_valid():
#             p = serializer.save()
#             p.user=request.user
#             p.save()
#             return Response(
#                 serializer.data
#                 )
#         return Response(serializer.errors)



class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_Ser
    lookup_field = 'id'

    def delete(self, request, id):
        Product.objects.get(id=id).delete()
        return Response("o'chirildi")
