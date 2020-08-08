from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

class Profile(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?\d{10,10}$',
                                 message=" format: '1234567890','1234567890','1234567890' Up to 10 digits allowed.")

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    dob = models.DateField(blank=True,null=True)
    phone = models.CharField(validators=[phone_regex],unique=True,max_length=13,null=False)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)



# Create your models here.
