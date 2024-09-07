from django.db import models
from categories.models import SubCategory

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    # Additional fields...
    def __str__(self):
        return self.name
    

class Phone(Item):
    screen_size = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    rom = models.CharField(max_length=50)
    battery_capacity = models.CharField(max_length=50)
    camera_resolution = models.CharField(max_length=50)

class Accessory(Item):
    compatibility = models.CharField(max_length=100)  # E.g., Compatible with iPhone, Samsung, etc.
    material = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

class Tablet(Item):
    screen_size = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    battery_life = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=50)  # E.g., iOS, Android, etc.

class SmartDevice(Item):
    type = models.CharField(max_length=50)  # E.g., Smartwatch, Fitness Tracker
    compatibility = models.CharField(max_length=100)  # E.g., Compatible with Android, iOS
    battery_life = models.CharField(max_length=50)
    features = models.TextField()  # E.g., Heart rate monitor, GPS, etc.