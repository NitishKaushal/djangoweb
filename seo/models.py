from django.db import models
#from django.db.models import ImageField
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)    # has to be different to identify each post
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(null=True,blank=True,upload_to='images/') #(null = True, blank = True (Don't have a image if we dont wantone.. ))#post.image.url
    # Want to Upload these Images to inside images/ directory - 'This directory will be created Automatically.

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s'% self.title
    def get_absolute_url(self):
        return reverse('seo.views.post', args=[self.slug])


class About(models.Model):
    title= models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    summary = models.CharField(max_length=1000)

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s'% self.title