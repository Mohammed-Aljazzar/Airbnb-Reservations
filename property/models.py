from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django_summernote.fields import SummernoteTextField

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='property/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=20000)
    # description = SummernoteTextField(max_length=10000)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='property_place')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='property_category')
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("property:property_detail", kwargs={"slug": self.slug})
    

class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="property_images")
    image = models.ImageField(upload_to="propertyimages/")

    def __str__(self):
        return str(self.property)

class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PropertyReview(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,related_name='review_property')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=2500)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.property)
    
    class Meta:
        ordering = ['created_at']
    
COUNT = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)

class PropertyBook(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,related_name='book_property')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_owner')
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    guest = models.IntegerField(max_length=2, choices=COUNT)
    childern = models.IntegerField(max_length=2, choices=COUNT)

    def __str__(self):
        return str(self.property)
    