from django.db import models

class TypeVehicle(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name  

class TypeUser(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    type_vehicle = models.ForeignKey(TypeVehicle, on_delete=models.CASCADE)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name  

class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=254)
  drivers_license = models.CharField(max_length=20)
  password = models.CharField(max_length=20)
  type_user = models.ForeignKey(TypeUser, on_delete=models.CASCADE)
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

  def __str__(self):
        return self.name

class TypeExpense(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    type_expense = models.ForeignKey(TypeExpense, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

class VehicleExpense(models.Model):
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
  expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
  value = models.FloatField()
  paid = models.BooleanField()

  def __str__(self):
      return self.name

