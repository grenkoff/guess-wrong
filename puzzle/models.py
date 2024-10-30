from django.db import models


class RealWord(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word

class WrongWord(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word
