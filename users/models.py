from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

CATEGORY_CHOICES = [
    ('ELT', 'Electronics'),
    ('JGP', 'Jewellery'),
    ('MSC', 'Mens Clothing'),
    ('WSC', 'Womens Clothing'),
    ('FWS', 'Footwear'),
]
class Product(models.Model):

    name = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank =True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    discount = models.IntegerField(default=0)
    category = models.CharField( choices=CATEGORY_CHOICES,  max_length= 10)
    image1 = models.ImageField(upload_to ='products', blank=True, null=True, max_length=255)
    image2 = models.ImageField(upload_to = 'products', blank=True, null=True, max_length=255)
    image3 = models.ImageField(upload_to = 'products', blank=True, null=True, max_length=255)
    timestamp = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-timestamp']

        def __str__(self):
            return str(self.name)

    def save (self, *args, **kwargs):

        super().save(*args, **kwargs)



@receiver(post_save , sender=User)
def send_email_to_user(*args, **kwargs):
    access = kwargs['instance']
    print('hhhh', access.email)
    if kwargs['created'] and access.email:
        send_mail(
        'Registration',
        'Thanks for signing up.',
        'jackie.botchway@gmail.com',
        ['wevokip124@karavic.com'],
        fail_silently=False,)
        print('email sent')