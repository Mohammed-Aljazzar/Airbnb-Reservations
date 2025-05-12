from django.db import models
from django.urls import reverse
from  django.utils import timezone
from django.contrib.auth.models import User 
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    tag = TaggableManager()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    description = models.TextField(max_length=15000)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='post_category')
    slug = models.SlugField(null=True, blank=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

