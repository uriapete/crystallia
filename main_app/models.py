from django.db import models
from django.urls import reverse

# Create your models here.
class Crystal(models.Model):

    name=models.CharField(max_length=250)
    mohs_hardness=models.DecimalField(max_digits=3,decimal_places=2)
    usual_color=models.CharField(max_length=250)
    img=models.CharField(max_length=5000)
    finding_place=models.CharField(max_length=9000)

    class Meta:
        verbose_name = "crystal"
        verbose_name_plural = "crystals"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("crystal_detail", kwargs={"pk": self.pk})
