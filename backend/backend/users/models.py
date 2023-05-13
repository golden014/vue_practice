from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# abstract user adalah built in model yang uda punya fungsionalitas2 utk authentication dan authorization
# abstract user biasa punya field2nya sendiri (bisa ditambah), tpi kalau g mau bisa pakai yg base
# abstract user (model yg punya bare minimum utk auth intinya gaada field2 tambahan)
# hanya gunakan utk auth (kyk user, tpi buat product misalnya no)
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)

    #ganti username jadi email supaya login pakai email (gjadi, error)
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



