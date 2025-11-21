from django.db import models
from django.core.validators import MinValueValidator

class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(1)])
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("Male", "Male"), ("Female", "Female")))

    def __str__(self):
        return self.name


