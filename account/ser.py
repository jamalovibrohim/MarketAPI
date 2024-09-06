from  rest_framework import serializers
from .models import User, Category, Product

class U_SER(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','photo', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
class User_Get(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','photo', 'username']
    
class ChangePasswordSer(serializers.Serializer):
    old_password = serializers.CharField(max_length =15)
    new_password = serializers.CharField(max_length =15)
    confirm_password = serializers.CharField(max_length =15)
    
# ---------------------------------------------------------------------------------------

class Category_Ser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'photo', 'parent']
# ---------------------------------------------------------------------------------------
        
# class Product_Ser(serializers.ModelSerializer):
#     class Meta:
#         model = Product 
#         fields = ['id','name', 'price', 'user', 'batafsil','created', 'updated', 'category']
#         extra_kwargs = {'user': {'read_only': True}}

class Product_Ser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'price','batafsil','created', 'updated', 'category']

    def create(self,validated_data):
        owner = self.context['request'].user
        new_product = Product.objects.create(**validated_data, user = owner)
        return new_product