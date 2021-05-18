from django.db import models
from django.utils import timezone
# Create your models here.

class user(models.Model):
    Firstname = models.CharField(max_length=150)
    Lastname = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Pwd = models.CharField(max_length=150)

class materiel(models.Model):
    numSerie = models.CharField(max_length=150)
    dateAchat = models.DateTimeField(default=timezone.now(), verbose_name="date d'ajoute")
    garantie = models.CharField(max_length=100)
    lieuAchat = models.CharField(max_length=100)
    prixAchat = models.CharField(max_length=100)
    marque = models.CharField(max_length=100)
    dateMaintenance = models.DateTimeField(default=timezone.now(), verbose_name="date de derniere maintenance")
    contrat = models.CharField(max_length=10)
    lieuAffectation = models.CharField(max_length=100)

    class Meta:
        verbose_name = "materiel"


    def __str__(self):
        return self.numSerie + "-" + str(self.prixAchat) + "-" +self.marque + "-" + self.lieuAffectation

