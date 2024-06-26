from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from home.models import Maqola


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.CharField(max_length=100, unique=True)
    username = None
    first_name = models.CharField(max_length=200,  null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email




class Reactions(models.Model):
    like = models.BooleanField(default=False)
    diss_like = models.BooleanField(default=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    maqola_id = models.ForeignKey(Maqola, on_delete=models.CASCADE)

    def __str__(self):
        return self.like
    
class Comments(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    maqola_id = models.ForeignKey(Maqola, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class CodeConfirmation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_code')
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} --- {self.code}"
