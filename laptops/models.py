from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Laptops(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.TextField()
    description = models.TextField()
    image_laptop = models.ImageField(default='laptops_images/default_laptop_image.jpg',upload_to='media/laptops_images/')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'laptops_table'


class Manufacturer (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'manufacturer_table'


class LaptopReview (models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptops, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    star_given = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.laptop.name

    class Meta:
        db_table = 'review_table'


