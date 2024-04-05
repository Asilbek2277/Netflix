from django.db import models

class Acter(models.Model):
    name=models.CharField(max_length=200)
    t_sana=models.DateField(blank=True)
    davlat=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Kino(models.Model):
    nomi=models.CharField(max_length=200)
    janr=models.CharField(max_length=200)
    yil=models.CharField(max_length=4)

    def __str__(self):
        return self.nomi

class KinoActer(models.Model):
    kino=models.ForeignKey(Kino, on_delete=models.CASCADE)
    aktyor=models.ForeignKey(Acter, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kino.nomi}-{self.aktyor.name}"

class Tarif(models.Model):
    nom=models.CharField(max_length=200)
    davomiyligi=models.CharField(max_length=10)
    narx=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nom



