from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField() 
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    # image = models.ImageField()
    # file = models.FileField()

    def __str__(self):
        return self.name
#     student = Student.objects.create(name="Alice", age=30)

# # Without __str__:
# print(student)  # Output: <Student: Student object (1)>

# # With __str__:
# print(student)  # Output: Alice

class Product(models.Model):
    name = models.CharField(max_length=100)
    