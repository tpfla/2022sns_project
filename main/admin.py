from django.contrib import admin
from .models import Post
import models

# Register your models here.
admin.site.register(Post)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]