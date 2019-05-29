from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ("Dish", "Dish"),
    ("Fruit", "Fruit"),
    ("Bevarage", "Bevarage"),
    ("Favorite", "Favorite"),
    ("Desert", "Desert"),
)

STATUS_CHOICES = (
    ("Available", "Available"),
    ("Not Available", "Not Available"),
)

class Menu(models.Model):
    title           = models.CharField(max_length=50)
    description     = models.TextField(null=True, blank=True)
    category        = models.CharField(max_length=120, choices=CATEGORY_CHOICES)
    status          = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Not Available")
    calories        = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    price_student   = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    price_guest     = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    price_attendant = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    day             = models.DateField()
    slug            = models.SlugField(unique=True)
    quantity        = models.IntegerField(default=0)
    timestamp       = models.DateTimeField(auto_now_add=True, auto_now=False)
    update          = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
         return self.title

    def get_description(self):
        if len(self.description) > 50:
            return self.description[:50] + " ........."
        return self.description


