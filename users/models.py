from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
   # Django ya incluye username, email, password, is_active, is_staff, etc.
    # Solo necesitas añadir los campos EXTRA que tú quieras.
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']
        
class Direction(models.Model):
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='directions')   
    
    def __str__(self):
        return f"{self.street} {self.number}, {self.city}, {self.state}, {self.zip_code}, {self.country}"
    
    class Meta:
        verbose_name = 'Direction'
        verbose_name_plural = 'Directions'
        ordering = ['city', 'street', 'number']
      