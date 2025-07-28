from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Owner(name =" + self.name + ")"



class Cat(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return "Cat(name =" + self.name + ", age = " + str(self.age) + ")"
