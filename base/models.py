from django.db import models

class Profile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    resume = models.FileField(upload_to='files/resume/')
    image = models.ImageField(upload_to='images/profile/')

    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/project/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.title