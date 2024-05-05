from django.db import models
from django.urls import reverse
from utils.slug import slugify



class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    made_in = models.CharField(max_length=32)
    slug = models.SlugField(max_length=128, null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.name} {self.price}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        kwargs = {
            "pk": self.pk,
            "slug": self.slug
        }
        return reverse("product:product-detail", kwargs=kwargs)