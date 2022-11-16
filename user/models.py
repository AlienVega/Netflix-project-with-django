from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid
 # Create your models here.
class Profil(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable=False)
    olusturan=models.ForeignKey(User,on_delete=models.CASCADE)
    isim=models.CharField(max_length=100)
    resim=models.FileField(upload_to="profiller")
    slug =models.SlugField(null=True , blank=True , editable=False)
    def __str__(self):
        return self.isim
    def save(self, *args, **kwargs):
        self.slug =slugify(self.isim)
        super().save(*args, **kwargs)
class Hesap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resim = models.FileField(upload_to ='hesaplar/')
    telefon = models.CharField(max_length=11)

    def __str__ (self):
        return self.user.username