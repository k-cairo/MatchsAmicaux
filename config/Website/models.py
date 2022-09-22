from django.db import models


class Announce(models.Model):
    LOCATION_CHOICES = (
        ("Domicile", "Domicile"),
        ("Extérieur", "Extérieur"),
        ("Peu Importe", "Peu Importe")
    )
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=50)
    author_club = models.CharField(max_length=50)
    author_category = models.CharField(max_length=10)
    author_practice_level = models.CharField(max_length=15)
    author_region = models.CharField(max_length=50)
    hour = models.CharField(max_length=5)
    date = models.DateField()
    location = models.CharField(choices=LOCATION_CHOICES, max_length=100)
    desired_level = models.CharField(max_length=50)
    published_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('published_date',)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('published_date',)

    def __str__(self):
        return f"Comment by {self.author} on {self.announce}"
