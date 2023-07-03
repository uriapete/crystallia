from django.db import models
from django.urls import reverse

# Create your models here.
class CrystalType(models.Model):

    name=models.CharField(max_length=250)
    mohs_hardness=models.DecimalField(max_digits=3,decimal_places=2,blank=True,null=True)
    usual_color=models.CharField(max_length=250,blank=True,null=True)
    img=models.CharField(max_length=5000,blank=True,null=True)
    bio=models.TextField(max_length=5000,blank=True,null=True)
    added_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "crystal_type"
        verbose_name_plural = "crystal_types"
        ordering=['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("crystal_type_detail", kwargs={"pk": self.pk})
    
class Crystal(models.Model):

    type=models.ForeignKey(CrystalType,on_delete=models.CASCADE,related_name="crystal",blank=False,null=False)
    img=models.CharField(max_length=5000,blank=True,null=True)
    summary=models.TextField(max_length=5000,blank=True,null=True)
    color=models.CharField(max_length=250,blank=True,null=True)
    mohs_hardness=models.DecimalField(max_digits=3,decimal_places=2,blank=True,null=True)
    added_on=models.DateTimeField(auto_now_add=True)
    found_on=models.DateField(null=True,blank=True)

    class Meta:
        verbose_name = _("crystal")
        verbose_name_plural = _("crystals")

    def __str__(self):
        return f"{self.type.name} {self.pk}"

    def get_absolute_url(self):
        return reverse("crystal_detail", kwargs={"pk": self.pk})
