from django.db import models

# Create your models here.


class Maqola(models.Model):
    WORLD = 'world'
    LOCAL = 'local'
    SPORT = 'sport'

    TAG = (
        ('world', WORLD),
        ('local', LOCAL),
        ('sport', SPORT)
    )
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    tag = models.CharField(choices=TAG, max_length=20)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50)

    @property
    def imageURL(self):
        return self.image.url

    def __str__(self):
        return f"{self.title}"
    
