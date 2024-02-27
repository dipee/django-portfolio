from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Profile(Base):
    title = models.CharField(max_length=100)
    description = models.TextField()
    resume = models.FileField(upload_to='files/resume/')
    image = models.ImageField(upload_to='images/profile/')

    
class Project(Base):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/project/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(Base):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Skill(Base):
    title = models.CharField(max_length=100)
    description = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.title