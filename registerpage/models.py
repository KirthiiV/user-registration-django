from django.db import models

class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=(("Male", "Male"), ("Female", "Female")),
        default="Male"
    )

    def __str__(self):
        return f"{self.name} ({self.email})"
