from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Vous devez entrer un email.")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    REGIONS = (("Auvergne-Rhône-Alpes", "Auvergne-Rhône-Alpes"),
               ("Bourgogne-Franche-Comté", "Bourgogne-Franche-Comté"),
               ("Bretagne", "Bretagne"),
               ("Centre-Val de Loire", "Centre-Val de Loire"),
               ("Corse", "Corse"),
               ("Grand Est", "Grand Est"),
               ("Hauts-de-France", "Hauts-de-France"),
               ("Ile-de-France", "Ile-de-France"),
               ("Normandie", "Normandie"),
               ("Nouvelle-Aquitaine", "Nouvelle-Aquitaine"),
               ("Occitanie", "Occitanie"),
               ("Pays de la Loire", "Pays de la Loire"),
               ("Provence-Alpes-Côte d’Azur", "Provence-Alpes-Côte d’Azur"))
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=255, blank=False)
    club = models.CharField(blank=False, max_length=300)
    region = models.CharField(max_length=255, choices=REGIONS)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
