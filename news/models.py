from django.db import models


class NewsData(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    img = models.ImageField(upload_to='news/')
    activity = models.BooleanField(default=False)
    monitoring = models.BooleanField(default=False)
    slider = models.BooleanField(default=False)

    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

class Activity(models.Model):
    text = models.TextField()

class Team(models.Model):
    name = models.CharField(max_length=100)
    fb = models.CharField(max_length=100)
    descrip = models.TextField()
    img = models.ImageField(upload_to='team/')

    @property
    def photo_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

class Aboutus(models.Model):
    text = models.TextField()

class Reference(models.Model):
    title = models.CharField(max_length=300)
    link = models.CharField(max_length=1500)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    source = models.CharField(max_length=300)
