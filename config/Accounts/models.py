from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None, club=None, region=None, category=None,
                    practice_level=None):
        if not email:
            raise ValueError("Vous devez entrer un email.")
        elif not first_name:
            raise ValueError("Vous devez entrer un prénom.")
        elif not last_name:
            raise ValueError("Vous devez entrer un nom.")
        elif not club:
            raise ValueError("Vous devez entrer un club.")
        elif not category:
            raise ValueError("Vous devez entrer une catégorie.")
        elif not practice_level:
            raise ValueError("Vous devez entrer un niveau de pratique.")
        elif not region:
            raise ValueError("Vous devez entrer une région.")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            club=club,
            category=category,
            practice_level=practice_level,
            region=region
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, first_name=None, last_name=None):
        user = self.create_user(email=email, password=password, first_name=first_name, last_name=last_name, club=" ",
                                region=" ", category=" ", practice_level=" ")
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
    CATEGORYS = (
        ("U6", "U6"), ("U7", "U7"), ("U8", "U8"), ("U9", "U9"), ("U10", "U10"), ("U11", "U11"), ("U12", "U12"),
        ("U13", "U13"), ("U14", "U14"), ("U15", "U15"), ("U16", "U16"), ("U17", "U17"), ("U18", "U18"), ("U19", "U19"),
        ("U20", "U20"), ("Sénior", "Sénior")
    )
    LEVELS = (
        ("Départemental", "Départemental"), ("Régional", "Régional"), ("National", "National"), ("D5", "D5"),
        ("D4", "D4"), ("D3", "D3"), ("D2", "D2"), ("D1", "D1"), ("R4", "R4"), ("R3", "R3"), ("R2", "R2"), ("R1", "R1"),
    )
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, max_length=255, blank=False)
    club = models.CharField(max_length=300)
    region = models.CharField(max_length=255, choices=REGIONS)
    category = models.CharField(max_length=10, choices=CATEGORYS)
    practice_level = models.CharField(max_length=15, choices=LEVELS)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
