from django.db import models
from django.core.validators import RegexValidator

class Student(models.Model):
    reg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    school = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    # Use a validator for phone numbers or a specialized field
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # blank=True allows empty phone numbers

    def __str__(self):
        return f'{self.name} ({self.reg_id})'
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
