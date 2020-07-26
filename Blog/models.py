from django.db import models
from django.contrib.auth.models import User

# creating a database called Author
class AuthorDetail(models.Model):
    profile_img = models.ImageField( upload_to = 'images/', null=True, blank = True)
    address =  models.CharField(max_length=100, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.email

# creating a database named Blog
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length=100)
    description = models.TextField( null=True)
    email = models.ForeignKey(AuthorDetail, on_delete= models.CASCADE, null= True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# use title as a blog name
    def __str__(self):
        return self.title

