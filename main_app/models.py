from django.db import models
from django.urls import reverse

# Create your models here.
class Crystal(models.Model):

    name=models.CharField(max_length=250)
    mohs_hardness=models.DecimalField(max_digits=3,decimal_places=2,blank=True,null=True)
    usual_color=models.CharField(max_length=250,blank=True,null=True)
    img=models.CharField(max_length=5000,blank=True,null=True)
    bio=models.CharField(max_length=9000,blank=True,null=True)
    added_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "crystal"
        verbose_name_plural = "crystals"
        ordering=['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("crystal_detail", kwargs={"pk": self.pk})
