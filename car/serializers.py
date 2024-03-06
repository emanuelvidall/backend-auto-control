from rest_framework import serializers
from .models import TypeVehicle, Brand, TypeUser, Vehicle, User, TypeExpense, Expense, VehicleExpense

class TypeVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeVehicle
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class TypeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeUser
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    type_vehicle = serializers.SlugRelatedField(slug_field='name', queryset=TypeVehicle.objects.all())
    brand_name = serializers.SlugRelatedField(slug_field='name', queryset=Brand.objects.all())
    
    class Meta:
        model = Vehicle
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    type_user = serializers.SlugRelatedField(slug_field='name', queryset=TypeUser.objects.all())
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
    
    class Meta:
        model = User
        fields = '__all__'

class TypeExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeExpense
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    type_expense = serializers.SlugRelatedField(slug_field='name', queryset=TypeExpense.objects.all())
    
    class Meta:
        model = Expense
        fields = '__all__'

class VehicleExpenseSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
    expense = serializers.PrimaryKeyRelatedField(queryset=Expense.objects.all())

    class Meta:
        model = VehicleExpense
        fields = '__all__'
